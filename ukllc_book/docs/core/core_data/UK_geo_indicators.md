# Geo indicators: England, Wales, Scotland and Northern Ireland

> Last modified: 25 Jul 2024

## Introduction
This file is intended to be linked to the health record dataset, CORE_NHSD_LSOA1. It adds geographical indicators to each encrypted small area geography (Lower Super Output Area for England and Wales, Data Zone for Scotland or Super Output Area for Northern Ireland). The indicators include measures of deprivation for all 4 nations, population estimates and urban-rural classification. The small area geographies are those developed using the 2011 census. The associated data for each geographical unit is the most up to date available data that uses the 2011 boundaries, this is due to not all of the indicators yet available using the new 2021 census boundaries. 

## CORE geo indicators

<details>
<summary>England</summary>

**1. Scale and Extent**

|**Field**|**Value**|
|:--:|:--:|
|Geographical coverage|England|
|Data Provider|Office of National Statistics, GOV.UK, Consumer Data Research Centre, My Society|
|Geographical Unit|LSOA11|
|Temporal Extent|2011-2020|
|Variables|15|
|Observations|32,844|
--

**2. Variables**

|**Variable Group**|**Variable**|**Description**|**Source**|**Date range of data**|
|:---:|:---:|:---:|:---:|:---:|
|**Geographical**|granularity|Lower Super Output Area code (2011)|Office of National Statistics|2011|
|**Geographical**|country|Country within the United Kingdom|Office of National Statistics|2011|
|**Geographical**|RGN11NM|Region within England|Office of National Statistics|2011|
**Deprivation**|imd2029eng|English indices of deprivation 2019, presented as quintiles, 1=most deprived, 5=least deprived.|[GOV.UK](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)|2019|
|**Deprivation**|imd2019eng_income|English indices of deprivation 2019, Income, presented as quintiles. 1= lowest income, 5= highest income.|[GOV.UK](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)|2019|
|**Deprivation**|imd2019eng_employment|English indices of deprivation 2019, Employment, presented as quintiles. 1=highest unemployment, 5= lowest unemployment.|[GOV.UK](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)|2019|
|**Deprivation**|imd2019eng_education|English indices of deprivation 2019, Education, presented as quintiles. 1= lowest education and skills, 5= highest education and skills.|[GOV.UK](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)|2019|
|**Deprivation**|imd2019eng_health|English indices of deprivation 2019, Health, presented as quintiles. 1= high health deprivation, 5= low health deprivation.|[GOV.UK](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)|2019|
|**Deprivation**|imd2019eng_crime|English indices of deprivation 2019, Crime, presented as quintiles. 1= high crime rates, 5= low crime rates.|[GOV.UK](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)|2019|
|**Deprivation**|imd2019eng_barriers|English indices of deprivation 2019, Barriers to Housing and Services, presented as quintiles. 1= high barriers, 5= low barriers.|[GOV.UK](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)|2019|
|**Deprivation**|imd2019eng_environment|English indices of deprivation 2019, Environment, presented as quintiles. 1= low quality environment, 5= high quality environment.|[GOV.UK](https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019)|2019|
|**Deprivation**|Imd2019har<sup>1</sup>|Consumer Data Research Centre’s Harmonisaed Index of Multiple Deprivation 2019, presented as quintiles. 1=most deprived, 5=least deprived. |[Consumer Data Research Centre](https://data.cdrc.ac.uk/dataset/index-multiple-deprivation-imd)|2019 (English IMD), 2019 (Welsh IMD), 2017 (Northern Irish MDM), 2020   (Scottish IMD)|
|**Population Estimate**|MPE_eng_2020|Mid-year (30 June) estimates of the usual resident population for Lower layer Super Output Areas (LSOAs) in England. 5 categories: <1200, 1200-1500, 1500-1600, 1600-1800 and >1800.|[Office for National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/lowersuperoutputareamidyearpopulationestimates)|2020|
|**Urban-Rural Indicator**|ur_eng_wal_2011|2011 Rural Urban Classification for England. 1= Urban major conurbation, 2= Urban minor conurbation, 3= Urban city and town, 4= Rural town and fringe, 5= Rural village and dispersed.|[GOV.UK](https://www.gov.uk/government/statistics/2011-rural-urban-classification)|2011|
|**Urban-Rural Indicator**|ur_harm_2021<sup>2</sup>|2021 UK Composite Rural Urban Classification. 1= Urban, 2= Rural, 3= More Rural. |[My Society](https://pages.mysociety.org/uk_ruc/analysis/background_and_analysis.html)|2011 (England and Wales), 2016 (Scotland), 2015 (Northern Ireland)|

<sup>1</sup> Citation if using the variable: Parsons, Alex (2021), UK Rural/Urban measures, https://github.com/mysociety/uk_ruc

<sup>2</sup> Citation if using the variable: Consumer Data Research Centre (2019), DOI: 10.20390/enginddepriv2015
</details>

<details>
<summary>Wales</summary>

**1. Scale and Extent**

|**Field**|**Value**|
|:--:|:--:|
|Geographical coverage|Wales|
|Data Provider|Office of National Statistics, GOV.WALES, Consumer Data Research Centre|
|Geographical Unit|LSOA11|
|Temporal Extent|2011-2020|
|Variables|15|
|Observations|1909|
--


**2. Variables**
|**Variable Group**|**Variable**|**Description**|**Source**|**Date range of data**|
|:---:|:---:|:---:|:---:|:---:|
|**Geographical**|granularity|Lower Super Output Area code (2011)|Office of National Statistics|2011|
|**Geographical**|country|Country within the United Kingdom|Office of National Statistics|2011|
|**Deprivation**|imd2019wal|Welsh Index of Multiple Deprivation 2019, presented as quintiles. 1= most deprived, 5= least deprived.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|imd2019wal_income|Welsh Index of Multiple Deprivation 2019, Income, presented as quintiles. 1= lowest income, 5= highest income.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|imd2019wal_employment|Welsh Index of Multiple Deprivation 2019, Employment, presented as quintiles. 1= highest unemployment, 5= lowest unemployment.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|imd2019wal_education|Welsh Index of Multiple Deprivation 2019, Education, presented as quintiles. 1= lowest education, 5= highest education.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|imd2019wal_health|Welsh Index of Multiple Deprivation 2019, Health, presented as quintiles. 1= high health deprivation, 5= low health deprivation.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|imd2019wal_safety|Welsh Index of Multiple Deprivation 2019, Community Safety, presented as quintiles. 1= low community safety, 5= high community safety.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|imd2019wal_services|Welsh Index of Multiple Deprivation 2019, Access to Services, presented as quintiles. 1= Strong access, 5= Weak access.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|imd2019wal_environment|Welsh Index of Multiple Deprivation 2019, Physical Environment, presented as quintiles. 1= low quality environment, 5= high quality environment.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|imd2019wal_housing|Welsh Index of Multiple Deprivation 2019, Housing, presented as quintiles. 1= low quality housing, 5= high quality.|[GOV.WALES](https://www.gov.wales/welsh-index-multiple-deprivation)|2019|
|**Deprivation**|Imd2019har<sup>1</sup>|Consumer Data Research Centre’s Harmonisaed Index of Multiple Deprivation 2019, presented as quintiles. 1= most deprived, 5= least deprived.|[Consumer Data Research Centre](https://data.cdrc.ac.uk/dataset/index-multiple-deprivation-imd)|2019 (English IMD), 2019 (Welsh IMD), 2017 (Northern Irish MDM), 2020   (Scottish IMD)|
|**Population Estimate**|MPE_wal_2020|Mid-year (30 June) estimates of the usual resident population for Lower layer Super Output Areas (LSOAs) in England and Wales. 5 categories: <1200, 1200-1500, 1500-1600, 1600-1800 and >1800.|[Office for National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/lowersuperoutputareamidyearpopulationestimates)|2020|
|**Urban-Rural Indicator**|ur_eng_wal_2011|2011 Rural Urban Classification for England. 1= Urban major conurbation, 2= Urban minor conurbation, 3= Urban city and town, 4= Rural town and fringe, 5= Rural village and dispersed.|[GOV.UK](https://www.gov.uk/government/statistics/2011-rural-urban-classification)|2011|
|**Urban-Rural Indicator**|ur_harm_2021 <sup>2</sup>|2021 UK Composite Rural Urban Classification. 1= Urban, 2= Rural, 3= More Rural|[My Society](https://pages.mysociety.org/uk_ruc/analysis/background_and_analysis.html)|2011 (England and Wales), 2016 (Scotland), 2015 (Northern Ireland)|

<sup>1</sup> Citation if using the variable: Parsons, Alex (2021), UK Rural/Urban measures, https://github.com/mysociety/uk_ruc

<sup>2</sup> Citation if using the variable: Consumer Data Research Centre (2019), DOI: 10.20390/enginddepriv2015
</details>


<details>
<summary>Scotland</summary>

**1. Scale and Extent**

|**Field**|**Value**|
|:--:|:--:|
|Geographical coverage|Scotland|
|Data Provider|GOV.UK, GOV.SCOT, Consumer Data Research Centre, National Records of Scotland|
|Geographical Unit|Data Zones|
|Temporal Extent|2011-2021|
|Variables|14|
|Observations|6976|
--

**2. Variables**

|**Variable Group**|**Variable**|**Description**|**Source**|**Date range of data**|
|:---:|:---:|:---:|:---:|:---:|
|**Geographical**|granularity|Data Zones (2011)|GOV.UK|2011|
|**Geographical**|country|Country within the United Kingdom|GOV.SCOT|2011|
|**Deprivation**|imd2020scot|Scottish Index of Multiple Deprivation 2019, presented as quintiles. 1= most deprived, 5= least deprived.|[GOV.SCOT](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)|2020|
|**Deprivation**|imd2020scot_income|Scottish Index of Multiple Deprivation 2019, Income, presented as quintiles. 1= lowest income, 5= highest income.|[GOV.SCOT](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)|2020|
|**Deprivation**|imd2020scot_employment|Scottish Index of Multiple Deprivation 2019, Employment, presented as quintiles. 1= highest unemployment, 5= lowest unemployment.|[GOV.SCOT](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)|2020|
|**Deprivation**|imd2020scot_education|Scottish Index of Multiple Deprivation 2019, Education, presented as quintiles. 1= lowest education, 5= highest education.|[GOV.SCOT](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)|2020|
|**Deprivation**|imd2020scot_health|Scottish Index of Multiple Deprivation 2019, Health, presented as quintiles. 1= high health deprivation, 5= low health deprivation.|[GOV.SCOT](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)|2020|
|**Deprivation**|imd2020scot_access|Scottish Index of Multiple Deprivation 2019, Access to Services, presented as quintiles. 1= strong access, 5= weak access.|[GOV.SCOT](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)|2020|
|**Deprivation**|imd2020scot_crime|Scottish Index of Multiple Deprivation 2019, Crime, presented as quintiles. 1= high crime rates, 5= low crime rates.|[GOV.SCOT](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)|2020|
|**Deprivation**|imd2020scot_housing|Scottish Index of Multiple Deprivation 2019, Housing, presented as quintiles. 1= low quality housing, 5= high quality.|[GOV.SCOT](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/)|2020|
|**Deprivation**|imd2019har<sup>1</sup> |Consumer Data Research Centre’s Harmonisaed Index of Multiple Deprivation 2019, presented as quintiles. 1= most deprived, 5= least deprived.|[Consumer Data Research Centre](https://data.cdrc.ac.uk/dataset/index-multiple-deprivation-imd)|2019 (English IMD), 2019 (Welsh IMD), 2017 (Northern Irish MDM), 2020 (Scottish IMD)|
|**Population Estimate**|MPE_scot_2021|Mid-year (30 June) estimates of the usual resident population for Data Zones (2011) in Scotland. 5 categories: <1200, 1200-1500, 1500-1600, 1600-1800 and >1800.|[National Records of Scotland](https://www.nrscotland.gov.uk/statistics-and-data/statistics/statistics-by-theme/population/population-estimates/mid-year-population-estimates/mid-2021)|2021|
|**Urban-Rural Indicator**|ur_scot_2020|Scottish Government Urban Rural Classification 2020. 1= Large Urban Areas, 2=Other Urban Areas, 3= Accessible Amall Towns, 4= Remote Small Towns, 5= Accessible Rural Areas, 6= Remote Rural Areas.|[GOV.SCOT](https://www.gov.scot/publications/scottish-government-urban-rural-classification-2020/pages/3/)|2020|
|**Urban-Rural Indicator**|ur_harm_2021<sup>2</sup>|2021 UK Composite Rural Urban Classification. 1= Urban, 2= Rural, 3= More Rural.|[My Society](https://pages.mysociety.org/uk_ruc/analysis/background_and_analysis.html)|2011 (England and Wales), 2016 (Scotland), 2015 (Northern Ireland)|

<sup>1</sup> Citation if using the variable: Parsons, Alex (2021), UK Rural/Urban measures, https://github.com/mysociety/uk_ruc

<sup>2</sup> Citation if using the variable: Consumer Data Research Centre (2019), DOI: 10.20390/enginddepriv2015
</details>

<details>
<summary>Northern Ireland</summary>

**1. Scale and Extent**

|**Field**|**Value**|
|:--:|:--:|
|Geographical coverage|Northern Ireland|
|Data Provider|Northern Ireland Statistics and Research Agency, Consumer Data Research Centre|
|Geographical Unit|SOA|
|Temporal Extent|2011-2020|
|Variables|14|
|Observations|890|
--

**2. Variables**

|**Variable Group**|**Variable**|**Description**|**Source**|**Date range of data**|
|:---:|:---:|:---:|:---:|:---:|
|**Geographical**|granularity|Super Output Areas (2011)|[NISRA](https://www.nisra.gov.uk/support/output-geography-census-2011/super-output-areas)|2011|
|**Geographical**|country|Country within the United Kingdom|[NISRA](https://www.nisra.gov.uk/support/output-geography-census-2011/super-output-areas)|2011|
|**Deprivation**|imd2017ir|Northern Ireland Multiple Deprivation Measure 2017, presented as quintiles. 1= most deprived, 5= least deprived.|[NISRA](https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017)|2017|
|**Deprivation**|imd2017ir_income|Northern Ireland Multiple Deprivation Measure 2017, Income, presented as quintiles. 1= lowest income, 5= highest income.|[NISRA](https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017)|2017|
|**Deprivation**|imd2017ir_employment|Northern Ireland Multiple Deprivation Measure 2017, Employment, presented as quintiles. 1= highest unemployment, 5= lowest unemployment.|[NISRA](https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017)|2017|
|**Deprivation**|imd2017ir_education|Northern Ireland Multiple Deprivation Measure 2017, Education, presented as quintiles. 1= lowest education, 5= highest education.|[NISRA](https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017)|2017|
|**Deprivation**|imd2017ir_ health|Northern Ireland Multiple Deprivation Measure 2017, Health, presented as quintiles. 1= high health deprivation, 5= low health deprivation.|[NISRA](https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017)|2017|
|**Deprivation**|imd2017ir_access|Northern Ireland Multiple Deprivation Measure 2017, Access to Services, presented as quintiles. 1= strong access, 5= weak access.|[NISRA](https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017)|2017|
|**Deprivation**|imd2017ir_crime|Northern Ireland Multiple Deprivation Measure 2017, presented as quintiles. 1= high crime rates, 5= low crime rates.|[NISRA](https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017)|2017|
|**Deprivation**|imd2017ir_environment|Northern Ireland Multiple Deprivation Measure 2017, presented as quintiles. 1= low quality environment, 5= high quality environment.|[NISRA](https://www.nisra.gov.uk/statistics/deprivation/northern-ireland-multiple-deprivation-measure-2017-nimdm2017)|2017|
|**Deprivation**|imd2019har<sup>1</sup>|Consumer Data Research Centre’s Harmonisaed Index of Multiple Deprivation 2019, presented as quintiles. 1= most deprived, 5= least deprived.|[Consumer Data Research Centre](https://data.cdrc.ac.uk/dataset/index-multiple-deprivation-imd)|2019 (English IMD), 2019 (Welsh IMD), 2017 (Northern Irish MDM), 2020 (Scottish IMD)|
|**Population Estimate**|MPE_ire_2020|Mid-year (30 June) estimates of the usual resident population for Super Output Areas (2011) in Northern Ireland. 5 categories: <1200, 1200-1500, 1500-1600, 1600-1800 and >1800.|[NISRA](https://www.nisra.gov.uk/publications/2020-mid-year-population-estimates-small-areas)|2020|
|**Urban-Rural Indicator**|ur_ire_2015|Settlement classification 2015. 1=Urban, 2= Mixed urban/rural, 3= Rural|[NISRA](https://www.nisra.gov.uk/publications/settlement-2015-documentation)|2015|
|**Urban-Rural Indicator**|ur_harm_2021<sup>2</sup>|2021 UK Composite Rural Urban Classification. 1= Urban, 2= Rural, 3= More Rural.|[My Society](https://pages.mysociety.org/uk_ruc/analysis/background_and_analysis.html)|2011 (England and Wales), 2016 (Scotland), 2015 (Northern Ireland)|

<sup>1</sup> Citation if using the variable: Parsons, Alex (2021), UK Rural/Urban measures, https://github.com/mysociety/uk_ruc

<sup>2</sup> Citation if using the variable: Consumer Data Research Centre (2019), DOI: 10.20390/enginddepriv2015
</details>  




## Data Linkage

To link LLC_XXXX.CORE_nhsd_lsoa11_v0000_YYYYMMDD with 
LLC_XXXX.CORE_lsoa11_geo_indicators_v0000_YYYYMMDD:

1. Retrieve data from database via helper syntax
2. Link datasets on the *geo_unit* field. Example of STATA syntax:

*load NHSD *lsoa11* dataset

*use* “S:\LLC_9999\data\stata_w_labs\CORE_nhsd_*lsoa11*_v0001_20221217.dta”, clear

*merge m:* 1 geo_unit using
“S:\LLC_9999\data\stata_w_labs\CORE_geo_indicators_nhsd_v0002_20240802.dta”
*drop geographical units not linked to any participant health record  
*drop if* _merge ** 2

CORE_nhsd_lsoa11 is a long dataset typically with millions of rows, depending on size of data request. It is therefore recommended that you subset both or either of these datasets before linking/processing/saving. An example of this would be to select the quintile from the Index of Multiple Deprivation that you are going to use and keep these variables only. This will ensure the dataset size remains as manageable as possible. It is also advised to only link to the country/ countries that you require.


## Data Harmonisation

>**Index of Multiple Deprivation**

To harmonise the Indices of Multiple Deprivation across England, Wales, Scotland and Northern Ireland, use the ‘imd2019har’ variable that is in the CORE geo datasets for all 4 countries. The variable uses the Consumer Data Research Centre’s Harmonised Index of Multiple Deprivation 2019. The indicator is a simple (non-reweighted) combination of the English IMD 2019, Welsh IMD 2019, Northern Irish MDM 2017 and the Scottish IMD 2020. The index is presented as quintiles. 

For more information, [click here](https://data.cdrc.ac.uk/dataset/index-multiple-deprivation-imd/resource/cdrc-harmonised-imd-2019#{view-graph:{graphOptions:{hooks:{processOffset:{},bindEvents:{}}}},graphOptions:{hooks:{processOffset:{},bindEvents:{}}}}).

>**Urban-Rural Classification**

To harmonise the urban-rural classifications across England, Wales, Scotland and Northern Ireland, use the ‘ur_harm_2021’ variable that is in the CORE geo datasets for all 4 countries. The variable is derived from the My Society’s UK Composite Rural Urban Classification. The indicator is a 3-fold metric that describes various small areas (LSOAs/Datazones/SOAs) on a rural/urbal scale that is comparable across the UK.

For more information, [click here](https://pages.mysociety.org/uk_ruc/analysis/background_and_analysis.html).