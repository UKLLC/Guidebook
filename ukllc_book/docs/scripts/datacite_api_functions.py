import requests
import os
import pandas as pd

dc_env = "TEST"

# DataCite API test env variables
if dc_env == "TEST":
    ID = 'WHRN.UKLLCTEST'
    pw = os.environ['DATACITE_TEST_PW']
    url_doi = "api.test.datacite.org"
    prefix = "10.83126"
# DataCite API prod  env variables
elif dc_env == "PROD":
    ID = 'VHFS.UKLLC'
    pw = os.environ['DATACITE_PROD_PW']
    url_doi = "api.datacite.org"
    prefix = "10.71760"

headers_doi = {
    "accept": "application/vnd.api+json",
    "content-type": "application/json",
}


def get_doi_datasets() -> pd.DataFrame:
    """Returns UK LLC dataset DOIs

    Returns:
        pd.DataFrame: DF of UK LLC dataset version DOIs
    """

    resp_doi_ds_get = requests.get(
        "https://{}/dois?prefix={}&"
        "resource-type-id=dataset&&page[size]=1000&"
        "fields[dois]=creators%2Ctitles%2Cversion%2Cstate%2Cidentifiers".format(url_doi, prefix),
        headers={
            "accept": "application/vnd.api+json",
                },
        auth=(ID, pw)
        )

    doi_datasets = resp_doi_ds_get.json()

    doi_dss = pd.json_normalize(doi_datasets['data'])
    if len(doi_dss) == 0:
        return doi_dss.reindex(doi_dss.columns.union(
            ["id",
             "state",
             "attributes.identifiers",
             "creators",
             "title",
             "source_table"]
            ), axis=1)

    else:
        doi_dss['creators'] = doi_dss['attributes.creators']\
            .apply(lambda x: x[0]['name'])
        doi_dss['title'] = doi_dss['attributes.titles']\
            .apply(lambda x: x[0]['title'])

        doi_dss = doi_dss.rename(columns={"attributes.state": "state"})

        return doi_dss.drop(
            [
                'attributes.creators', 'type'
            ],
            axis=1
            )


def get_doi_series() -> pd.DataFrame:
    """Returns DF of UK LLC series DOIs

    Returns:
        pd.DataFrame: DF of UK LLC series DOIs
    """

    resp_doi_ds_get = requests.get(
        "https://{}/dois?prefix={}"
        "&resource-type-id=other&resource-type=series&&page[size]=1000"
        "&fields[dois]=creators%2Ctitles%2Cversion%2Cstate%2Cidentifiers".format(url_doi, prefix),
        headers={
            "accept": "application/vnd.api+json",
            }, auth=(ID, pw)
        )

    doi_sources = resp_doi_ds_get.json()

    doi_ss = pd.json_normalize(doi_sources['data'])
    if len(doi_ss) == 0:
        return doi_ss.reindex(doi_ss.columns.union(
            ["id",
             "state",
             "attributes.identifiers",
             "creators",
             "title",
             "source"]), axis=1)

    else:
        doi_ss['creators'] = doi_ss['attributes.creators']\
            .apply(lambda x: x[0]['name'])
        doi_ss['title'] = doi_ss['attributes.titles']\
            .apply(lambda x: x[0]['title'])
        doi_ss = doi_ss.rename(columns={"attributes.state": "state"})
        doi_ss["source"] = doi_ss["attributes.identifiers"].apply(
            lambda x: x[0]["identifier"])

        return doi_ss.drop(
            [
                'attributes.creators', 'attributes.titles',
                'attributes.version', 'type'
            ],
            axis=1
            )


def get_doi_frz() -> pd.DataFrame:
    """Returns UK LLC Freeze DOIs

    Returns:
        pd.DataFrame: Freeze DOIs
    """

    resp_doi_ds_get = requests.get(
        "https://{}/dois?prefix={}&"
        "resource-type-id=other&resource-type=freeze&&page[size]=1000"
        "&fields[dois]=creators%2Ctitles%2Cversion%2Cstate%2Cidentifiers".format(url_doi, prefix),
        headers={
            "accept": "application/vnd.api+json",
            }, auth=(ID, pw)
        )

    doi_datasets = resp_doi_ds_get.json()

    doi_dss = pd.json_normalize(doi_datasets['data'])
    if len(doi_dss) == 0:

        return doi_dss.reindex(doi_dss.columns.union(
            ["id", "state", "attributes.identifiers", "creators", "title"]),
                               axis=1)
    else:
        doi_dss['creators'] = doi_dss['attributes.creators']\
            .apply(lambda x: x[0]['name'])
        doi_dss['title'] = doi_dss['attributes.titles']\
            .apply(lambda x: x[0]['title'])
        # turn back on once finished bug fix!
        # doi_dss['version'] = doi_dss['attributes.version']\
        #    .apply(lambda x: int(float(x)))
        doi_dss = doi_dss.rename(columns={"attributes.state": "state"})

        return doi_dss.drop(
            [
                'attributes.creators', 'attributes.titles',
                'attributes.version', 'type'
            ],
            axis=1
            )


def get_doi_prj() -> pd.DataFrame:
    """Returns UK LLC Project DOIs

    Returns:
        pd.DataFrame: Project DOIs in DF
    """

    resp_doi_ds_get = requests.get(
        "https://{}/dois?prefix={}&"
        "resource-type-id=Project&&page[size]=1000"
        "&fields[dois]=creators%2Ctitles%2Cversion%2Cstate%2Cidentifiers".format(url_doi, prefix),
        headers={
            "accept": "application/vnd.api+json",
            }, auth=(ID, pw)
        )

    doi_datasets = resp_doi_ds_get.json()

    doi_dss = pd.json_normalize(doi_datasets['data'])
    if len(doi_dss) == 0:

        return doi_dss.reindex(doi_dss.columns.union(
            ["id", "state", "attributes.identifiers", "creators", "title"]),
                               axis=1)
    else:
        doi_dss['title'] = doi_dss['attributes.titles']\
            .apply(lambda x: x[0]['title'])
        # turn back on once finished bug fix!
        # doi_dss['version'] = doi_dss['attributes.version']\
        #    .apply(lambda x: int(float(x)))
        doi_dss = doi_dss.rename(columns={"attributes.state": "state",
                                          "attributes.creators": "creators"})

        return doi_dss.drop(
            [
                'attributes.titles', 'attributes.version',
                'type'
            ],
            axis=1
            )
