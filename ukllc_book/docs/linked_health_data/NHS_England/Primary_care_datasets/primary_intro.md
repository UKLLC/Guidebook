# NHS England primary care datasets
>Last modified: 01 Apr 2025

## Introduction
NHS England flows extracts of **two primary care datasets** into the UK LLC TRE - see Table 1.  

Researchers are permitted access to the **GDPPR dataset** under specific terms set by NHS England:
1. Research must be related to **COVID-19**. For examples of research purposes acceptable to NHS England see the [**COVID-19 Public Health Directions 2020**.](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/covid-19-public-health-directions-2020#:~:text=identifying%20and%20understanding) 
2. The GDPPR dataset must **not** be used for any form of performance management of General Practices.  

## Coverage of primary care datasets
As explained in the overarching [**NHS England datasets guide**](../NHSE_intro.md), the UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE. However, some datasets have alternative names. The **PCM dataset** is also known as **Medicines dispensed in Primary Care NHS Business Services Authority (NHSBSA) dataset**. We receive the data from NHS England as the PCM dataset and so use this name in our documentation.

Both the PCM and GDPPR datasets use primarily SNOMED codes - see the [**Coded variables guide**](../Coding/coding_intro.md) for further details.

Further information about the **GDPPR dataset** is below, with summary metrics on the next page [(GDPPR)](../Primary_care_datasets/GDPPR/GDPPR.ipynb).

**Table 1** Names, temporal coverage and availability of primary care datasets in the UK LLC TRE

| **Name in TRE**|**Full name**|**Other name**|**Domain**|**From**|**Until**|**Data available in TRE<sup>1</sup>**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|
|[**PCM**](../Other%20datasets/PCM/PCM.ipynb)|Primary Care Medicines|Medicines dispensed in Primary Care NHS Business Services Authority (NHSBSA) dataset|Primary care|01/04/2015|Ongoing|01/04/2015 onwards|
|[**GDPPR**](../Primary_care_datasets/GDPPR/GDPPR.ipynb)|General Practice Extraction Service (GPES) Data for Pandemic Planning and Research|N/A|Primary care|1940s|Ongoing|1940s onwards|NHSE|| 
<sup>1</sup>As documented in the data sharing agreement. 


## GDPPR dataset
Comprehensive information on the structure and purpose of the GDPPR dataset is available from [**NHS England**](https://digital.nhs.uk/coronavirus/gpes-data-for-pandemic-planning-and-research/guide-for-analysts-and-users-of-the-data#download-for-data-items)<sup>2</sup>.  

In summary:  
* The GDPPR dataset was established to fulfil the urgent need for general practice data for planning and research in response to the COVID-19 pandemic.  
* Data is only taken from GP practices where a practice has opted into the service via the Calculating Quality Reporting Service [**(CQRS)**](https://welcome.cqrs.nhs.uk/).  
* Only specific coded and structured data are extracted from the General Practice Extraction Service [**(GPES)**](https://digital.nhs.uk/services/general-practice-extraction-service/gpes-extracts-and-benefits) for inclusion in the GDPPR dataset, meaning that not all patients' records are included.  
* The GDPPR dataset uses [**SNOMED CT**](https://termbrowser.nhs.uk/?) codes, grouped into 'clusters' or 'reference sets'.  
* The list of SNOMED CT codes that are included in the GDPPR dataset is updated periodically in line with the business rules that govern patient inclusion and extracted record content. These rules can be downloaded via NHS England's [**Quality and Outcomes Framework (QoF)**](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/coronavirus-business-rules/gp-data-for-pandemic-planning-and-research)   


**Information about code clusters are available online:**
* The full list of code clusters can be explored via an NHS England dashboard: [**Microsoft Power BI**](https://app.powerbi.com/view?r=eyJrIjoiMjY4OTRhNmUtZDdiMy00NzVhLTkzMmMtZmRhMzAyOWFkZjc4IiwidCI6IjM3YzM1NGIyLTg1YjAtNDdmNS1iMjIyLTA3YjQ4ZDc3NGVlMyJ9).  
* The individual SNOMED codes included in each code cluster are listed on [**OpenCodelists**](https://www.opencodelists.org/)  
 
**SNOMED CT codes included in the GDPPR**  
All releases of the clusters are available online via the NHS [**TRUD**]([https://isd.digital.nhs.uk/trud/users/guest/filters/0/home) (Technology Reference Update Distribution). UK LLC has downloaded Release 51.0.0<sup>3</sup> and made it available as a [**downloadable text file**](http://apply.ukllc.ac.uk/apply/view_document/gdppr).  


>This material includes SNOMED Clinical Terms® (SNOMED CT®) which is used by permission of the International Health Terminology Standards Development Organisation (IHTSDO). All rights reserved. SNOMED CT®, was originally created by The College of American Pathologists. "SNOMED" and "SNOMED CT" are registered trademarks of the IHTSDO.  

N.B. The downloadable file contains 44,172 unique SNOMED CT codes and is in 'long' format to reflect the fact that most of the codes are in more than one cluster.

**Note**  
Every endeavour has been made by UK LLC to ensure the links provided contain up-to-date and helpful information about the content of the GDPPR dataset. UK LLC reviews these links regularly, but cannot guarantee the accuracy or completeness of the information provided. Guidebook users can help to update, or expand, the information available to other researchers by emailing [**support@ukllc.ac.uk**](mailto:support@ukllc.ac.uk).  
**We welcome all contributions to UK LLC Guidebook.**

***
1. <i>As documented in the data sharing agreement 
2. Web page accessed 24.03.2025 
3. N.B. Release 51.0.0 is dated 15.02.2024, while UK LLC’s GDPPR data was extracted on 26.04.2024. There is a chance that some of the drug cluster content may have changed slightly between the two dates because drug reference sets are released more frequently than the broader Primary Care Domain reference sets.</i>



 
