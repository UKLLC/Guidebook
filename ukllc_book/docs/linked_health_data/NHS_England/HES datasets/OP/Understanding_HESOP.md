# Understanding the HESOP dataset
>Last modified: 27 Feb 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>HESOP is a record of outpatient care in NHS hospitals in England.</strong></div>  

## 1. Introduction
The OP (outpatient care) dataset records summary information about all **outpatient appointments** to NHS hospitals in England.  

**Note**: NHS England's definition of a hospital admission (i.e. not 'outpatient') includes day cases allocated a hospital bed, and what constitutes an outpatient procedure **varies between hospitals**.  

<aside class="admonition warning"><p class="admonition-title">HESOP is primarily a financial dataset; data are collected for the reimbursement of hospital activity</p>As with all NHS England datasets, it is not designed to be used for research.</aside>

## 2. Strengths of HESOP  
Although not designed as a research resource, the HESOP dataset can be used for research. Its strengths include:  
1) It is longitudinal making it possible for researchers to study cohorts over time
2) It provides complete coverage of the population, including all hospital outpatient appointments and procedures   
3) It uses standardised [coding systems](#coding-systems-used), enabling comparative work to be undertaken internationally
4) The clinical speciality under which someone was treated is recorded in 99% of records

## 3. Limitations of HESOP
1) It is an administrative dataset, meaning only conditions that have financial implications are likely to be recorded in the dataset
2) There are inconsistencies in the definition of an 'outpatient appointment', both between and within hospitals
3) Coding is unlikely to be consistent as there are variations between hospitals and over time
4) Primary diagnosis is recorded as 'missing' in over 90% of records as this field is not mandatory
5) Main procedure (or intervention) is missing in over 70% of records
6) There is no information about prescribed or dispensed medicines
7) It excludes private hospital care (unless funded by the NHS)

## 4. Scope and coverage
As well as costing information, the dataset contains patient-level coded information about:  
* diagnoses
* procedures (operations)
* appointment dates
* flags for first and 'follow up' appointments
* whether the patient attended the scheduled appointment
* source of referral
* waiting times
* patients' ethnic group, GP practice & [Index of Multiple Deprivation (IMD)](../../../../linked_geo_data/population_datasets/IMD/IMD.ipynb)

## 5. Data collection methodology
All NHS England [hospital datasets](../Hospital_intro.md) serve the primary purpose of recording care activities for the reimbursement to hospitals for the care they have provided to patients. This process is summarised on Guidebook's [hospital datasets page](../Hospital_intro.md#purpose-of-data-collection).

Some data (e.g. postcode, date of birth) are generated automatically from local patient administration systems. In HESOP, diagnosis and procedure codes are based on information input by administrative and clinical teams into the local hospital systems. Up to 12 diagnoses, and 24 procedures, are recorded for each outpatient 'episode' (see [Structure of the dataset](#6-structure-of-the-dataset) below).  

## 6. Structure of the dataset
Each record (line) represents a single outpatient appointment at a single location (a consultant-led or other health clinic).

Each record can contain up to 12 diagnoses, and up to 24 procedures. See [Coding systems](#coding-systems-used) below for more information.

For diagnoses, the field **diag_01** records the main reason for an individual being invited to an outpatient appointment. The subsequent fields **diag_02...diag_12**, where used, record comorbidities.  

For procedures, the field **opertn_01** records the main procedure. Secondary procedures are recorded in fields **opertn_02...opertn_24**. 

## 7. Coding systems used
HESOP uses two main medical coding systems: **ICD-10** for diagnoses and **OPCS** for procedures and operations. It also uses **NHS National Codes** to record record the specialised service within which a patient is treated.

**ICD-10** (International Statistical Classification of Diseases and Related Health Problems)
Contains 22 hierarchical chapters, based on body systems (e.g. respiratory, digestive). It is used to record all diagnoses and, where relevant, causes of injuries.

**OPCS** (Office for Population Censuses and Surveys)
Contains 24 hierarchical chapters, based on body systems (e.g. respiratory, digestive). 
This codiing system is UK-specific, so cannot be used for international comparisons. It records all procedures (e.g. surgery, MRI scans).  

## 8. Evolution of the dataset
NHS England started collecting HESOP data in 2003-04, first releasing it as an 'experimental' dataset in 2006. HESOP became an accredited National Statistic in 2008. 

## 9. Availability in the UK LLC TRE
The UK LLC TRE holds an extract of the HESOP dataset, going back to 2003 (when the data was first collected). The HESOP records of participants in UK LLC's partner LPS, where individual or LPS permissions allow linkage to NHS data, are included in the TRE. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHSE data not be shared via UK LLC.

More detailed information about the UK LLC's HESOP extract is [here](../OP/HESOP.ipynb).

## 10. Missing information
* **Variable and value labels**  
UK LLC is infilling missing variable and value labels in the NHSE datasets in the TRE. Where variable labels have been added by UK LLC, rather than being found in NHSE documentation, this is made apparent by the phrase 'label added by UK LLC' being included in the variable label.  
* **Missing data**  
The amount of missing data varies widely between variables and across datasets. Throughout 2026, we will update this section with information about missingness in HESOP.


## 11. Tips for researchers using HESOP in the UK LLC TRE
### a) Data quality issues
There may be inconsistencies and other data quality issues with HESOP data collected during the early, experimental, phase of data collection (prior to 2008). Not all fields were mandatory when the data was first collected so earlier records have more missing data than do more recent ones.  

**The primary diagnosis and main procedure are missing from the vast majority of HESOP records.**  
Where the main diagnosis is not recorded, diag_4_01 = **R69X**.  
Where the primary procedure is not recorded, opertn_3_01 = **X99** *or* **-** *or* **&**.

### b) Working with medical codes
 
>When applying to access linked HESOP data in the UK LLC TRE, researchers must [**submit a codelist**](../../Coding/codelists.md) specifying the ICD-10 and / or OPCS codes which are relevant to their research question. 

In HESOP, as is the case for **all HES datasets**, ICD-10 and OPCS codes are provided as both 3-character and 4-character fields. The 3-character version is a truncation of the 4-character field, providing a higher-level (less specific) diagnosis or procedure code. N.B. Not all diagnoses and procedures have a 4-character version. Where this is the case, the final character is infilled with 'X'.

The dataset also includes fields which concatenate the ICD-10 and OPCS codes, simplifying the process of identifying a specific diagnosis or operation across multiple fields. More information on these fields is included with the [HESAPC](../APC/Understanding_HESAPC.md#b-working-with-diagnostic-codes) dataset.

### c) Key variables in HESOP
| Variable name | Variable label | Description |
|---|---|---|
| apptdate | Appointment date | The date when an appointment was scheduled |
| attended | Attended | Whether or not a patient attended an appointment | 
| mainspef | Speciality under which the outpatient appointment is recorded | The speciality of the consultant responsible for the patient during that appointment (recorded for administrative purposes) |
| outcome | Outcome of outpatient attendance | e.g. discharged from consultant's care, another appointment made |
| refsourc | Source of referral for the outpatient episode | e.g. from GP, from A&E, from optometrist |
| tretspef | Speciality that provided the care or treatment during the appointment | Can differ from mainspef if a patient receives treatment from a someone in a speciality other than that of their consultant. Records which speciality delivered the care, so can be used for clinical analysis | 
| waitdays | Waiting time in days | Number of days between the decision to treat being made and treatment being received |

<br>The full **HES data dictionary** can be downloaded from <a href="https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics/hospital-episode-statistics-data-dictionary" target="_blank" rel="noopener noreferrer">NHS England.</a>
  
## 12. Useful syntax
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the <a href="https://github.com/UKLLC" target="_blank" rel="noopener noreferrer">UK LLC Github</a> repository where you can find the full scripts.

## 13. Further reading  
Information in this section will be added in due course.