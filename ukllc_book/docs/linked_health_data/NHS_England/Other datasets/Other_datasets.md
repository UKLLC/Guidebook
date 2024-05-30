# Other datasets
## Introduction
NHS England flows extracts of **three datasets** into the UK LLC TRE that do not fit into the other categories in this Jupyter book. These are the **Community Services Data Set (CSDS)**, the **Maternity Services Data Set (MSDS)** and the **Primary Care Medicines (PCM) dataset** - see Table 1. 

NHS England has stipulated that researchers are permitted access to the **PCM dataset** only for research that provides information about the **safety and effectiveness of medicines**, as specified by the [**NHSBSA Medicines Data Directions**.](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/nhs-business-services-authority-nhsbsa-medicines-data-directions-2019)


## Coverage of datasets
Table 1 summarises the **temporal coverage** of the three datasets. All three datasets primarily only cover **England** - see below.  

As explained in the overarching [**NHS England datasets guide**](../NHS_England/NHSE_intro.md), the UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE. However, some datasets have alternative names. The **PCM dataset** is also known as **Medicines dispensed in Primary Care NHS Business Services Authority (NHSBSA) dataset**. We receive the data from NHS England as the PCM dataset and so use this name in our documentation.

**Table 1** Names, temporal coverage and availability of datasets in the UK LLC TRE

| **Name in TRE**|**Full name**|**Other name**|**From**|**Data available in TRE<sup>1</sup>**|
|---|:---:|:---:|:---:|:---:|
|**CSDS**|Community Services Data Set|N/A|01/10/2017|01/04/2015 onwards|
|**MSDS**|Maternity Services Data Set|N/A|01/04/2015|01/04/2015 onwards|
|**PCM**|Primary Care Medicines|Medicines dispensed in Primary Care NHS Business Services Authority (NHSBSA) dataset|01/04/2015|01/04/2015 onwards|
|  

<sup>1</sup>As documented in the data sharing agreement.  

## CSDS dataset
The CSDS collects data about **children, young people** and **adults** who are in contact with NHS funded organisations that provide **community services** in **England**. Settings include health centres, day care facilities, schools or community centres, mobile facilities or people's homes. 

The CSDS dataset replaced the **Children and Young People's Health Services Data Set (CYPHS)** which was restricted to those aged 18 years and under.  

The dataset provides information about social and personal circumstances, breastfeeding and nutrition, care event and screening activity, diagnoses, including long-term conditions and disabilities, scored assessments, and weight management services.


## MSDS dataset
The MSDS collects data about all **NHS funded maternity care** in **England**. The starting point for inclusion in the dataset is the formal antenatal booking and the end point is when the mother is discharged from maternity services, which is typically 10 days after discharge from hospital.

The dataset provides information about the mother’s demographics, booking appointments, admissions and re-admissions, screening tests, labour and delivery, along with the baby’s demographics, admissions, diagnoses and screening tests. 


Further information about the data collected is available [**here.**](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/maternity-services-data-set/guidance/general-msds-guidance)

## PCM dataset
The PCM dataset contains information about all **prescriptions** that have been submitted by prescribers to the NHS Business Services Authority (NHSBSA) for reimbursement purposes. 

The dataset includes prescriptions issued by pharmacists, dentists and doctors in general practice, community clinics, dentists, hospital clinics and community nursing homes. The prescriptions may have been **written in England** and dispensed UK-wide or written elsewhere in the UK and **dispensed in England**. 

For a full list of variables see the [**NHS England Metadata Dashboard.**](https://app.powerbi.com/view?r=eyJrIjoiMjY4OTRhNmUtZDdiMy00NzVhLTkzMmMtZmRhMzAyOWFkZjc4IiwidCI6IjM3YzM1NGIyLTg1YjAtNDdmNS1iMjIyLTA3YjQ4ZDc3NGVlMyJ9)

## Clinical classifications in these datasets
MSDS and CSDS use SNOMED, ICD-10 and OPCS-4. The PCM dataset uses primarily SNOMED - see the [**Coded variables guide**](../NHS_England/Coding/coding_intro.md) for further details.

## Structure of these datasets
The **CSDS** comprises more than 30 datasets. To access the CSDS data model and technical output specification, click [**here.**](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/community-services-data-set/implementing-the-community-services-data-set-csds-v1.6-tools-and-guidance)

The **MSDS** comprises more than 20 datasets. To access the MSDS data model and technical output specification, click [**here.**](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/maternity-services-data-set/tools-and-guidance)

To access the **PCM dataset** technical output specification, click [**here.**](9https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/medicines-dispensed-in-primary-care-nhsbsa-data)

## Data quality of these datasets
TBC