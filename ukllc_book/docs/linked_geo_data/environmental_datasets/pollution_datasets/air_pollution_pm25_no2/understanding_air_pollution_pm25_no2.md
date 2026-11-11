# Understanding: Air pollution NO2 & PM

>Last modified: 29 Oct 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong> </strong>UK LLC provides annual-average NO₂ and PM₂.₅ exposure data at high spatial resolution which can support health and environmental research.</div>
<br>

## Introduction

Continuous annual-average nitrogen dioxide (NO2) and fine particulate matter (PM2.5) exposure surfaces are available across Great Britain, at 25x25m resolution in 2015 [(Wang et al. 2022)](https://doi.org/10.1016/j.apr.2022.101506). These surfaces capture the variability in exposure within streets and on a street-by-street basis. However, these surfaces do not capture the temporal change in exposures.

**Nitrogen dioxide (NO2):**
NO2 gas is mainly produced during combustion of fossil fuels. Short term exposure to elevated concentrations of **NO2 can have adverse health impacts** such as inflammation of the airways and increased susceptibility to respiratory infections and allergens. NO2 can exacerbate symptoms of those suffering from heart or lung conditions <a href="https://www.gov.uk/government/statistics/air-quality-statistics/ntrogen-dioxide" target="_blank" rel="noopener noreferrer">Food & Rural Affairs Department for Environment, 2023</a>.

**Fine particulate matter (PM):**
Particulate matter (PM) is everything in the air that is not a gas and as such it is made up from a huge variety of chemical compounds and materials. PM is classified according to size. The UK currently focuses on estimating the fractions of PM emissions where particles are less than 10 micrometres in diameter (PM10) and less than 2.5 micrometres in diameter (PM2.5). Some PM is toxic and due to the small size of the particles, some toxins can enter the bloodstream and can be transported around the body, entering the heart, brain and other organs <a href="https://www.gov.uk/government/statistics/emissions-of-air-pollutants/emissions-of-air-pollutants-in-the-uk-particulate-matter-pm10-and-pm25" target="_blank" rel="noopener noreferrer">Food & Rural Affairs Department for Environment, 2024</a>.

The UK government, Department for Environment, Food & Rural Affairs (Defra) has modelled background annual-average air pollution concentrations at a 1x1km resolution since 2001. These surfaces approximate changes in air pollution over time at a sub-regional geographic resolution. Beneficially, they provide exposure estimates between the monitoring stations in the UK Automatic Urban and Rural Network (AURN), which are separated by 10-100’s of kilometres and tend to be skewed towards major urban agglomerations.

Air pollution exposure timeseries datasets were created by applying ratios, which describe the annual change in sub-regional pollutant concentrations, to the 25x25m resolution exposure surfaces in 2015. It is assumed that the location and within-year contributions from pollutant sources have remained stable over the period of 2010-19.

## Methodology

#### Underlying air pollution surfaces

Two environmental exposure surfaces were required for the development of a high spatial-temporal exposure surface for NO2 and PM2.5 at a national scale:

1) **High spatial resolution** annual average pollutant surfaces at 25x25m resolution produced by <a href="https://www.sciencedirect.com/science/article/pii/S130910422200188X" target="_blank" rel="noopener noreferrer">Wang et al., (2022)</a>. 

2) UK government, Department for Environment, Food & Rural Affairs **(DEFRA)** high temporal resolution background concentration surfaces for 2010 to 2019.

The acquired environmental exposure surfaces exist in raster formats. A raster is simply a matrix of values organised into rows and columns, representing pairs of evenly spaced XY coordinates on a gridded spatial surface.

* Exposure surfaces produced by [Wang et al. (2022)](https://doi.org/10.1016/j.apr.2022.101506) capture modelled annual-average concentrations of NO2, particulate matter (PM2.5 and PM10) and ozone on a 25m grid for 2011 to 2015. The generalised additive mixed model utilises air pollution measurements, spatial data on land use, road network, traffic, topography, population density, metrological conditions, and chemical maps within a two-stage SpatioTemporal-Land Use Regression (ST-LUR) in alignment with research conducted by [Eeftens et al. (2012)](https://doi.org/10.1021/es301948k) and [Yanosky et al. (2014)](https://link.springer.com/article/10.1186/1476-069X-13-63). 

* Firstly, verified daily mean air pollutant measurement data for NO2, particulate matter and ozone from 2011 to 2015 was obtained from the Automatic Urban and Rural Network (AURN). The AURN is the UK’s largest automatic monitoring network providing hourly pollutant concentrations from 6 classified monitoring sites (background urban, background suburban, background rural, traffic urban, industrial urban and industrial suburban). 

* 2 main criteria were followed when selecting monitoring sites; 1) only monitoring sites with more than 75% daily mean measurements each month and year were included (~50% for PM) to ensure sufficient daily data availability; and 2) Industrial sites were excluded to optimise residential exposure assessment modelling. 

* Alongside daily concentrations, Wang’s model also incorporated local scale predictor variables to characterise the local environment (topography, landcover, building height), information on traffic flow (AADT for major and minor roads), represent emission sources/sinks of air pollution, daily estimates from chemical transport models and population demographics (density). 

* Circular distance buffers (ranging from 25m to 5000m) were derived using a Geographical Information System (GIS) to quantify spatial predictor variables around monitoring sites. The following predictor variables were then implemented into 2 LUR models (a standardised LUR model and a two-step LUR model) to firstly test the spatio-temporal model’s ability to predict annual concentrations and secondly, to account for time-varying spatial variability. A penalised spline smooth function was also applied to covariates to reduce any potential overfitting of data. 

* Model evaluation and sensitivity tests showed that the model performed well in explaining the variability in daily average measured concentrations at 63% for NO2, 77% for PM2.5, 80% for PM10, 85% for O3. The NO2 model performed best using spatial predictor variables such as traffic loads in a 50m buffer, major road length in a 1000m buffer and building volume around main roads in a 50m buffer, producing an RMSE of 12.7 ug/m3, slope of 0.79 and bias of 8.5ug/m3. PM2.5 showed similar results (RMSE 5.0 ug/m3, slope of 0.81, and bias of 3.0ug/m3) using meteorological covariates, traffic load in a 50m buffer, natural land in a 1000m buffer and building volume around main roads in a 50/100m buffer. 

Exposure surfaces produced by DEFRA’s Modelling of Ambient Air Quality contract capture background concentrations for 8 pollutants (PM10, PM2.5, NOx, NO2, CO, SO2, Ozone and Benzene) at a 1kmx1km spatial resolution for years 2001 to 2020. To model background concentrations across the UK, contributions from the sources highlighted are required to meet relevant metrics as set out in the [Air Quality Standards Regulations (2022)](https://uk-air.defra.gov.uk/library/reports?report_id=1022): 
- Large point source emissions modelled using ADMS and emissions estimates from the UK National Atmospheric Emissions Inventory (NAEI 2019)
- Small point sources
- Emissions Trading Scheme (ETS) point sources
- Distant sources – characterised by rural background concentration
- Area sources (diffuse emissions) related to domestic combustion
- Area sources related to road traffic – modelled using a dispersion kernel using time varying emissions from NAEI 2019.
- Fugitive point source emissions – modelled using fugitive source kernel model and fugitive components derived from NAEI 2019 (C6H6 only).

For PM2.5 and PM10 the following additional contribution are also included for modelling:
- Secondary inorganic aerosol
- Secondary organic aerosol
- Regional primary particles
- Regional calcium rich dust from re-suspension of soils
- Regional iron rich dusts from re-suspension
- Iron rich dusts from re-suspension due to vehicle activity
- Sea salt
- Residual

Dispersion modelling is undertaken by modelling the following contributions alongside meteorological data from the Weather Research and Forecasting (WRF) models using ADMS 5.2. Background concentration estimates are then calibrated using UK national network monitoring data. 

Minimum and maximum pollutant concentrations for the baseline year are required to ensure that resampling methods to scale the pollutant surfaces do not exceed annual-mean values.  Minimum and maximum pollutant values for 2015 were derived from Automatic Urban and Rural Network (AURN) data (Table 1) which can be accessed through the R package ‘Open Air’.

#### Scaled Air Quality Surfaces

All raster surface creation and rescaling methods were carried out within the statistical software R (version 4.2.3) using the spatial data analysis packages Raster and TERRA (soon to supersede the Raster package). TERRA is an open library package which provides both generalised and specific functions for creating, reading, manipulating, and writing raster data. The TERRA package has been designed to alleviate issues regarding slow processing times and memory shortages noted when using large raster datasets with the Raster package, i.e., making use of C++ code and not needing to read entire raster grid information into memory (RAM).   

#### DEFRA background surface concentration creation

Background NO2 and PM2.5 pollutant maps between 2010 and 2020 were obtained from the DEFRA UK Air data archive [(UK Air, n.d)](https://uk-air.defra.gov.uk/data/pcm-data#startcontent) in its original .csv file format. Each file presents a basic summary of each dataset (pollutant, year, metrics, and units), as well as, the unique code (ukgridcode), xy coordinates and pollutant measurement for each 1x1km grid cell. Firstly, the time-series .csv files for each pollutant were imported into R as a single data frame, except for the baseline year 2015. It was noted that there were several grid cells that did not have any associated pollutant values and were instead labelled as ‘MISSING’. These cells are identified as coastal grids in which the centre of the grid cell is not located on land. Since there was no associated pollutant concentration these cells were assigned an NA value. The NO2 and PM2.5 spatial data frames were then rasterised into a 1km x 1km grid cell format (projection, British National Grid:27700), displaying the annual average pollutant concentration for each grid to 3.dp.

#### High resolution spatial-temporal scaling

A R programming script was created to model a high spatial-temporal resolution environmental exposure surface across the UK, using the spatial granularity of Wang’s NO2 and PM2.5 exposure surface and temporal regularity of the DEFRA background concentration maps. Upon initial inspection it was noted that the extent of Wang’s exposure raster maps was mis-aligned to the regular DEFRA raster grid. To ensure that both rasters were spatially aligned, an empty raster template was created which utilises a rounding function to align xy coordinates to the nearest grid cell. Minimum, and maximum annual-mean pollutant values at each monitoring site within UK-AURN were then extracted in R using the ‘Openair’ package (Table 1). These minimum and maximum pollutant measurements are implemented during the resampling functions described later in this section to ensure that resampling methods to scale the pollutant surfaces do not exceed annual-mean values.  Additionally, in alignment to Wang et al., annual-mean observations for each year were extracted from monitoring sites which had a 75%- hourly data capture for each year to ensure that time-varying spatial variability in population concentrations was accounted for.  

| Date | NO₂ n | NO₂ min (µg/m³) | NO₂ median (µg/m³) | NO₂ max (µg/m³) | PM₂.₅ n | PM₂.₅ min (µg/m³) | PM₂.₅ median (µg/m³) | PM₂.₅ max (µg/m³) |
|------|------:|----------------:|-------------------:|----------------:|--------:|------------------:|---------------------:|------------------:|
| 2010 | 102 | 2.97 | 29.59 | 98.30 | 52 | 7.07 | 13.55 | 23.05 |
| 2011 | 105 | 3.22 | 24.84 | 97.25 | 54 | 4.00 | 14.57 | 24.45 |
| 2012 | 103 | 2.96 | 24.82 | 93.98 | 57 | 3.82 | 12.83 | 21.46 |
| 2013 | 105 | 2.50 | 24.14 | 84.74 | 54 | 7.52 | 12.99 | 20.08 |
| 2014 | 99 | 2.31 | 22.34 | 93.62 | 56 | 7.09 | 12.55 | 18.19 |
| 2015 | 115 | 2.20 | 22.29 | 88.32 | 65 | 2.96 | 10.41 | 15.80 |
| 2016 | 124 | 2.04 | 24.33 | 89.12 | 63 | 2.55 | 10.38 | 15.88 |
| 2017 | 139 | 2.00 | 23.46 | 83.68 | 64 | 4.53 | 9.68 | 15.93 |
| 2018 | 148 | 1.87 | 22.09 | 84.71 | 68 | 4.98 | 10.06 | 15.80 |
| 2019 | 150 | 1.90 | 21.94 | 64.02 | 76 | 4.36 | 9.75 | 14.55 |
| 2020 | 147 | 1.65 | 16.90 | 46.88 | 76 | 3.33 | 7.97 | 11.56 |

**Table 1** – The statistical range of the annual-mean observations recorded at AURN sites with >= 75% hourly data capture in each year. N = valid site count. 

Two raster surface resampling approaches were used from within from the ‘Terra 1.7.23’ package:

- Firstly, a Lanczos interpolation, was used update the Wang et al 20xx surfaces to a 25x25m grid, with a regular extent that nests within the DEFRA grids. This method is designed to maintain (rather than smooth) the details of an image during resizing, allowing for the use of values outside of the original dataset. This technique uses windowed sinc functions, referred to as Lanczos kernels, as a convolution filter to reduce aliasing artefacts and improves edge sharpness [(Burger and Burge, 2022)](https://link.springer.com/book/10.1007/978-3-031-05744-1). The outputs generated are then imported into the aligned empty raster template.

Baseline year – DEFRA surfaces to 2015 year

- Secondly, a cubic spline interpolation was used to resample the 1x1km Defra pollution scaling ratios to the 25x25m output cells. Cubic interpolation calculates the weighted average of the nearest 16 pixels, providing a smoother pixel result compared to nearest-neighbour and bilinear (4 nearest pixels) methods. Cubic spline interpolation differs by applying polynomials to smooth the continuity at neighbouring pixels of the raster data. It is known to be an effective resampling technique that doesn’t compromise on image quality and yields superior results when compared to nearest-neighbour and bilinear methods ([Baboo et al. 2010](https://globaljournals.org/GJCST_Volume10/10-An-Analysis-of-Different-Resampling-Methods-in-Coimbatore-District.pdf); [Perich et al. 2023](https://www.sciencedirect.com/science/article/pii/S0378429023000175)).

#### Geocoding of participant addresses

In order to derive the environmental characteristics and exposures associated with residential locations, participant addresses were geocoded. More information on this process can be found on the Guidebook page: [Environmental Exposure Estimates](https://guidebook.ukllc.ac.uk/docs/linked_geo_data/processing/processing_and_linkage.html#environmental-exposure-estimates)

## Caveats:

*  The dataset output consists of annual average concentrations of NO₂ and PM₂.₅ at 25 x 25m resolution for each year from 2010 to 2019 and is therefore not suitable for investigating seasonal patterns, short-term pollution episodes, or daily exposure variation.

* Some coastal grid cells did not have corresponding pollutant concentration estimates as the centre of the grid cell is not located on land and were assigned missing (NA) values.

## Limitations:

* Geocoding accuracy and completeness are dependent on the quality, completeness and specificity of the source address information, resulting in varying match confidence, positional uncertainty and a proportion of unmatched records. More information on the match success and confidence level of the geocoding used in the datasets can be found [here](https://guidebook.ukllc.ac.uk/docs/linked_geo_data/processing/processing_and_linkage.html#environmental-exposure-estimates).

## Useful Syntax

#### Dataset/table split
The data are split over 2 tables/datasets:
1) **PLACE_air_pollution_hh** which contain LPS that have permitted a participant’s full residential address to be geocoded and the environmental exposure metrics have been assigned using the participant’s geocoded residential address. 
2) **PLACE_air_pollution_pc** which contain LPS that have permitted a participant’s postcode to be geocoded and the environmental exposure metrics have been assigned using the participant’s residential postcode.

Further details on which LPS are in which dataset can be found [here](https://guidebook.ukllc.ac.uk/docs/available_linkages/lps_actual_geographic.html). 

### Air pollution variables
Air pollution variables in the form *no2_YYYY/pm_YYYY* are annual averages. These should be used in **conjunction with the address start and end dates** to assign the annual averages for the years that correspond to when the participant was at that address.

#### Geographical units
Additional to the air pollution measures, these data contain a number of geographical units/levels:
* UK region
* Lower Super Output Area (LSOA) for England and Wales/ Data Zone (DZ) for Scotland and Super Output Area (SOA) for Northern Ireland,encrypted.
* Middle Super Output Area (MSOA) encrypted
* Postcode encrypted
* Unique Property Reference Number (UPRN) encrypted.

These allow participants to be **grouped into common geographical units**. The encryption is a disclosure control measure due to the elevated risk in providing individual level geolocation data. However, statistics about the encrypted LSOA/equivalent can be added by linking to the [Index of Multiple Deprivation (**PLACE_imd**)](../../../population_datasets/IMD/imd.ipynb) datasets. These datasets are available to request and can be linked to LPS with the [appropriate permissions](../../../../available_linkages/lps_actual_geographic.md). The datasets contain deciles of Indices of Multiple Deprivation (IMD) including sub domains, population density, and an urban rural indicator. When linked to the air pollution dataset, this will enable **additional economic and environmental insight** into the geographical area.

