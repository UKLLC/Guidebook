# NHS England other datasets
>Last modified: 05 Jul 2024
## Introduction
NHS England flows extracts of **three datasets** into the UK LLC TRE that do not fit into the other categories in the UK LLC Guidebook. These are the **Community Services Data Set (CSDS)**, the **Maternity Services Data Set (MSDS)** and the **Primary Care Medicines (PCM) dataset** - see Table 1. 

NHS England has stipulated that researchers are permitted access to the **PCM dataset** only for research that provides information about the **safety and effectiveness of medicines**, as specified by the [**NHSBSA Medicines Data Directions**.](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/nhs-business-services-authority-nhsbsa-medicines-data-directions-2019)

MSDS and CSDS use SNOMED, ICD-10 and OPCS-4. The PCM dataset uses primarily SNOMED - see the [**Coded variables guide**](../Coding/coding_intro.md) for further details.

## Coverage of datasets
Table 1 summarises the **temporal coverage** of the three datasets. All three datasets primarily only cover **England** - see below.  

As explained in the overarching [**NHS England datasets guide**](../NHSE_intro.md), the UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE. However, some datasets have alternative names. The **PCM dataset** is also known as **Medicines dispensed in Primary Care NHS Business Services Authority (NHSBSA) dataset**. We receive the data from NHS England as the PCM dataset and so use this name in our documentation.

**Table 1** Names, temporal coverage and availability of datasets in the UK LLC TRE

| **Name in TRE**|**Full name**|**Other name**|**Domain**|**From**|**Until**|**Data available in TRE<sup>1</sup>**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|
|[**CSDS**](../Other%20datasets/CSDS/CSDS.ipynb)|Community Services Data Set|N/A|Community|01/10/2017|Ongoing|01/04/2015 onwards|
|[**MSDS**](../Other%20datasets/MSDS/MSDS.md)|Maternity Services Data Set|N/A|Maternity|01/04/2015|Ongoing|TBC<sup>2</sup>|
|[**PCM**](../Other%20datasets/PCM/PCM.ipynb)|Primary Care Medicines|Medicines dispensed in Primary Care NHS Business Services Authority (NHSBSA) dataset|Medicines|01/04/2015|Ongoing|01/04/2015 onwards|

<sup>1</sup>As documented in the data sharing agreement. 

<sup>2</sup>MSDS data have not yet flowed into the TRE.  




