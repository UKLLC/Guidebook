# DATAMIND mental health datasets

>Last modified: 30 Jan 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has worked with DATAMIND to create a number of derived mental health datasets.</strong></div>

## Introduction
**Datasets will be available for selection shortly**. 

Identifying the earliest diagnosis date, as captured in secondary data sources, is critical for designing research projects, establishing clear inclusion criteria, distinguishing incident from prevalent cases, and examining changes in disease patterns over time. To provide this support for researchers, UK LLC has undertaken an initiative to derive the earliest recorded diagnosis date for selected mental health conditions using a combination of linked NHS England datasets and predefined diagnostic codes from the [**DATAMIND collection in the HDR UK Phenotype Library**](https://phenotypes.healthdatagateway.org/phenotypes/?collections=27). This includes the following conditions: Eating disorders, Anxiety, Depression, and Severe Mental Illnesses (SMIs), including Schizophrenia; Bipolar disorder and other mood-related disorders; and Other psychotic disorders and severe mental illnesses. This approach allows researchers to use derived outcomes without needing to select diagnostic or procedural codes from phenotype libraries or to manually combine multiple datasets. However, the derived outcomes are dependent on the completeness and accuracy of diagnoses recorded in the underlying datasets. 

<aside class="admonition info"><p class="admonition-title">This initiative, undertaken by UK LLC to identify the first occurrence of mental health conditions was funded by DATAMIND (grant number: MR/Z504816/1).</aside>


## Methodology: Severe Mental Illnesses (SMIs)
<details><summary>The NHSE datasets included in the SMI datasets are HESOP, HESAPC and MHSDS</summary>
<br>

### Data Sources
Anonymised data from NHS England were used to identify the earliest diagnosis dates. The datasets considered were: 
 1. [**Mental Health Services Data Set (MHSDS)**.](../../../linked_health_data/NHS_England/Mental%20health%20datasets/MHSDS/MHSDS.ipynb)
 2. [**Hospital Episode Statistics – Outpatients (HES OP)**.](../../../linked_health_data/NHS_England/HES%20datasets/OP/HESOP.ipynb)
 3. [**Hospital Episode Statistics – Admitted Patient Care (HES APC)**.](../../../linked_health_data/NHS_England/HES%20datasets/APC/HESAPC.ipynb)

 
 The following **MHSDS** datasets were used for diagnosis identification: 
 - MHS601 – Medical History (Previous Diagnosis) 
 - MHS603 – Provisional Diagnosis 
 - MHS604 – Primary Diagnosis 
 - MHS605 – Secondary Diagnosis 

 <aside class="admonition note"><p class="admonition-title">Self‑reported Longitudinal Population Study (LPS) data are not currently included. We are collaborating with mental health researchers to capture this information more efficiently, and it will be incorporated into future versions of the derived outcomes.</aside>

### Measures 
Participants diagnosed with the specific health conditions were identified using the disease-specific ICD-10 (4-digit) codes sourced from the [**DATAMIND collection in the HDR UK Phenotype Library**](https://phenotypes.healthdatagateway.org/phenotypes/?collections=27).

### Derivation of Outcomes 
The first date of diagnosis is defined as the earliest recorded inpatient admission date, appointment date, diagnosis date, or referral date within secondary care datasets. For SMI, this date was derived from MHSDS and HES based on predefined criteria and assumptions (see below), using a predefined code list for the specific SMI health outcome. Records containing specific SMI related codes were then filtered, and the algorithm selected the earliest applicable date and its corresponding data source. The resulting diagnoses were processed according to the conventions of each dataset. 

#### MHSDS 
The MHSDS contains two date columns: Diagnosis Date and Coded Diagnosis Timestamp. Only the first diagnosed date was considered. The dates were obtained using the following steps: 
1. If a date was present in either column, or only in the Coded Diagnosis Timestamp column, it was retained. If the date was present in the Diagnosis Date column, it was copied into the Coded Diagnosis Timestamp column, which was then considered the primary diagnosis date. 
2. Participants with missing diagnosis dates in both date columns were removed. 
3. The dates and diagnosis codes were filtered accordingly. 

#### HES
 1. HES OP records used the appointment date, and HES APC records used the admission date, which was considered to represent the first diagnosis of SMIs. No missing dates were identified for these cases. 
 2. Dates and diagnosis codes from HES OP and HES APC were filtered.  



All health outcome-specific filtered data from each dataset were then combined. Participants were grouped using cohort key (individual - level identifiers, used to uniquely identify participants from the LPS), and by diagnosis. The earliest date for each diagnosis was considered. 

Participants without any diagnosis dates who were removed earlier were checked. There were two types of missing participants as listed below: 
1. For participants whose diagnoses were initially recorded with dates but later appeared as missing for the same diagnosis, the earlier dates were prioritised. 
2. For participants with diagnoses recorded in the database without diagnosis dates, dates were imputed using the earliest recorded diagnosis date from a previously diagnosed condition. 

The dataset was then pivoted to one row per patient, and the earliest diagnosis date for each SMI category was derived from individual ICD-10 codes. 
The source diagnosis column indicates the dataset from which the first date of diagnosis was recorded, specifying whether the source was MHSDS, HES OP, or HES APC. For example, in cases where a participant had received diagnoses of both paranoid schizophrenia and simple schizophrenia on different dates, and these diagnoses originated from two separate data sources (HES and MHSDS, respectively), the source diagnosis column was populated with the data source linked to the earliest diagnosis date.

<aside class="admonition info"><p class="admonition-title">The derived datasets are available in both wide and long formats.</aside>


### 1. Schizophrenia
All ICD‑10 diagnosis codes for schizophrenia, from the DATAMIND collection within the HDR UK Phenotyping Library, are included in the dataset.

|**Diagnosis codes**|**Description**| 
|:---|:---|
|F20  |schizophrenia |
|F20.0|paranoid schizophrenia |
|F20.1|hebephrenic schizophrenia |
|F20.2|catatonic schizophrenia |
|F20.3|undifferentiated schizophrenia | 
|F20.4|post-schizophrenic depression |
|F20.5 |residual schizophrenia | 
|F20.6|simple schizophrenia |
|F20.8|other schizophrenia | 
|F20.9|schizophrenia, unspecified |
|F21  |schizotypal disorder |                      
|F21.X|schizotypal disorder |                      
|F22  |persistent delusional disorders |            
|F22.0|delusional disorder |                        
|F22.8|other persistent delusional disorders |     
|F22.9|persistent delusional disorder, unspecified | 
|F24  |induced delusional disorder |              
|F24.X|induced delusional disorder |                
|F25  |schizoaffective disorders |                  
|F25.0|schizoaffective disorder, manic type |       
|F25.1|schizoaffective disorder, depressive type |  
|F25.2|schizoaffective disorder, mixed type |       
|F25.8|other schizoaffective disorders |            
|F25.9|schizoaffective disorder, unspecified |  
                   


### 2. Bipolar disorder and other mood-related disorders 
All ICD‑10 diagnosis codes for bipolar disorder and other mood-related disorders from the DATAMIND collection in the HDR UK Phenotyping Library are included in the dataset. 

|**Diagnosis codes**|**Description**| 
|:---|:---|
|F30.2|mania with psychotic symptoms |
|F31  |bipolar affective disorder |
|F31.0|bipolar affective disorder,current episode hypomanic |
|F31.1|bipolar affective disorder, current episode manic without psychotic symptoms  |
|F31.2|bipolar affective disorder, current episode manic with psychotic symptoms  | 
|F31.3|bipolar affective disorder, current episode mild or moderate depression  |
|F31.4|bipolar affective disorder, current episode severe depression without psychotic symptoms  | 
|F31.5|bipolar affective disorder, current episode severe depression with psychotic symptoms |
|F31.6|bipolar affective disorder, current episode mixed  | 
|F31.7 |bipolar affective disorder, currently in remission|
|F31.8 |other bipolar affective disorders  |                      
|F31.9 |bipolar affective disorder, unspecified  |   

### 3. Other psychotic disorders and severe mental illnesses 
All ICD-10 diagnosis codes for other psychotic disorders and severe mental illnesses from the DATAMIND collection in the HDR UK Phenotyping Library are included in the dataset.

|**Diagnosis codes**|**Description**| 
|:---|:---|
|F23  |acute and transient psychotic disorders|
|F23.0|acute polymorphic psychotic disorder without symptoms of schizophrenia|
|F23.1|acute polymorphic psychotic disorder with symptoms of schizophrenia|
|F23.2|acute schizophrenia-like psychotic disorder|
|F23.3|other acute predominantly delusional psychotic disorders| 
|F23.8|other acute and transient psychotic disorders   |
|F23.9|acute and transient psychotic disorder, unspecified | 
|F28  |other nonorganic psychotic disorders|
|F28.X|other nonorganic psychotic disorders  | 
|F29  |unspecified nonorganic psychosis |
|F29.X|unspecified nonorganic psychosis|                      
|F30  |maniac episodes|   
|F30.0|hypomania|
|F30.1|mania without psychotic symptoms|
|F30.8|other maniac episodes|
|F30.9|maniac episode, unspecified|
|F32.3|severe depressive episode with psychotic symptoms|
|F33.3|recurrent depressive disorder, current episode severe with psychotic symptoms|
|F38  |other mood [affective] disorders|
|F38.1|other recurrent mood [affective] disorders|
|F38.0|other single mood [affective] disorders|
|F38.8|other specified mood [affective] disorders|
|F39  |unspecified mood [affective] disorder|
|F39.X|unspecified mood [affective] disorder|


</details>

## Methodology: Eating disorders, Anxiety and Depression
<details><summary>The NHSE datasets included in the Eating disorders, Anxiety and Depression datasets are HESOP, HESAPC and IAPT</summary>
<br>
Content will be added in due course.
</details>





## References 

 1. [John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., & Lloyd, K. (2018).](https://www.sciencedirect.com/science/article/pii/S0920996418301981?via%3Dihub) Premature mortality among people with severe mental illness - New evidence from linked primary care data. Schizophrenia Research, 199, 154-162.

 2. [John, A., Friedmann, Y., DelPozo-Banos, M., Frizzati, A., Ford, T., & Thapar, A. (2022).](https://www.sciencedirect.com/science/article/pii/S2215036621003679) Association of school absence and exclusion with recorded neurodevelopmental disorders, mental disorders, or self-harm: a nationwide, retrospective, electronic cohort study of children and young people in Wales, UK. The Lancet Psychiatry, 9(1), 23-34.

 3. [First Occurrence of Health Outcomes defined by 3-character ICD10 code, report 2019, UK Biobank.](https://biobank.ndph.ox.ac.uk/ukb/ukb/docs/first_occurrences_outcomes.pdf)

 4. [Algorithmically Defined Outcomes (ADOs), report 2022, UK Biobank.](https://biobank.ctsu.ox.ac.uk/ukb/ukb/docs/alg_outcome_main.pdf)
