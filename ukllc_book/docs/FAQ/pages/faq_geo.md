# Working with place-based data 

 

> Last modified: 20 Feb 2025

 
<details>
<summary>What is place-based data?</summary>

UK LLC place-based data covers the attributes, activities or experience of people derived from the places they have lived.  
</details>
  
<details>
<summary>What is geocoding?</summary>

Geocoding is the assigning of geographical coordinates to a location. The following address data are provided by LPS to UK LLC: 

Address line 1 (Premises level) 

Address line 2 (Street name) 

Address line 3 (Locality name) 

Address line 4 (Town) 

Address line 5 (Administrative area) 

Postcode 

These data are matched using a database lookup to convert the physical address into geographical coordinates, where LPS participants’ permissions allow full address to flow. Where permissions are set to postcode only, only the postcode is used in the geocoding process. Addresses are verified and geocoded to one metre accuracy using Experian QAS Batch API software programme (formerly QAS QuickAddress Batch API Software). For documentation on how to interpret the Experian matchcode see the Experian documentation.  
</details>
 

<details>
<summary>What can I do with place-based datasets? How might they enhance my research project?</summary>  

Place-based data provides information about the attributes and environment of where participants live. The linked data can be used to investigate the impact of environmental exposures on participants’ health. In addition, spatial covariates (risk factors) into can be introduced into your models to reduce the error in the model to increase the power of the factor tests eg. Analysis attempting to understand environmental triggering of a disease. 
</details>
 

<details>
<summary>How much pre-processing of the datasets has UK LLC done?</summary>  

During our place-based risk assessment we identify and evaluate the potential risks of disclosing sensitive geographic information that could result in the spontaneous recognition of a participant or place. During the variable transformation stage of the risk assessment, perturbation techniques such as removing identifiers and aggregating data are applied. The perturbation method for each variable is selected based on the transformation that preserves the most utility. Utility measurement is used to assess the usefulness of each variable after anonymisation. As data are updated, the associated risk assessment is also updated, ensuring that UK LLC is continuously refining the balance between risk and utility through an iterative process. 
</details>
 

<details>
<summary>How does UK LLC make sure that I can’t see where people live?</summary>    

UK LLC performs rigorous disclosure control checks before place-based data enter the TRE. These checks ensure that there are no counts below 5 for a specific characteristic at either local authority level or regional level, thereby minimising the risk of spontaneous recognition of places and participants by researchers. The checks also address the following risks:  

- whether the inclusion of two time periods would lead to disclosure (e.g. the building or demolishing of houses) 

- whether recognisable patterns in the data disclose specific location types (e.g. care homes, prisons, small islands, student accommodation)  

- whether anomalies in the data disclose specific buildings (e.g. the tallest building in a region)  

- whether a date can be used to identify a location (e.g. a data point might be generated when someone moves house) 

- whether a geographical unit has such a specific set of characteristics that it can be spontaneously identified (e.g. the City of London)  

- whether the inclusion of boundary changes over time could lead to disclosure.  
</details>
 

<details>
<summary>LPS have to provide permissions at 4 levels, but what does this mean to me as a researcher?</summary>      

Not every LPS has [permissions for place-based linkages](https://guidebook.ukllc.ac.uk/docs/lps/linkages/lps_linkages) and the geographic unit of the permissions differs, i.e. address level vs. neighbourhood level. We will be adding more information about the geo linkages to future freezes.
</details>
 

<details>
<summary>Are match scores available to indicate the accuracy of each linked record?</summary>   

Geomodelled datasets have match scores i.e. only place-based datasets that require geocoding for linkage – see Experian documentation. Otherwise, match scores are not available.   
</details>
 

<details>
<summary>What are the potential disclosure risks of linking at property level vs postcode level?</summary>  

For household level data that is added to the UK LLC TRE, the datasets have passed disclosure control checks at the UPRN/household level. When a postcode is geocoded, it is associated with multiple UPRNs – on average there are 15 properties in a postcode. While the risk is marginally higher for full address level data, it is still minimal because of the robust disclosure checks prior to data entering the TRE. 
</details>