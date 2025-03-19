# NHS England primary care datasets
>Last modified: 10 Feb 2025
## Introduction
The **General Practice Extraction Service (GPES) Data for Pandemic Planning and Research** [**(GDPPR)**](../Primary_care_datasets/GDPPR/GDPPR.ipynb) dataset is the only primary care dataset currently in the UK LLC TRE.  

Researchers are permitted access to the GDPPR dataset under specific terms set by NHS England:
1. Research must be related to **COVID-19**. For examples of research purposes acceptable to NHS England see the [**COVID-19 Public Health Directions 2020**.](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/covid-19-public-health-directions-2020#:~:text=identifying%20and%20understanding) 
2. The GDPPR dataset must **not** be used for any form of performance management of General Practices.  


## Coverage of the GDPPR dataset


**Table 1** Names, coverage, availability and ownership of primary care datasets in the UK LLC TRE

| **Name in TRE**|**Full name**|**Other name**|**Domain**|**Coverage**|**From**|**Data available in TRE<sup>1</sup>**|**Owner**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|[**GDPPR**](../Primary_care_datasets/GDPPR/GDPPR.ipynb)|General Practice Extraction Service (GPES) Data for Pandemic Planning and Research|N/A|Primary care|England|1940s onwards|1940s onwards|NHSE||  


<br>

Comprehensive information on the structure and purpose of the GDPPR dataset is available from [**NHS England**](https://digital.nhs.uk/coronavirus/gpes-data-for-pandemic-planning-and-research/guide-for-analysts-and-users-of-the-data#download-for-data-items)<sup>2</sup>.  
In summary:  
* The GDPPR dataset was established to fulfil the urgent need for general practice data for planning and research in response to the COVID-19 pandemic.  
* Data is only taken from GP practices where a practice has opted into the service via the [CQRS](https://welcome.cqrs.nhs.uk/).  
* Only specific coded and structured data are extracted from the General Practice Extraction Service [(GPES)](https://digital.nhs.uk/services/general-practice-extraction-service/gpes-extracts-and-benefits) for inclusion in the GDPPR dataset, meaning that not all patients' records are included.  
* The subset of available data is defined by a set of business rules, which specify the target cohort of patients, the coded record content for each extraction, and time period cut-offs.  

Over [**34,000 SNOMED**](https://digital.nhs.uk/coronavirus/gpes-data-for-pandemic-planning-and-research/guide-for-analysts-and-users-of-the-data#download-for-data-items) codes are used in the GDPPR data (of the 900,000+ SNOMED codes in the UK and international releases . Individual codes are grouped into clusters, e.g. the cluster BP_COD includes 162 codes related to blood pressure.  

**Further information about code clusters used in the GDPPR dataset is available online:**
* The full list of code clusters can be explored via an NHS England dashboard: [**Microsoft Power BI**](https://app.powerbi.com/view?r=eyJrIjoiMjY4OTRhNmUtZDdiMy00NzVhLTkzMmMtZmRhMzAyOWFkZjc4IiwidCI6IjM3YzM1NGIyLTg1YjAtNDdmNS1iMjIyLTA3YjQ4ZDc3NGVlMyJ9).  
* The individual SNOMED codes included in each code cluster are listed on [**OpenCodelists**](https://www.opencodelists.org/)  
* The business rules governing patient inclusion and extracted record content can be downloaded via NHS England's [**Quality and Outcomes Framework (QoF)**](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof/coronavirus-business-rules/gp-data-for-pandemic-planning-and-research)  

**Note**  
Every endeavour has been made by UK LLC to ensure the links provided contain up-to-date and helpful information about the content of the GDPPR dataset. UK LLC reviews these links regularly, but cannot guarantee the accuracy or completeness of the information provided. Guidebook users can help to update, or expand, the information available to other researchers either via Github (using these [**instructions**](../../../user_guide/contribute.md) or by emailing support@ukllc.ac.uk. **We welcome all contributions to UK LLC Guidebook.**


<sup>1</sup> As documented in the data sharing agreement.  
<sup>2</sup> Web page accessed 07.02.2025



 
