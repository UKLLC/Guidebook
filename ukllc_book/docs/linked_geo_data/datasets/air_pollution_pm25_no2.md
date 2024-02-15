# Background
This dataset contains continuous annual-average nitrogen dioxide (NO2) and fine particulate matter (PM2.5) exposure data. This covers the years 2010 - 2019 for all residential address points where a UK LLC participant has permissions in place.

## Nitrogen dioxide (NO2)
NO2 gas is mainly produced during combustion of fossil fuels. Short term exposure to elevated concentrations of NO2 can have adverse health impatcs sich as inflammation of the airways and increase susceptibility to respiratory infections and allergens. NO2 can exacerbate symptoms of those suffering from heart of lung conditions {cite}`GOVNO2`.

## Fine particulate matter (PM2.5)
Particulate Matter (PM) is everything in the air that is not a gas and as such it is made up from a huge variety of chemical compounds and materials. PM is classified according to size. The UK currently focuses on estimating the fractions of PM emissions where particles are less than 10 micrometres in diameter (PM10) and less than 2.5 micrometres in diameter (PM2.5). Some PM is toxic and due to the small size of the particles, some toxins can enter the bloodstream and can be transported around the body, entering the heart, brain and other organs {cite}`GOVPM25`.

## Input surfaces 
The UK government, Department for Environment, Food & Rural Affairs (DEFRA) have modelled background annual-average air pollution concentrations since 2001 (1 x 1km resolution). These surfaces approximate changes in air pollution over time and provide exspoure estimates between the UK Automatic Urban and Rural Network (AURN). These are typically 10 - 100's kms apart and with high numbers in urban areas. 

Continuous annual-average NO2 and PM2.5 exposure surfaces are available across Great Britain, at 25x25m resolution in 2015 (Wang et al. 2022). Unlike the DEFRA surface these surfaces do not capture the temporal change in exposures. However, they do capture variability within and between streets. 

## Created surface
The NO2 and PM2.5 surfaces were created at a national scale using:
1) a high spatial resolution annual average pollutant surfaces produced by {cite}`WANG2022101506`and {cite}`ruby`
2) DEFRA’s high temporal resolution background concentration surfaces for 2010 to 2019.
creating high spatial-temporal exposure raster surfaces.

## Linkage to address
UK LLC participants residenital address points are linked to the raster surfaces containing the air pollution measures using a spatial join and (programme and package - R or ArcGIS??? and exact method e.g. NN, IDW?). This involves overlaying the address points over the raster images and assigning the ...

## Understanding the data
### table structure
The data is split over 2 tables/datasets:
1) GEO_air_pollution_hh where addresses are geocoded to the household level
2) GEO_air_pollution_pc where addresses are geocoded to the postcode level
see [geo linkage and processing page](../linkage_and_processing.md) for further info on linkage resolution.



```{bibliography}
```









