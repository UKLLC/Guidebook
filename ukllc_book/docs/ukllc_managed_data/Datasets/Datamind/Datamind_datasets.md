# DATAMIND Collection

>Last modified: 10 MAR 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has worked with DATAMIND to create a number of derived mental health and neurodevelopmental datasets.</strong></div>

## Introduction
**Datasets will be available for selection shortly**. 

Identifying the earliest diagnosis date, as captured in secondary data sources, is critical for designing research projects, establishing clear inclusion criteria, distinguishing incident from prevalent cases, and examining changes in disease patterns over time. To support researchers in this work, UK LLC has undertaken an initiative to derive the earliest recorded diagnosis date for selected mental health conditions using a combination of linked NHS England datasets and predefined diagnostic codes (ICD-10 and SNOMED CT) from the [**DATAMIND collection in the HDR UK Phenotype Library**](https://phenotypes.healthdatagateway.org/phenotypes/?collections=27). This initiative covers a range of mental health and neurodevelopmental conditions. The conditions included, and the NHS England datasets used to derive the earliest diagnosis dates are summarised in Table 1.
This approach allows researchers to use derived outcomes directly, without needing to select diagnostic or procedural codes from phenotype libraries or to manually combine multiple datasets. However, the derived outcomes depend on the completeness and accuracy of diagnoses recorded in the underlying datasets. 

<aside class="admonition info"><p class="admonition-title">This initiative, undertaken by UK LLC to identify the first occurrence of mental health conditions, was funded by DATAMIND (grant number: MR/Z504816/1).</aside>

**Table 1** Mental health conditions included, and NHS England datasets used to derive the earliest diagnosis dates. (Click on each condition name to download the corresponding codelist)

| **Datasets**|**HES APC**|**HES OP**|**MHSDS**|**IAPT**|**Mortality**|
|:---|:---|:---|:---|:---|:---|
|[**Schizophrenia**](../../../../images/nhs_scizo_v1.0.xltm)|✓|✓|✓|✓|✓|
|[**Bipolar Disorder and Other Mood-Related Disorders**](../../../../images/nhs_bipolar_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Other Psychotic Disorders and Severe Mental Illnesses**](../../../../images/nhs_psychosis_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Eating Disorders Phenotype**](../../../../images/nhs_eating_v1.0.xltm) |✓|✓|✓|✓|✓|
|[**Depression**](../../../../images/nhs_depression_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Anxiety**](../../../../images/nhs_anxiety_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Conduct Disorder**](../../../../images/nhs_conduct_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Attention – Deficit hyperactivity disorder (ADHD)**](../../../../images/nhs_attention_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Autism Spectrum Disorder (ASD)**](../../../../images/nhs_autism_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Learning difficulties**](../../../../images/nhs_learning_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Childhood Maltreatment**](../../../../images/nhs_child_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Self-harm**](../../../../images/nhs_self_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Alcohol use**](../../../../images/nhs_alcohol_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Drug use**](../../../../images/nhs_drug_v1.0.xltm) |✓|✓|✓|✓|✗|
|[**Death by suicide**](../../../../images/nhs_deathbysuicide_v1.0.xltm) |✗|✗|✗|✗|✓|
|[**Death by mental and behavioural disorders (natural cause)**](../../../../images/nhs_deathbymental_v1.0.xltm) |✗|✗|✗|✗|✓|

## Methodology
### Data Sources
Anonymised data from NHS England were used to identify the earliest diagnosis dates. The datasets considered were: 
 1. [**Mental Health Services Data Set (MHSDS)**.](../../../linked_health_data/NHS_England/Mental%20health%20datasets/MHSDS/MHSDS.ipynb)
 2. [**Hospital Episode Statistics – Outpatients (HES OP)**.](../../../linked_health_data/NHS_England/HES%20datasets/OP/HESOP.ipynb)
 3. [**Hospital Episode Statistics – Admitted Patient Care (HES APC)**.](../../../linked_health_data/NHS_England/HES%20datasets/APC/HESAPC.ipynb)
 4. [**Talking Therapies for Anxiety and Depression (IAPT)**.](../../../linked_health_data/NHS_England/Mental%20health%20datasets/IAPT/IAPT.ipynb)
 5. [**Civil Registrations of Death – Mortality**.](../../../linked_health_data/NHS_England/Registration%20datasets/MORTALITY/MORTALITY.ipynb) 
 
 The following **MHSDS** datasets were used for diagnosis identification: 
 - MHS601 – Medical History (Previous Diagnosis) 
 - MHS603 – Provisional Diagnosis 
 - MHS604 – Primary Diagnosis 
 - MHS605 – Secondary Diagnosis 

 <aside class="admonition note"><p class="admonition-title">Self‑reported Longitudinal Population Study (LPS) data are not currently included. We are collaborating with mental health researchers to capture this information more efficiently, and it will be incorporated into future versions of the derived outcomes.</aside>

### Measures 
Participants diagnosed with specific mental health conditions were identified using the disease-specific ICD-10 (4-digit) codes and SNOMED CT codes sourced from the [**DATAMIND collection in the HDR UK Phenotype Library**](https://phenotypes.healthdatagateway.org/phenotypes/?collections=27).

 <aside class="admonition note"><p class="admonition-title">The original phenotype definitions from the HDR UK Phenotype Library include READ codes. However, READ codes have been excluded from the code lists used in this resource because the linked NHS England datasets available within UK LLC contain diagnoses recorded using ICD-10 and SNOMED CT coding systems only.</aside>

 <aside class="admonition note"><p class="admonition-title">SNOMED CT mappings have been included in the dataset to enhance the coverage of clinical conditions; however, they have not yet been formally validated by the DATAMIND collection.</aside>

### Derivation of Outcomes 
The first date of diagnosis is defined as the earliest recorded inpatient admission date, appointment date, diagnosis date, or referral date within secondary care datasets. For all conditions, this date was derived from the NHS England datasets based on predefined criteria and assumptions (see below), using code list for specific mental health outcome. Records containing relevant mental health-related codes were identified and filtered, and the algorithm selected the earliest applicable date and its corresponding data source. The resulting diagnoses were subsequently processed according to the conventions of each dataset. 

###### MHSDS 
The MHSDS contains two date columns: Diagnosis Date and Coded Diagnosis Timestamp. Only the earliest diagnosed date was considered. The dates were obtained using the following steps: 
1. If a date was present in either column, or only in the Coded Diagnosis Timestamp column, it was retained. If the date was present in the Diagnosis Date column, it was copied into the Coded Diagnosis Timestamp column, which was then considered the primary diagnosis date. 
2. Participants with missing diagnosis dates in both date columns were removed. 
3. The dates and diagnosis codes were filtered accordingly. 

###### HES
 1. HES OP records used the appointment date, and HES APC records used the admission date, which was considered to represent the first diagnosis of mental health outcome. No missing dates were identified for these cases. 
 2. Dates and diagnosis codes from HES OP and HES APC were filtered.  

###### IAPT
 1. In IAPT records, the Mental and Physical Health Recorded Date was used as the earliest available indication of the mental health outcome. All records contained valid dates,  and no missing values were identified. 
 2. Relevant dates and diagnosis codes from this field were then selected according to the specific mental health outcome.

 ###### Mortality
 1. Mortality records were used to identify the date of disease occurrence based on the death date associated with the underlying condition. The recorded death date and the corresponding underlying ICD-10 codes were used as indicators of relevant mental health outcomes. 
 2. Deaths related to other mental health conditions, specifically schizophrenia and eating disorders, were assigned to their respective mental health datasets as defined by the Datamind collection.
 3. All remaining death-related mental health conditions were maintained as conditions within the death by mental and behavioural disorders dataset.

All health outcome-specific filtered data from each dataset were then combined. Participants were grouped using cohort key (individual-level identifiers, used to uniquely identify participants from the LPS), and by diagnosis. The earliest date for each diagnosis was considered. 

Participants without any diagnosis dates who were removed earlier, were checked. There were two types of missing participants as listed below: 
1. For participants whose diagnoses were initially recorded with dates but later appeared as missing for the same diagnosis, the earlier dates were prioritised. 
2. For participants with diagnoses recorded in the database without diagnosis dates, dates were imputed using the earliest recorded diagnosis date from a previously diagnosed condition. 

The source diagnosis column indicated the dataset from which the first date of diagnosis was recorded, specifying whether the source was MHSDS, HES OP, HES APC, IAPT or mortality. For example, in cases where a participant had received diagnoses of both paranoid schizophrenia and simple schizophrenia on different dates, and these diagnoses originated from two separate data sources (HES and MHSDS, respectively), the source diagnosis column was populated with the data source linked to the earliest diagnosis date.

<aside class="admonition info"><p class="admonition-title">The derived datasets are available in long formats only, where each row represents a diagnosis record for a participant.</aside>

</details>

## References 

 1. [John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., & Lloyd, K. (2018).](https://www.sciencedirect.com/science/article/pii/S0920996418301981?via%3Dihub) Premature mortality among people with severe mental illness - New evidence from linked primary care data. Schizophrenia Research, 199, 154-162.

 2. [John, A., Friedmann, Y., DelPozo-Banos, M., Frizzati, A., Ford, T., & Thapar, A. (2022).](https://www.sciencedirect.com/science/article/pii/S2215036621003679) Association of school absence and exclusion with recorded neurodevelopmental disorders, mental disorders, or self-harm: a nationwide, retrospective, electronic cohort study of children and young people in Wales, UK. The Lancet Psychiatry, 9(1), 23-34.

 3. [First Occurrence of Health Outcomes defined by 3-character ICD10 code, report 2019, UK Biobank.](https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/first_occurrences_outcomes.pdf)

 4. [Algorithmically Defined Outcomes (ADOs), report 2022, UK Biobank.](https://biobank.ctsu.ox.ac.uk/ukb/ukb/docs/alg_outcome_main.pdf)
