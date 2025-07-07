# Access to Healthy Assets and Hazards (AHAH) 

> Last modified: 19 Jun 2025

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The Access to Healthy Assets and Hazards dataset is a multi-dimensional indices which describes accessibility to certain environmental features relating to health and wellbeing.</strong></div>  
<br>

AHAH (the index of ‘Access to Health Assets and Hazards’) is a multi-dimensional index developed by the [Geographic Data Service](https://data.geods.ac.uk/dataset/access-to-healthy-assets-hazards-ahah) for Great Britain measuring how ‘healthy’ neighbourhoods are. The AHAH index combines indicators under four different domains of accessibility: Retail environment (access to fast food outlets, pubs, tobacconists, gambling outlets), Health services (access to GPs, hospitals, pharmacies, dentists, leisure services), Physical environment (Blue Space, Green Space - Passive), and Air quality (NO₂, PM10, SO₂). Measurement data and deciles for the overall index, 4 domains and 14 inputs are produced for Lower Level Super Output Areas (LSOAs) for England and Wales, and Data Zones (DZ) for Scotland. Distances shown for some of the measurement data are means of the time (in minutes) for driving by car along the established road network, between the population weighted centroid of each postcode contained within each statistical geographical unit, and the actual location of the outlet/service. 

## 1. Summary 

<details>
<summary>Lower Layer Super Output Area level (LSOA), England and Wales</summary>

AHAH (the index of ‘Access to Healthy Assets and Hazards’) is a multi-dimensional index combining indicators under four different domains of accessibility: Retail environment (access to fast food outlets, pubs, tobacconists, gambling outlets), Health services (access to GPs, hospitals (NHS trust sites), pharmacies, dentists, leisure services), Physical environment (Blue Space, Green Space - Passive), and
Air quality (NO₂, PM10, SO₂), this dataset covers England and Wales.


| **Dataset Descriptor**             | **Dataset-specific Information**                                                                                                                                                           |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name of dataset in TRE            | AHAH_geo_indicators_england_wales                                                                                                                                                            |
| Citation (APA)                    | Daras, K., Green, M.A., Davies, A. et al. Open data on health-related neighbourhood features in Great Britain. Sci Data 6, 107 (2019). (Note this is for v1 which used a different methodology.) |
| Download citation                 | [https://doi.org/10.1038/](s41597-019-0114-6s41597-019-0114-6)                                                                                                |
| Owner                             | Geographic Data Service                                                                                                                                                                     |
| Temporal coverage                 | 2022                                                                                                                                                                                   |
| Geographical coverage             | England and Wales                                                                                                                                                                           |
| Key link                          | [Geographic Data Service: AHAH](https://data.geods.ac.uk/dataset/access-to-healthy-assets-hazards-ahah)                                                                                                |
| Keywords                          | Health, Retail, Environment, Air quality                                                                                                                                                          |
| Participant count                 |                                                                                                                                                                                             |
| Number of variables               |                                                                                                                                                                                             |
| Number of observations            |                                                                                                                                                                                             |
| Latest extract date               |                                                                                                                                                                                             |
| Specific restrictions to data use |                                                                                                                                                                                             |
| Build a data request              |                                                                                                                                                                                             |
| Version                           | 
3                                                                                                                                                                                           | 

**Variables**
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
|Health|ah3leis|Distance to nearest Leisure Centre (minutes)|Local Data Company|2019|
|Green/bluespace|ah3blue|Distance to nearest Blue space (minutes)|OpenStreetMap|2021|
|Green/bluespace|ah3gpas|NVDI value indicating Passive Green Space|Sentinel Satellite|2021|
|Air|ah3no2|Annual mean Nitrogen Dioxide (μgm³)|DEFRA|2019|
|Air|ah3pm10|Annual mean Particulate Matter (μgm³)|DEFRA|2019|
|Air|ah3so2|Annual mean Sulphur Dioxide (μgm³)|DEFRA|2019|
|Health|ah3h|Health Domain Score|Geographic Data Service|2022|
|Green/bluespace|ah3g|Green/Bluespace Domain Score|Geographic Data Service|2022|
|Air|ah3e|Air quality Domain Score|Geographic Data Service|2022|
|Retail|ah3r|Retail Domain Score|Geographic Data Service|2022|
|Healthy Assets and Hazards|ahah_index|Access to Healthy Assets and Hazards index score|Geographic Data Service|2022|

</details>

<details>
<summary>Data Zones (DZ), Scotland</summary>

AHAH (the index of ‘Access to Healthy Assets and Hazards’) is a multi-dimensional index combining indicators under four different domains of accessibility: Retail environment (access to fast food outlets, pubs, tobacconists, gambling outlets), Health services (access to GPs, hospitals (NHS trust sites), pharmacies, dentists, leisure services), Physical environment (Blue Space, Green Space - Passive), and
Air quality (NO₂, PM10, SO₂), this dataset covers Scotland.

| **Dataset Descriptor**             | **Dataset-specific Information**                                                                                                                                                           |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name of dataset in TRE            | AHAH_geo_indicators_scotland                                                                                                                                                            |
| Citation (APA)                    | Daras, K., Green, M.A., Davies, A. et al. Open data on health-related neighbourhood features in Great Britain. Sci Data 6, 107 (2019). (Note this is for v1 which used a different methodology.) |
| Download citation                 | [https://doi.org/10.1038/](s41597-019-0114-6s41597-019-0114-6)                                                                                                |
| Owner                             | Geographic Data Service                                                                                                                                                                     |
| Temporal coverage                 | 2022                                                                                                                                                                                   |
| Geographical coverage             | Scotland                                                                                                                                                                           |
| Key link                          | [Geographic Data Service: AHAH](https://data.geods.ac.uk/dataset/access-to-healthy-assets-hazards-ahah)                                                                                                |
| Keywords                          | Health, Retail, Environment, Air quality                                                                                                                                                          |
| Participant count                 |                                                                                                                                                                                             |
| Number of variables               |                                                                                                                                                                                             |
| Number of observations            |                                                                                                                                                                                             |
| Latest extract date               |                                                                                                                                                                                             |
| Specific restrictions to data use |                                                                                                                                                                                             |
| Build a data request              |                                                                                                                                                                                             |
| Version                           | 
3                                                                                                                                                                                           | 



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
|Health|ah3leis|Distance to nearest Leisure Centre (minutes)|Local Data Company|2019|
|Green/bluespace|ah3blue|Distance to nearest Blue space (minutes)|OpenStreetMap|2021|
|Green/bluespace|ah3gpas|NVDI value indicating Passive Green Space|Sentinel Satellite|2021|
|Air|ah3no2|Annual mean Nitrogen Dioxide (μgm³)|DEFRA|2019|
|Air|ah3pm10|Annual mean Particulate Matter (μgm³)|DEFRA|2019|
|Air|ah3so2|Annual mean Sulphur Dioxide (μgm³)|DEFRA|2019|
|Health|ah3h|Health Domain Score|Geographic Data Service|2022|
|Green/bluespace|ah3g|Green/Bluespace Domain Score|Geographic Data Service|2022|
|Air|ah3e|Air quality Domain Score|Geographic Data Service|2022|
|Retail|ah3r|Retail Domain Score|Geographic Data Service|2022|
|Healthy Assets and Hazards|ahah_index|Access to Healthy Assets and Hazards index score|Geographic Data Service|2022|

</details>

## 2. Metrics 

Click on the plus sign to see the number of participants represented in each dataset. 

## 3. Version History 

## 4. Documentation 

We are currently building a documentation storage system which will host relevant and useful documents related to datasets, groupings, and studies themselves. 

## 5. Useful Syntax 

**Data Linkage:**
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
