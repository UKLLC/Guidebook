# Understanding: Access to Healthy Assets and Hazards (AHAH) Index

>Last modified: 18 Jul 2025

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The Access to Healthy Assets and Hazards (AHAH) dataset provides a suite of open-access health indicators, including a novel multidimensional index that summarises health-related features of neighbourhoods across Great Britain.</strong></div>  
<br>

## Access to Healthy Assets and Hazards (AHAH)

Information on the full version history of the AHAH index can be found on the [Geographic Data Service](https://data.geods.ac.uk/dataset/access-to-healthy-assets-hazards-ahah-previous-versions) website.

### Methodology

The AHAH index has been created by a ranked combination of the time-weighted distance required to travel by road between every postcode in Great Britain and a selection of health-related points of interest.

The index defines 'access' through the average time-weighted road network distance for each postcode within each Lower Super Output Area/Data Zone to the nearest point of interest of a particular type. The road highways network and road speed estimates provided through Ordnance Survey were used, in combination with the ONS Postcode Directory, which provides centroids for every postcode in Great Britain.

The authors [(Konstantinos et al. 2019)](https://doi.org/10.1038/s41597-019-0114-6) describe the index calculation as computationally intense, as the total road network used has ~3.8 million edges, and ~3.2 million nodes. Access to each nearest health-related point of interest was calculated using the [Multi Source Shortest Path algorithm](https://github.com/ESRC-CDRC/ahah/blob/main/ahah/route.py), for all ~1.7 million postcodes in Great Britain.

The full methodology and code used to develop the index can be found [here.](https://github.com/ESRC-CDRC/ahah?tab=readme-ov-file)

## Caveats:

- The AHAH index assumes a framework that environments can be separated into a linear scale of positive or negative environments. Using this framework is arguably simplistic and ignores that different combinations of neighbourhood features may create positive or negative environments ([Green et al., 2014](https://doi.org/10.1016/j.healthplace.2014.09.011)).

- The authors opted not to incorporate measures of the social environment in the AHAH index, so as not to replicate other commonly used deprivation measures. In fact, [Green et al. (2018)](https://doi.org/10.1016/j.healthplace.2018.08.019) demonstrate that AHAH was not found to be correlated to the Index of Multiple Deprivation. Nevertheless, the work of [Pampel et al. (2010)](https://doi.org/10.1146/annurev.soc.012809.102529) and Sampson (2012)* demonstrates the importance of social environment (e.g. poverty level, housing quality, access to good schools) in determining health.

- Further discussion on the data sources used in the AHAH index, their quality and a sensitivity analysis of the data 
outputs is available in the supplementary appendix of the paper [Green et al. (2018)](https://doi.org/10.1016/j.healthplace.2018.08.019).

\* **Sampson, R.J., 2012. _Great American City: Chicago and the Enduring Neighbourhood Effect_. University of Chicago Press.**

## Limitations:

- The input variables included in the index do not cover all features of environments that could influence an individual's health. The authors focused on environmental aspects that they could gain access to data on and where there was a clear association to health (Green et al. [2018](https://doi.org/10.1016/j.healthplace.2018.08.019)).One example is that the authors did not include access to convenience stores or supermarkets in the index as these outlets sell both 'healthy' and 'unhealthy' food and drink. As a result, indicators such as the presence of off-licenses and tobacconists may underestimate the prevalence of unhealthy retail environments, since alcohol and tobacco can also be purchased in other types of outlets 

- [Green et al. (2018)](https://doi.org/10.1016/j.healthplace.2018.08.019) explains that the input measure and the overall domain scores were weighted equally, however they may not contribute equally towards influencing health. The authors selected equal weightings because they could not identify agreement across the literature over how to fairly weight each input. However, the authors do make all of the inputs [openly available](https://data.geods.ac.uk/dataset/access-to-healthy-assets-hazards-ahah), so that researchers can alter and refine how the index is constructed to reflect their needs.

