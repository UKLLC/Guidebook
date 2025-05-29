import requests
import json
import os
import sqlalchemy
import pandas as pd
import mdapi_functions as md
from IPython.display import display, Markdown
import markdown
from bokeh.plotting import figure, show
from bokeh.models import Span, TabPanel, Tabs
from bokeh.io import output_notebook
from math import pi
from datetime import datetime
import datacite_api_functions as dcf

pd.options.mode.chained_assignment = None


class DocHelper:
    def __init__(self, datasource, dataset, version, filepath):
        '''

        Parameters
        ----------
        datasource : str
            data source of target table/dataset
        dataset : str
            dataset/table name of target table/dataset
        version : str
            version number of target table/dataset
        filepath : str
            filepath of py scripts and NHS pid lookups

        Returns
        -------
        None.

        '''
        # define std input variables
        self.data = dataset
        self.source = datasource
        self.version = version
        self.fp = filepath
        # ukllc api connection
        self.api_key = os.environ['FASTAPI_KEY']

    def connect(self):
        '''

        Raises
        ------
        Exception
            Database connection failure

        Returns
        -------
        cnxn : database connection
            connection to heroku database with metrics

        '''
        # attempt db connection
        try:
            db_str = os.environ['DATABASE_URL'].replace("postgres", "postgresql+psycopg2", 1)
            cnxn = sqlalchemy.create_engine(db_str)
            return(cnxn)
        # raise exception if connection failure
        except Exception as e:
            raise Exception("DB connection failed with error", e)


    def get_cohort_count(self):
        '''

        Returns
        -------
        cnt : df
            dataframe containing counts of participants by LPS

        '''

        # get data from api endpoint
        url = "https://metadata-api-4a09f2833a54.herokuapp.com/nhs-dataset-counts/?table={}".format(self.data)
        r = requests.get(url, headers={'access_token': self.api_key})
        data = r.text
        # convert to json
        pj = json.loads(data)
        # convert to dataframe
        df = pd.json_normalize(pj)

        # remove cohorts not included
        rm = ['GENSCOT', 'NICOLA', 'SABRE']
        df = df[~df['cohort'].isin(rm)]

        # strip down df and rename
        df = df[['cohort', 'count']].rename(columns={'cohort': 'LPS',
                                'count': 'Participant count'})

        # CALC TOTAL
        # treat <10 as 0
        df['count1'] = df['Participant count'].replace('<10', '0')
        # convert to ensure counts are numeric
        df['count1'] = df['count1'].astype(int)
        # get total
        df.loc["Total"] = df['count1'].sum()
        # drop temp column
        df = df.drop(columns = ['count1'])
        # sort index and total naming
        df = df.reset_index(drop = True)
        df.loc[df.index[-1], 'LPS'] = 'TOTAL'
        return df

    def get_dataset_info(self):
        '''

        Returns
        -------
        dfm : dataframe
            retrieved data from multiple endpoints of UK LLC metadata API and creating summary table

        '''

        # get observation and row counts from versions endpoint
        # IAPT and CSDS being multi part tables need skipping via dummy dfs
        multi = ['IAPT', 'CSDS']
        if any(i in self.data for i in multi):
            # create dummy dataframe
            df1 = pd.DataFrame()
        else:
            # get observation and row counts from versions endpoint
            url1 = "https://metadata-api-4a09f2833a54.herokuapp.com/all-datasets-versions/?source={}&table={}".format(self.source, self.data)
            r1 = requests.get(url1, headers={'access_token': self.api_key })
            data1 = r1.text
            # convert to json
            pj1 = json.loads(data1)
            # convert to dataframe
            df1 = pd.json_normalize(pj1)
            # dedup keeping latest
            df1 = df1.sort_values('version_num').drop_duplicates('table', keep='last')
            # keep only select columns
            to_keep = ['num_columns', 'num_rows']
            df1 = df1[to_keep]
            df1['num_columns'] = df1['num_columns'].astype(int)
            df1['num_rows'] = df1['num_rows'].astype(int)
            # rename
            df1 = df1.rename(columns={'num_columns': 'Number of variables',
                                    'num_rows': 'Number of observations'})
            # transpose and rename columns
            df1 = df1.T
            df1 = df1.rename(columns = {df1.columns[0] : 'Dataset-specific information'})

        # guidebook specific table/endpoint
        multipart = ['IAPT_', 'CSDS_']
        if any(i in self.data for i in multipart):
            # create dummy dataframe
            df2 = pd.DataFrame()
        else:
            url2 = "https://metadata-api-4a09f2833a54.herokuapp.com/nhs-datasets-gb/?Name_of_dataset_in_TRE={}".format(self.data)
            r2 = requests.get(url2, headers={'access_token': self.api_key })
            data2 = r2.text
            # convert to json
            pj2 = json.loads(data2)
            # convert to dataframe
            df2 = pd.json_normalize(pj2)
            # shift dataset name to first place
            col_ord = ['Name_of_dataset_in_TRE', 'Other_name', 'Temporal_coverage', 'TRE_temporal_coverage']
            df2 = df2[col_ord + [col for col in df2.columns if col not in col_ord]]
            # transpose and rename columns
            df2 = df2.T
            df2 = df2.rename(columns = {df2.columns[0] : 'Dataset-specific information'})
        # need to merge 2 dataframe to get complete picture
        dfm = pd.concat([df2, df1])

        # get total count of participants in each dataset
        if any(i in self.data for i in multi):
            # create dummy dataframe
            df3 = pd.DataFrame()
        else:
            df3 = self.get_cohort_count()
            df3 = df3[df3['LPS'] == 'TOTAL'].drop('LPS', axis=1)
            # and transpose
            df3 = df3.T
            df3 = df3.rename(columns = {df3.columns[0] : 'Dataset-specific information'})
        # and merge
        dfm = pd.concat([dfm, df3])

        # End point for latest extract
        if any(i in self.data for i in multi):
            # create dummy dataframe
            df4 = pd.DataFrame()
        else:
            url4 = "https://metadata-api-4a09f2833a54.herokuapp.com/nhs-extract-dates/"
            r4 = requests.get(url4, headers={'access_token': self.api_key })
            data4 = r4.text
            # convert to json
            pj4 = json.loads(data4)
            # convert to dataframe
            df4 = pd.json_normalize(pj4)
            # dedup keeping latest and filter to target dataset
            df4 = df4[df4['dataset'].str.contains(self.data)].sort_values('date').drop_duplicates('dataset', keep='last')
            df4 = df4[['date']]
            # rename
            df4 = df4.rename(columns={'date': 'Date of last extract'})
            # and transpose
            df4 = df4.T
            df4 = df4.rename(columns = {df4.columns[0] : 'Dataset-specific information'})
        # and merge
        dfm = pd.concat([dfm, df4])

        # FINAL CLEARUP
        dfm = dfm.reset_index()
        dfm = dfm.rename(columns = {'index' : 'Dataset descriptor'})
        dfm = dfm.reset_index(drop = True)
        dfm['Dataset descriptor'] = dfm['Dataset descriptor'].str.replace('_', ' ')
        return dfm


    def style_table(self, df):
        '''

        Parameters
        ----------
        df : dataframe
            df to be styled

        Returns
        -------
        df : dataframe
            df with styling applied

        '''

        # apply styling
        df = df.style.set_table_attributes('style="font-size: 14px"')\
        .set_table_styles([dict(selector='th', props=[('text-align', 'left'),])])\
        .set_properties(**{'text-align': 'left'})
        # LPS tables
        if 'LPS' in df.columns:
            df.set_properties(subset = ['LPS'], **{'font-weight' : 'bold'})\
            .set_properties(subset = df.index[-1], **{'font-weight' : 'bold'})
        # hide index as don't want to display
        df.hide()
        return df


class LPSDataSet:
    def __init__(self, source, dataset):
        '''

        Parameters
        ----------
        source : str
            data source of target table/dataset
        dataset : str
            dataset/table name of target table/dataset
        version : str
            version number of target table/dataset

        Returns
        -------
        None.

        '''
        # define std input variables
        self.dataset = dataset
        self.source = source

        infill = os.path.abspath('../../../../scripts/dsvs_infill.csv')
        df = md.prep_dsvs_for_gb_pages(infill)
        self.df_ds = df[df["source_table"] == source + "_" + dataset]

    def title(self):
        return display(Markdown("# " + self.df_ds.iloc[0]["table_name"] + " (" + self.df_ds.iloc[0]["source"] + ")"))


    def summary(self):
        return display(Markdown(self.df_ds.iloc[0]["long_desc"]))


    def info_table(self):
        pref = "10.83126/" # switch to autograb from datacite API when minted
        suff = "ukllc-dataset-00032-01" # switch to autograb from API  when minted
        cite = json.loads(requests.get(
            "https://api.test.datacite.org/dois/" + pref + suff,
        ).text)['data']['attributes']

        citeprocjson = "https://api.datacite.org/application/vnd.citationstyles.csl+json/"
        bibtex = "https://api.datacite.org/application/x-bibtex/"
        ris = "https://api.datacite.org/application/x-research-info-systems/"

        apa_cite = cite['creators'][0]["name"] +             ". (" + str(cite["publicationYear"]) + "). <i>" +             cite["titles"][0]["title"] +             ".</i> (Version " +             cite["version"] +             ") [Data set]. " +             cite["publisher"] +             ". " + md.make_hlink("https://doi.org/" + pref + suff, "https://doi.org/" + pref + suff)

        dl_cites = md.make_hlink(citeprocjson + pref + suff, "Citeproc JSON") + "&nbsp;&nbsp;&nbsp;&nbsp;" +             md.make_hlink(bibtex + pref + suff, "BibTeX") + "&nbsp;&nbsp;&nbsp;&nbsp;" + md.make_hlink(ris + pref + suff, "RIS")


        ds_info_list = [
        [
            "Name of Dataset in TRE",
            "Citation (APA)",
            "Download Citation",
            "Series",
            "Owner",
            "Temporal Coverage",
            "Keywords",
            "Participants Invited",
            "Participant Count",
            "Number of variables",
            "Number of observations",
            "Specific Restrictions to Data Use",
            "Build a Data Request"
        ],
        [
            self.df_ds.iloc[0]["source_table"], # DS in TRE
            apa_cite, # Citation
            dl_cites, # Download Cite
            md.make_hlink("https://guidebook.ukllc.ac.uk/docs/lps/lps%20profiles/{}".format(self.df_ds.iloc[0]["source"]), self.df_ds.iloc[0]["source_name"]), # Series
            self.df_ds.iloc[0]["Owner"], # Owner
            self.df_ds.iloc[0]["collection_start"] + " - " + self.df_ds.iloc[0]["collection_end"], # Temporal Coverage
            self.df_ds.iloc[0]["topic_tags"], # Keywords
            self.df_ds.iloc[0]["participants_invited"], # Participants invited
            self.df_ds.iloc[0]["participants_included"], # Participants included
            md.get_num_vars(self.df_ds.iloc[0]["source"], self.df_ds.iloc[0]["table"]), # Number of variables
            int(self.df_ds.iloc[0]["num_rows"]), # Number of observations
            "None", # Restrictions to Data Use
            md.make_hlink("https://explore.ukllc.ac.uk/","https://explore.ukllc.ac.uk/") # Build a data request
        ]
        ]

        df_ss_info = pd.DataFrame(ds_info_list, index=["Dataset Descriptor", "Dataset-specific Information"]).T
        df_ss_info = DocHelper.style_table("_", df_ss_info)
        return df_ss_info

    def version_history(self):
        dsvs = md.get_md_api_dsvs()
        dsvs = dsvs[(dsvs["source"] == self.source) & (dsvs["table"] == self.dataset)]
        dsvs["version_num"] = dsvs["version_num"].apply(lambda x: "Version " + str(int(x.split("v")[1])))
        dsvs["version_date"] = dsvs["version_date"].apply(lambda x: datetime.strftime(datetime.strptime(str(int(x)), "%Y%m%d"), "%d %b %Y"))
        dsvs["num_columns"] = dsvs["num_columns"].apply(lambda x: int(x))
        dsvs["num_participants"] = dsvs["num_participants"].apply(lambda x: int(x))
        dsvs["DOI"] = "10.83126/ukllc-dataset-00032-01" # placeholder for now
        dsvs2 = dsvs[["version_num", "version_date", "num_columns", "num_participants", "DOI"]].rename(columns = {"version_num": "Version Number", "version_date": "Version Date", "num_columns": "Number of Variables", "num_participants": "Number of Participants"}).set_index("Version Number")
        return dsvs2.T

    def change_log(self):
        return display(Markdown("We are currently working on a metadata management system, which will allow for studies to change metadata for their resources held in the UK LLC. Changes to metadata of datasets (such as dataset name or summary) will surface here."))

    def documentation(self):
        return display(Markdown("We are currently building a documentation storage system, which will host relevant and useful documents related to datasets, groupings, and studies themselves. Relevant documentation for this particular dataset will go here."))

    def useful_syntax(self):
        return display(Markdown("Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to Git where you can find the full script"))


class LPSSource:
    def __init__(self, source):
        '''

        Parameters
        ----------
        source : str
            data source of target table/dataset

        Returns
        -------
        None.

        '''
        # define std input variables
        self.source = source
        self.df_ss = md.get_md_api_ss()[md.get_md_api_ss()["source"] == self.source]
        self.cohort_profile = md.get_md_api_profiles()[md.get_md_api_profiles()["source"] == self.source].iloc[0]["profile_doi"]

        def ss_doi(x):
            df = dcf.get_doi_series()
            if len(df[(df["source"] == x) & (df["state"] == "findable")]) == 1:
                return df[df["source"] == x].iloc[0]["id"]
            else:
                return "DOI TBC"

        self.doi = ss_doi(self.source)

        def cites(x):
            citeprocjson = "https://api.datacite.org/application/vnd.citationstyles.csl+json/"
            bibtex = "https://api.datacite.org/application/x-bibtex/"
            ris = "https://api.datacite.org/application/x-research-info-systems/"
            if x == "DOI TBC":
                apa_cite = "DOI and Citation TBC"
                dl_cites = "DOI and Citation Downloads TBC"
                return apa_cite, dl_cites

            else:
                cite = json.loads(requests.get(
                    "https://api.test.datacite.org/dois/" + x,
                ).text)['data']['attributes']

                citeprocjson = "https://api.datacite.org/application/vnd.citationstyles.csl+json/"
                bibtex = "https://api.datacite.org/application/x-bibtex/"
                ris = "https://api.datacite.org/application/x-research-info-systems/"

                apa_cite = cite['creators'][0]["name"] + \
                    ". (" + str(cite["publicationYear"]) + "). <i>" + \
                    cite["titles"][0]["title"] + \
                    ".</i> " + \
                    cite["publisher"] + \
                    ". " + md.make_hlink("https://doi.org/" + x, "https://doi.org/10.83126/ukllc-series-00001")

                dl_cites = md.make_hlink(citeprocjson + x, "Citeproc JSON") + "&nbsp;&nbsp;&nbsp;&nbsp;" + \
                    md.make_hlink(bibtex + x, "BibTeX") + "&nbsp;&nbsp;&nbsp;&nbsp;" + md.make_hlink(ris + x, "RIS")
                return apa_cite, dl_cites

        self.apa_cite, self.dl_cites = cites(self.doi)

    def summary(self):
        return display(Markdown(self.df_ss.iloc[0]["Aims"]))

    def info_table(self):

        ss_info_list = [
        [
            "Citation (APA)",
            "Download Citation",
            "Owner",
            "Cohort",
            "Age at Recruitment",
            "Geographical Coverage - Nations",
            "Geographical Coverage - Regions",
            "Start Date",
            "Permitted Linkages",
            "Inclusion in Linkages",
            "Cohort Profile",
            "LPS Homepage",
            "Build a Data Request"
        ],
        [
            self.apa_cite,
            self.dl_cites,
            self.df_ss.iloc[0]["Owner"],
            self.df_ss.iloc[0]["sample_size_at_recruitment"],
            self.df_ss.iloc[0]["age_at_recruitment"],
            self.df_ss.iloc[0]["geographic_coverage_Nations"],
            self.df_ss.iloc[0]["geographic_coverage_Regions"],
            self.df_ss.iloc[0]["start_date"],
            "See " + md.make_hlink("https://guidebook.ukllc.ac.uk/docs/lps/linkages/lps_linkages","here"),
            self.df_ss.iloc[0]["participant_pathway"],
            md.make_hlink("https://doi.org/" + self.cohort_profile, self.cohort_profile),
            markdown.markdown(self.df_ss.iloc[0]["Website"]),
            md.make_hlink("https://explore.ukllc.ac.uk/","https://explore.ukllc.ac.uk/")
        ]
        ]

        df_ss_info = pd.DataFrame(ss_info_list, index=["Series Descriptor", "Series-specific Information"]).T
        return DocHelper.style_table("_", df_ss_info)

    def datasets(self):
        infill = os.path.abspath('../../scripts/dsvs_infill.csv')
        df = md.prep_dsvs_for_gb_pages(infill)

        ds_dois = dcf.get_doi_datasets()
        ds_dois = ds_dois[ds_dois["state"] == "findable"]
        ds_dois["source_table"] = ds_dois["attributes.titles"].apply(lambda x: x[1]["title"])

        # TODO: latest dataset version DOI rather than 1st one
        df["DOI"] = df["source_table"].apply(lambda x: ds_dois[ds_dois["source_table"] == x].iloc[0]["id"] if len(ds_dois[ds_dois["source_table"] == x]) == 1 else "DOI TBC")
        df = df[df["source"] == self.source][["table", "table_name", "DOI"]].rename(columns={"table": "Table", "table_name": "Table Name"})
        return DocHelper.style_table("_", df)

    def linkages_plot(self):
        dff = md.get_md_api_frz_link_nhse()
        dff = dff[(dff["LPS"] == self.source) & (dff["frz_num"] == dff["frz_num"].max())]

        lx = ["NHS England", "NHS Wales", "NHS Scotland", "Neighbourhood Geographies", "Address Geographies", "DfE", "DWP", "HMRC"]
        ly = [dff.iloc[0]["n_l_tot"], 0, 0, 0, 0, 0, 0, 0]

        output_notebook(hide_banner=True)
        p = figure(x_range=lx, width=600, height=400, title="Linkage of {} participants to linked Datasets".format(self.source))
        p.vbar(x=lx, top=ly, width=0.8)
        vline = Span(location=dff.iloc[0]["n_sent"], dimension='width', line_color='grey', line_width=2)
        p.add_layout(vline)
        p.y_range.start = 0
        p.y_range.end = round(dff.iloc[0]["n_sent"]*1.2, -3)
        p.xaxis.major_label_orientation = pi/4

        show(p)

    def linkages_all_plots(self):
        output_notebook(hide_banner=True)
        dff = md.get_md_api_frz_link_nhse()
        plist = []
        lx = ["NHS England", "NHS Wales", "NHS Scotland", "Neighbourhood Geographies", "Address Geographies", "DfE", "DWP", "HMRC"]

        for i in range(1,dff["frz_num"].max()+1):
            dffi = dff[(dff["LPS"] == self.source) & (dff["frz_num"] == i)]
            ly = [dffi.iloc[0]["n_l_tot"], 0, 0, 0, 0, 0, 0, 0]
            p = figure(x_range=lx, width=600, height=400, title="Linkage of {} participants to linked Datasets".format(self.source))
            p.vbar(x=lx, top=ly, width=0.8)
            vline = Span(location=dffi.iloc[0]["n_sent"], dimension='width', line_color='grey', line_width=2)
            p.add_layout(vline)
            p.y_range.start = 0
            p.y_range.end = round(dff[(dff["LPS"] == self.source)]["n_sent"].max()*1.2, -3)
            p.xaxis.major_label_orientation = pi/4
            plist.append(p)

        tabs = Tabs(tabs=[
            TabPanel(child=plist[x-1], title="Freeze {}".format(x)) for x in range(1,dff["frz_num"].max()+1)
        ], active=dff["frz_num"].max()-1)

        show(tabs)

    def change_log(self):
        return display(Markdown("We are currently working on a metadata management system, which will allow for studies to change metadata for their resources held in the UK LLC. Changes to metadata of datasets (such as dataset name or summary) will surface here."))

    def documentation(self):
        return display(Markdown("We are currently building a document repository which will host relevant and useful documents related to datasets, groupings, and studies themselves. Relevant documentation for this particular dataset will go here."))


class NHSEDataSet:
    def __init__(self, dataset):
        '''

        Parameters
        ----------
        dataset : str
            dataset/table name of target table/dataset
        version : str
            version number of target table/dataset

        Returns
        -------
        None.

        '''
        def get_nhse_ds(x):
            ds = md.get_md_api_dss()
            df_ds = ds[(ds["source"] == "NHSE") & (ds["table"] == x)]
            df_ds["source_table"] = df_ds["source"] + "_" + df_ds["table"]
            ss = md.get_md_api_ss()[["source", "Owner"]]
            df_ds = df_ds.merge(ss, on="source")
            df_gb_temp = md.get_nhs_gb_info(x)
            df_ds = df_ds.merge(df_gb_temp, on="table")
            return df_ds

        def ds_doi(x):
            doi_ds = dcf.get_doi_datasets()[dcf.get_doi_datasets()["state"] == "findable"]
            doi_ds["source_table"] = doi_ds["attributes.titles"].apply(lambda x: x[1]["title"] if len(x) > 1 else "NA")

            reg = ["CANCER", "MORTALITY", "DEMOGRAPHICS"]
            if x in reg:
                doi_ds = doi_ds[doi_ds["source_table"].str.startswith("NHSE_" + x)]
                doi_ds = doi_ds.sort_values(by="source_table", ascending=False).head(1)
            else:
                doi_ds = doi_ds[doi_ds["source_table"] == "NHSE_" + x]
                doi_ds = doi_ds.sort_values(by="attributes.version", ascending=False).drop_duplicates(subset="source_table")

            if len(doi_ds) == 1:
                return doi_ds.iloc[0]["id"]
            else:
                return "DOI TBC"

        def get_ed(x):
            req = requests.get("https://metadata-api-4a09f2833a54.herokuapp.com/nhs-extract-dates/", headers={'access_token': os.environ['FASTAPI_KEY'] })
            df_ed = pd.json_normalize(json.loads(req.text))
            df_ed = df_ed[df_ed["dataset"].str.startswith(x)].sort_values(by="date", ascending=False)
            return df_ed.iloc[0]["date"]

        def cites(x):
            citeprocjson = "https://api.datacite.org/application/vnd.citationstyles.csl+json/"
            bibtex = "https://api.datacite.org/application/x-bibtex/"
            ris = "https://api.datacite.org/application/x-research-info-systems/"
            if x == "DOI TBC":
                apa_cite = "DOI and Citation TBC"
                dl_cites = "DOI and Citation Downloads TBC"
                return apa_cite, dl_cites

            else:
                cite = json.loads(requests.get(
                    "https://api.test.datacite.org/dois/" + x,
                ).text)['data']['attributes']

                citeprocjson = "https://api.datacite.org/application/vnd.citationstyles.csl+json/"
                bibtex = "https://api.datacite.org/application/x-bibtex/"
                ris = "https://api.datacite.org/application/x-research-info-systems/"

                apa_cite = cite['creators'][0]["name"] + \
                    ". (" + str(cite["publicationYear"]) + "). <i>" + \
                    cite["titles"][0]["title"] + \
                    ".</i> " + \
                    cite["publisher"] + \
                    ". " + md.make_hlink("https://doi.org/" + x, "https://doi.org/" + x)

                dl_cites = md.make_hlink(citeprocjson + x, "Citeproc JSON") + "&nbsp;&nbsp;&nbsp;&nbsp;" + \
                    md.make_hlink(bibtex + x, "BibTeX") + "&nbsp;&nbsp;&nbsp;&nbsp;" + md.make_hlink(ris + x, "RIS")
                return apa_cite, dl_cites

        # define std input variables
        self.dataset = dataset
        self.df_ds = get_nhse_ds(self.dataset)
        self.doi = ds_doi(self.df_ds.iloc[0]["table"])
        self.ed = get_ed(self.dataset)
        self.apa_cite, self.dl_cites = cites(self.doi)

    def title(self):
        return display(Markdown("# " + self.df_ds.iloc[0]["table_name"] + " (" + self.df_ds.iloc[0]["source"] + ")"))

    def three_sec_summary(self):
        display(Markdown('<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>{}</strong></div>'.format(self.df_ds.iloc[0]["short_desc"])))

    def summary(self):
        return display(Markdown(self.df_ds.iloc[0]["long_desc"]))

    def info_table(self):
        ds_info_list = [
        [
            "Name of Dataset in TRE",
            "Citation (APA)",
            "Download Citation",
            "Series",
            "Owner",
            "Temporal Coverage in the TRE",
            "Geographical Coverage",
            "Key Link",
            "Keywords",
            "Latest Extract Date",
            "Specific Restrictions to Data Use",
            "Build a Data Request"
        ],
        [
            self.df_ds.iloc[0]["source_table"], # DS in TRE
            self.apa_cite, # Citation
            self.dl_cites, # Download Cite
            md.make_hlink("https://guidebook.ukllc.ac.uk/docs//linked_health_data/NHS_England/NHSE_intro", self.df_ds.iloc[0]["source_name"]), # Series
            self.df_ds.iloc[0]["Owner"], # Owner
            self.df_ds.iloc[0]["collection_start"] + " - " + self.df_ds.iloc[0]["collection_end"], # Temporal Coverage
            self.df_ds.iloc[0]["Geographical_coverage"], # Geo Coverage
            md.make_hlink(self.df_ds.iloc[0]["Key_link"], self.df_ds.iloc[0]["Key_link"]),
            self.df_ds.iloc[0]["Keywords"], # Keywords
            self.ed,
            self.df_ds.iloc[0]["Specific_restrictions_to_data_use"], # Restrictions to Data Use
            md.make_hlink("https://explore.ukllc.ac.uk/","https://explore.ukllc.ac.uk/") # Build a data request
        ]
        ]

        df_ss_info = pd.DataFrame(ds_info_list, index=["Dataset Descriptor", "Dataset-specific Information"]).T
        return DocHelper.style_table("_", df_ss_info)

    def metrics(self):
        return display(Markdown("TBC"))

    def version_history(self):
        return display(Markdown("TBC"))

    def change_log(self):
        return display(Markdown("We are currently working on a metadata management system, which will allow for studies to change metadata for their resources held in the UK LLC. Changes to metadata of datasets (such as dataset name or summary) will surface here."))

    def documentation(self):
        return display(Markdown("We are currently building a documentation storage system, which will host relevant and useful documents related to datasets, groupings, and studies themselves. Relevant documentation for this particular dataset will go here."))

    def useful_syntax(self):
        return display(Markdown("Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to Git where you can find the full script"))
