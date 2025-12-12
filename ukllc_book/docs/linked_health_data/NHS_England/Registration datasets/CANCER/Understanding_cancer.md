# Understanding the Cancer Registration Dataset
>Last modified: 12 Dec 2025

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The cancer dataset is a record of all registered cancer diagnoses in England.</strong></div>  

## 1. Introduction
The Cancer Registration Dataset was introduced in 1971.  It records information on all cancer diagnoses, including date of diagnosis and the type and behaviour of each cancer.

## 2. Strengths of the cancer registration dataset  
1) It provides complete coverage of all cancer diagnoses in England
2) It uses a standardised [coding systems](#7-coding-systems-used), enabling comparative work to be undertaken over time and internationally
3) The dataset includes diagnostic information such as cancer type and stage, and date of diagnosis
4) Cancer registration data are validated and checked for completeness, meaning the dataset is a reliable representation of all cancer diagnoses in a given period

## 3. Limitations of the cancer registration dataset
1) It is a clinical dataset, rather than one specifically designed for research
2) There is no information on treatments or test results
3) The thorough validation and completeness checks mean there can be a delay of up to 24 months before a diagnosis appears in the registry data
4) Information on disease recurrence or progression is not included

## 4. Scope and coverage
The dataset contains patient-level information about:  
* tumour details (site, behaviour, staging)
* date of diagnosis
* patients' sex, age and geographic location

## 5. Data collection methodology
Data are collected and collated from a range of clinical sources. These include: Hospital Episode Statistics (HES), lab reports, screening programmes, primary care prescriptions and death certificates. 
  
## 6. Structure of the dataset
The dataset is diagnosis-level with each record (line) representing a single diagnosis. For individuals diagnosed with more than one type of cancer, each diagnosis is on a separate line.

## 7. Coding systems used
The dataset uses two main medical coding systems: **ICD-10** for diagnoses and **ICD-O-3** for morphology and behaviour.

**ICD-10** (International Statistical Classification of Diseases and Related Health Problems) contains 22 hierarchical chapters, based on body systems.  All cancers are recorded in Chapter II 'Neoplasms'.

**ICD-O-3** (International Classification of Diseases for Oncology) is used to code the morphology, behaviour and grading of neoplasms. 

These two coding systems were introduced to the cancer registry in 1995, superseding ICD-9 (previously ICD-8) and ICD-O-2 (previously ICD-O-1).

## 8. Evolution of the dataset
The cancer registry was established in 1971. It was initially based on snapshots of incidence counts by age, sex, cancer site and type, drawn from paper records. In the 2010s it became event-based and captured every diagnosis, drawing from multiple sources of health data. 

## 9. Availability in the UK LLC TRE
The UK LLC TRE holds an extract of the cancer registration dataset, going back to 1971 when it was first established. The cancer registration dataset records of participants in UK LLC's partner LPS, where individual or LPS permissions allow linkage to NHS data, are included in the TRE. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHSE data not be shared via UK LLC.

More detailed information about the UK LLC's cancer registration extract is [here](../CANCER/CANCER.ipynb).

## 10. UK LLC transformations of the dataset
All variables which identify organisations (e.g. GP practice, NHS Trust) or geographic areas smaller than a region (e.g. LSOA) are encrypted before being ingested into the UK LLC TRE. The encrypted variables (identifiable by the suffix **_e**) enable researchers to identify which participants were treated by the same organisation, or live in the same area, but not to identify the organisation or area.

## 11. Tips for researchers using cancer registration dataset in the UK LLC TRE
>When applying to access linked cancer registration data in the UK LLC TRE, researchers must [**submit a codelist**](../../Coding/codelists.md) specifying the **ICD-10** codes which are relevant to their research question. 

In the dataset, ICD-10 codes are provided with up to 4 characters (e.g. C504). ICD-O-3 codes are split into two fields: cancer type and cancer behaviour (see Table below).

**Key variables in the cancer registration dataset**
| Variable name | Variable label | Description |
|---|---|---|
| cancer_site | Site of cancer | ICD-9 or ICD-10 code |
| cancer_type | Cell type (histology) | First 4 digits of an ICD-O morphology code |
| cancer_behaviour | Cancer behaviour | Final (5th) digit of an ICD-O morphology code |

  
## 12. Useful syntax
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the <a href="https://github.com/UKLLC" target="_blank" rel="noopener noreferrer">UK LLC Github</a> repository where you can find the full scripts.

## 13. Further reading  
Henson KE, Elliss-Brookes L, Coupland VH, Payne E, Vernon S, Rous B, Rashbass J. **Data Resource Profile: National Cancer Registration Dataset in England.** International Journal of Epidemiology, February 2020. <a href="https://doi.org/10.1093/ije/dyz076" target="_blank" rel="noopener noreferrer">https://doi.org/10.1093/ije/dyz076</a>

UK Biobank. **The use of International Classification of Diseases for Oncology (3rd edition) in UK Biobank.** Version 1.1, February 2023. Available <a href="https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/ICDcancermorph.pdf" target="_blank" rel="noopener noreferrer">here</a>. 

