# Understanding: Index of Multiple Deprivation (IMD)

> Last modified: 21 Jul 2025

## IMD, urban/rural classification and population estimates

This file is intended to be linked to the health record dataset, CORE_NHSD_LSOA11. It adds geographical indicators to each encrypted small area geography (Lower Super Output Area for England and Wales, Data Zone for Scotland or Super Output Area for Northern Ireland). The indicators include measures of deprivation for all 4 nations, population estimates and urban-rural classification. The small area geographies are those developed using the 2011 census. The associated data for each geographical unit is the most up to date available data that uses the 2011 boundaries, this is due to not all of the indicators yet available using the new 2021 census boundaries. 

### Methodology

Each of the 4 nations has its own versions of the Index of Multiple Deprivation, please see below for the individual statistical release information:

**England:** The English Indices of Deprivation [(2019)](../../../images/IoD2019_Statistical_Release.pdf)

**Wales:** Welsh Index of Multiple Deprivation [(2019)](../../../images/welsh-index-multiple-deprivation-2019-results-report.pdf)

**Scotland:** Scottish Index of Multiple Deprivation [(2020)](../../../images/SIMD+2020+technical+notes.pdf)

**Northern Ireland:** Northern Ireland Multiple Deprivation Measures [(2017)](../../../images/NIMDM%202017_Technical%20Report.pdf)


England and Wales have a combined urban-rural classification, while Scotland and Northern Ireland have a separate classification system. The supporting documentation for each classification can be found below:

**England and Wales:** Rural Urban Clasification of Statistical Geographies, England and Wales [(2021)](../../../images/RUC_2021_methodology.pdf)

**Scotland:** Scottish Government Urban Rural Classification [(2020)](../../../images/scottish-government-urban-rural-classification-2020.pdf)

**Northern Ireland:** Northern Ireland Statistis and Research Agency Urban-Rural Classification [(2015)](../../../images/technical-guidance-on-production-of-official-statistics-for-settlements-and-urban-rural-classification.pdf)


Information on the quality and methdology information for mid-year population estimates in the UK including the strengths and limitations of the data has been developed by the [Office of National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/methodologies/midyearpopulationestimatesqmi). 

***Data Harmonisation:***

Indices of deprivation:

To harmonise the Indices of Multiple Deprivation across England, Wales, Scotland and Northern Ireland, use the ‘imd2019har’ variable that is in the IMD datasets for all 4 nations. The variable uses the [Geographic Data Service’s](https://data.geods.ac.uk/dataset/index-of-multiple-deprivation-imd) Harmonised Index of Multiple Deprivation 2019. The indicator is a simple (non-reweighted) combination of the English IMD 2019, Welsh IMD 2019, Northern Irish Multiple Deprivation Measure (MDM) 2017 and the Scottish IMD 2020. The index is presented as quintiles. 

For more information, [click here](https://data.geods.ac.uk/dataset/index-of-multiple-deprivation-imd)

Urban-Rural Classification:

To harmonise the urban-rural classifications across England, Wales, Scotland and Northern Ireland, use the ‘ur_harm_2021’ variable that is in the IMD datasets for all 4 nations. The variable is derived from the [My Society’s](https://www.mysociety.org/) UK Composite Rural Urban Classification. The indicator is a 3-fold metric that describes various small areas (LSOAs/Datazones/SOAs) on a rural/urbal scale that is comparable across the UK. For more information, [click here](https://pages.mysociety.org/uk_ruc/analysis/background_and_analysis.html).

## Caveats:

- The associated data for each geographical unit is the most up to date available data that uses the 2011 boundaries, this is due to not all of the indicators yet available using the new 2021 census boundaries.

## Limitations:

- Each of the 4 nations has its own versions of the Index of Multiple Deprivation and Urban-Rural classification in order to fit the local context and meet their local needs. As a result each nation's data source for IMD and urban-rural classification will have its own set of biases. Please refer to the individual statistical release documents in the Methodology section of this page for the relevant limitations to each source of data.