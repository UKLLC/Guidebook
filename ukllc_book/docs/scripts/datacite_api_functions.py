import requests
import json
import os
import pandas as pd

# DataCite API environment variables
ID = 'WHRN.UKLLCTEST'
pw = os.environ['DATACITE_TEST_PW']

# DataCite API variables
url_doi = "https://api.test.datacite.org/dois"
headers_doi = {
    "accept": "application/vnd.api+json",
    "content-type": "application/json",
}


def get_doi_datasets():
    """
    Queries DataCite with an API GET request of all  UKLLC minted datasets and
    version and returns a DataFrame.

    Args:
        None

    Returns:
       DataFrame: datasets in MMS
            id (str)
            creators (str)
            title (str)
            version (int)
    """

    resp_doi_ds_get = requests.get(
        "https://api.test.datacite.org/dois?prefix=10.83126&"
        "resource-type-id=dataset&&page[size]=1000&"
        "fields[dois]=creators%2Ctitles%2Cversion%2Cstate%2Cidentifiers",
        headers={
            "accept": "application/vnd.api+json",
                },
        auth=(ID, pw)
        )

    doi_datasets = resp_doi_ds_get.json()

    doi_dss = pd.json_normalize(doi_datasets['data'])
    if len(doi_dss) == 0:
        return doi_dss.reindex(doi_dss.columns.union(
            ["id", "state", "attributes.identifiers", "creators", "title", "source_table"]
                                                  ), axis=1)
    else:
        doi_dss['creators'] = doi_dss['attributes.creators']\
            .apply(lambda x: x[0]['name'])
        doi_dss['title'] = doi_dss['attributes.titles']\
            .apply(lambda x: x[0]['title'])

        doi_dss = doi_dss.rename(columns={"attributes.state": "state"})
        doi_dss["source_table"] =

        return doi_dss.drop(
            [
                'attributes.creators', 'type'
            ],
            axis=1
            )


def get_doi_series():
    """
    Queries DataCite with an API GET request of all  UKLLC minted datasets and
    version and returns a DataFrame.

    Args:
        None

    Returns:
       DataFrame: datasets in MMS
            id (str)
            creators (str)
            title (str)
            version (int)
    """

    resp_doi_ds_get = requests.get(
        "https://api.test.datacite.org/dois?prefix=10.83126"
        "&resource-type-id=other&resource-type=series&&page[size]=1000"
        "&fields[dois]=creators%2Ctitles%2Cversion%2Cstate%2Cidentifiers",
        headers={
            "accept": "application/vnd.api+json",
            }, auth=(ID, pw)
        )

    doi_sources = resp_doi_ds_get.json()

    doi_ss = pd.json_normalize(doi_sources['data'])
    if len(doi_ss) == 0:
        return doi_ss.reindex(doi_ss.columns.union(
            ["id", "state", "attributes.identifiers", "creators", "title", "source"]
                                                  ), axis=1)

    else:
        doi_ss['creators'] = doi_ss['attributes.creators']\
            .apply(lambda x: x[0]['name'])
        doi_ss['title'] = doi_ss['attributes.titles']\
            .apply(lambda x: x[0]['title'])
        doi_ss = doi_ss.rename(columns={"attributes.state": "state"})
        doi_ss["source"] = doi_ss["attributes.identifiers"].apply(lambda x: x[0]["identifier"])

        return doi_ss.drop(
            [
                'attributes.creators', 'attributes.titles',
                'attributes.version', 'type'
            ],
            axis=1
            )


def get_doi_frz():
    """
    Queries DataCite with an API GET request of all  UKLLC minted freezes
    and returns a DataFrame.

    Args:
        None

    Returns:
       DataFrame: datasets in MMS
            id (str)
            creators (str)
            title (str)
            version (int)
    """

    resp_doi_ds_get = requests.get(
        "https://api.test.datacite.org/dois?prefix=10.83126&"
        "resource-type-id=other&resource-type=freeze&&page[size]=1000"
        "&fields[dois]=creators%2Ctitles%2Cversion%2Cstate%2Cidentifiers",
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


def get_doi_prj():
    """
    Queries DataCite with an API GET request of all  UKLLC minted freezes
    and returns a DataFrame.

    Args:
        None

    Returns:
       DataFrame: datasets in MMS
            id (str)
            creators (str)
            title (str)
            version (int)
    """

    resp_doi_ds_get = requests.get(
        "https://api.test.datacite.org/dois?prefix=10.83126&"
        "resource-type-id=Project&&page[size]=1000"
        "&fields[dois]=creators%2Ctitles%2Cversion%2Cstate%2Cidentifiers",
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