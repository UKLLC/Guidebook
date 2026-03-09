# Understanding the HESAE dataset
>Last modified: 27 Feb 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>HESAE is a record of Accident & Emergency (A&E) attendances in NHS hospitals in England.</strong></div>  

## 1. Introduction
HESAE was introduced was the national dataset for emergency care in England between 2007 and 2020.  It recorded information about why people attended **emergency departments** and any treatment they were given.  

<aside class="admonition note"><p class="admonition-title">HESAE was replaced by the Emergency Care Data Set <a 
href="https://guidebook.ukllc.ac.uk/docs/linked_health_data/nhs_england/hes%20datasets/ecds/ecds"><strong>(ECDS)</strong></a> in 2020.</p></aside>

## 2. Strengths of HESAE  
1) It is longitudinal making it possible for researchers to study cohorts over time
2) It provides complete coverage of all NHS emergency departments in England
3) It uses a standardised [coding system](#7-coding-systems-used), enabling comparative work to be undertaken over time

## 3. Limitations of HESAE
1) Use of a specific A&E coding system, rather than the more granular SNOMED codes, means the level of clinical detail is limited 
2) Coding is unlikely to be consistent as there are variations between hospitals and over time
3) Not all attendances at A&E are captured by the dataset
4) Its focus is administrative, rather than looking at health outcomes
5) Data collection ended in 2020, with the replacement of HESAE by [ECDS](../ECDS/ECDS.ipynb), so the dataset cannot be used for contemporary research

## 4. Scope and coverage
The dataset contains patient-level information about:  
* dates and times of arrival and departure
* source of referral
* discharge outcome and destination
* waiting times
* patients' age, sex, and geographic location

## 5. Data collection methodology
Data about each attendance at an A&E department were input into local record systems by clinicians and administrative staff. Some data (e.g. postcode, date of birth) were generated automatically from local patient administration systems. 
  
## 6. Structure of the dataset
>Each record (line) represents a single visit to an emergency care department. 

**Clinical information:**
Each record contains coded information on up to **12 diagnoses made in A&E** (fields **diag_01** to _12). There also up to 12 coded fields for anatomical area of diagnosis, investigations and treatments. All medical codes are presented as two character codesm with a third character being included where further details are available.

**Dates and times:** HESAE includes multiple date and time fields which facilitate the tracking of a patients' progress through A&E experience from arrival to discharge, e.g. 'arrivaldate' (ddmmmyyyy) and 'arrivaltime' (hhmm).

**Other information:** The dataset also provides broader information such the discharge destination (e.g. home, admitted to hospital) and the GP practice with which the patient was registered.

## 7. Coding systems used
HESAE uses a specific **A&E Diagnosis coding system**. This is now archived but can be accessed via the 
<a href="https://v2.datadictionary.nhs.uk/web_site_content/pages/codes/administrative_codes/a_amp_e_diagnosis_tables.asp@shownav=0.html" target="_blank" rel="noopener noreferrer"><strong>NHS Data Dictionary</strong></a>. A&E diagnosis codes comprise up to six characters, split into four sub-parts. These are represented in the dataset as four fields:
| Description | Format | Length | Field names | Value range<sup>1</sup> |
|---|---|:---:|---|:---:|
| **Diagnosis Condition** | Numeric | 2 char. | diag2_01 ... diag2_12 | 01 - 39 |
| Sub-analysis (optional) | Numeric | 1 char. | n.a. | 1 - 4 |
| **Diagnosis Condition + sub-analysis<sup>2</sup>** | Numeric | 3 char. | diag3_01 ... diag3_12 | Combination of above
| **Anatomical area** | Numeric | 2 char. | diaga_01 ... diaga_12 | 01 - 36 | 
| **Anatomical side** | Alphanumeric | 1 char. | diags_01 ... diags_12 | L,R,B,8  

*Notes*  
<sup><strong>1</strong></sup> These are the permitted values, as defined in the NHS Data Dictionary, but some of the values in the HESAE dataset fall outside these ranges.  
<sup><strong>2</strong></sup> If a sub-analysis is not applicable, or not provided, 'diag3_' is the same as 'diag2_'. 

## 8. Evolution of the dataset
NHS England started collecting A&E data in 2007-08. It was an ‘experimental’ dataset until 2012-13 when data collected in emergency departments became a national standard for official statistics. HESAE was replaced by the [**ECDS**](../ECDS/ECDS.ipynb) (Emergency Care Data Set) in 2020. ECDS uses SNOMED codes rather than the now-archived A&E coding system, so the two datasets cannot easily be compared or combined.

## 9. Availability in the UK LLC TRE
The UK LLC TRE holds an extract of HESAE, going back to 2007 when it was first established. The HESAE records of participants in UK LLC's partner LPS, where individual or LPS permissions allow linkage to NHS data, are included in the TRE. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHSE data not be shared via UK LLC.

More detailed information about the UK LLC's HESAE extract is [here](../AE/HESAE.ipynb).

## 10. Missing information
* **Variable and value labels**  
UK LLC is infilling missing variable and value labels in the NHSE datasets in the TRE. Where variable labels have been added by UK LLC, rather than being found in NHSE documentation, this is made apparent by the phrase 'label added by UK LLC' being included in the variable label.
* **Missing data**
The amount of missing data varies widely between variables and across datasets. Throughout 2026, we will update this section with information about missingness in HESAE.


## 11. Tips for researchers using HESAE in the UK LLC TRE
### a) Data quality
When HESAE was first introduced, it did not capture all visits to A&E so cannot be regarded as the complete picture of attendances. Overall coverage improved when it became part of official statistics in 2012, but the completeness of some key fields reduced with the phased introduction of the Emergency Care Dataset (ECDS) starting in 2017.

### b) Working with medical codes
 >When applying to access linked HESAE data in the UK LLC TRE, researchers must [**submit a codelist**](../../Coding/codelists.md) specifying the A&E codes which are relevant to their research question.  
 >UK LLC requires only the **Diagnosis Condition**, i.e. the first two characters of the A&E Diagnosis Code.  

**Key variables in HESAE**
| Variable name | Variable label | Description |
|---|---|---|
| arrivaldate | Arrival date | Date on which the patient arrived |
| aepatgroup | A&E Patient Group | The reason for attendance at A&E | 
| initdur | Initial duration | Number of minutes between the patient's arrival and their initial assessment | 
| diag3_01 ... diag3_12 | A&E diagnosis | See [coding systems](#7-coding-systems-used) above |   


## 12. Useful syntax
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the <a href="https://github.com/UKLLC" target="_blank" rel="noopener noreferrer">UK LLC Github</a> repository where you can find the full scripts.

## 13. Further reading  
Hospital Episode Statistics as a whole are covered in more depth elsewhere in [Guidebook](../APC/Understanding_HESAPC.md).

Information on the structure of HESAE and the coding systems used can be found in the <a href="https://www.datadictionary.nhs.uk/index.html" target="_blank" rel="noopener noreferrer">NHS Data Model and Dictionary</a>.