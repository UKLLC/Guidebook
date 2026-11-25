# Understanding the MSDS V1.5
>Last modified: 25 Nov 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The Maternity Services Data Set (MSDS) is a record of NHS-funded maternity services in England.</strong></div>  

## 1. Introduction
The Maternity Services Data Set (MSDS) V1.5 was introduced in May 2015, and was replaced by the [MSDS V2.0](../msds/msds.ipynb) in April 2019. UK LLC holds both V1.5 and V2.0 in the Trusted Research Environment (TRE); researchers approved to use the MSDS are provided with access to both versions of the dataset.

## 2. Strengths of MSDS V1.5  
1) It provides more detailed information on pregnancies and deliveries than is available in the Hospital Episode Statistics Admitted Patient Care (HESAPC) dataset
2) It may contain some information about pregnancies and deliveries that are not recorded in HESAPC (e.g. home births, early miscarriages)
3) MSDS V1.5 comprises a single table with one row per recorded pregancy, making it fairly simple to use  
4) All maternity services provided to an individual - from initial booking to discharge from maternity services - are included in the dataset 
5) It is linked to MSDS V2.0 in the UK LLC TRE, increasing the temporal coverage of available linked maternity data.


## 3. Limitations of MSDS V1.5
1) It is a clinical dataset, rather than one specifically designed for research
2) The dataset only covers a four-year period so there is limited longitudinal value in using the dataset alone
3) Not all providers submitted data during the first few years of data collection so it may not be nationally representative
4) It uses different coding systems, and has a different structure, from V2.0 making direct comparisions difficult
5) In multi-generational LPS, the MSDS is linked only to the mother's self-reported and linked health data (not the baby's).


## 4. Scope and coverage
The dataset contains information about:  
* routine booking appointments 
* maternity care plan
* antenatal screening tests
* labour and delivery
* newborn screening
* maternal or neonatal death


## 5. Data collection methodology
Data were mandated to be collected by all NHS-commissioned maternity services in England, and to be submitted to a centralised system every month. Based on both clinical and operational data, its intended purpose was to monitor maternity services.

## 6. Structure of the dataset
Each record (line) represents a single pregnancy known to the NHS England. If a participant had more than one pregancy recorded in the time period covered by the dataset, there is one row per pregnancy. For multiple pregnancies (i.e., twins, triplets), information about each fetus is recorded on the same line as the mother.

## 7. Coding systems used
The MSDS V1.5 largely comprises dates, activity flags (e.g., 'water birth'), and care provider codes (encrypted) rather than commonly used clinical codes. There are some **NHS National Codes** for categorical variables such as diagnoses, types of care professionals, etc..


## 8. Evolution of the dataset
The MSDS V1.5 was introduced in May 2015 and replaced by MSDS V2.0 in April 2019.

## 9. Availability in the UK LLC TRE
The UK LLC TRE holds an extract of the MSDS V1.5 from to 2015 when it was first established to 2019 when it was replaced by MSDS V2.0. The MSDS V1.5 records of participants in UK LLC's partner LPS, where individual or LPS permissions allow linkage to NHS data, are included in the TRE. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHSE data not be shared via UK LLC.

More detailed information about the UK LLC's MSDS V1.5 extract is [here](../msds_v1_5/msds_v1_5.ipynb).

## 10. Missing information
* **Variable and value labels**  
UK LLC is infilling missing variable and value labels in the NHSE datasets in the TRE. Where variable labels have been added by UK LLC, rather than being found in NHSE documentation, this is made apparent by the phrase 'label added by UK LLC' being included in the variable label.
* **Missing data**  
The amount of missing data varies widely between variables and across datasets. Throughout 2027, we will update this section with information about missingness in the MSDS V1.5.


## 11. Tips for researchers using MSDS V1.5 in the UK LLC TRE
There is a large amount of missing data in MSDS V1.5. Researchers should be aware that it is unlikely to contain complete information about each included pregnancy, and is not a comprehensive record of all pregnancies in England during the period covered.  

Cross-referencing pregnancies recorded in the MSDS V1.5 with both MSDS V2.0 and self-reported data may help researchers to identify maternity events not recorded in MSDS V1.5.
  
## 12. Useful syntax
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the <a href="https://github.com/UKLLC" target="_blank" rel="noopener noreferrer">UK LLC Github</a> repository where you can find the full scripts.

## 13. Further reading  
Information in this section will be added in due course.