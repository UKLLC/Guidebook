import os
import requests
import json
import pandas as pd

API_KEY = os.environ['FASTAPI_KEY']


def get_nhse_cohort_counts(ds: str) -> pd.DataFrame:
    """Returns cohort counts per study for a given NHSE dataset

    Args:
        ds (str): NHSE dataset name e.g. "IAPT" or "HESCC"

    Returns:
        DF: dataframe of cohort participant counts
    """

    url = ("https://metadata-api-4a09f2833a54.herokuapp.com/nhs-dataset-counts/"
           + "?table={}".format(ds))
    r = requests.get(url, headers={'access_token': API_KEY})
    data = r.text
    pj = json.loads(data)
    return pd.json_normalize(pj)[["cohort", "count"]]


def get_nhs_gb_info(ds: str) -> pd.DataFrame:
    """Returns additional information for NHSE datasets not in "datasets"
    endpoint for GB pages
    NOTE: endpoint and table may be removed in the future

    Args:
        ds (str): dataset name e.g. IAPT or HESCC

    Returns:
        pd.DataFrame: additional info for dataset needed for GB
    """
    req = requests.get(
        "https://metadata-api-4a09f2833a54.herokuapp.com/nhs-datasets-gb/"
        "?Name_of_dataset_in_TRE={}".format(ds),
        headers={'access_token': API_KEY})

    df = pd.json_normalize(json.loads(req.text))
    return df[
        ["Name_of_dataset_in_TRE",
         "Keywords",
         "Key_link",
         "Geographical_coverage",
         "Specific_restrictions_to_data_use"]
               ].rename(columns={"Name_of_dataset_in_TRE": "table"})


def get_md_api_ss() -> pd.DataFrame:
    """Returns all series metadata from MD API

    Returns:
        pd.DataFrame: DF of all series metadata
    """

    r_d = requests.get(
        "https://metadata-api-4a09f2833a54.herokuapp.com/source",
        headers={'access_token': API_KEY.strip()})

    # return error message if API response != 200
    try:
        r_d.raise_for_status()

    except requests.exceptions.HTTPError as err:
        return "HTTP Error: " + str(err)

    return pd.DataFrame(json.loads(r_d.text))


def get_md_api_profiles() -> pd.DataFrame:
    """Returns all cohort profile papers for all LPS

    Returns:
        pd.DataFrame: DF of cohort profile papers
    """

    r_d = requests.get(
        "https://metadata-api-4a09f2833a54.herokuapp.com/all-source-profiles",
        headers={'access_token': API_KEY.strip()})

    # return error message if API response != 200
    try:
        r_d.raise_for_status()

    except requests.exceptions.HTTPError as err:
        return "HTTP Error: " + str(err)

    return pd.DataFrame(json.loads(r_d.text))


def get_md_api_dss() -> pd.DataFrame:
    """Returns all metadata for all datasets in /all-datasets endpoing in API

    Returns:
        pd.DataFrame: DF of all dataset metadata
    """

    r_d = requests.get(
        "https://metadata-api-4a09f2833a54.herokuapp.com/all-datasets",
        headers={'access_token': API_KEY.strip()})

    # return error message if API response != 200
    try:
        r_d.raise_for_status()

    except requests.exceptions.HTTPError as err:
        return "HTTP Error: " + str(err)

    dsall = pd.DataFrame(json.loads(r_d.text))
    return dsall[dsall["table"] != "Custom"]


def get_md_api_dsvs() -> pd.DataFrame:
    """Returns all dataset versions from MD DB

    Returns:
        DF: dataframe of all dataset versions from MD DB
    """

    r_d = requests.get(
      "https://metadata-api-4a09f2833a54.herokuapp.com/all-datasets-versions",
      headers={'access_token': API_KEY.strip()})

    # return error message if API response != 200
    try:
        r_d.raise_for_status()

    except requests.exceptions.HTTPError as err:
        return "HTTP Error: " + str(err)

    dsall = pd.DataFrame(json.loads(r_d.text))

    # return dsall[(dsall["source"] != "nhsd") & (dsall["source"] != "GEO")]
    return dsall


def prep_dsvs_for_gb_pages(infill: str) -> pd.DataFrame:
    """Reads datasets and datasets-versions endpoints along with
    dsvs_infill.csv file to create necessary info for GB pages

    Args:
        infill (str): path of dsvs_infill.dsv file

    Returns:
        pd.DataFrame: prepped DF of datasets
    """

    dss1 = get_md_api_dss()
    dss1["source_table"] = dss1["source"] + "_" + dss1["table"]
    dsvs1 = get_md_api_dsvs()
    dsvs1 = dsvs1[~dsvs1["num_rows"].isnull()]
    dsvs1["source_table"] = dsvs1["source"] + "_" + dsvs1["table"]
    dsvs2 = dsvs1.merge(dss1, how="left", left_on="source_table",
                        right_on="source_table")
    ss1 = get_md_api_ss()
    dsvs3 = dsvs2.merge(ss1, how='inner', left_on="source_x",
                        right_on="source")
    dsvs3["version_num"] = dsvs3["version_num"].\
        apply(lambda x: int(x.replace("v", "")))
    dsvs_t1 = dsvs3[[
        "source",
        "source_table",
        "version_num",
        "table_x",
        "version_date",
        "table_name",
        "long_desc",
        "collection_start",
        "collection_end",
        "topic_tags",
        "source_name_x",
        "research_grouping",
        "participants_invited",
        "participants_included",
        "num_rows",
        "Owner",
        "geographic_coverage_Nations",
        "geographic_coverage_Regions"
        ]]
    dsvs_t2 = dsvs_t1.\
        rename(columns={"table_x": "table", "source_name_x": "source_name"})
    dsvs_t2.loc[
        (dsvs_t2["source_table"] == "GLAD_FILE2") &
        (dsvs_t2["version_date"] == 20231107.0), "version_num"] = 2
    dsvs_t3 = dsvs_t2.sort_values('version_num').drop_duplicates('table',
                                                                 keep='last')
    dsvs_t3 = dsvs_t3.set_index("source_table", drop=False)
    df_infill = pd.read_csv(infill, sep=",")
    df_infill["source_table"] = df_infill["source"] + "_" + df_infill["table"]
    df_infill = df_infill.set_index(
        'source_table',
        drop=False).rename(columns={"new_table_name": "table_name"})
    dsvs_t3 = dsvs_t3.fillna(df_infill)
    dsvs_t3["collection_start"] = dsvs_t3["collection_start"].fillna("Unknown")
    dsvs_t3["collection_end"] = dsvs_t3["collection_end"].fillna("Unknown")
    return dsvs_t3.fillna("")


def make_hlink(url: str, text: str) -> str:
    """Makes HTML hyperlink

    Args:
        url (str): url to link to (e.g. "https://guidebook.ukllc.ac.uk/")
        text (str): text (e.g. "Click Here for Guidebook")

    Returns:
        str: hyperlink in HTML format
    """

    return ' <a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.\
        format(url, text)


def get_num_vars(source: str, table_name: str) -> int:
    """Reads dataset metadata endpoint to get number of variables

    Args:
        source (str): source e.g. "ALSPAC" or "nhsd"
        table_name (str): table name e.g. "serology1m" or "MORTALITY"

    Returns:
        int: number of variables
    """

    response = requests.get(
        "https://metadata-api-4a09f2833a54.herokuapp.com/datasets/"
        "{{source_and_table_name}}?source={}&table_name={}".
        format(source.lower(),
               table_name.lower()),
        headers={'access_token': API_KEY.strip()})

    return len(pd.DataFrame(json.loads(response.text))
               ["variable_name"].unique())


def get_md_api_frz_link_nhse() -> pd.DataFrame:
    """Returns dataframe of all freeze linkage rates (NHSE only for now)

    Returns:
        pd.DataFrame: dataframe of all freeze linkage metrics
    """
    r_d = requests.get(
            "https://metadata-api-4a09f2833a54.herokuapp.com/"
            "freeze-linkage-nhse/",
            headers={'access_token': API_KEY.strip()})

    try:
        r_d.raise_for_status()

    except requests.exceptions.HTTPError as err:
        return "HTTP Error: " + str(err)

    return pd.DataFrame(json.loads(r_d.text))
