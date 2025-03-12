# NHS England COVID-19 datasets
>Last modified: 05 Feb 2025
## Introduction  
NHS England flows extracts of **six COVID-19 datasets** into the UK LLC TRE - see Table 1.  
Researchers are permitted access to these six datasets provided that their research is related to **COVID-19**. This is a specific term set by NHS England. (For examples of research purposes acceptable to NHS England see the [**COVID-19 Public Health Directions 2020**.](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/covid-19-public-health-directions-2020#:~:text=identifying%20and%20understanding)) 


NHS England introduced new dm+d and SNOMED codes during the COVID-19 pandemic, which were mapped to the World Health Organization's [**Emergency use ICD codes for COVID-19 disease outbreak**.](https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak) Primarily, **SNOMED codes** are used in the **COVID-19 datasets** - see the [**Coded variables guide**](../Coding/coding_intro.md) for further details.

## Coverage of COVID-19 datasets
Table 1 summarises the **temporal and geographical coverage** of each of the six COVID-19 datasets. 

As explained in the overarching [**NHS England datasets guide**](../NHSE_intro.md), the UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE, apart from **SGSS** where we added COVID in front of it to distinguish it from the UK Health Security Agency’s (UKHSA's) generalised Second Generation Surveillance System (SGSS).   

Some datasets have been renamed by NHS England, e.g. **CHESS** is now called the **Severe Acute Respiratory Infection (SARI-Watch) surveillance system** dataset and some datasets have alternative names, e.g. **NPEX** is also called the **Covid-19 UK Non-hospital Antigen Testing Results** dataset. We receive the data from NHS England as the CHESS and NPEX datasets and these are the names researchers will see in the UK LLC TRE. Therefore, we refer to them by these names in our documentation. 

**Table 1** Names, coverage, availability and ownership of COVID-19 datasets in the UK LLC TRE (the dataset in italics is retired)

| **Name in TRE**|**Full name**|**Other name**|**Domain**|**Coverage**|**From**|**Data available in TRE<sup>1</sup>**|**Owner**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|[***COVIDSGSS***](../COVID%20datasets/COVIDSGSS/COVIDSGSS.ipynb)|*COVID-19 Second Generation Surveillance System*|*N/A*|*Testing (Pillars 1, 2, 4<sup>2</sup>)*|*England*|*06/04/2020 to Feb 2024*|*06/04/2020 to Feb 2024*|*NHSE*|
|[***IELISA***](../COVID%20datasets/IELISA/IELISA.ipynb)|*Enzyme-Linked Immunosorbent Assay*|*Covid-19 UK Non-hospital Antibody Testing Results*|*Testing (Pillars 3, 4<sup>2</sup>)*|*UK*|*01/09/2020 to July 2022*|*01/09/2020 to July 2022*|*DHSC*|
|[***NPEX***](../COVID%20datasets/NPEX/NPEX.ipynb)|*National Pathology Exchange*|*Covid-19 UK Non-hospital Antigen Testing Results*|*Testing (Pillars 2, 4<sup>2</sup>)*|*UK*|*17/04/2020 to Feb 2024*|*17/04/2020 to Feb 2024*|*DHSC*|
|[***CHESS***](../COVID%20datasets/CHESS/CHESS.ipynb)|*COVID-19 Hospitalisation in England Surveillance System*|*Severe Acute Respiratory Infection (SARI-Watch) surveillance system*|*Hospital*|*England*|*12/03/2020 to Oct 2022*|*12/03/2020 to Oct 2022*|*NHSE*|
|[**CVS**](../COVID%20datasets/CVS/CVS.ipynb)|COVID-19 Vaccination Status|N/A|Vaccination|England|08/12/2020 onwards|08/12/2020 onwards|NHSE|
|[***CVAR***](../COVID%20datasets/CVAR/CVAR.ipynb)|*COVID-19 Vaccination Adverse Reactions*|*N/A*|*Vaccination*|*England*|*08/12/2020 to Sept 2023*|*08/12/2020 to Sept 2023*|*NHSE*||  

DHSC: Department of Health and Social Care  
<sup>1</sup>As documented in the data sharing agreement.  
<sup>2</sup>As explained in the DHSC's [**COVID-19 Scaling up our testing programmes**](https://assets.publishing.service.gov.uk/media/5e888f05e90e0707799498b3/coronavirus-covid-19-testing-strategy.pdf), four pillars comprised the UK government's approach to testing for SARS-CoV-2.   
**Pillar 1** quantified the number of people with a clinical need, and health and care workers, who returned positive swab (antigen) tests (processed in PHE labs and NHS hospitals).  
**Pillar 2** quantified the number of people in the wider community who returned positive swab (antigen) tests (processed in commercial labs).  
**Pillar 3** quantified the number of people who returned positive serology (antibody) tests to detect immunity and to understand the efficacy of the different testing methods.   
**Pillar 4** quantified the number of people who returned positive serology (antibody) and swab (antigen) tests to detect immunity and to understand the efficacy of the different testing methods.  
For further details see the DHSC's [**COVID-19 testing data: methodology note**.](https://www.gov.uk/government/publications/coronavirus-covid-19-testing-data-methodology/covid-19-testing-data-methodology-note)

