# README: Air pollution NOx, NO2 and O3 


>Last modified: 06 Jun 2025

## Hybrid Air Dispersion Exposure System (HADES) 

### Methodology

The exposure surfaces were created using the HADES: Hybrid Air Dispersion Exposure System modelling framework. 

The model’s statistical calibration parameters were constructed from up to 6,024 hourly-annual average concentrations, collected at 130 monitoring sites across England and Wales in 2018-19.  

- NO2 and NOx = 6,024 annual-hourly average values were calculated (all hours had a capture rate > 50% and were checked for unusual outliers) 

***For further context: 124 sites in 2018 (2,976 hours), and 127 sites in 2019 (3,048 hours) = 6,024 hours in total from 130 unique sites*** 

- O3 = 2,832 annual-hourly average values from 60 sites (60 sites in 2018, of which 58 operated in 2019) 

  

The entire analysis considered 2018, 2019, and 2020 there are 136 unique sites 

- 2020 was used for cross-validation prediction of air quality 

 

Validation of the hourly-annual average 10m x 10m surfaces for England and Wales was achieved by comparison with time-weighted measurements (by season and month) at 136 locations in the UK governments air pollution network (UK-AURN). Sites were required to have recorded valid observations following network ratification, for at least 50% of the available hourly measurements in the specified period. 

The 10m annual-average concentration surfaces reported r-squared (goodness-of fit) values of 0.80 for NO2 and 0.86 for O3, with respect to measurement data at 136 locations in the UK governments automatic monitoring network. The same annual-average NO2 and O3 surfaces are associated with root mean squared error (RMSE) values of 4.90 µg/m3 and 3.17 µg/m3, respectively. 

## Caveats: 

- These datasets are limited to annual average assessments (hourly and 24-hour) for NOx, NO2 and O3 across England and Wales. 

- The datasets include 3-D building data as a GIS surrogate (i.e., street canyon) for the effect of ventilation on pollutant dispersion. Buildings are used in the statistical calibration, as it would not be practical to produce a physical model of the effects of buildings at national scale.  

## Limitations:  

- Reduced model performance was observed at some traffic (kerbside) locations, but these represent a small part of dataset. Kerbside concentrations are difficult to capture due to their high levels of spatiotemporal variability (i.e., NOx ranges from 9.7 to 175 µg/m3) and immediate proximity to the source.  

- All environmental modelling applications are limited by the spatial accuracy and precision of the emission data that underpins them.  

 

 