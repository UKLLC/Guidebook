import requests
import json
import os
import sqlalchemy
import pandas as pd
import mdapi_functions as md
from IPython.display import display, Markdown
import markdown
from bokeh.plotting import figure, show
from bokeh.models import (Span, TabPanel, Tabs, ColumnDataSource, DataCube,
                          GroupingInfo, StringFormatter, SumAggregator,
                          TableColumn)
from bokeh.io import output_notebook
from math import pi
from datetime import datetime
import datacite_api_functions as dcf
import numpy as np

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
    """Class for LPS datasets featuring all functions for GB pages
    """
    def __init__(self, source: str, dataset: str):
        """Init function to generate self.variables needed for functions

        Args:
            source (str): source i.e. study e.g. "ALSPAC" or "BCS70"
            dataset (str): name of dataset e.g. "serology1m"

        Returns:
            self.dataset (str): dataset
            self.source (str): source
            self.df_ds (DF): dataframe of dataset metrics
        """

        # define std input variables
        self.dataset = dataset
        self.source = source
        infill = os.path.abspath('../../../../scripts/dsvs_infill.csv')
        df = md.prep_dsvs_for_gb_pages(infill)
        self.df_ds = df[df["source_table"] == source + "_" + dataset]

    def title(self):
        """Retrieves title of dataset from DF

        Args:
            self.df_ds (DF): dataframe of dataset metrics

        Returns:
            markdown: displayed arkdown of title in "# dataset name" format
        """

        return display(Markdown("# " + self.df_ds.iloc[0]["table_name"] +
                                " (" + self.df_ds.iloc[0]["source"] + ")"))

    def summary(self):
        """Summary paragraph of dataset from MD API

        Args:
            self.df_ds (DF): dataframe of dataset metrics

        Returns:
            markdown: Displayed Markdown of Summary of dataset
        """

        return display(Markdown(self.df_ds.iloc[0]["long_desc"]))

    def info_table(self):
        """Returns information table of Dataset

        Args:
            self.df_ds (DF): dataframe of dataset metrics

        Returns:
            markdown: displayed markdown of info DF with formatting applied
        """

        pref = "10.83126/"  # switch to autograb from datacite API when minted
        suff = "ukllc-dataset-00032-01"  # switch to autograb from API
        cite = json.loads(requests.get(
            "https://api.test.datacite.org/dois/" + pref + suff,
        ).text)['data']['attributes']

        citeprocjson = "https://api.datacite.org/application/"
        "vnd.citationstyles.csl+json/"
        bibtex = "https://api.datacite.org/application/x-bibtex/"
        ris = "https://api.datacite.org/application/x-research-info-systems/"

        apa_cite = (cite['creators'][0]["name"] + ". ("
                    + str(cite["publicationYear"]) + "). <i>"
                    + cite["titles"][0]["title"]
                    + ".</i> (Version "
                    + cite["version"]
                    + ") [Data set]. "
                    + cite["publisher"]
                    + ". " + md.make_hlink(
                        "https://doi.org/" + pref + suff,
                        "https://doi.org/" + pref + suff)
                    )

        dl_cites = (md.make_hlink(citeprocjson + pref + suff, "Citeproc JSON")
                    + "&nbsp;&nbsp;&nbsp;&nbsp;"
                    + md.make_hlink(bibtex + pref + suff, "BibTeX")
                    + "&nbsp;&nbsp;&nbsp;&nbsp;"
                    + md.make_hlink(ris + pref + suff, "RIS")
                    )

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
             self.df_ds.iloc[0]["source_table"],  # DS in TRE
             apa_cite,  # Citation
             dl_cites,  # Download Cite
             md.make_hlink(
                 "https://guidebook.ukllc.ac.uk/docs/lps/lps%20profiles/{}"
                 .format(self.df_ds.iloc[0]["source"]),
                 self.df_ds.iloc[0]["source_name"]
                 ),  # Series
             self.df_ds.iloc[0]["Owner"],  # Owner
             (self.df_ds.iloc[0]["collection_start"]
              + " - " + self.df_ds.iloc[0]["collection_end"]),  # Temp Coverage
             self.df_ds.iloc[0]["topic_tags"],  # Keywords
             self.df_ds.iloc[0]["participants_invited"],  # part invited
             self.df_ds.iloc[0]["participants_included"],  # part included
             md.get_num_vars(
                 self.df_ds.iloc[0]["source"],
                 self.df_ds.iloc[0]["table"]
                 ),  # Number of variables
             int(self.df_ds.iloc[0]["num_rows"]),  # Number of observations
             "None",  # Restrictions to Data Use
             md.make_hlink("https://explore.ukllc.ac.uk/",
                           "https://explore.ukllc.ac.uk/")  # data request
            ]
        ]

        df_ss_info = pd.DataFrame(ds_info_list, index=[
            "Dataset Descriptor",
            "Dataset-specific Information"]
            ).T
        df_ss_info = DocHelper.style_table("_", df_ss_info)
        return df_ss_info

    def version_history(self):
        """Creates and displays version history table for dataset

        Args:
            self.source (str): source i.e. study (e.g. "ALSPAC" or "BCS70")
            self.dataset (str): dataset (e.g. "serology1m")

        Returns:
            markdown: markdown of DF of version history information for dataset
        """

        dsvs = md.get_md_api_dsvs()
        dsvs = dsvs[(dsvs["source"] == self.source)
                    & (dsvs["table"] == self.dataset)]
        dsvs["version_num"] = dsvs["version_num"].apply(
            lambda x: "Version " + str(int(x.split("v")[1])))
        dsvs["version_date"] = dsvs["version_date"].apply(
            lambda x: datetime.strftime(datetime.strptime(
                str(int(x)), "%Y%m%d"), "%d %b %Y"))
        dsvs["num_columns"] = dsvs["num_columns"].apply(lambda x: int(x))
        dsvs["num_participants"] = dsvs["num_participants"].apply(
            lambda x: int(x))
        dsvs["DOI"] = "10.83126/ukllc-dataset-00032-01"  # placeholder for now
        dsvs2 = dsvs[["version_num",
                      "version_date",
                      "num_columns",
                      "num_participants",
                      "DOI"]].rename(
                        columns={
                            "version_num": "Version Number",
                            "version_date": "Version Date",
                            "num_columns": "Number of Variables",
                            "num_participants": "Number of Participants"}
                            ).set_index("Version Number")
        return dsvs2.T

    def change_log(self):
        """Creates and displays table showing change log for the dataset DOIs

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """

        return display(
            Markdown(
                "We are currently working on a change log "
                "which will show changes to the dataset's metadata."
                    ))

    def documentation(self):
        """Creates and displays docs showing change log for the dataset DOIs

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """

        return display(
            Markdown(
                "We are currently building a documentation storage system "
                "which will host relevant and useful documents related to "
                "datasets, groupings, and studies themselves."))

    def useful_syntax(self):
        """Creates and displays useful syntax saved for the datasets

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """
        return display(
            Markdown(
                "Below we will include syntax that may be helpful to other "
                "researchers in the UK LLC TRE. For longer scripts, we will "
                "include a snippet of the code plus a link to Git where you "
                "can find the full scripts."))


class LPSSource:
    """Class for LPS series featuring all functions for the GB pages
    """

    def __init__(self, source: str):
        """Init function to yield self.variables for subsequent functions

        Args:
            source (str): source i.e. study (e.g. "ALSPAC" or "BCS70")

        Returns:
           self.source (str): source i.e study
           self.df_ds (DF): dataframe of study information / metadata
           self.cohort_profile (str): profile paper DOI
           self.doi (str): UKLLC DOI of study
        """
        # define std input variables
        self.source = source
        self.df_ss = md.get_md_api_ss()[md.get_md_api_ss()["source"] == self.source]
        self.cohort_profile = md.get_md_api_profiles()[md.get_md_api_profiles()["source"] == self.source].iloc[0]["profile_doi"]

        def ss_doi(x: str):
            """Returns UKLLC DOI of series

            Args:
                x (str): source i.e. study

            Returns:
                str: UKLLC DOI of series
            """

            df = dcf.get_doi_series()
            if len(df[(df["source"] == x) & (df["state"] == "findable")]) == 1:
                return df[df["source"] == x].iloc[0]["id"]
            else:
                return "DOI TBC"

        self.doi = ss_doi(self.source)

        def cites(x: str):
            """Returns citation APA style for DOI and trio of citation DL links

            Args:
                x (str): UKLLC DOI of study

            Returns:
                str: formatted citation APA style
                str: trio of citation DL links
            """

            citeprocjson = "https://api.datacite.org/application/vnd.citationstyles.csl+json/"
            bibtex = "https://api.datacite.org/application/x-bibtex/"
            ris = "https://api.datacite.org/application/x-research-info-systems/"
            if x == "DOI TBC":
                apa_cite = "DOI and Citation TBC"
                dl_cites = "DOI and Citation Downloads TBC"

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
        """Returns and displays summary/aims of study

        Args:
            self.df_ss (DF): DF of study info and metadata

        Returns:
            markdown: displayed markdown of summary/aims of study
        """
        return display(Markdown(self.df_ss.iloc[0]["Aims"]))

    def info_table(self):
        """Returns and displays info/metrics table of study

        Args:
            self.df_ss (DF): DF of study info and metadata

        Returns:
            markdown/DF: markdown-formatted DF of info/metrics for study
        """

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

    def table_caption_ds(self):
        return display(Markdown("**Table 1:** Datasets and metrics in the UK "
                                "LLC belonging to {}.".format(self.source)))

    def datasets(self):
        """Returns table of datasets for study

        Args:
            self.source (str): source i.e. study (e.g. "ALSPAC")
        Returns:
            markdown: markdown-formatted table of datasets
        """

        # NOTE: old code using datacite api - remove if v2 of function approved
        # df = md.prep_dsvs_for_gb_pages()

        # ds_dois = dcf.get_doi_datasets()
        # ds_dois = ds_dois[ds_dois["state"] == "findable"]
        # ds_dois["source_table"] = ds_dois["attributes.titles"].apply(lambda x: x[1]["title"])

        # # TODO: latest dataset version DOI rather than 1st one
        # df["DOI"] = df["source_table"].apply(lambda x: ds_dois[ds_dois["source_table"] == x].iloc[0]["id"] if len(ds_dois[ds_dois["source_table"] == x]) == 1 else "DOI TBC")
        # df = df[df["source"] == self.source][["table", "table_name", "DOI"]].rename(columns={"table": "Table", "table_name": "Table Name"})
        # return DocHelper.style_table("_", df)

        df = md.prep_dsvs_for_gb_pages()
        df = df[df["source"] == self.source]
        df = df[[
            "table",
            "table_name",
            "participants_included",
            "num_rows",
            "num_columns"
        ]].rename(columns={
            "table": "Dataset",
            "table_name": "Dataset Name",
            "participants_included": "# Participants",
            "num_rows": "# Observations",
            "num_columns": "# Variables"
            })

        df["Dataset"] = df["Dataset"].apply(
            lambda x: md.make_hlink(
                "https://guidebook.ukllc.ac.uk/docs/LPS_data/Datasets/"
                "{}/Datasets/{}.html".format(self.source, x), x))
        df["# Observations"] = df["# Observations"].apply(lambda x: int(x))
        df["# Variables"] = df["# Variables"].apply(lambda x: int(x))
        return DocHelper.style_table("_", df)

    def linkages_plot(self):
        """Returns linkage plot for latest freeze as bar chart

        Args:
            self.source (str): source i.e. study

        Returns:
            figure: bokeh bar chart for linkage to different types of data
                    e.g. NHSE, NHSW, PLACE, DWP etc...
        """

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
        """Returns linkage plot for all freezes as bar chart

        Args:
            self.source (str): source i.e. study

        Returns:
            figure: tabs of bokeh bar charts for linkage to different linked
                    data e.g. NHSE, NHSW, PLACE, DWP etc...
        """

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
        """Creates and displays table showing change log for the dataset DOIs

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """

        return display(
            Markdown(
                "We are currently working on a change log "
                "which will show changes to the dataset's metadata."
                    ))

    def documentation(self):
        """Creates and displays docs showing change log for the dataset DOIs

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """

        return display(
            Markdown(
                "We are currently building a documentation storage system "
                "which will host relevant and useful documents related to "
                "datasets, groupings, and studies themselves."))


class NHSEDataSet:
    """Datasets in NHSE and subsequent functions for GB pages
    """

    def __init__(self, dataset: str):
        """Init function generating self.variables for later use in functions

        Args:
            dataset (str): name of NHSE dataset e.g. IAPT or HESCC

        Returns:
            self.dataset (str): dataset
            self.df_ds (DF) DF of dataset info / metrics
            self.doi (str): UKLLC DOI of dataset
            self.ed (str): latest extract date in "DD Mon YYYY" format
            self.apa_cite (str): citation of latest v DOI in APA style
            self.dl_cites (str): trio of DLable citations
            self.latest_v (str): DF of metrics of latest dataset version
        """

        def get_nhse_ds(x: str):
            """Returns DF of dataset info/metrics

            Args:
                x (str): dataset e.g. "IAPT" or "HESCC"

            Returns:
                DF: dataframe of dataset info/metrics
            """

            ds = md.get_md_api_dss()
            df_ds = ds[(ds["source"] == "NHSE") & (ds["table"] == x)]
            df_ds["source_table"] = df_ds["source"] + "_" + df_ds["table"]
            ss = md.get_md_api_ss()[["source", "Owner"]]
            df_ds = df_ds.merge(ss, on="source")
            df_gb_temp = md.get_nhs_gb_info(x)
            df_ds = df_ds.merge(df_gb_temp, on="table")
            return df_ds

        def ds_doi(x: str):
            """Returns UKLLC DOI of dataset

            Args:
                x (str): dataset e.g. "IAPT" or "HESCC"

            Returns:
                str: UKLLC DOI of dataset or "DOI TBC" if none minted
            """

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

        def get_ed(x: str):
            """Returns latest extracte date of NHSE dataset

            Args:
                x (str): NHSE dataset e.g. IAPT or HESCC

            Returns:
                str: Date of last extract in DD Mon YYYY form
            """

            req = requests.get("https://metadata-api-4a09f2833a54.herokuapp.com/nhs-extract-dates/", headers={'access_token': os.environ['FASTAPI_KEY'] })
            df_ed = pd.json_normalize(json.loads(req.text))
            df_ed = df_ed[df_ed["dataset"].str.startswith(x)].sort_values(by="date", ascending=False)
            return df_ed.iloc[0]["date"]

        def cites(x: str):
            """Returns citation APA style and trio of DL links

            Args:
                x (str): UKLLC DOI of dataset

            Returns:
                str: APA style citation of dataset
                str: trio of DL links for citation
            """

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

                apa_cite = cite['creators'][0]["name"].strip() + \
                    ". (" + str(cite["publicationYear"]) + "). <i>" + \
                    cite["titles"][0]["title"] + \
                    ".</i> " + \
                    cite["publisher"] + \
                    ". " + md.make_hlink("https://doi.org/" + x, "https://doi.org/" + x)

                dl_cites = md.make_hlink(citeprocjson + x, "Citeproc JSON") + "&nbsp;&nbsp;&nbsp;&nbsp;" + \
                    md.make_hlink(bibtex + x, "BibTeX") + "&nbsp;&nbsp;&nbsp;&nbsp;" + md.make_hlink(ris + x, "RIS")

                return apa_cite, dl_cites

        def get_latest_dsvs(x: str):
            """Returns dataframe of metrics for latest version of dataset

            Args:
                x (str): name of dataset e.g. IAPT or HESCC

            Returns:
                DF: dataframe of metrics for latest version
            """

            dss1 = md.get_md_api_dss()
            dss1["source_table"] = dss1["source"] + "_" + dss1["table"]
            dsvs1 = md.get_md_api_dsvs()
            dsvs1 = dsvs1[dsvs1["source"] == "nhsd"]
            dsvs1["source"] = "NHSE"
            dsvs1["version_num"] = dsvs1["version_num"].fillna("v0001")
            def rm_aux_dss(x):
                if x.split("_")[0] in ["CSDS", "IAPT", "MHSDS", "HESOP", "HESAE"]:
                    return x.split("_")[0].upper()
                else:
                    return x.upper()

            dsvs1["table"] = dsvs1["table"].apply(lambda x: rm_aux_dss(x))

            def rm_aux_dss_full(x):
                if x.split("_")[0] in ["CSDS", "IAPT", "MHSDS", "HESOP", "HESAE"]:
                    return x.split("_")[0] + "_" + x.split("_")[-1]
                else:
                    return x

            dsvs1["table_full"] = dsvs1["table_full"].apply(lambda x: rm_aux_dss_full(x))
            dsvs1 = dsvs1.sort_values("num_columns", ascending=False)
            dsvs1 = dsvs1.drop_duplicates(subset=["table_full"])
            dsvs1["source_table"] = dsvs1["source"] + "_" + dsvs1["table"]
            dsvs1["version_num"] = dsvs1["version_num"].\
                apply(lambda x: int(x.replace("v", "")))
            def rename_reg_dss(table, vdate):
                return table + "_" + str(int(vdate))
            dsvs1["table"] = dsvs1.apply(lambda row: rename_reg_dss(row["table"], row["version_date"]) if row["table"] in ["CANCER", "DEMOGRAPHICS", "MORTALITY"] else row["table"], axis=1)
            def rename_reg_src_tbl(src, tbl):
                return src + "_" + tbl
            dsvs1["source_table"] = dsvs1.apply(lambda row: rename_reg_src_tbl(row["source"], row["table"]) if row["source_table"] in ["NHSE_CANCER", "NHSE_DEMOGRAPHICS", "NHSE_MORTALITY"] else row["source_table"], axis=1)
            def infill_vdates(vdate, vnum):
                    vdict = {1: 20221221.0, 2: 20230413.0, 3: 20240426.0}
                    if np.isnan(vdate):
                        return vdict[vnum]
                    else:
                        return vdate

            dsvs1["version_date"] = dsvs1.apply(lambda row: infill_vdates(row["version_date"], row["version_num"]), axis=1)
            if dataset == "HESAPC":
                dsvs_i = dsvs1[dsvs1["source_table"] == "NHSE_" + x]
            else:
                dsvs_i = dsvs1[dsvs1["source_table"].str.startswith("NHSE_" + x)]

            dsvs_i = dsvs_i.sort_values("version_date", ascending=False).head(1)
            dsvs_i["num_columns"] = dsvs_i["num_columns"].apply(lambda x: int(x))
            dsvs_i["num_rows"] = dsvs_i["num_rows"].apply(lambda x: int(x))
            return dsvs_i

        # define std input variables
        self.dataset = dataset
        self.df_ds = get_nhse_ds(self.dataset)
        self.doi = ds_doi(self.df_ds.iloc[0]["table"])
        self.ed = get_ed(self.dataset)
        self.apa_cite, self.dl_cites = cites(self.doi)
        self.latest_v = get_latest_dsvs(self.dataset)

    def title(self):
        """Returns title of dataset

        Args:
            self.df_ds (DF): dataframe of dataset metrics

        Returns:
            markdown: markdown of table name in "# TITLE" format
        """
        return display(Markdown("# " + self.df_ds.iloc[0]["table_name"] + " (" + self.df_ds.iloc[0]["source"] + ")"))

    def three_sec_summary(self):
        """Returns mini-summary of dataset

        Args:
            self.df_ds (DF): dataframe of dataset metrics

        Returns:
            markdown: markdown of summary of table
        """

        return display(Markdown('<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>{}</strong></div>'.format(self.df_ds.iloc[0]["short_desc"])))

    def summary(self):
        """Returns summary of dataset

        Args:
            self.df_ds (DF): dataframe of dataset metrics

        Returns:
            markdown: markdown of table summary
        """

        return display(Markdown(self.df_ds.iloc[0]["long_desc"]))

    def info_table(self):
        """Returns and displays info/metrics table of study

        Args:
            self.df_ds (DF): DF of dataset info/metadata

        Returns:
            markdown/DF: markdown-formatted DF of info/metrics for study
        """

        ds_info_list = [
        [
            "Name of Dataset in TRE",
            "Citation (APA)",
            "Download Citation",
            "Series",
            "Owner",
            "Temporal Coverage in the TRE",
            "Geographical Coverage",
            "Participant Count",
            "Number of Variables",
            "Number of Observations",
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
            self.df_ds.iloc[0]["source_name"], # Owner
            self.df_ds.iloc[0]["collection_start"] + " - " + self.df_ds.iloc[0]["collection_end"], # Temporal Coverage
            self.df_ds.iloc[0]["Geographical_coverage"], # Geo Coverage
            self.df_ds.iloc[0]["participants_included"], # Participant Count
            "N/A - Dataset comprises of multiple auxiliary tables" if self.dataset in ["IAPT", "MHSDS", "CSDS"] else self.latest_v.iloc[0]["num_columns"], # Number of Variables
            "N/A - Dataset comprises of multiple auxiliary tables" if self.dataset in ["IAPT", "MHSDS", "CSDS"] else self.latest_v.iloc[0]["num_rows"], # Number of Observations
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
        """Returns cohort counts for datasets and auxiliary dataset
            if applicable (e.g. for IAPT and MHSDS)

        Args:
            self.dataset (str): dataset e.g. IAPT or HESCC

        Returns:
            str: "TBC" for any datasets not in cohort-count API
            OR
            figure: bokeh datacube of cohort counts
        """

        if self.dataset in ["MHSDS", "CSDS", "HESAE", "HESAPC", "HESOP"]:
            return display(Markdown("Cohort counts for the {} dataset will be issued in due course.".format(self.dataset)))

        else:
            output_notebook(hide_banner=True)
            df = md.get_md_api_dsvs()
            df = df[(df["source"] == "nhsd") & (df["table"].str.startswith(self.dataset))].drop_duplicates(subset="table")

            dfcc = md.get_nhse_cohort_counts(df.iloc[0]["table"])

            tbl_names = []
            metrics_tables = []

            for i in range(0, len(df)):
                dfcc = md.get_nhse_cohort_counts(df.iloc[i]["table"])
                dfcc = dfcc[~dfcc['cohort'].isin(['GENSCOT', 'NICOLA', 'SABRE'])]
                tbl_names += len(dfcc) * [df.iloc[i]["table"]]
                dfcc["count"] = dfcc["count"].replace("<10", "0").astype(int)
                metrics_tables.append(dfcc)

            source = ColumnDataSource(data=dict(
                d0=tbl_names,
                d1=pd.concat(metrics_tables)["cohort"].to_list(),
                px=pd.concat(metrics_tables)["count"].to_list(),
            ))

            target = ColumnDataSource(data=dict(row_indices=[], labels=[]))

            formatter = StringFormatter(font_style='bold')

            columns = [
                TableColumn(field='d1', title='{} Dataset'.format(self.dataset), width=80, sortable=False, formatter=formatter),
                TableColumn(field='px', title='Participant Count', width=40, sortable=False),
            ]

            grouping = [
                GroupingInfo(getter='d0', aggregators=[SumAggregator(field_='px')]),
            ]

            cube = DataCube(source=source, columns=columns, grouping=grouping, target=target)
            display(Markdown("Click on the plus sign to see the number of participants represented in each dataset."))
            display(Markdown("**Table 2:** Participants from each LPS represented in the {} dataset in the UK LLC TRE. **Note:** Individual cohort counts of less than 10 are suppressed to 0 and are therefore excluded from total participant counts for datasets".format(self.dataset)))
            show(cube)

    def version_history(self):
        """Creates and displays version history table for dataset

        Args:
            self.dataset (str): dataset (e.g. "IAPT" or "CANCER)

        Returns:
            markdown: markdown of DF of version history information for dataset
        """

        dss1 = md.get_md_api_dss()
        dss1["source_table"] = dss1["source"] + "_" + dss1["table"]
        dsvs1 = md.get_md_api_dsvs()
        dsvs1 = dsvs1[dsvs1["source"] == "nhsd"]
        dsvs1["source"] = "NHSE"
        dsvs1["version_num"] = dsvs1["version_num"].fillna("v0001")
        def rm_aux_dss(x):
            if x.split("_")[0] in ["CSDS", "IAPT", "MHSDS", "HESOP", "HESAE"]:
                return x.split("_")[0].upper()
            else:
                return x.upper()

        dsvs1["table"] = dsvs1["table"].apply(lambda x: rm_aux_dss(x))

        def rm_aux_dss_full(x):
            if x.split("_")[0] in ["CSDS", "IAPT", "MHSDS", "HESOP", "HESAE"]:
                return x.split("_")[0] + "_" + x.split("_")[-1]
            else:
                return x

        dsvs1["table_full"] = dsvs1["table_full"].apply(lambda x: rm_aux_dss_full(x))
        dsvs1 = dsvs1.sort_values("num_columns", ascending=False)
        dsvs1 = dsvs1.drop_duplicates(subset=["table_full"])
        dsvs1["source_table"] = dsvs1["source"] + "_" + dsvs1["table"]
        dsvs1["version_num"] = dsvs1["version_num"].\
            apply(lambda x: int(x.replace("v", "")))

        def rename_reg_dss(table, vdate):
            return table + "_" + str(int(vdate))
        dsvs1["table"] = dsvs1.apply(lambda row: rename_reg_dss(row["table"], row["version_date"]) if row["table"] in ["CANCER", "DEMOGRAPHICS", "MORTALITY"] else row["table"], axis=1)

        def rename_reg_src_tbl(src, tbl):
            return src + "_" + tbl
        dsvs1["source_table"] = dsvs1.apply(lambda row: rename_reg_src_tbl(row["source"], row["table"]) if row["source_table"] in ["NHSE_CANCER", "NHSE_DEMOGRAPHICS", "NHSE_MORTALITY"] else row["source_table"], axis=1)

        def infill_vdates(vdate, vnum):
                vdict = {1: 20221221.0, 2: 20230413.0, 3: 20240426.0}
                if np.isnan(vdate):
                    return vdict[vnum]
                else:
                    return vdate

        dsvs1["version_date"] = dsvs1.apply(lambda row: infill_vdates(row["version_date"], row["version_num"]), axis=1)
        ds_dois = dcf.get_doi_datasets()
        ds_dois = ds_dois[ds_dois["state"] == "findable"]
        ds_dois["source_table"] = ds_dois["attributes.titles"].apply(lambda x: x[1]["title"])
        ds_dois["attributes.version"] = ds_dois["attributes.version"].apply(lambda x: int(x))
        dsvsf = dsvs1.merge(ds_dois, left_on=["source_table", "version_num"], right_on=["source_table", "attributes.version"])[["source_table", "version_num", "version_date", "num_columns", "num_rows", "id"]]
        if self.dataset == "HESAPC":
            dsvs_i = dsvsf[dsvsf["source_table"] == "NHSE_" + self.dataset]
        else:
            dsvs_i = dsvsf[dsvsf["source_table"].str.startswith("NHSE_" + self.dataset)]

        dsvs_i = dsvs_i.sort_values("version_date")
        dsvs_i["version_date"] = dsvs_i["version_date"].apply(lambda x: datetime.strftime(datetime.strptime(str(int(x)), "%Y%m%d"), "%d %b %Y"))
        dsvs_i["num_columns"] = dsvs_i["num_columns"].apply(lambda x: int(x))
        dsvs_i["num_rows"] = dsvs_i["num_rows"].apply(lambda x: int(x))
        dsvs_i = dsvs_i.rename(columns = {"source_table": "Name in TRE", "version_num": "Version Number", "version_date": "Version Date", "num_columns": "Number of Variables", "num_rows": "Number of Rows", "id": "DOI"}).set_index("Version Number")

        return dsvs_i.T

    def change_log(self):
        """Creates and displays table showing change log for the dataset DOIs

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """

        return display(
            Markdown(
                "We are currently working on a change log "
                "which will show changes to the dataset's metadata."
                    ))

    def documentation(self):
        """Creates and displays docs showing change log for the dataset DOIs

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """

        return display(
            Markdown(
                "We are currently building a documentation storage system "
                "which will host relevant and useful documents related to "
                "datasets, groupings, and studies themselves."))

    def useful_syntax(self):
        """Creates and displays useful syntax saved for the datasets

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """

        return display(
            Markdown(
                "Below we will include syntax that may be helpful to other "
                "researchers in the UK LLC TRE. For longer scripts, we will "
                "include a snippet of the code plus a link to the [UK LLC GitHub](https://github.com/UKLLC) repository where you "
                "can find the full scripts."))