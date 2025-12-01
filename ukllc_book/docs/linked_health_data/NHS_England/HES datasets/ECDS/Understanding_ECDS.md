# Understanding the Emergency Care Dataset (ECDS)
>Last modified: 01 Dec 2025

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>ECDS is a record of Accident & Emergency (A&E) attendances in NHS hospitals in England.</strong></div>  

## 1. Introduction
The Emergency Care Data Set (ECDS) was introduced in 2017 and is the national dataset for emergency care in England.  It records information about why people attend **emergency departments** and any treatment they are given.

## 2. Strengths of ECDS  
1) It is longitudinal making it possible for researchers to study cohorts over time
2) It provides complete coverage of all NHS emergency departments in England
3) The severity of cases is recorded   
4) It uses a standardised [coding system](#7-coding-systems-used), enabling comparative work to be undertaken over time and internationally
5) Patient-level data from all NHS emergency departments, urgent treatment centres and some walk-in centres is included

## 3. Limitations of ECDS
1) It is a clinical dataset, rather than one specifically designed for research
2) Coding is unlikely to be consistent as there are variations between hospitals and over time
3) The dataset was only established in 2017 so there is limited longitudinal value in using ECDS alone


## 4. Scope and coverage
The dataset contains patient-level information about:  
* diagnoses
* outcomes
* referral sources
* dates and times of arrival and departure
* waiting times
* discharge destination
* patients' stated gender, age, ethnic group and geographic location

## 5. Data collection methodology
Data about each attendance at an A&E department are input into local record systems by clinicians and administrative staff. Some data (e.g. postcode, date of birth) are generated automatically from local patient administration systems. 
  
## 6. Structure of the dataset
>Each record (line) represents a single visit to an emergency care department. 

**Clinical information:**
Each record contains coded information on the **'chief complaint'** (main reason for attending A&E) and up to 10 comorbidities (fields **comorbidities_1** to _10). There also up to 12 coded fields for diagnoses, investigations and treatments.

**Dates and times:** The ECDS includes multiple date and time fields which facilitate the tracking of a patients' progress through A&E experience from arrival to discharge, e.g. 'arrival_date' (ddmmmyyyy) and 'arrival_time' (hh:mm:ss).

**Other information:** The dataset also provides broader information such as which care professionals were involved in a patient's care while they were in A&E, and the discharge destination (e.g. home, admitted to hospital).

## 7. Coding systems used
The ECDS uses [**SNOMED CT**](../../Coding/coding_intro.md) (Systematized Nomenclature of Medicine Clinical Terms), usually abbreviated to just **SNOMED**. It is an international system used to classify many types of medical data, including diagnoses, procedures, symptoms, family history, assessment tools, observations and medications. SNOMED CT is designed for direct management and care of patients. The codes are numeric, typically between 6 and 18 digits long, and do not follow a pattern or hierarchy.

The **UK edition** of SNOMED CT contains the UK extensions, which include UK-specific screening procedures and assessment scales. There are also ECDS-specific SNOMED codes (known as **ECDS Diagnosis Core** and **ECDS Diagnosis Max**). 

As in all HES datasets, ECDS uses **NHS National Codes** used for administrative information such as source of admission and discharge destination.

## 8. Evolution of the dataset
NHS England started collecting A&E data, as ([HESAE](../AE/HESAE.ipynb)), in 2007-08. It was an ‘experimental’ dataset until 2012-13 when data collected in emergency departments became a national standard for official statistics. The ECDS (Emergency Care Data Set) was introduced in 2017, remaining 'experimental' until it **ECDS replaced HESAE as the national standard in 2020**. 

Rather than SNOMED codes, HESAE used the now-archived <a href="https://v2.datadictionary.nhs.uk/web_site_content/pages/codes/administrative_codes/a_amp_e_diagnosis_tables.asp@shownav=0.html" target="_blank" rel="noopener noreferrer">A&E Diagnosis codes</a> so the two datasets cannot easily be compared or combined.

## 9. Availability in the UK LLC TRE
The UK LLC TRE holds an extract of the ECDS, going back to 2017 when it was first established. The ECDS records of participants in UK LLC's partner LPS, where individual or LPS permissions allow linkage to NHS data, are included in the TRE. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHSE data not be shared via UK LLC.

More detailed information about the UK LLC's ECDS extract is [here](../ECDS/ECDS.ipynb).

## 10. UK LLC transformations of the dataset
All variables which identify organisations (e.g. GP practice, NHS Trust) or geographic areas smaller than a region (e.g. LSOA) are encrypted before being ingested into the UK LLC TRE. The encrypted variables (identifiable by the suffix **_e**) enable researchers to identify which participants were treated by the same organisation, or live in the same area, but not to identify the organisation or area.

## 11. Tips for researchers using ECDS in the UK LLC TRE

**Key variables in the ECDS**
| Variable name | Variable label | Description | Additional information |
|---|---|---|---|
| arrival_date | Arrival date | Date on which the patient arrived | ddmmmyyyy
| arrival_mode | Emergency care arrival mode | Mode of transport by which the patient arrived | SNOMED code
| arrival_time | Arrival time | Time at which the patient arrived (24hrs) | hh:mm:ss
| chief_complaint | Patient's chief complaint | The nature of the patient's primary reason for attending | SNOMED code

<br>The full **HES data dictionary** can be downloaded from <a href="https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics/hospital-episode-statistics-data-dictionary" target="_blank" rel="noopener noreferrer">NHS England.</a>
  
## 12. Useful syntax
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the <a href="https://github.com/UKLLC" target="_blank" rel="noopener noreferrer">UK LLC Github</a> repository where you can find the full scripts.

## 13. Further reading  
Information in this section will be added in due course.