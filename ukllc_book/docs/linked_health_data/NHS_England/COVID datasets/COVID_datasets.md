# NHS England COVID-19 datasets
>Last modified: 20 Jun 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The COVID-19 datasets cover vaccinations, tests and hospitalisations.</strong></div>

## Timeline for COVID-19 relevant events in the UK:
This timeline illustrates the progress of the pandemic in the UK, alongside policy measures, national and international events, and key milestones for population studies such as the approval of vaccines and wider events that impacted on public awareness and trust.
<br>
<iframe width="100%" height="400" src="https://time.graphics/embed?v=1&id=4c88cc0482538f247bcb58b299463ca2" frameborder="0" allowfullscreen></iframe>
<div><a  style="font-size: 10px; text-decoration: none;" title="Free timeline templates" href="https://time.graphics">Free timeline templates</a></div>
The graphic was developed as part of work led by the ALSPAC (University of Bristol) and Generation Scotland (University of Edinburgh) studies and funded by the Wellcome Trust funded <i>“Longitudinal Population Study Covid-19 Steering Group and Secretariat” as a Strategic Support Science Grant - 221574/Z/20/Z award.</i> Thanks to ALSPAC and Generation Scotland staff and all the wider individuals and studies that helped to contribute to its production. Please see <a href="https://www.bristol.ac.uk/alspac/covid-19/wellcome-covid-19/"> https://www.bristol.ac.uk/alspac/covid-19/wellcome-covid-19/</a> for more details.
<br>
<br>

>## Summary:
>* UK LLC holds **six NHS England COVID-19 datasets**: [**COVID-19 Second Generation Surveillance System (COVIDSGSS)**](../COVID%20datasets/COVIDSGSS/COVIDSGSS.ipynb), [**Enzyme-Linked Immunosorbent Assay (IELISA)**](../COVID%20datasets/IELISA/IELISA.ipynb), [**National Pathology Exchange (NPEX)**](../COVID%20datasets/NPEX/NPEX.ipynb), [**COVID-19 Hospitalisation in England Surveillance System (CHESS)**](../COVID%20datasets/CHESS/CHESS.ipynb), [**COVID-19 Vaccination Status (CVS)**](../COVID%20datasets/CVS/CVS.ipynb) and [**COVID-19 Vaccination Adverse Reactions (CVAR)**](../COVID%20datasets/CVAR/CVAR.ipynb).
<br>
>* Three datasets have alternative names. **IELISA** is also known as **Covid-19 UK Non-hospital Antibody Testing Results**, **NPEX** as **Covid-19 UK Non-hospital Antigen Testing Results** and **CHESS** as **Severe Acute Respiratory Infection (SARI-Watch) surveillance system**. We receive the data from NHS England as the IELISA, NPEX and CHESS datasets and these are the names researchers will see in the UK LLC TRE. Therefore, we refer to them by these names in our documentation.
<br>
>* Researchers are permitted access to the COVID-19 datasets under a **specific term** set by NHS England: Research must be related to **COVID-19**. For examples of research purposes acceptable to NHS England see the <strong><a href="https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/covid-19-public-health-directions-2020#:~:text=identifying%20and%20understanding" target="_blank" rel="noopener noreferrer">COVID-19 Public Health Directions 2020</a></strong>
<br>
>* The datasets span **2020 onwards**, although a number are now retired.
<br>
>* Primarily, **SNOMED codes** are used in the **COVID-19 datasets**. See the [**Coded variables guide**](../Coding/coding_intro.md) for further details. NHS England introduced new dm+d and SNOMED codes during the COVID-19 pandemic, which were mapped to the World Health Organization's <strong><a href="https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak" target="_blank" rel="noopener noreferrer">Emergency use ICD codes for COVID-19 disease outbreak</a></strong>
<br>

## Overview of COVID-19 datasets
For further information see the **individual dataset guides.**

**Table 1** Names, geographical coverage and availability of COVID-19 datasets in the UK LLC TRE ((the datasets in italics are retired)

| **Dataset**|**Dataset name**|**Other name**|**Grouping**|**Coverage**|**Data available in TRE**|**Data owner**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|
|[***COVIDSGSS***](../COVID%20datasets/COVIDSGSS/COVIDSGSS.ipynb)|*COVID-19 Second Generation Surveillance System*|*N/A*|*Testing (Pillars 1, 2, 4<sup>1</sup>)*|*England*|*06/04/2020 to Feb 2024*|*NHSE*|
|[***IELISA***](../COVID%20datasets/IELISA/IELISA.ipynb)|*Enzyme-Linked Immunosorbent Assay*|*Covid-19 UK Non-hospital Antibody Testing Results*|*Testing (Pillars 3, 4<sup>1</sup>)*|*UK*|*01/09/2020 to July 2022*|*DHSC*|
|[***NPEX***](../COVID%20datasets/NPEX/NPEX.ipynb)|*National Pathology Exchange*|*Covid-19 UK Non-hospital Antigen Testing Results*|*Testing (Pillars 2, 4<sup>1</sup>)*|*UK*|*17/04/2020 to Feb 2024*|*DHSC*|
|[***CHESS***](../COVID%20datasets/CHESS/CHESS.ipynb)|*COVID-19 Hospitalisation in England Surveillance System*|*Severe Acute Respiratory Infection (SARI-Watch) surveillance system*|*Hospital*|*England*|*12/03/2020 to Oct 2022*|*NHSE*|
|[**CVS**](../COVID%20datasets/CVS/CVS.ipynb)|COVID-19 Vaccination Status|N/A|Vaccination|England|08/12/2020 onwards|NHSE|
|[***CVAR***](../COVID%20datasets/CVAR/CVAR.ipynb)|*COVID-19 Vaccination Adverse Reactions*|*N/A*|*Vaccination*|*England*|*08/12/2020 to Sept 2023*|*NHSE*||

DHSC: Department of Health and Social Care
<sup>1</sup>As explained in the DHSC's <strong><a href="https://assets.publishing.service.gov.uk/media/5e888f05e90e0707799498b3/coronavirus-covid-19-testing-strategy.pdf" target="_blank" rel="noopener noreferrer">COVID-19 Scaling up our testing programmes</a></strong>, four pillars comprised the UK government's approach to testing for SARS-CoV-2.
**Pillar 1** quantified the number of people with a clinical need, and health and care workers, who returned positive swab (antigen) tests (processed in PHE labs and NHS hospitals).
**Pillar 2** quantified the number of people in the wider community who returned positive swab (antigen) tests (processed in commercial labs).
**Pillar 3** quantified the number of people who returned positive serology (antibody) tests to detect immunity and to understand the efficacy of the different testing methods.
**Pillar 4** quantified the number of people who returned positive serology (antibody) and swab (antigen) tests to detect immunity and to understand the efficacy of the different testing methods.
For further details see the DHSC's <strong><a href="https://www.gov.uk/government/publications/coronavirus-covid-19-testing-data-methodology/covid-19-testing-data-methodology-note" target="_blank" rel="noopener noreferrer">COVID-19 testing data: methodology note</a></strong>
