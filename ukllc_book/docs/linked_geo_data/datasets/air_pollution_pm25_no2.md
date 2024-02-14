# Background
What is nitrogen dioxide (NO2) and fine particulate matter (PM2.5)

## Input surfaces 
The UK government, Department for Environment, Food & Rural Affairs (DEFRA) have modelled background annual-average air pollution concentrations since 2001 (1 x 1km resolution). These surfaces approximate changes in air pollution over time and provide exspoure estimates between the UK Automatic Urban and Rural Network (AURN). These are typically 10 - 100's kms apart and with high numbers in urban areas. 

Continuous annual-average NO2 and PM2.5 exposure surfaces are available across Great Britain, at 25x25m resolution in 2015 (Wang et al. 2022). Unlike the DEFRA surface these surfaces do not capture the temporal change in exposures. However, they do capture variability within and between streets. 

## Created surface
The NO2 and PM2.5 surfaces were created at a national scale using:
1) a high spatial resolution annual average pollutant surfaces produced by {cite}`WANG2022101506` and {cite}`ruby`
2) DEFRA’s high temporal resolution background concentration surfaces for 2010 to 2019.
creating high spatial-temporal exposure raster surfaces.  