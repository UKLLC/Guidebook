# Registration datasets
## Introduction  
NHS England flows extracts of three registration datasets into the UK LLC TRE - see Table 1.


## Coverage of registration datasets
Table 1 summarises the **temporal and geographical coverage** of each of the three registration datasets. For a list of **variables** in the three datasets, see the [**NHS England Metadata dashboard**.](https://digital.nhs.uk/services/data-access-request-service-dars/dars-products-and-services/metadata-dashboard) 

**Table 1** Names, coverage, availability and ownership of registration datasets in the UK LLC TRE

| **Dataset name in TRE**|**Coverage**|**From**|**Until**|**Data available in TRE**|**Owner**|
|---|:---:|:---:|:---:|:---:|:---:|
|**CANCER**|England|01/01/1971|Ongoing|01/01/1971 onwards|NHSE|
|**DEMOGRAPHICS**|England & Wales|01/06/2004|Ongoing|01/06/2004 onwards|NHSE|
|**MORTALITY**|England & Wales|01/01/1993|Ongoing|01/01/1993 onwards|ONS|
|  |  

ONS: Office for National Statistics  


## Cancer Registration dataset
Data are collected by the **National Cancer Registration and Analysis Service (NCRAS)**, which is part of NHS England's [**National Disease Registration Service (NDRS)**](https://digital.nhs.uk/ndrs/).  

The Cancer Registration dataset is a subset of the **Cancer Outcomes and Services Dataset (COSD)**, which is the national standard for collecting cancer data in the NHS. The Cancer Registration dataset includes **all patients** (adults and children) **diagnosed with or receiving cancer treatment** in or funded by the NHS in **England since 1971**. Data collected include **demographic characteristics** and information about **diagnoses and treatments**.  

Data are collected under **section 251 of the NHS Act 2006**. Patients may opt out of the Cancer Registry, but this is different from the [**National data opt out**](https://digital.nhs.uk/services/national-data-opt-out). NCRAS works closely with cancer charities to promote the value of population-based cancer registration; **<1 in 10,000 cancer patients opt out of the registry**. For further information see the [**National Cancer Registration Dataset Data Resource Profile**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7124503/pdf/dyz076.pdf). 

## Demographics dataset  
The Demographics dataset is derived from the [**Personal Demographics Service (PDS) database**](https://digital.nhs.uk/services/personal-demographics-service), which is the national database of all **NHS patients** in **England, Wales** and the **Isle of Man** in or after **2004**. People born in these areas are registered and issued an NHS number at birth; people moving into these areas are registered when they first interact with an NHS care setting. Data collected include NHS numbers and basic **demographic details** such as date of birth, name, sex and address. The PDS does not hold any clinical information. NHS healthcare professionals use the PDS to accurately identify patients so they can find their correct medical records.

## Civil Registration of Deaths dataset
The Civil Registrations of Death dataset is collected by the [**Office for National Statistics**](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths). 
It is a legal requirement to report a death to a register office within five days. The informant provides **demographic details** to the registrar about the deceased, including occupation, sex, usual address, date and place of birth, marital status, date of death and place of death. If applicable, the informant also provides details about the **deceased's spouse**. If the deceased was a child, the full names and occupations of the parents are required. The informant usually also gives the **Medical Certificate of Cause of Death (MCCD)** to the registrar, which is a form completed by a medical practitioner when a death is certified. The MCCD includes information such as whether the body was seen after death, cause of death, when the deceased was last seen alive and whether a post-mortem was carried out. In instances where deaths are referred to and sometimes then investigated by a coroner, the coroner sends information to the registrar and this is used instead of the MCCD.  

The dataset includes details of all registered deaths in **England and Wales** since **1993**. For further information see the [**ONS Guide to Mortality Statistics**.](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/methodologies/userguidetomortalitystatisticsjuly2017#information-collected-at-death-registration)

 
## Clinical classifications in registration datasets
There are **ICD-9** and **ICD-10 codes** in the **CANCER** and **MORTALITY** datasets. No clinical classifications are used in the DEMOGRAPHICS dataset. See the [**Coded variables guide**](../NHS_England/Coding/coding_intro.md) for further details.

## Structure of registration datasets
The structure of the **CANCER, DEMOGRAPHICS** and **MORTALITY** datasets is **straightforward**, with each line representing one participant. 

## Data quality of registration datasets
### Cancer Registration dataset
Data submitted to the Cancer Registry are checked using a combination of **automated tools** and **manual review** by cancer registration officers who have detailed knowledge of cancer biology, coding and terminology. Care should be taken when interpreting time series, because clinical and coding definitions of cancer have changed over time. For further details see the [**National Cancer Registration Dataset Data Resource Profile**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7124503/pdf/dyz076.pdf). 

### Demographics dataset
The [**National Back Office (NBO)**](https://digital.nhs.uk/services/national-back-office-for-the-personal-demographics-service) provides a **data quality service** for the Personal Demographics Service. 


### Civil Registrations of Death dataset
It is a **legal requirement** for all deaths to be registered and it is an **offence** for informants to provide knowingly false information. This means that civil registrations of death data provide the **most complete information source for mortality statistics**. The Registration Online System (RON) used by registrars conducts **automatic checks**. Most deaths (around 80%) have the underlying cause of death coded automatically; the remainder are coded manually by experienced coders. ICD-10 codes for cause of death replaced ICD-9 codes on 01/01/2001 and this may affect the interpretation of trends. For further details see section 12 of the [**ONS Guide to Mortality Statistics**,](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/methodologies/userguidetomortalitystatisticsjuly2017#information-collected-at-death-registration) includes links to [**Quality and Methodology Information Reports**](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/methodologies/mortalitystatisticsinenglandandwalesqmi).




