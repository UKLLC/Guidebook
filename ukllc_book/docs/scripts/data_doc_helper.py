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
                          TableColumn, HoverTool)
from bokeh.io import output_notebook
from math import pi
from datetime import datetime
import datacite_api_functions as dcf
import numpy as np

pd.options.mode.chained_assignment = None

dc_env = "TEST"

# DataCite API test env variables
if dc_env == "TEST":
    url_doi = "api.test.datacite.org"
    prefix = "10.83126"
# DataCite API prod  env variables
elif dc_env == "PROD":
    url_doi = "api.datacite.org"
    prefix = "10.71760"


def last_modified():
    return display(
        Markdown(">Last modified: {}".format(
            datetime.strftime(datetime.now(), "%d %b %Y"))))


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
        df = md.prep_dsvs_for_gb_pages()
        self.df_ds = df[df["source_table"] == source + "_" + dataset]

        def ds_doi(ss, ds: str):
            """Returns UKLLC DOI of LPS dataset

            Args:
                ss (str): source e.g. "ALSPAC" or "BCS70"
                ds (str): dataset e.g. "serology1m" or "bcs10_housing"

            Returns:
                str: UKLLC DOI of dataset or "DOI TBC" if none minted
            """

            doi_ds = dcf.get_doi_datasets()[dcf.get_doi_datasets()["state"] == "findable"]

            if len(doi_ds) == 0:
                return "DOI TBC"

            else:
                doi_ds["source_table"] = doi_ds["attributes.titles"].apply(lambda x: x[1]["title"] if len(x) > 1 else "NA")

                doi_ds = doi_ds[doi_ds["source_table"] == ss + "_" + ds]
                doi_ds = doi_ds.sort_values(by="attributes.version", ascending=False).drop_duplicates(subset="source_table")

                if len(doi_ds) == 1:
                    return doi_ds.iloc[0]["id"]
                else:
                    return "DOI TBC"

        self.doi = ds_doi(self.source, self.dataset)

        def cites(x: str):
            """Returns citation APA style for DOI and trio of citation DL links

            Args:
                x (str): UKLLC DOI of dataset

            Returns:
                str: formatted citation APA style
                str: trio of citation DL links
            """

            citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
            bibtex = "https://{}/application/x-bibtex/".format(url_doi)
            ris = "https://{}/application/x-research-info-systems/".format(url_doi)
            if x == "DOI TBC":
                apa_cite = "DOI and Citation TBC"
                dl_cites = "DOI and Citation Downloads TBC"

            else:
                cite = json.loads(requests.get(
                    "https://{}/dois/".format(url_doi) + x,
                ).text)['data']['attributes']

                citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
                bibtex = "https://{}/application/x-bibtex/".format(url_doi)
                ris = "https://{}/application/x-research-info-systems/".format(url_doi)

                apa_cite = cite['creators'][0]["name"] + \
                    ". (" + str(cite["publicationYear"]) + "). <i>" + \
                    cite["titles"][0]["title"] + \
                    ".</i> " + \
                    cite["publisher"] + \
                    ". " + md.make_hlink("https://doi.org/" + x, "https://doi.org/" + x)

                dl_cites = md.make_hlink(citeprocjson + x, "Citeproc JSON") + "&nbsp;&nbsp;&nbsp;&nbsp;" + \
                    md.make_hlink(bibtex + x, "BibTeX") + "&nbsp;&nbsp;&nbsp;&nbsp;" + md.make_hlink(ris + x, "RIS")

            return apa_cite, dl_cites

        self.apa_cite, self.dl_cites = cites(self.doi)

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
             self.apa_cite,  # Citation
             self.dl_cites,  # Download Cite
             md.make_hlink_same_tab(
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
        dsvs["source_table"] = dsvs["source"] + "_" + dsvs["table"]
        dsvs["version_num"] = dsvs["version_num"].\
            apply(lambda x: int(x.replace("v", "")))

        # fill missing n_rows
        dsvs["num_rows"] = dsvs["num_rows"].fillna(0.0)

        # manual editing v nums to avoid duplicates
        dsvs.loc[
            (dsvs["source_table"] == "GLAD_FILE2") &
            (dsvs["version_date"] == 20231107.0), "version_num"] = 2

        dsvs.loc[
            (dsvs["source_table"] == "GENSCOT_SMOKING") &
            (dsvs["version_date"] == 20220302.0), "version_num"] = 2

        dsvs.loc[
            (dsvs["source_table"] == "GENSCOT_SPQ") &
            (dsvs["version_date"] == 20220302.0), "version_num"] = 2

        ds_dois = dcf.get_doi_datasets()
        ds_dois = ds_dois[ds_dois["state"] == "findable"]

        # create dummy cols if zero DOIs minted
        if len(ds_dois) == 0:
            ds_dois["source_table"] = ""
            ds_dois["attributes.version"] = ""

        else:
            ds_dois["source_table"] = ds_dois["attributes.titles"].apply(lambda x: x[1]["title"])
            ds_dois["attributes.version"] = ds_dois["attributes.version"].apply(lambda x: int(x))
            ds_dois = ds_dois[ds_dois["source_table"] == self.source + "_" + self.dataset]

        dsvs2 = dsvs.merge(ds_dois, how="left", left_on=["source_table", "version_num"], right_on=["source_table", "attributes.version"])[["source_table", "version_num", "version_date", "num_participants", "num_columns", "num_rows", "id"]]

        # infill missing DOI with TBC then make hlink for DOI and activities
        dsvs2["id"] = dsvs2["id"].fillna("TBC")
        dsvs2["act"] = dsvs2["id"].apply(lambda x: "TBC" if x == "TBC" else md.make_hlink("https://api.test.datacite.org/dois/" + x + "/activities", x + "/activities"))
        dsvs2["id"] = dsvs2["id"].apply(lambda x: "TBC" if x == "TBC" else md.make_hlink("https://doi.org/" + x, x))

        dsvs2["version_date"] = dsvs2["version_date"].apply(lambda x: datetime.strftime(datetime.strptime(str(int(x)), "%Y%m%d"), "%d %b %Y"))
        dsvs2["num_participants"] = dsvs2["num_participants"].apply(lambda x: "N/A" if np.isnan(x) else int(x))
        dsvs2["num_columns"] = dsvs2["num_columns"].apply(lambda x: int(x))
        dsvs2["num_rows"] = dsvs2["num_rows"].apply(lambda x: int(x))

        # remove part counts from table for now as missing from MDDB for NHS
        dsvs2 = dsvs2[["version_num",
                        "version_date",
                        "num_columns",
                        "num_rows",
                        "id",
                        "act"]].rename(
                        columns={
                            "version_num": "Version Number",
                            "version_date": "Version Date",
                            "num_columns": "Number of Variables",
                            "num_rows": "Number of Observations",
                            "id": "DOI",
                            "act": "Change Log"}
                            ).set_index("Version Number")

        dsvs2_T = dsvs2.T.reset_index().rename(columns={"index": "Version"})

        return DocHelper.style_table("_", dsvs2_T)

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
                "We are currently building a documentation storage system which will host useful documents related to datasets and data owners. We will surface these documents on Guidebook."))

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

            citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
            bibtex = "https://{}/application/x-bibtex/".format(url_doi)
            ris = "https://{}/application/x-research-info-systems/".format(url_doi)

            if x == "DOI TBC":
                apa_cite = "DOI and Citation TBC"
                dl_cites = "DOI and Citation Downloads TBC"

            else:
                cite = json.loads(requests.get(
                    "https://{}/dois/".format(url_doi) + x,
                ).text)['data']['attributes']

                citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
                bibtex = "https://{}/application/x-bibtex/".format(url_doi)
                ris = "https://{}/application/x-research-info-systems/".format(url_doi)

                apa_cite = cite['creators'][0]["name"] + \
                    ". (" + str(cite["publicationYear"]) + "). <i>" + \
                    cite["titles"][0]["title"] + \
                    ".</i> " + \
                    cite["publisher"] + \
                    ". " + md.make_hlink("https://doi.org/" + x, "https://doi.org/" + x)

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
            lambda x: md.make_hlink_same_tab(
                "{}.html".format(x), x))
        df["# Observations"] = df["# Observations"].apply(lambda x: '' if x == '' else int(x))
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

        if self.source in ["AIRWAVE", "UKREACH", "GENSCOT", "NICOLA", "SABRE"]:
            return display(Markdown("Linkage rates will be displayed for {} in due course.".format(self.source)))

        else:
            dff = md.get_md_api_frz_link_nhse()
            dff = dff[(dff["LPS"] == self.source) & (dff["frz_num"] == dff["frz_num"].max())]

            lx = ["NHS England", "NHS Wales"]
            ly = [100*(dff.iloc[0]["n_l_tot"]/dff.iloc[0]["n_sent"]), 0]
            lz = [dff.iloc[0]["n_sent"]] * 2
            ll = [dff.iloc[0]["n_l_tot"], 0 ]

            data = {
                "link_series": lx,
                "link_pct": ly,
                "n_sent": lz,
                "n_linked": ll
            }

            output_notebook(hide_banner=True)
            p = figure(x_range=lx, width=600, height=400, title="Linkage rates (%) of {} participants to linked Datasets for Freeze {}".format(self.source, dff["frz_num"].max()))
            p.vbar(x="link_series", top="link_pct", width=0.8, source=data)

            hover = HoverTool(tooltips=[
                ("Linked Participants", "@n_linked"),
                ("Participants sent to UK LLC", "@n_sent")])
            p.add_tools(hover)

            p.y_range.start = 0
            p.y_range.end = 100
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
                "We are currently building a documentation storage system which will host useful documents related to datasets and data owners. We will surface these documents on Guidebook."))


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
            # ss = md.get_md_api_ss()[["source", "Owner"]]
            # df_ds = df_ds.merge(ss, on="source")
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

            if len(doi_ds) == 0:
                return "DOI TBC"

            else:
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
            """Returns latest extract date of NHSE dataset

            Args:
                x (str): NHSE dataset e.g. IAPT or HESCC

            Returns:
                str: Date of last extract in DD Mon YYYY form
            """

            req = requests.get("https://metadata-api-4a09f2833a54.herokuapp.com/nhs-extract-dates/", headers={'access_token': os.environ['FASTAPI_KEY'] })
            df_ed = pd.json_normalize(json.loads(req.text))

            if x:
                df_ed = df_ed[df_ed["dataset"].str.startswith("HESAPC")].sort_values(by="date", ascending=False)
                return df_ed.iloc[0]["date"]
            else:
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

            citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
            bibtex = "https://{}/application/x-bibtex/".format(url_doi)
            ris = "https://{}/application/x-research-info-systems/".format(url_doi)
            if x == "DOI TBC":
                apa_cite = "DOI and Citation TBC"
                dl_cites = "DOI and Citation Downloads TBC"
                return apa_cite, dl_cites

            else:
                cite = json.loads(requests.get(
                    "https://{}/dois/".format(url_doi) + x,
                ).text)['data']['attributes']

                citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
                bibtex = "https://{}/application/x-bibtex/".format(url_doi)
                ris = "https://{}/application/x-research-info-systems/".format(url_doi)

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

        def cohort_total(ds):
            if ds in ["MHSDS", "IAPT", "CSDS"]:
                return "N/A - Dataset comprises of multiple auxiliary tables"
            else:
                df = md.get_nhse_cohort_counts(ds)
                df["count"] = df["count"].apply(lambda x: int(x.replace("<10", "0")))
                return str(df["count"].sum())

        # define std input variables
        self.dataset = dataset
        self.df_ds = get_nhse_ds(self.dataset)
        self.doi = ds_doi(self.df_ds.iloc[0]["table"])
        self.ed = get_ed(self.dataset)
        self.apa_cite, self.dl_cites = cites(self.doi)
        self.latest_v = get_latest_dsvs(self.dataset)
        self.participants = cohort_total(self.dataset)

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
            self.df_ds.iloc[0]["Owner"], # Owner
            self.df_ds.iloc[0]["collection_start"] + " - " + self.df_ds.iloc[0]["collection_end"], # Temporal Coverage
            self.df_ds.iloc[0]["Geographical_coverage"], # Geo Coverage
            self.participants, # Participant Count
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

        output_notebook(hide_banner=True)
        df = md.get_md_api_dsvs()
        def fix_hes(x):
            if x in ["HESAPC_acp", "HESAPC_mat"]:
                return x.upper()
            else:
                return x
        df["table"] = df["table"].apply(lambda x: fix_hes(x))
        df = df[(df["source"] == "nhsd") & (df["table"].str.startswith(self.dataset))].drop_duplicates(subset="table")

        df = df[~df["table"].isin(["MHSDS_MHS003AccommStatus", "MHSDS_MHS104RTT", "MHSDS_MHS301GroupSession", "MHSDS_MHS901StaffDetails", "CSDS_group_sessions"])]

        if self.dataset in ["HESAPC", "HESOP", "HESAE"]:
            df = df[df["table"] == self.dataset]

        tbl_names = []
        metrics_tables = []

        for i in range(0, len(df)):
            dfcc = md.get_nhse_cohort_counts(df.iloc[i]["table"])
            dfcc = dfcc[~dfcc['cohort'].isin(['GENSCOT', 'NICOLA', 'SABRE'])]
            tbl_names += len(dfcc) * [df.iloc[i]["table"]]
            dfcc["count"] = dfcc["count"].replace("<10", np.nan).astype(float)
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
            TableColumn(field='px', title='Participant Count', width=40, sortable=False, formatter=StringFormatter(text_align='right', nan_format='<10')),
        ]

        grouping = [
            GroupingInfo(getter='d0', aggregators=[SumAggregator(field_='px')]),
        ]

        cube = DataCube(source=source, columns=columns, grouping=grouping, target=target)
        display(Markdown("Click on the plus sign to see the number of participants represented in each dataset."))
        display(Markdown("**Table 2:** Participants from each LPS represented in the {} dataset in the UK LLC TRE. **Note:** Individual cohort counts of less than 10 are suppressed to <10 and excluded from total participant counts for datasets.".format(self.dataset)))
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

        # create dummy cols if zero DOIs minted
        if len(ds_dois) == 0:
            ds_dois["source_table"] = ""
            ds_dois["attributes.version"] = ""

        else:
            ds_dois["source_table"] = ds_dois["attributes.titles"].apply(lambda x: x[1]["title"])
            ds_dois["attributes.version"] = ds_dois["attributes.version"].apply(lambda x: int(x))

        dsvsf = dsvs1.merge(ds_dois, how="left", left_on=["source_table", "version_num"], right_on=["source_table", "attributes.version"])[["source_table", "version_num", "version_date", "num_participants", "num_columns", "num_rows", "id"]]
        if self.dataset == "HESAPC":
            dsvs_i = dsvsf[dsvsf["source_table"] == "NHSE_" + self.dataset]
        else:
            dsvs_i = dsvsf[dsvsf["source_table"].str.startswith("NHSE_" + self.dataset)]

        dsvs_i = dsvs_i.sort_values("version_date")

        dsvs_i["version_date"] = dsvs_i["version_date"].apply(lambda x: datetime.strftime(datetime.strptime(str(int(x)), "%Y%m%d"), "%d %b %Y"))
        dsvs_i["num_participants"] = dsvs_i["num_participants"].apply(lambda x: "N/A" if np.isnan(x) else int(x))
        dsvs_i["num_columns"] = dsvs_i["num_columns"].apply(lambda x: int(x))
        dsvs_i["num_rows"] = dsvs_i["num_rows"].apply(lambda x: int(x))

        # infill missing DOIs as TBC
        dsvs_i["id"] = dsvs_i["id"].fillna("TBC")
        dsvs_i["Change Log"] = dsvs_i["id"].apply(lambda x: "TBC" if x == "TBC" else md.make_hlink("https://api.test.datacite.org/dois/{}/activities".format(x), x + "/activities"))
        dsvs_i["id"] = dsvs_i["id"].apply(lambda x: "TBC" if x == "TBC" else md.make_hlink("https://doi.org/" + x, x))



        if self.dataset in ["CANCER", "MORTALITY", "DEMOGRAPHICS"]:
            dsvs_i["version_num"] = dsvs_i.apply(lambda row: str(row["version_num"]) + " (" + row["version_date"] + ")", axis=1)

        dsvs_i = dsvs_i.rename(columns={"source_table": "Name in TRE", "version_num": "Version Number", "version_date": "Version Date", "num_participants": "Participant Count", "num_columns": "Number of Variables", "num_rows": "Number of Observations", "id": "DOI"})

        # remove part counts from table for now as missing from MDDB for NHS
        dsvs_i = dsvs_i[["Version Number",
                         "Version Date",
                         "Number of Variables",
                         "Number of Observations",
                         "DOI",
                         "Change Log"]].set_index("Version Number")
        dsvs_i_T = dsvs_i.T.reset_index().rename(columns={"index": "Version"})

        return DocHelper.style_table("_", dsvs_i_T)

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
                "We are currently building a documentation storage system which will host useful documents related to datasets and data owners. We will surface these documents on Guidebook."))

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


class NHSESource:
    """Class for NHSE series featuring all functions for the GB pages
    """

    def __init__(self):
        """Init function to yield self.variables for subsequent functions

        Args:
            source (str): source i.e. study (e.g. "ALSPAC" or "BCS70")

        Returns:
           self.source (str): source i.e study
           self.df_ds (DF): dataframe of study information / metadata
           self.doi (str): UKLLC DOI of NHSE
        """
        # define std input variables
        self.source = "NHSE"
        self.df_ss = md.get_md_api_ss()[md.get_md_api_ss()["source"] == self.source]

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

            citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
            bibtex = "https://{}/application/x-bibtex/".format(url_doi)
            ris = "https://{}/application/x-research-info-systems/".format(url_doi)
            if x == "DOI TBC":
                apa_cite = "DOI and Citation TBC"
                dl_cites = "DOI and Citation Downloads TBC"

            else:
                cite = json.loads(requests.get(
                    "https://{}/dois/".format(url_doi) + x,
                ).text)['data']['attributes']

                citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
                bibtex = "https://{}/application/x-bibtex/".format(url_doi)
                ris = "https://{}/application/x-research-info-systems/".format(url_doi)

                apa_cite = cite['creators'][0]["name"] + \
                    ". (" + str(cite["publicationYear"]) + "). <i>" + \
                    cite["titles"][0]["title"] + \
                    ".</i> " + \
                    cite["publisher"] + \
                    ". " + md.make_hlink("https://doi.org/" + x, "https://doi.org/" + x)

                dl_cites = md.make_hlink(citeprocjson + x, "Citeproc JSON") + "&nbsp;&nbsp;&nbsp;&nbsp;" + \
                    md.make_hlink(bibtex + x, "BibTeX") + "&nbsp;&nbsp;&nbsp;&nbsp;" + md.make_hlink(ris + x, "RIS")

            return apa_cite, dl_cites

        self.apa_cite, self.dl_cites = cites(self.doi)

    def info_table(self):
        """Returns and displays info/metrics table of NHSE

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
            "Geographical Coverage - Nations",
            "Start Date of Data Available",
            "Build a Data Request"
        ],
        [
            self.apa_cite,
            self.dl_cites,
            self.df_ss.iloc[0]["Owner"],
            self.df_ss.iloc[0]["geographic_coverage_Nations"],
            "1940s (GDPPR)",
            md.make_hlink("https://explore.ukllc.ac.uk/","https://explore.ukllc.ac.uk/")
        ]
        ]

        df_ss_info = pd.DataFrame(ss_info_list, index=["Series Descriptor", "Series-specific Information"]).T
        return DocHelper.style_table("_", df_ss_info)

    def datasets_table(self):
        df = md.get_md_api_dss()
        df = df[df["source"] == "NHSE"]
        df["date_available"] = df["collection_start"] + " - " + df["collection_end"]
        df["date_available"] = df["date_available"].fillna("N/A")
        # df = df[~df["table"].isin(["HESAPC_MAT", "HESAPC_ACP"])]

        owners = {
            "NHS England": "NHSE",
            "Department of Health and Social Care": "DHSC",
            "Office for National Statistics": "ONS"
            }

        df["owner_abbr"] = df["table"].apply(lambda x: owners[md.get_nhs_gb_info(x).iloc[0]["Owner"]])


        grps = {
            'MSDS': "Community",
            'HESOP': "Hospital",
            'DEMOGRAPHICS': "Registration",
            'MORTALITY': "Registration",
            'CANCER': "Registration",
            'HESAPC': "Hospital",
            'HESAPC_MAT': "Hospital",
            'HESAPC_ACP': "Hospital",
            'HESCC': "Hospital",
            'HESAE': "Hospital",
            'ECDS': "Hospital",
            'MHSDS': "Mental Health",
            'PCM': "Primary Care",
            'GDPPR': "Primary Care",
            'CVS': "COVID-19",
            'CVAR': "COVID-19",
            'CHESS': "COVID-19",
            'COVIDSGSS': "COVID-19",
            'NPEX': "COVID-19",
            'IELISA': "COVID-19",
            'CSDS': "Community",
            'IAPT': "Mental Health",
        }

        df["grouping"] = df["table"].apply(lambda x: grps[x])

        links = {
            "PCM": "../NHS_England/Primary_care_datasets/PCM/PCM.html",
            "HESOP": "../NHS_England/HES%20datasets/OP/HESOP.html",
            "HESAPC": "../NHS_England/HES%20datasets/APC/HESAPC.html",
            "HESAPC_ACP": "../NHS_England/HES%20datasets/ACP/HESAPC_ACP.html",
            "HESAPC_MAT": "../NHS_England/HES%20datasets/MAT/HESAPC_MAT.html",
            "HESCC": "../NHS_England/HES%20datasets/CC/HESCC.html",
            "ECDS": "../NHS_England/HES%20datasets/ECDS/ECDS.html",
            "HESAE": "../NHS_England/HES%20datasets/AE/HESAE.html",
            "COVIDSGSS": "../NHS_England/COVID%20datasets/COVIDSGSS/COVIDSGSS.html",
            "IELISA": "../NHS_England/COVID%20datasets/IELISA/IELISA.html",
            "NPEX": "../NHS_England/COVID%20datasets/NPEX/NPEX.html",
            "CHESS": "../NHS_England/COVID%20datasets/CHESS/CHESS.html",
            "CVS": "../NHS_England/COVID%20datasets/CVS/CVS.html",
            "CVAR": "../NHS_England/COVID%20datasets/CVAR/CVAR.html",
            "GDPPR": "../NHS_England/Primary_care_datasets/GDPPR/GDPPR.html",
            "CANCER": "../NHS_England/Registration%20datasets/CANCER/CANCER.html",
            "DEMOGRAPHICS": "../NHS_England/Registration%20datasets/DEMOGRAPHICS/DEMOGRAPHICS.html",
            "MORTALITY": "../NHS_England/Registration%20datasets/MORTALITY/MORTALITY.html",
            "MHSDS": "../NHS_England/Mental%20health%20datasets/MHSDS/MHSDS.html",
            "IAPT": "../NHS_England/Mental%20health%20datasets/IAPT/IAPT.html",
            "CSDS": "../NHS_England/Community%20datasets/CSDS/CSDS.html",
            "MSDS": "../NHS_England/Community%20datasets/MSDS/MSDS.html"
        }

        df = df.set_index("table", drop=False).reindex([
            "GDPPR",
            "PCM",
            "HESOP",
            "HESAPC",
            "HESAPC_ACP",
            "HESAPC_MAT",
            "HESCC",
            "ECDS",
            "HESAE",
            "COVIDSGSS",
            "IELISA",
            "NPEX",
            "CHESS",
            "CVS",
            "CVAR",
            "CANCER",
            "DEMOGRAPHICS",
            "MORTALITY",
            "MHSDS",
            "IAPT",
            "CSDS",
            "MSDS"
        ])

        df["table"] = df["table"].apply(lambda x: md.make_hlink_same_tab(links[x], x))
        df = df[
            [
                "table",
                "table_name",
                "grouping",
                "date_available",
                "owner_abbr"
            ]].rename(
                columns={
                "table": "Dataset",
                "table_name": "Dataset Name",
                "grouping": "Grouping",
                "date_available": "Data Available in TRE",
                "owner_abbr": "Data Owner"
            })

        return DocHelper.style_table("_", df)

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
                "We are currently building a documentation storage system which will host useful documents related to datasets and data owners. We will surface these documents on Guidebook."))


class PlaceDataSet:
    """Datasets in PLACE and subsequent functions for GB pages
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

        def get_place_ds(x):
            ds = md.get_md_api_dss()
            df_ds = ds[(ds["source"] == "PLACE") & (ds["table"] == x)]
            df_ds["source_table"] = df_ds["source"] + "_" + df_ds["table"]
            ss = md.get_md_api_ss()[["Owner", "source"]]
            df_ds = df_ds.merge(ss, on="source")
            df_ds["dataset"] = x
            df_ds2 = md.get_place_dataset_info()
            df_ds2 = df_ds2[df_ds2["dataset"] == x][["dataset", "geographical_coverage", "authors", "hyperlink"]]
            df_ds = df_ds.merge(df_ds2, on="dataset")

            return df_ds

        def get_lastest_dsvs(x):
            dsvs = md.get_md_api_dsvs()
            dsvs = dsvs[(dsvs["source"] == "PLACE") & (dsvs["table"] == x)]
            dsvs["source_table"] = dsvs["source"] + "_" + dsvs["table"]
            dsvs["version_num"] = dsvs["version_num"].\
                            apply(lambda x: int(x.replace("v", "")))
            dsvs = dsvs.sort_values(by="version_num", ascending=False).drop_duplicates(subset="table")
            dsvs["num_columns"] = dsvs["num_columns"].apply(lambda x: int(x))
            dsvs["num_rows"] = dsvs["num_rows"].apply(lambda x: int(x))
            return dsvs

        def ds_doi(x: str):
                """Returns UKLLC DOI of dataset

                Args:
                    x (str): dataset e.g. "IAPT" or "HESCC"

                Returns:
                    str: UKLLC DOI of dataset or "DOI TBC" if none minted
                """

                doi_ds = dcf.get_doi_datasets()[dcf.get_doi_datasets()["state"] == "findable"]

                if len(doi_ds) == 0:
                    return "DOI TBC"

                else:
                    doi_ds["source_table"] = doi_ds["attributes.titles"].apply(lambda x: x[1]["title"] if len(x) > 1 else "NA")

                    doi_ds = doi_ds[doi_ds["source_table"] == "GEO_" + x]
                    doi_ds = doi_ds.sort_values(by="attributes.version", ascending=False).drop_duplicates(subset="source_table")

                    if len(doi_ds) == 1:
                        return doi_ds.iloc[0]["id"]
                    else:
                        return "DOI TBC"

        def cites(x: str):
            """Returns citation APA style and trio of DL links

            Args:
                x (str): UKLLC DOI of dataset

            Returns:
                str: APA style citation of dataset
                str: trio of DL links for citation
            """

            citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
            bibtex = "https://{}/application/x-bibtex/".format(url_doi)
            ris = "https://{}/application/x-research-info-systems/".format(url_doi)
            if x == "DOI TBC":
                apa_cite = "DOI and Citation TBC"
                dl_cites = "DOI and Citation Downloads TBC"
                return apa_cite, dl_cites

            else:
                cite = json.loads(requests.get(
                    "https://{}/dois/".format(url_doi) + x,
                ).text)['data']['attributes']

                citeprocjson = "https://{}/application/vnd.citationstyles.csl+json/".format(url_doi)
                bibtex = "https://{}/application/x-bibtex/".format(url_doi)
                ris = "https://{}/application/x-research-info-systems/".format(url_doi)

                apa_cite = cite['creators'][0]["name"].strip() + \
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
        self.df_ds = get_place_ds(self.dataset)
        self.doi = ds_doi(self.df_ds.iloc[0]["table"])
        self.apa_cite, self.dl_cites = cites(self.doi)
        self.latest_v = get_lastest_dsvs(self.dataset)
        # self.participants = cohort_total(self.dataset)

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
            "Owner",
            "Authors",
            "Temporal Coverage",
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
            self.apa_cite,  # Citation
            self.dl_cites,  # Download Cite
            self.df_ds.iloc[0]["Owner"], # Owner
            self.df_ds.iloc[0]["authors"], # Owner
            self.df_ds.iloc[0]["collection_start"] + " - " + self.df_ds.iloc[0]["collection_end"], # Temporal Coverage
            self.df_ds.iloc[0]["geographical_coverage"], # Geo Coverage
            self.df_ds.iloc[0]["participants_included"], # Participant Count
            self.latest_v.iloc[0]["num_columns"], # Number of Variables
            self.latest_v.iloc[0]["num_rows"], # Number of Observations
            md.make_hlink(self.df_ds.iloc[0]["hyperlink"], self.df_ds.iloc[0]["hyperlink"]),
            self.df_ds.iloc[0]["topic_tags"], # Keywords
            "TBC", # self.ed,
            "None", # self.df_ds.iloc[0]["Specific_restrictions_to_data_use"], # Restrictions to Data Use
            md.make_hlink("https://explore.ukllc.ac.uk/","https://explore.ukllc.ac.uk/") # Build a data request
            ]
            ]

        df_ss_info = pd.DataFrame(ds_info_list, index=["Dataset Descriptor", "Dataset-specific Information"]).T
        return DocHelper.style_table("_", df_ss_info)

    def variable_table(self):
        df = md.get_table_vars("place", self.dataset)[["variable_name", "variable_label"]]
        df2 = md.get_place_var_info()
        df2 = df2[df2["dataset"] == self.dataset][["variable", "owner", "date_range", "category"]]
        df = df.merge(df2, left_on="variable_name", right_on="variable")[["category", "variable_name", "variable_label", "owner", "date_range"]]
        df = df.rename(columns={"category": "Variable Group", "variable_name": "Variable", "variable_label": "Description", "owner": "Source", "date_range": "Date range of data"})
        return DocHelper.style_table("_", df)

    def documentation(self):
        """Creates and displays docs showing change log for the dataset DOIs

        Returns:
            markdown: placeholder "TBC" text in markdown format
        """

        return display(
            Markdown(
                "We are currently building a documentation storage system which will host useful documents related to datasets and data owners. We will surface these documents on Guidebook."))

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
