# NHS Datasets

>Last modified: 30 Oct 2024

## Introduction  


From existing place-based core dataset intro page:


## Overview
UK LLC makes available a number of standard ‘**core**’ place-based files with each project. These files contain information that enables researchers to understand their sample and define the denominator for their project. 

Currently, the following place-based core datasets are available:

* **NHSD LSOA11**
* **LSOA11 geo indicators**
* **Geo indicators: England, Wales, Scotland and Northern Ireland**

**OVERVIEW TABLE TO BE ADDED SHORTLY** 

## Permissions and data refreshes
Core datasets containing data derived from NHS England datasets are filtered on the LPS selected in the NHS England linked section of the UK LLC data request form. In these cases participants are also filtered using the NHS England permissions. Core datasets are updated each quarter but researchers' views of these data are 'locked' to permissions at the time of first data provision. The permissions themselves can be found in the CORE denominator file1 e.g. CORE_denominator_file1_v0001_20220412.

## How to link LSOA datasets

To link CORE_nhsd_lsoa11_v0000_YYYYMMDD with CORE_lsoa11_geo_indicators_v0000_YYYYMMDD:
1.	Retrieve data from database via helper syntax.
2.	Link datasets on lsoa11cd_e field. Example of stata syntax:

![nhs_lsoa_link](nhs_lsoa_link.png)

**Note on linkage preprocessing**:
CORE_nhsd_lsoa11 is a long dataset typically with millions of rows, depending on size of data request. It is therefore recommended that you subset both or either of these datasets before linking/processing/saving. An example of this would be to select the quantile of IMD that you are going to use and keep these variables only. This will ensure the dataset size remains as manageable as possible.
</details>