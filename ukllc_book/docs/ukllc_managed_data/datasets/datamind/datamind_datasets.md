# DATAMIND Collection

>Last modified: 08 May 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has worked with DATAMIND to create derived mental health and neurodevelopmental datasets.</strong></div>

<aside class="admonition info"><p class="admonition-title">This initiative was funded by DATAMIND (grant number: MR/Z504816/1).</aside>

## Introduction
**Datasets will be available for selection shortly**. 

Identifying the earliest diagnosis date, as captured in secondary data sources, is critical for designing research projects, establishing clear inclusion criteria, distinguishing incident from prevalent cases, and examining changes in disease patterns over time. To support researchers, UK LLC has undertaken an initiative to derive the earliest recorded diagnosis date for selected mental health and neurodevelopmental conditions using a combination of linked NHS England datasets and predefined diagnostic codes (ICD-10 and SNOMED CT) from the [**DATAMIND collection in the HDR UK Phenotype Library**](https://phenotypes.healthdatagateway.org/phenotypes/?collections=27). This approach allows researchers to use derived outcomes directly, without needing to select diagnostic or procedural codes from phenotype libraries or to manually combine multiple datasets. However, the derived outcomes depend on the completeness and accuracy of diagnoses recorded in the underlying datasets.

See Table 1 for the list of datasets, the coding schema included in each dataset and the NHS England datasets used to derive the earliest diagnosis date of each condition. Note, if a participant has been diagnosed with more than one condition, they will be included in each relevant dataset. 

<aside class="admonition danger"><p class="admonition-title">UK LLC is unable to include English GP records because the GDPPR dataset can currently only be used for research relating to COVID-19.</p>For anxiety and depression, in particular, this is a potential limitation because most diagnoses of these conditions are recorded in primary care.</aside>

**Table 1** List of datasets, coding schema and NHS England datasets used to derive the earliest diagnosis date of each condition (click the dataset name to download the corresponding codelist) 

| **Datasets**|**Coding schema***|[**HESAPC**](../../../linked_health_data/nhs_england/hes_datasets/apc/hesapc.ipynb)|[**HESOP**](../../../linked_health_data/nhs_england/hes_datasets/op/hesop.ipynb)|[**MHSDS**](../../../linked_health_data/nhs_england/mental_health_datasets/mhsds/mhsds.ipynb)|[**IAPT**](../../../linked_health_data/nhs_england/mental_health_datasets/iapt/iapt.ipynb)|[**Mortality**](../../../linked_health_data/nhs_england/registration_datasets/mortality/)|
|:---|:---|:---:|:---:|:---:|:---:|:---:|
|[**Schizophrenia**](../../../../images/nhs_scizo_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✓|
|[**Bipolar disorder and other mood-related disorders**](../../../../images/nhs_bipolar_v1.0.xltm)|ICD10 & SNOMED |✓|✓|✓|✓|✗|
|[**Other psychotic disorders and severe mental illnesses**](../../../../images/nhs_psychosis_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Eating disorders phenotype**](../../../../images/nhs_eating_v1.0.xltm)|ICD10|✓|✓|✓|✓|✓|
|[**Depression**](../../../../images/nhs_depression_v1.0.xltm)|ICD10|✓|✓|✓|✓|✗|
|[**Anxiety**](../../../../images/nhs_anxiety_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Conduct disorder**](../../../../images/nhs_conduct_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Attention deficit hyperactivity disorder (ADHD)**](../../../../images/nhs_attention_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Autism spectrum disorder (ASD)**](../../../../images/nhs_autism_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Learning difficulties**](../../../../images/nhs_learning_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Childhood maltreatment**](../../../../images/nhs_child_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Self-harm**](../../../../images/nhs_self_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Alcohol use**](../../../../images/nhs_alcohol_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Drug use**](../../../../images/nhs_drug_v1.0.xltm)|ICD10 & SNOMED|✓|✓|✓|✓|✗|
|[**Death by suicide**](../../../../images/nhs_deathbysuicide_v1.0.xltm)|ICD10|✗|✗|✗|✗|✓|
|[**Death by mental and behavioural disorders (natural cause)**](../../../../images/nhs_deathbymental_v1.0.xltm)|ICD10|✗|✗|✗|✗|✓|

*The phenotype definitions from the HDR UK Phenotype Library include **READ codes**. However, the NHS England datasets available to UK LLC only contain diagnoses recorded using ICD-10 and SNOMED CT and so we have excluded READ codes from the codelists.
## Methodology
### Data Sources
Anonymised data from NHS England were used to identify the earliest diagnosis date for each condition. The datasets considered were: 
 1. [**Hospital Episode Statistics (HES) Admitted Patient Care (HESAPC)**.](../../../linked_health_data/nhs_england/hes_datasets/apc/hesapc.ipynb)
 2. [**HES Outpatients (HESOP)**.](../../../linked_health_data/nhs_england/hes_datasets/op/hesop.ipynb)
 3. [**Mental Health Services Data Set (MHSDS)**.](../../../linked_health_data/nhs_england/mental_health_datasets/mhsds/mhsds.ipynb)
 4. [**Improving Access to Psychological Therapies (IAPT)**.](../../../linked_health_data/nhs_england/mental_health_datasets/iapt/iapt.ipynb)
 5. [**Civil Registrations of Death (Mortality)**.](../../../linked_health_data/nhs_england/registration_datasets/mortality/mortality.ipynb) 
 
 The following **MHSDS** datasets were used for diagnosis identification: 
 - MHS601 – Medical History (Previous Diagnosis) 
 - MHS603 – Provisional Diagnosis 
 - MHS604 – Primary Diagnosis 
 - MHS605 – Secondary Diagnosis 

 <aside class="admonition note"><p class="admonition-title">Self‑reported Longitudinal Population Study (LPS) data are not currently included.</p>We are collaborating with mental health researchers to capture this information more efficiently and it will be incorporated into future versions of the derived outcomes.</aside>

### Measures 
Participants diagnosed with specific mental health and neurodevelopmental conditions were identified using the disease-specific ICD-10 (4-digit) codes and SNOMED CT codes sourced from the [**DATAMIND collection in the HDR UK Phenotype Library**](https://phenotypes.healthdatagateway.org/phenotypes/?collections=27). **Note**: the SNOMED CT mappings have not yet been formally validated by the DATAMIND collection.

### Derivation of outcomes 
The first date of diagnosis is defined as the earliest recorded inpatient admission date, appointment date, diagnosis date, or referral date within secondary care datasets. For all conditions, this date was derived from the NHS England datasets based on predefined criteria and assumptions (see below), using the code list for each specific mental health or neurodevelopmental outcome. Records containing relevant codes were identified and filtered, and the algorithm selected the earliest applicable date and its corresponding data source. The resulting diagnoses were subsequently processed according to the conventions of each dataset. 

**HES**
 1. HESOP records used the appointment date, and HESAPC records used the admission date, which was considered to represent the first diagnosis of mental health or neurodevelopmental outcome. No missing dates were identified for these cases. 
 2. Dates and diagnosis codes from HESOP and HESAPC were filtered.  
 
**MHSDS**   
The MHSDS contains two date columns: Diagnosis Date and Coded Diagnosis Timestamp. Only the earliest diagnosed date was considered. The dates were obtained using the following steps: 
1. If a date was present in either column, or only in the Coded Diagnosis Timestamp column, it was retained. If the date was present in the Diagnosis Date column, it was copied into the Coded Diagnosis Timestamp column, which was then considered the primary diagnosis date. 
2. Participants with missing diagnosis dates in both date columns were removed. 
3. The dates and diagnosis codes were filtered accordingly. 

**IAPT**
 1. In IAPT records, the Mental and Physical Health Recorded Date was used as the earliest available indication of the mental health outcome. All records contained valid dates and no missing values were identified. 
 2. Relevant dates and diagnosis codes from this field were then selected according to the specific mental health or neurodevelopmental outcome.

**Mortality**
 1. Mortality records were used to identify the date of disease occurrence based on the death date associated with the underlying condition. The recorded death date and the corresponding underlying ICD-10 codes were used as indicators of relevant mental health or neurodevelopmental outcomes. 
 2. Deaths related to other mental health conditions, specifically schizophrenia and eating disorders, were assigned to their respective mental health datasets as defined by the Datamind collection.
 3. All remaining death-related mental health conditions were maintained as conditions within the death by mental and behavioural disorders dataset.

All health outcome-specific filtered data from each dataset were then combined. Participants were grouped using cohort key (individual-level identifiers used to uniquely identify participants from the LPS), and by diagnosis. The earliest date for each diagnosis was considered. Participants without any diagnosis dates who were removed earlier, were checked. There were two types of missing participants as listed below: 
1. For participants whose diagnoses were initially recorded with dates but later appeared as missing for the same diagnosis, the earlier dates were prioritised. 
2. For participants with diagnoses recorded in the database without diagnosis dates, dates were imputed using the earliest recorded diagnosis date from a previously diagnosed condition. 

The source diagnosis column indicated the dataset from which the first date of diagnosis was recorded, specifying whether the source was HESOP, HESAPC, MHSDS, IAPT or Mortality. For example, in cases where a participant had received diagnoses of both paranoid schizophrenia and simple schizophrenia on different dates, and these diagnoses originated from two separate data sources (HES and MHSDS, respectively), the source diagnosis column was populated with the data source linked to the earliest diagnosis date.

<aside class="admonition info"><p class="admonition-title">The derived datasets are available in long format only.</p>Each row represents a diagnosis record for a participant.</aside>

</details>

## References 

 1. [John A, McGregor J, Jones I, Lee SC, Walters JTR, Owen MJ, O'Donovan M, DelPozo-Banos M, Berridge D, & Lloyd K (2018).](https://www.sciencedirect.com/science/article/pii/S0920996418301981?via%3Dihub) Premature mortality among people with severe mental illness - New evidence from linked primary care data. Schizophrenia Research, 199, 154-162.

 2. [John A, Friedmann Y, DelPozo-Banos M, Frizzati A, Ford T, & Thapar A (2022).](https://www.sciencedirect.com/science/article/pii/S2215036621003679) Association of school absence and exclusion with recorded neurodevelopmental disorders, mental disorders, or self-harm: a nationwide, retrospective, electronic cohort study of children and young people in Wales, UK. The Lancet Psychiatry, 9(1), 23-34.

 3. [First Occurrence of Health Outcomes defined by 3-character ICD10 code, report 2019, UK Biobank.](https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/first_occurrences_outcomes.pdf)

 4. [Algorithmically Defined Outcomes (ADOs), report 2022, UK Biobank.](https://biobank.ctsu.ox.ac.uk/ukb/ukb/docs/alg_outcome_main.pdf)
