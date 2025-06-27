# README: Air pollution NO2 & PM

>Last modified: 27 Jun 2025

## Annual-average Nitrogen Dioxide (NO2) and Fine particulate matter (PM2.5)

**Nitrogen dioxide (NO2):**
NO2 gas is mainly produced during combustion of fossil fuels. Short term exposure to elevated concentrations of **NO2 can have adverse health impacts** such as inflammation of the airways and increased susceptibility to respiratory infections and allergens. NO2 can exacerbate symptoms of those suffering from heart or lung conditions {cite}`GOVNO2`.

**Fine particulate matter (PM):**
Particulate matter (PM) is everything in the air that is not a gas and as such it is made up from a huge variety of chemical compounds and materials. PM is classified according to size. The UK currently focuses on estimating the fractions of PM emissions where particles are less than 10 micrometres in diameter (PM10) and less than 2.5 micrometres in diameter (PM2.5). Some PM is toxic and due to the small size of the particles, some toxins can enter the bloodstream and can be transported around the body, entering the heart, brain and other organs {cite}`GOVPM25`.

### Methodology

**Geospatial surface data:** 
NO2 and PM2.5 geospatial surface data were created at a national scale using two existing surfaces:

1) The UK government, Department for Environment, Food & Rural Affairs **(DEFRA)** has modelled background **annual-average air pollution concentrations** since 2001 (1 x 1km resolution). These surfaces approximate **changes in air pollution over time** and provide exposure estimates between the UK Automatic Urban and Rural Network (AURN). These are typically 10 to 100s kms apart and with higher numbers in urban areas. 
2) **High spatial resolution** annual average pollutant surfaces at 25x25m resolution produced by Wang et al. (2022) {cite}`WANG2022101506`. Unlike the DEFRA surfaces, these surfaces do not capture the temporal change in exposures. However, they do capture variability within and between streets. 

**High spatial-temporal resolution environmental exposure surfaces were created** across the UK, using the spatial granularity of Wang’s NO2 and PM2.5 exposure surface and temporal regularity of the DEFRA background concentration maps. 

## Linkage to addresses
UK LLC participant residential address points were linked to the geospatial surface data using ArcGIS Pro ['Extract Values to Points'](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/extract-values-to-points.htm) tool. This assigns the surface cell value (air pollution measure) that the address point falls on. All annual average air pollution measures were then rounded to integers to minimise disclosure risk.

## Understanding the data
### Dataset/table split
The data are split over 2 tables/datasets:
1) **GEO_air_pollution_hh** where addresses are geocoded to the household (hh) level.
2) **GEO_air_pollution_pc** where addresses are geocoded to the postcode (pc) level.

See the [Linkage and processing of address data guide](../Processing & linkage.md) for further information on geo-linkage resolution. Variables are common between the household and postcode level datasets to allow the datasets to be easily unioned/appended. 

### Address start and end dates
Address start and end dates are provided by each LPS to indicate when the participant moved into and out of each address location. In many cases these **dates are null, address periods are not contiguous**, and do not cover the full time periods where participants are part of an LPS. These are **data quality issues** and the UK LLC Data Team is exploring solutions to improve the usability of these data. This documentation will be updated once these improvements are in place.  

### Matchcodes
The files contain a *matchcode* variable which indicates how successfully the Experian geocoding software was able to match the address. The *matchcode* also contains an indicator for confidence and whether any actions took place to correct postcode or address elements during the geocoding process. See the [Linkage and processing of address data guide](../linkage_and_processing.md) for background information on this. For full documenation on how to interpret the Experian *matchcode* see the [Experian documentation](https://docs.experianaperture.io/address-validation/batch-api/api-process/address-match-codes/#k-s~match-success). 

### Air pollution variables
Air pollution variables in the form *no2_YYYY/pm_YYYY* are annual averages. These should be used in **conjunction with the address start and end dates** to assign the annual averages for the years that correspond to when the participant was at that address. Note, the UK LLC Data Team will build a transformed version of this dataset with this pre-processing step already completed in due course. This documentation will be updated when this is place.

### Geographical units
Additional to the air pollution measures, these data contain a number of geographical units/levels:
* UK region
* Lower Super Output Area (LSOA) encrypted
* Middle Super Output Area (MSOA) encrypted 
* Postcode encrypted
* Unique Property Reference Number (UPRN) encrypted.

These allow participants to be **grouped into common geographical units**. The encryption is a disclosure control measure due to the elevated risk in providing individual level geolocation data. However, statistics about the encrypted LSOA can be added by linking to table/dataset **CORE_lsoa11_geo_indicators** on variable *lsoa11_e*. This dataset is available to all researchers working in the UK LLC TRE. It contains deciles of Indices of Multiple Deprivation (IMD) including sub domains, population density, and an urban rural indicator. When linked to the air pollution dataset, this will enable **additional economic and environmental insight** into the geographical area.

### Scottish geographies 
Scotland and Northern Ireland use different community geography terminologies in their censuses. The Scottish equivalent of MSOAs are called ‘Intermediate Zones' (IZ), and ‘Datazones’ (DZ) are used as equivalent of LSOAs. For data storage these are all stored in a single field:

**Table 1** Scottish equivalent geographies
| **England & Wales** | **Scotland** | **Column name in dataset** |
|---|:---:|:---:|
| LSOA (Lower Layer Super Output Area)| Datazones (DZ) | lsoa11_e |
| MSOA (Middle Layer Super Output Area) | Intermediate Zones (IZ) | msoa11_e |

## References
```{bibliography}
```

## Caveats: 

- Background NO2 and PM2.5 pollutant maps between 2010 and 2020 were obtained from the DEFRA UK Air data archive (UK Air, n.d) in its original .csv file format. Each file presents a basic summary of each dataset (pollutant, year, metrics, and units), as well as, the unique code (ukgridcode), xy coordinates and pollutant measurement for each 1x1km grid cell. Firstly, the time-series .csv files for each pollutant were imported into R as a single data frame, except for the baseline year 2015. It was noted that there were several grid cells that did not have any associated pollutant values and were instead labelled as ‘MISSING’. These cells are identified as coastal grids in which the centre of the grid cell is not located on land. Since there was no associated pollutant concentration these cells were assigned an NA value. The NO2 and PM2.5 spatial data frames were then rasterised into a 1km x 1km grid cell format (projection, British National Grid:27700), displaying the annual average pollutant concentration for each grid to 3.dp.










