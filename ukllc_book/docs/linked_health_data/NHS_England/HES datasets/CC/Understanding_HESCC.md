# Understanding the HESCC dataset
>Last modified: 03 Dec 2025

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>HESCC is a record of critical care periods in NHS hospitals in England.</strong></div>  

## 1. Introduction
The HESCC dataset contains critical care data for patients who were treated in an **adult critical care unit** during their stay in an NHS hospital in England. Every 'episode' in HESCC occurs as **part of an inpatient admission** recorded in [HESAPC](../APC/Understanding_HESAPC.md). 

>Critical care refers to care provided in **Intensive Care** or **High Dependency** Units (ICU or HDU). 

## 2. Strengths of HESCC  
1) It captures all adult critical care episodes in NHS hospitals in England
2) It is longitudinal making it possible for researchers to study cohorts over time
3) It can be linked to HESAPC episodes via identifiers and admission dates which enables researchers to study critical care episodes in the context of an entire hospital admission

## 3. Limitations of HESCC
1) There is no detailed physiological data (e.g. test results, vital signs)  
2) There are no medical codes (e.g. ICD-10, OPCS) in the dataset
3) It does not measure severity of illness (other than flagging organ support indicators) 
4) Requires linking to HESAPC for complete information on a hospital admission
5) Data entry practices vary between hospitals and over time

## 4. Scope and coverage
HESCC focuses on resource use and level of care provision. It contains patient-level coded information about:  
* start and end dates for each critical care episode
* level of care provided, including 'organ support days' (e.g. ventilation)
* patient identifiers to link back to the main admission (recorded in HESAPC)
* discharge destinations and re-admissions

## 5. Data collection methodology
NHS Trusts in England extract critical care episode details from their patient administration systems. These data are submitted alongside HES Admitted Patient Care (HESAPC) data. More information on how HESAPC data are collected is [here](../APC/Understanding_HESAPC.md#5-data-collection-methodology) 

## 6. Structure of the dataset
HESCC contains one record (line) for each critical care episode; a patient may have more than one CC episode per hospital admission.

## 7. Coding systems used
The [medical codes](../APC/Understanding_HESAPC.md#7-coding-systems-used) used in HESAPC are not replicated in HESCC. To get detailed information on a patient's diagnosis, HESCC must be linked to HESAPC.  

HESCC uses HES internal codes to record information such as type of critical care unit, level of care provided, organ support indicators, and discharge destination.

## 8. Evolution of the dataset
HESCC is a subset of HESAPC so shares much of [HESAPC's history](../APC/Understanding_HESAPC.md#8-evolution-of-the-dataset). All adult critical care episodes were included in HESAPC until 2008, when HESCC became a separate dataset.  

Data quality and completeness have improved since reporting became mandatory for adult critical care units in the 2010s. The consistency of reporting continued to improve when new validation rules were introduced in 2017.

## 9. Availability in the UK LLC TRE
The UK LLC TRE holds an extract of the HESCC dataset dating back to 2008. The HESCC records of participants in UK LLC's partner LPS, where individual or LPS permissions allow linkage to NHS data, are included in the TRE. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHSE data not be shared via UK LLC.

More detailed information about the UK LLC's HESCC extract is [here](../CC/HESCC.ipynb).

## 10. UK LLC transformations of the dataset
HESAPC (and other NHSE hospital datasets) contain variables which identify organisations or small geographic areas. These are encrypted before being ingested into the UK LLC TRE, and are identifiable by a suffix **_e** on the variable name(s).  
HESCC does not contain any of these variables, but researchers should be aware of this encryption when linking HESCC to HESAPC.

## 11. Tips for researchers using HESCC in the UK LLC TRE
### a) Linking to HESAPC
**Episodes**: critical care episodes recorded in HESCC are a subset of full hospital episodes found in HESAPC. Researchers should be aware that every CC episode can be linked to an inpatient episode (in HESAPC) and that patients can have more than one CC episode per hospital episode.  

**Diagnoses and procedures**: HESCC must be linked to the main HESAPC dataset to make use of any clinical information beyond 'organ support'.  

**Dates**: the start and end dates of critical care episodes always fall between the admitted patient care (APC) admission and discharge dates
  
### b) Examples of variables in HESCC
| Variable name | Variable label | Description | Additional information |
|---|---|---|---|
| ccstartdate | Critical care start date | Date a patient was admitted to ICU or HDU | 
| ccdisdate | Critical care discharge date | Date a patient was discharged from unit | If alive. Otherwise this field contains date of death |
| cclev2days | Critical care level 2 (days) | Total days during which level 2 care was provided | A comparable variable exists for level 3
| liversupdays | Liver support days | Number of days of liver support | Comparable variables exist for other organ support (e.g. renal, cardiovascular) |
| orgsupmax | Organ support maximum | Maximum number of organs supported at any one time, at any point in the critical care period |
  
## 12. Useful syntax
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the <a href="https://github.com/UKLLC" target="_blank" rel="noopener noreferrer">UK LLC Github</a> repository where you can find the full scripts.

## 13. Further reading  
Information in this section will be added in due course.





