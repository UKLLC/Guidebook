# COVID-19 datasets
## Introduction  
NHS England flows extracts of **seven COVID-19 datasets** into the UK LLC TRE - see Table 1. Researchers are permitted access to these seven datasets under the following specific terms set by NHS England:
1. Research must be related to **COVID-19**.
2. **GDPPR data** must not be used for any form of performance management of General Practices.


## Coverage of COVID-19 datasets
Table 1 summarises the **temporal and geographical coverage** of each of the seven COVID-19 datasets.  

As explained in the overarching [**NHS England datasets guide**](../NHS_England/NHSE_intro.md), the UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE, apart from **SGSS** where we added COVID in front of it to distinguish it from the UK Health Security Agency’s (UKHSA's) generalised Second Generation Surveillance System (SGSS). Some datasets have been renamed by NHS England, e.g. **CHESS** is now called the **Severe Acute Respiratory Infection (SARI-Watch) surveillance system** dataset and some datasets have alternative names, e.g. **NPEX** is also called the **Covid-19 UK Non-hospital Antigen Testing Results** dataset. We receive the data from NHS England as the CHESS and NPEX datasets and these are the names researchers will see in the UK LLC TRE. Therefore, we refer to them by these names in our documentation. 

**Table 1** Names, coverage, availability and ownership of COVID-19 datasets in the UK LLC TRE

| **Name in TRE**|**Full name**|**Other name**|**Domain**|**Coverage**|**From**|**Data available in TRE<sup>1</sup>**|**Owner**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**COVIDSGSS**|COVID-19 Second Generation Surveillance System|N/A|Testing|England|06/04/2020 onwards|06/04/2020 onwards|NHSE|
|**IELISA**|Enzyme-Linked Immunosorbent Assay|Covid-19 UK Non-hospital Antibody Testing Results|Testing|UK|01/09/2020 onwards|01/09/2020 onwards|DHSC|
|**NPEX**|National Pathology Exchange|Covid-19 UK Non-hospital Antigen Testing Results|Testing|UK|17/04/2020 onwards|17/04/2020 onwards|DHSC|
|**CHESS**|COVID-19 Hospitalisation in England Surveillance System|Severe Acute Respiratory Infection (SARI-Watch) surveillance system|Hospital|England|12/03/2020 to 01/10/2022|12/03/2020 to 01/10/2022|NHSE|
|**CVS**|COVID-19 Vaccination Status|N/A|Vaccination|England|08/12/2020 onwards|08/12/2020 onwards|NHSE|
|**CVAR**|COVID-19 Vaccination Adverse Reactions|N/A|Vaccination|England|08/12/2020 onwards|08/12/2020 onwards|NHSE|
|**GDPPR**|General Practice Extraction Service (GPES) Data for Pandemic Planning and Research|N/A|Primary care|England|01/06/2020 onwards|01/06/2020 onwards|NHSE|
|  

DHSC: Department of Health and Social Care  
<sup>1</sup>As documented in the data sharing agreement.  

## COVID-19 testing datasets
The focus of **COVIDSGSS, IELISA** and **NPEX** is **testing**. As explained in the DHSC's [**COVID-19 Scaling up our testing programmes**](https://assets.publishing.service.gov.uk/media/5e888f05e90e0707799498b3/coronavirus-covid-19-testing-strategy.pdf), **four pillars** comprised the UK government's approach to testing for SARS-CoV-2. In Table 2 we summarise the aim of each pillar and list the COVID-19 dataset(s) that apply to each. For further details see the DHSC's [**COVID-19 testing data: methodology note**.](https://www.gov.uk/government/publications/coronavirus-covid-19-testing-data-methodology/covid-19-testing-data-methodology-note)

**Table 2** Aim and approach of each testing pillar and the relevant datasets in the UK LLC TRE

| **Pillar**|**Aim**|**Approach**|**Dataset**|
|:---:|:---:|:---:|:---:|
|**Pillar 1**|To quantify the number of people with a clinical need, and health and care workers, testing postive|Swab testing conducted in PHE labs and NHS hospitals to detect the virus (antigen testing)|COVIDSGSS|
|**Pillar 2**|To quantify the number of people in the wider population testing positive|Swab testing conducted in commercial labs to detect the virus (antigen testing)|COVIDSGSS & NPEX|
|**Pillar 3**|To understand the spread of the disease and the efficacy of different testing methods|Serology testing to detect immunity (antibody testing)|IELISA|
|**Pillar 4**|To understand the spread of the disease and the efficacy of different testing methods|Swab and serology testing to detect the virus and immunity, respectively (antigen and antibody testing)|COVIDSGSS, NPEX & IELISA|  
|  |

PHE: Public Health England (since April 2021 replaced by the UKHSA)


### 1. COVIDSGSS dataset
UKHSA's **Second Generation Surveillance System (SGSS)** is used to capture routine **laboratory surveillance data** on infectious diseases from diagnostic laboratories across **England**. Diagnostic laboratories are required to notify the UKHSA when specified causative agents are found in a human sample. The **COVIDSGSS data** reflect **swab testing** offered to those in **hospital and NHS key workers** (i.e. **Pillar 1**) and the **wider community** at drive through test centres, walk in centres, home kits returned by post, care homes, etc. (i.e. **Pillar 2**). The dataset available in the UK LLC TRE includes **demographic** information only about people **who test positive for SARS-CoV-2**. For a full list of variables see the [**NHS England Metadata dashboard**.](https://digital.nhs.uk/services/data-access-request-service-dars/dars-products-and-services/metadata-dashboard)

### 2. IELISA dataset
Also referred to as the **Covid-19 UK Non-hospital Antibody Testing Results** dataset, IElisa documents individuals who have had a **finger prick test for antibodies following a COVID-19 infection** (i.e. **Pillar 3**). The dataset is **UK wide** and includes **demographic** and **diagnostic** information. 

### 3. NPEX dataset
Also known as the **Covid-19 UK Non-hospital Antigen Testing Results** dataset, NPEX reflects **swab testing** undertaken by the **wider community** at drive through test centres, walk in centres, home kits returned by post, care homes, etc. (i.e. **Pillar 2**). The dataset is **UK wide** and includes **demographic** and **diagnostic** information. For a full list of variables see the [**NHS England Metadata dashboard**.](https://digital.nhs.uk/services/data-access-request-service-dars/dars-products-and-services/metadata-dashboard)

## COVID-19 hospitalisation dataset
Formerly known as the **COVID-19 Hospitalisation in England Surveillance System (CHESS)** dataset, UKHSA's **Severe Acute Respiratory Infection (SARI-WATCH) surveillance system** dataset records **demographic, risk factor, treatment** and **outcome information** for patients **admitted to hospital in England** with a confirmed **COVID-19 diagnosis**. This includes people admitted to intensive care or high dependency units. 

## COVID-19 vaccination datasets 
The focus of the **CVS** and **CVAR** datasets is **vaccination**. The datasets include anyone vaccinated **within England** and anyone vaccinated in a devolved administration where this information is **subsequently passed to England**. The source of all vaccination data is the **National Immunisation Management System (NIMS) database**.

### 1. CVS dataset
The CVS records individual vaccination events. Data collected include **demographic information, vaccination details** and **vaccine batch details**. For a full list of variables see the [**NHS England Metadata dashboard**.](https://digital.nhs.uk/services/data-access-request-service-dars/dars-products-and-services/metadata-dashboard)

### 2. CVAR dataset
The CVAR includes information relating to patients who have had any **adverse reaction to a COVID-19 vaccination**, which occurs within the first 15 minutes after administration of the vaccine. Data collected include **demographic information** and **adverse reaction details**. For a full list of variables see the [**NHS England Metadata dashboard**.](https://digital.nhs.uk/services/data-access-request-service-dars/dars-products-and-services/metadata-dashboard)

## COVID-19 primary care dataset
The existing General Practice Extraction Service (GPES) is used to run regular extracts from **General Practices in England that have opted into contributing to the GDPPR dataset**. Included in the extracts are all patients currently registered with a GP or with a date of death on or after 1 November 2019 whose health record contains **coded information relevant to pandemic planning and research**. Data collected include **demographic information, diagnoses and findings, medications and other prescribed items, investigations, tests and results, treatments and outcomes**, and **vaccinations and immunisations**.

For a full list of variables see the [**NHS England Metadata dashboard**.](https://digital.nhs.uk/services/data-access-request-service-dars/dars-products-and-services/metadata-dashboard)
For further information see the [**GDPPR guide for analysts**.](https://digital.nhs.uk/coronavirus/gpes-data-for-pandemic-planning-and-research/guide-for-analysts-and-users-of-the-data)

## Clinical classifications in COVID-19 datasets
NHS England introduced new dm+d and SNOMED codes during the COVID-19 pandemic, which were mapped to the World Health Organization's [**Emergency use ICD codes for COVID-19 disease outbreak**.](https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak) Primarily, **SNOMED codes** are used in the **COVID-19 datasets** - see the [**Coded variables guide**](../NHS_England/Coding/coding_intro.md) for further details.

## Structure of COVID-19 datasets
The structure of all seven datasets is **straightforward**, with each line representing one participant. 

## Data quality of COVID-19 datasets
There are known issues with the accuracy of **negative tests** for SARS-CoV-2.