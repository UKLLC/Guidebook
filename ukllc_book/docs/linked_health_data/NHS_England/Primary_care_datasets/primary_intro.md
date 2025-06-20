# NHS England primary care datasets
>Last modified: 20 Jun 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The primary care datasets cover GP records and prescriptions in England.</strong></div>  
<br>

>## Summary:
>* UK LLC holds **two NHS England primary care datasets**: [**General Practice Extraction Service (GPES) Data for Pandemic Planning and Research (GDPPR)**](../Primary_care_datasets/GDPPR/GDPPR.ipynb) and [**Primary Care Medicines (PCM)**](../Primary_care_datasets/PCM/PCM.ipynb).  
<br>
>* The **PCM dataset** is also known as **Medicines dispensed in Primary Care NHS Business Services Authority (NHSBSA) dataset**.  
<br>
>* Researchers are permitted access to the GDPPR dataset under two **specific terms** set by NHS England: 1. Research must be related to **COVID-19**. For examples of research purposes acceptable to NHS England see the [**COVID-19 Public Health Directions 2020**.](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/covid-19-public-health-directions-2020#:~:text=identifying%20and%20understanding) 2. The GDPPR dataset must **not** be used for any form of performance management of General Practices.    
<br>
> * The GDPPR dataset spans **1940s onwards** and the PCM dataset **2015 onwards**.  
<br>
> * Both the GDPPR and PCM datasets use primarily **SNOMED CT codes**. See the [**Coded variables guide**](../Coding/coding_intro.md) for further details.   
<br>      

## Overview of primary care datasets
For further information see the **individual dataset guides.**

**Table 1** Names, geographical coverage and availability of primary care datasets in the UK LLC TRE 

|**Dataset**|**Dataset name**|**Other name**|**Grouping**|**Coverage**|**Data available in TRE**|**Data owner**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|
|[**GDPPR**](../Primary_care_datasets/GDPPR/GDPPR.ipynb)|General Practice Extraction Service (GPES) Data for Pandemic Planning and Research|N/A|GP records|England|1940s onwards|NHSE|
|[**PCM**](../Other%20datasets/PCM/PCM.ipynb)|Primary Care Medicines|Medicines dispensed in Primary Care NHS Business Services Authority (NHSBSA) dataset|Prescriptions|England|01/04/2015 onwards|NHSE||




## GDPPR dataset - MOVE TO README??
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



 
