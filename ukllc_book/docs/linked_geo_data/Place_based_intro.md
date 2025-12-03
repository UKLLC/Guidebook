# Place-based data

> Last modified: 03 Dec 2025

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has established data pipelines to ingest both open-source place-based data and datasets provided by agreed partners into the UK LLC Trusted Research Environment (TRE).</strong></div>  

## Introduction
Place-based data can be linked to participants using address data provided by Longitudinal Population Studies (LPS) or linked area indicators (e.g. Lower Super Output Area, LSOA) in participants’ NHS records. All geographic identifiers in the UK LLC TRE below the region/devolved nation level are encrypted.

The place-based datasets cover a variety of domains and time periods, as summarised in Table 1. Their geographic coverage varies per dataset based on availability across the four UK nations. Further details, including external links to publications and metadata, are available in the individual dataset guides.

Researchers never access participants’ address data – the only location variables in the clear in the UK LLC TRE are English region (e.g. South West England) or devolved nation (e.g. Scotland).

Place-based data can be linked using LPS-provided address data or linked area indicators (e.g., LSOA, which is in participants’ NHS records).

All address data are sent by the LPS to our trusted third party – NHS Digital Health and Care Wales (DHCW). This address data is only used for place-based linkage and geocoding, subject to individual LPS approval.

Visit <strong><a href="https://explore.ukllc.ac.uk/" target="_blank" rel="noopener noreferrer">UK LLC Explore</a></strong> to discover more about each place-based dataset, including variable names, labels, and values.  

**Table 1** A summary of the place-based datasets in the UK LLC TRE, grouped by theme.

| Dataset name | Primary domain | Secondary domain | Summary | Coverage | Smallest data resolution | Data available in TRE | Owner |
|--------------|----------------|------------------|---------|----------|---------------------------|------------------------|--------|
| [Access to Healthy Assets and Hazards (AHAH)](../linked_geo_data/environmental_datasets/neighbourhood_datasets/AHAH/AHAH.ipynb) | Environmental | Neighbourhood | A multi-dimensional index measuring how ‘healthy’ neighbourhoods are. | England, Scotland, Wales | Lower Super Output Area/Data Zone | 2022 | [Geographic Data Service](https://data.geods.ac.uk/) |
| [Greenspace](../linked_geo_data/environmental_datasets/neighbourhood_datasets/greenspace/greenspace.ipynb) | Environmental | Neighbourhood | Greenspace metrics on greenspace coverage, access and walkability. | England, Scotland, Wales, Northern Ireland (selected variables) | Address | 2018 | University of Leicester |
| [Energy Performance Certificates (EPC)](../linked_geo_data/environmental_datasets/property_datasets/EPC/Understanding_epc.md) <br>*Coming in 2026* | Environmental | Property | Energy efficiency and property qualities. | England, Wales | Address | 2008–2024 | Department for Levelling Up, Housing & Communities |
| [Air pollution NO2 & PM](../linked_geo_data/environmental_datasets/pollution_datasets/air_pollution_pm25_no2/air_pollution_pm25_no2.ipynb) | Environmental | Pollution | Annual-average nitrogen dioxide (NO2) and fine particulate matter (PM2.5) exposure data. | England, Scotland, Wales | Address | 2010–2019 | University of Leicester and St George's, University of London |
| [Air pollution NOx, NO2 and O3](../linked_geo_data/environmental_datasets/pollution_datasets/air_pollution_o3/air_pollution_o3.ipynb) | Environmental | Pollution | Annual average assessments (hourly and 24-hour) for NOx, NO2 and O3. | England, Wales | Address | 2018–2020 | University of Leicester and St George's, University of London |
| [Noise pollution](../linked_geo_data/environmental_datasets/pollution_datasets/noise_pollution/noise_pollution.ipynb) | Environmental | Pollution | Modelled road-transport noise estimates. | England, Wales | Address | 2013 | University of Leicester and St George's, University of London |
| [Index of Multiple Deprivation](../linked_geo_data/population_datasets/IMD/IMD.ipynb)| Population | Deprivation | A relative indicator of deprivation, urban/rural classification and population density |England, Scotland, Wales, Northern Ireland | Lower Super Output Area/Data Zone/Super Output Area | 2011-2020 | UK LLC |
| [Townsend Index](../linked_geo_data/population_datasets/townsend/townsend.ipynb) | Population | Material deprivation | A relative indicator of material deprivation | England and Wales | Lower Super Output Area | 2021 | University of Leicester and St George's, University of London |


<br>

We are currently in the process of adding new place-based datasets into the TRE. If you require a specific dataset, or additional variables in an existing dataset to provide a higher level of granularity, please contact **support@ukllc.ac.uk**.  

>**Note**  
While access to standard place-based datasets is free, the preparation of bespoke datasets may involve a cost depending on the complexity of the request.  
