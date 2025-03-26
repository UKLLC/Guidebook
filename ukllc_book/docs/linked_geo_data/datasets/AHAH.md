# Access to Healthy Assets and Hazards (AHAH)

> Last modified: 10 Dec 2024

## Introduction
This file can be linked to the health record dataset, CORE_NHSD_LSOA11.
AHAH (the index of ‘Access to Health Assets and Hazards’) is a multi-dimensional index developed by the Consumer Data Research Centre (CDRC) for Great Britain measuring how ‘healthy’ neighbourhoods are. The AHAH index combines indicators under four different domains of accessibility: Retail environment (access to fast food outlets, pubs, tobacconists, gambling outlets), Health services (access to GPs, hospitals, pharmacies, dentists, leisure services), Physical environment (Blue Space, Green Space - Passive), and Air quality (NO₂, PM10, SO₂). Measurement data and deciles for the overall index, 4 domains and 14 inputs are produced for Lower Level Super Output Areas (LSOAs) for England and Wales, and Data Zones (DZ) for Scotland. Distances shown for some of the measurement data are means of the time (in minutes) for driving by car along the established road network, between the population weighted centroid of each postcode contained within each statistical geographical unit, and the actual location of the outlet/service. 

## AHAH datasets

<details>
<summary>England and Wales</summary>

**1. Scale and Extent**

| **Dataset descriptor**                             | **Dataset-specific information**                                                                                                                                                                                                                               |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name of dataset in TRE**                         | AHAH_geo_indicators_england_wales                                                                                                                                                                                                                              |
| **Other name**                                     | Access to Healthy Assets & Hazards (AHAH)                                                                                                                                                                                                                     |
| **Owner**                                          | Consumer Data Research Centre                                                                                                                                                                                                                                 |
| **Geographical coverage**                          | England and Wales                                                                                                                                                                                                                                               |
| **Temporal coverage**                              | 2022                                                                                                                                                                                                                                                           |
| **TRE temporal coverage**                          | 2022                                                                                                                                                                                                                                                           |
| **Frequency of update**                            | Every few years                                                                                                                                                                                                                                                |
| **Date of last extract**                           | None                                                                                                                                                                                                                                                          |
| **Keywords**                                       | Health, Retail, Environment, Air quality                                                                                                                                                                                                                       |
| **Short description**                              | AHAH (the index of ‘Access to Health Assets and Hazards’) is a multi-dimensional index developed by the CDRC for Great Britain measuring how ‘healthy’ neighbourhoods are. The AHAH index combines indicators under four different domains of accessibility: Retail environment (access to fast food outlets, pubs, tobacconists, gambling outlets), Health services (access to GPs, hospitals, pharmacies, dentists, leisure services), Physical environment (Blue Space, Green Space - Passive), and Air quality (NO₂, PM10, SO₂). Measurement data and deciles for the overall index, 4 domains and 14 inputs are produced for Lower Level Super Output Areas (LSOAs) for England and Wales, and Data Zones (DZ) for Scotland. Distances shown for some of the measurement data are means of the time (in minutes) for driving by car along the established road network, between the population weighted centroid of each postcode contained within each statistical geographical unit, and the actual location of the outlet/service. |
| **DOI**                                            | None                                                                                                                                                                                                                                                          |
| **Data resolution**                                | Lower Super Output Area code (2011)                                                                                                                                                                                                                           |
| **Number of variables**                            | 21                                                                                                                                                                                                                                                            |
| **Number of participants**                         | None                                                                                                                                                                                                                                                          |
| **Number of observations**                         | 34,753                                                                                                                                                                                                                                                        |
| **Version**                                        | 3                                                                                                                                                                                                                                                             |
| **Key link**                                       | [AHAH Dataset Link](https://data.cdrc.ac.uk/dataset/access-healthy-assets-hazards-ahah)                                                                                                                                                                       |
| **Specific restrictions to data use**              | None                                                                                                                                                                                                                                                          |


**2. Variables**
|**Variable Group**|**Variable**|**Description**|**Source**|**Date range of data**|
|:---:|:---:|:---:|:---:|:---:|
|Geographical|lsoa11|Lower Super Output Area code (2011)|Office of National Statistics|2011|
|Retail|ah3gamb|Distance to nearest Gambling Outlet (minutes)|Local Data Company|2019|
|Retail|ah3ffood|Distance to nearest Fast Food Outlet (minutes)|Local Data Company|2019|
|Retail|ah3pubs|Distance to nearest Pubs/Bars/Nightclub (minutes)|Local Data Company|2019|
|Retail|ah3tob|Distance to nearest Tobacconists/Vape Store (minutes)|Local Data Company|2019|
|Health|ah3gp|Distance to nearest GP Practice (minutes)|NHS England|Feb-22|
|Health|ah3hosp|Distance to nearest Hospital (minutes)|NHS England|Feb-22|
|Health|ah3dent|Distance to nearest Dentist (minutes)|NHS England|Jan-22|
|Health|ah3phar|Distance to nearest Pharmacy (minutes)|NHS England|Jan-22|
|Health|ah3phar|Distance to nearest Pharmacy (minutes)|NHS Wales|Nov-21|
|Health|ah3leis|Distance to nearest Leisure Centre (minutes)|Local Data Company|Jul-05|
|Green/bluespace|ah3blue|Distance to nearest Blue space (minutes)|OpenStreetMap|2021|
|Green/bluespace|ah3gpas|NVDI value indicating Passive Green Space|Sentinel Satellite|2021|
|Air|ah3no2|Annual mean Nitrogen Dioxide (μgm³)|DEFRA|2019|
|Air|ah3pm10|Annual mean Particulate Matter (μgm³)|DEFRA|2019|
|Air|ah3so2|Annual mean Sulphur Dioxide (μgm³)|DEFRA|2019|
|Health|ah3h|Health Domain Score|CDRC|2022|
|Green/bluespace|ah3g|Green/Bluespace Domain Score|CDRC|2022|
|Air|ah3e|Air quality Domain Score|CDRC|2022|
|Retail|ah3r|Retail Domain Score|CDRC|2022|
|Healthy Assets and Hazards|ahah_index|Access to Healthy Assets and Hazards index score|CDRC|2022|

</details>

<details>
<summary>Scotland</summary>

**1. Scale and Extent**

| **Dataset descriptor**                             | **Dataset-specific information**                                                                                                                                                                                                                               |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name of dataset in TRE**                         | AHAH_geo_indicators_scotland                                                                                                                                                                                                                                  |
| **Other name**                                     | Access to Healthy Assets & Hazards (AHAH)                                                                                                                                                                                                                     |
| **Owner**                                          | Consumer Data Research Centre                                                                                                                                                                                                                                 |
| **Geographical coverage**                          | Scotland                                                                                                                                                                                                                                                       |
| **Temporal coverage**                              | 2022                                                                                                                                                                                                                                                           |
| **TRE temporal coverage**                          | 2022                                                                                                                                                                                                                                                           |
| **Frequency of update**                            | Every few years                                                                                                                                                                                                                                                |
| **Date of last extract**                           | None                                                                                                                                                                                                                                                          |
| **Keywords**                                       | Health, Retail, Environment, Air quality                                                                                                                                                                                                                       |
| **Short description**                              | AHAH (the index of ‘Access to Health Assets and Hazards’) is a multi-dimensional index developed by the CDRC for Great Britain measuring how ‘healthy’ neighbourhoods are. The AHAH index combines indicators under four different domains of accessibility: Retail environment (access to fast food outlets, pubs, tobacconists, gambling outlets), Health services (access to GPs, hospitals, pharmacies, dentists, leisure services), Physical environment (Blue Space, Green Space - Passive), and Air quality (NO₂, PM10, SO₂). Measurement data and deciles for the overall index, 4 domains and 14 inputs are produced for Lower Level Super Output Areas (LSOAs) for England and Wales, and Data Zones (DZ) for Scotland. Distances shown for some of the measurement data are means of the time (in minutes) for driving by car along the established road network, between the population weighted centroid of each postcode contained within each statistical geographical unit, and the actual location of the outlet/service. |
| **DOI**                                            | None                                                                                                                                                                                                                                                          |
| **Data resolution**                                | Data Zones (2011)                                                                                                                                                                                                                                              |
| **Number of variables**                            | 21                                                                                                                                                                                                                                                            |
| **Number of participants**                         | None                                                                                                                                                                                                                                                          |
| **Number of observations**                         | 6,976                                                                                                                                                                                                                                                         |
| **Version**                                        | 3                                                                                                                                                                                                                                                             |
| **Key link**                                       | [AHAH Dataset Link](https://data.cdrc.ac.uk/dataset/access-healthy-assets-hazards-ahah)                                                                                                                                                                       |
| **Specific restrictions to data use**              | None                                                                                                                                                                                                                                                          |


**2. Variables**
|**Variable Group**|**Variable**|**Description**|**Source**|**Date range of data**|
|:---:|:---:|:---:|:---:|:---:|
|Geographical|lsoa11|Data Zones|gov.scot|2011|
|Retail|ah3gamb|Distance to nearest Gambling Outlet (minutes)|Local Data Company|2019|
|Retail|ah3ffood|Distance to nearest Fast Food Outlet (minutes)|Local Data Company|2019|
|Retail|ah3pubs|Distance to nearest Pubs/Bars/Nightclub (minutes)|Local Data Company|2019|
|Retail|ah3tob|Distance to nearest Tobacconists/Vape Store (minutes)|Local Data Company|2019|
|Health|ah3gp|Distance to nearest GP Practice (minutes)|NHS Scotland|Jan-22|
|Health|ah3hosp|Distance to nearest Hospital (minutes)|NHS Scotland|Dec-21|
|Health|ah3dent|Distance to nearest Dentist (minutes)|NHS Scotland|Jun-21|
|Health|ah3phar|Distance to nearest Pharmacy (minutes)|NHS Scotland|Oct-21|
|Health|ah3leis|Distance to nearest Leisure Centre (minutes)|Local Data Company|Jul-05|
|Green/bluespace|ah3blue|Distance to nearest Blue space (minutes)|OpenStreetMap|2021|
|Green/bluespace|ah3gpas|NVDI value indicating Passive Green Space|Sentinel Satellite|2021|
|Air|ah3no2|Annual mean Nitrogen Dioxide (μgm³)|DEFRA|2019|
|Air|ah3pm10|Annual mean Particulate Matter (μgm³)|DEFRA|2019|
|Air|ah3so2|Annual mean Sulphur Dioxide (μgm³)|DEFRA|2019|
|Health|ah3h|Health Domain Score|CDRC|2022|
|Green/bluespace|ah3g|Green/Bluespace Domain Score|CDRC|2022|
|Air|ah3e|Air quality Domain Score|CDRC|2022|
|Retail|ah3r|Retail Domain Score|CDRC|2022|
|Healthy Assets and Hazards|ahah_index|Access to Healthy Assets and Hazards index score|CDRC|2022|

</details>


## Data Linkage
England/Wales and Scotland each have their own geo indicator dataset, since England and Wales use the geographic unit of Lower Super Output Areas (LSOA) and Scotland uses Data Zones (DZ).

To link LLC_XXXX.CORE_nhsd_lsoa11_v0000_YYYYMMDD with
LLC_XXXX.AHAH_geo_indicators_england_wales_v0000_YYYYMMDD 
LLC_XXXX.AHAH_geo_indicators_scotland_v0000_YYYYMMDD 


To link LLC_XXXX.CORE_nhsd_lsoa11_v0000_YYYYMMDD with 
LLC_XXXX.AHAH_geo_indicators_england_wales_v0000_YYYYMMDD:

1. Retrieve data from database via helper syntax
2. Link datasets on the *lsoa11cd_e* field. Example of STATA syntax linking to England and Wales:

*load NHSD *lsoa11* dataset

*use* “S:\LLC_9999\data\stata_w_labs\CORE_nhsd_*lsoa11*_v0001_20221217.dta”, clear

*merge m:* 1 lsoa11cd_e using
“S:\LLC_9999\data\stata_w_labs\AHAH_geo_indicators_england_wales_20240731.dta”
*drop geographical units not linked to any participant health record  
*drop if* _merge ** 2

CORE_nhsd_lsoa11 is a long dataset typically with millions of rows, depending on size of data request. It is therefore recommended that you subset both or either of these datasets before linking/processing/saving. An example of this would be to select the quintile from the Access to Healthy Assets and Hazards Index that you are going to use and keep these variables only. This will ensure the dataset size remains as manageable as possible. It is also advised to only link to the country/ countries that you require.

The Index for Healthy Assets and Hazards is provided by the Consumer Data Research Centre, an ESRC Data Investment: ES/L011840/1, ES/L011891/1
