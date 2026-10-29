# Understanding: Air pollution NOx, NO2 and O3 

>Last modified: 29 Oct 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong> </strong>UK LLC provides high-resolution national exposure surfaces for NO₂ and O₃ in England and Wales (2018–2020), modelled using the HADES framework and linked to residential locations and Census geographies for population-level analysis.</div>  
<br>

## Introduction

Hybrid Air Dispersion Exposure System (HADES) is a national-scale model of outdoor air pollution model that was developed for the rapid production of concentration maps of nitrogen dioxide (NO2) and ozone (O3) at very high spatial resolution (10m).  The model combines local dispersion modelling with satellite-derived estimates of background concentrations, land cover, and a 3-D representation of buildings, using open access datasets that are available in many countries. The model’s statistical calibration parameters were constructed from 6,072 hourly-annual average concentrations, collected at 130 monitoring sites across England and Wales in 2018-19.

### Methodology

The dataset provides estimates of NOx, NO₂, and O₃ concentrations across England and Wales. Data are available as both annual datasets for the years 2018, 2019, and 2020, and as hourly-annual datasets, which contain 24 values representing the average hourly concentration for each hour of a typical day for a given year and pollutant. The data are modelled at a 10 m × 10 m spatial resolution, with each grid cell recording surface-level exposures at a height of 1 m above ground level. Concentrations are reported in micrograms per cubic metre (µg/m³).

Full details of the dataset development, modelling methods, and evaluation are available in: Jephcote, C., & Gulliver, J. (2025). Development and evaluation of rapid, national-scale outdoor air pollution modelling and exposure assessment: Hybrid Air Dispersion Exposure System (HADES). Environment International, 197, 109304. DOI: https://doi.org/10.1016/j.envint.2025.109304.

Note: The annual-average nitrogen dioxide (NO₂) and ozone (O₃) surface-level exposure surfaces at 10 m × 10 m resolution for 2018–2020, together with their associated census data summaries, are also freely available for non-commercial use under a CC BY-NC 4.0 licence via: https://doi.org/10.6084/m9.figshare.27073906.

Residential addresses are linked to one of the 10 m × 10 m cells. This returns 9 annual (3 pollutants × 3 years) and 216 hourly-annual average (3 pollutants × 3 years × 24 hours) exposure values at each location.

High resolution hourly-annual and annual average surfaces were created across England and Wales for 2018-2020. The analysis covered the years 2018, 2019, and 2020, using data from 136 unique monitoring sites.

- NO₂ and NOx = 6,024 annual-hourly average values were calculated (all hours had a capture rate > 50% and were checked for unusual outliers).

  ***For further context: 124 sites in 2018 (2,976 hours), and 127 sites in 2019 (3,048 hours) = 6,024 hours in total from 130 unique sites***

- O₃ = 2,832 annual-hourly average values from 60 sites (60 sites in 2018, of which 58 operated in 2019).

- 2020 was used for cross-validation prediction of air quality.

Modelling explained 77-79% for NO₂ and 87-89% for O₃ of the variability in hourly-annual average concentrations, and was robust to changes in NOx emissions during the COVID pandemic.

Validation of the hourly-annual average 10 m × 10 m surfaces for England and Wales was achieved by comparison with time-weighted measurements (by season and month) at 136 locations in the UK governments air pollution network (UK-AURN). Sites were required to have recorded valid observations following network ratification, for at least 50% of the available hourly measurements in the specified period.

The 10 m annual-average concentration surfaces reported r-squared (goodness-of-fit) values of 0.80 for NO₂ and 0.86 for O₃, with respect to measurement data at 136 locations in the UK governments automatic monitoring network. The same annual-average NO₂ and O₃ surfaces are associated with root mean squared error (RMSE) values of 4.90 µg/m³ and 3.17 µg/m³, respectively. The R² values indicate how well the model predictions match observed data, while RMSE reflects the average prediction error in µg/m³.

In February 2023, environmental exposure modellers from the University of Leicester, Centre for Environmental Health and Sustainability were provided with either the full address level information or postcodes of participants from 7 Longitudinal Population Studies (ALSPAC, BIB, EXCEED, NIHRBIO_COPING, NSHD46, SABRE, TWINSUK) depending on the permitted linkage permissions.

Individual household hourly-annual and annual average air pollution estimates from HADES have been provided for:

- 178,301 receptor locations in England and Wales from the file where full participant addresses were provided.
- 201,476 receptor locations in England and Wales from the file where only participant postcodes were provided.

-Following disclosure control checks the original environmental exposure values have been rounded prior to be made available in the UK LLC TRE. While the original exposure values ranged between 0-6 decimal places, the submitted values are integers. 


#### Geocoding of participant addresses

In order to derive the environmental characteristics and exposures associated with residential locations, participant addresses were geocoded. More information on this process can be found on the Guidebook page: [Environmental Exposure](Estimates https://guidebook.ukllc.ac.uk/docs/linked_geo_data/processing/processing_and_linkage.html#environmental-exposure-estimates)

## Caveats: 

- These datasets are limited to annual average assessments (hourly and 24-hour) for NOx, NO2 and O3 across England and Wales. 

- The datasets include 3-D building data as a GIS surrogate (i.e., street canyon) for the effect of ventilation on pollutant dispersion. Buildings are used in the statistical calibration, as it would not be practical to produce a physical model of the effects of buildings at national scale.  

## Limitations:  

- Reduced model performance was observed at some traffic (kerbside) locations, but these represent a small part of the dataset. Kerbside concentrations are difficult to capture due to their high levels of spatiotemporal variability (i.e., NOx ranges from 9.7 to 175 µg/m3) and immediate proximity to the source.  

- All environmental modelling applications are limited by the spatial accuracy and precision of the emission data that underpins them.  

 ## Useful Syntax

#### Dataset/table split
The data are split over 2 tables/datasets:
1) **PLACE_hades_air_pollution_hh** which contain LPS that have permitted a participant’s full residential address to be geocoded and the environmental exposure metrics have been assigned using the participant’s geocoded residential address. 
2) **PLACE_hades_air_pollution_pc** which contain LPS that have permitted a participant’s postcode to be geocoded and the environmental exposure metrics have been assigned using the participant’s residential postcode.

Further details on which LPS are in which dataset can be found [here](https://guidebook.ukllc.ac.uk/docs/available_linkages/lps_actual_geographic.html). 

#### Geographical units
Additional to the air pollution measures, these data contain a number of geographical units/levels:
* UK region
* Lower Super Output Area (LSOA) for England and Wales/ Data Zone (DZ) for Scotland and Super Output Area (SOA) for Northern Ireland,encrypted.
* Middle Super Output Area (MSOA) encrypted
* Postcode encrypted
* Unique Property Reference Number (UPRN) encrypted.

These allow participants to be **grouped into common geographical units**. The encryption is a disclosure control measure due to the elevated risk in providing individual level geolocation data. However, statistics about the encrypted LSOA/equivalent can be added by linking to the [Index of Multiple Deprivation (**PLACE_imd**)](../../../population_datasets/IMD/imd.ipynb) datasets. These datasets are available to request and can be linked to LPS with the [appropriate permissions](../../../../available_linkages/lps_actual_geographic.md). The datasets contain deciles of Indices of Multiple Deprivation (IMD) including sub domains, population density, and an urban rural indicator. When linked to the air pollution dataset, this will enable **additional economic and environmental insight** into the geographical area.

 