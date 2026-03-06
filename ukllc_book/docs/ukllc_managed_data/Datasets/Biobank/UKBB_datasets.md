# UK Biobank collection

>Last modified: 06 Mar 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC is working towards reproducing UK Biobank's 'algorithmically-defined outcomes' (ADOs) for a range of health outcomes.</strong></div>

## Introduction
**Datasets will be available for selection shortly**. 

UK LLC has generated derived datasets for 7 health outcomes, partially based on algorithms developed and validated by <strong><a href="https://www.ukbiobank.ac.uk/" target="_blank" rel="noopener noreferrer">UK Biobank</a></strong>. These are:  
* [Asthma](#asthma)
* [Chronic obstructive pulmonary disease (COPD)](#chronic-obstructive-pulmonary-disease-copd)
* [Dementia](#dementia)  
* [Myocardial infarction (MI)](#myocardial-infarction-mi)
* [Motor neurone disease (MND)](#motor-neurone-disease-mnd)
* [Parkinson's disease](#parkinsons-disease)
* [Stroke](#stroke)  

The datasets have been derived based on <strong><a href="https://biobank.ndph.ox.ac.uk/showcase/ukb/docs/alg_outcome_main.pdf" target="_blank" rel="noopener noreferrer">UK Biobank's methodology</a></strong>, though it is not possible to replicate UK Biobank's work exactly. The differences between the two approaches are outlined below.

### UK Biobank's approach
UK Biobank's full methodology and description of the **algorithmically-defined outcomes (ADOs)** is available <a href="https://biobank.ndph.ox.ac.uk/showcase/ukb/docs/alg_outcome_main.pdf" target="_blank" rel="noopener noreferrer">online</a>.

In brief, the ADOs identify two key features of health outcomes:  
1. the **earliest recorded date of a given health outcome** (across self-reported data, hospital admissions, and death records)
2) whether a clinical code for a health outcome is the **primary (underlying) or secondary (contributory)** cause of hospital admission or death.  


### UK LLC's approach  
The key difference between UK Biobank's methodology and UK LLC's is that UK LLC has not yet incorporated self-reported diagnoses into the derived datasets. Researchers interested in self-reported health data for individual LPS are encouraged to use <a href="https://explore.ukllc.ac.uk/" target="_blank" rel="noopener noreferrer">UK LLC Explore</a> to identify variables of interest.  

The different data sources used by UK Biobank and UK LLC are shown below.
|<div stype="width: 20px;">Data source</div> | UK Biobank| UK LLC |
|:---|:---:|:---:|
| <b>Hospital admission data: 
|&emsp;&emsp;[HES APC (England)](../../../linked_health_data/NHS_England/HES%20datasets/APC/HESAPC.ipynb)                 |✓|✓|
|&emsp;&emsp;PEDW (Wales) <sup>1</sup>         |✓|✗|
|&emsp;&emsp;SMR01 (Scotland)  <sup>1</sup>    |✓|✗|
| <b>[Death register data](../../../linked_health_data/NHS_England/Registration%20datasets/MORTALITY/MORTALITY.ipynb)           |✓|✓|
| <b>Self-reported data from LPS</b> <sup>2</sup> |✓|✗|

<sup>1</sup> UK LLC's derived datasets will be updated to include linked hospital data from NHS Wales and NHS Scotland once these data are available.  
<sup>2</sup> UK LLC is hoping to harmonise LPS participants' self-reported diagnoses of each of the 7 health outcomes.

## Health outcomes: derived datasets
UK Biobank's ADOs include clinical codes from both <strong><a href="https://icd.who.int/browse10/2019/en" target="_blank" rel="noopener noreferrer">ICD-10</a></strong> and ICD-9, for hospital admission data, and ICD-10 only for mortality data. The HES datasets in the UK LLC Trusted Research Environment (TRE) do not include ICD-9 codes, so only ICD-10 codes have been included. These are summarised, by health outcome, [below](#icd-10-codes-for-each-health-outcome).

<aside class="admonition note"><p class="admonition-title">The ADOs do not include primary care data</p>Outcomes most frequently managed in primary care (e.g. asthma, dementia) are likely to be under-represented.</aside>

UK LLC's derived datasets are in **long format** and comprise just four variables:
* **study id** (individual identifier)
* **date** (the earliest recorded occurence of the outcome in the HES or mortality datasets)
* **source** (i.e. hospital primary, hospital secondary, mortality underlying, mortality contributory)
* **outcome** (e.g. asthma, Alzheimer's disease)

**Asthma, COPD, MND**: for these 3 outcomes, the algorithm treats all disease sub-types as one, so there is only one record (row) per participant in the dataset. E.g. the algorithm for COPD comprises 11 ICD-10 codes, covering both emphysema and COPD, ultimately presented as a single outcome.

**Dementia, MI, Parkinson's disease, stroke**: for these outcomes, event subtypes are recorded independently. E.g. a participant with a record having had both a subarachnoid haemorrhage and an intracerebral haemorrhage will have these recorded separately in the dataset, plus an additional line for 'All cause stroke'.

### ICD-10 codes for each health outcome

#### Asthma
<details><summary>ICD-10 codes for asthma</summary>

|Code| Description |
|---|---|
|J45 <sup>a</sup> | Asthma |
|J46.X | Status asthmaticus |

<sup>a</sup> All ICD-10 codes beginning 'J45' are included 
</details>

#### Chronic obstructive pulmonary disease (COPD)
<details><summary>ICD-10 codes for COPD</b></summary>

|Code <sup>a</sup>| Description |
|---|---|
|J43   | Emphysema
|J44   | Other COPD

<sup>a</sup> All ICD-10 codes beginning 'J43' or 'J44' are included 
</details>

#### Dementia
<details><summary>ICD-10 codes for dementia</summary>
UK Biobank's ADO for dementia considers <b>Alzheimer's Disease (AD)</b>, <b>Vascular Dementia (VD)</b>, and <b>Frontotemporal Dementia (FTD)</b> separately. In UK LLC's derived dementia dataset, the first recorded date and the record source are provided for each separately.  

|Code| Description |AD|VD|FTD|Dementia<br>(all causes) |
|---|---|:---:|:---:|:---:|:---:|
|A81.0 | Sporadic Creutzfeldt-Jakob disease                     | | | |✓|
|F00 <sup>a</sup>   | Dementia in AD                            | ✓| ||✓|
|F01  <sup>b</sup>   | Vascular dementia                        | |✓ ||✓|
|F02 <sup>c</sup>   | Dementia in diseases classified elsewhere | | | |✓|
|F02.0 | Dementia in Pick's disease                             || |✓|✓|
|F03   | Unspecified dementia                                  | | | |✓ |
|F05.1   | Delirium superimposed on dementia | | | |✓|
|F10.6   | Mental and behavioural disorders due to <br>use of alcohol - amnesic syndrome | | | |✓|
|G30 <sup>d</sup>   | Alzheimer's disease |✓| | |✓|
|G31.0 | Circumscribed brain atrophy | | |✓|✓|
|G31.1   | Senile degeneration of brain | | | |✓|
|G31.8   | Other specified degenerative diseases of nervous system | | | |✓|
|I67.3  | Binswanger's disease                         | |✓| ||

**Notes**  
<sup>a</sup> All ICD-10 codes beginning 'F00' are included   
<sup>b</sup> All ICD-10 codes beginning 'F01' are included   
<sup>c</sup> All ICD-10 codes beginning 'F02' are included   
<sup>d</sup> All ICD-10 codes beginning 'G30' are included 
</details>

#### Myocardial infarction (MI)
<details><summary>ICD-10 codes for MI</summary>
UK Biobank's ADO for MI considers ST-elevation myocardial infarction <b>(STEMI)</b> and Non-ST-elevation myocardial infarction <b>(NSTEMI)</b> separately. In UK LLC's derived MI dataset, the first recorded date and the record source are provided for each type separately.  

|Code| Description |STEMI|NSTEMI|MI|
|---|---|:---:|:---:|:---:|
|I21| Acute MI                                   | | |✓ |
|I21.0| Acute transmural MI of anterior wall     |✓| |✓ |
|I21.1| Acute transmural MI of inferior wall     |✓| |✓ |
|I21.2| Acute transmural MI of other sites       |✓| |✓ |
|I21.3| Acute transmural MI of unspecified sites |✓| |✓ |
|I21.4| Acute subendocardial MI                  | |✓|✓ |
|I21.9| Acute MI, unspecified                    | |✓|✓ |
|I22| Subsequent MI                              | | |✓ |
|I22.0| Subsequent MI of anterior wall           |✓| |✓ |
|I22.1| Subsequent MI of inferior wall           |✓| |✓ |
|I22.8| Subsequent MI of other sites             |✓| |✓ |
|I22.9| Subsequent MI of unspecified site        | |✓|✓ |
|I23 <sup>a</sup>| Certain current complications following acute MI                                   | | |✓ |
|I24.1| Dressier syndrome                             | | |✓ |
|I25.2| Old MI                                   | | |✓ |

<sup>a</sup> All ICD-10 codes beginning 'I23' are included   

</details>

#### Motor Neurone Disease (MND)
<details><summary>ICD-10 code for MND</summary>

|Code| Description |
|---|---|
|G12.2 | Motor Neurone Disease

</details>

#### Parkinson's disease
<details><summary>ICD-10 codes for Parkinson's disease</summary>
UK Biobank's ADO for Parkinson's disease considers <b>Parkinson's disease (PD)</b>, <b>Multiple System Atrophy (MSA)</b>, and <b>Progressive Supranuclear Palsy (PSP)</b> separately. In UK LLC's derived Parkinson's disease dataset, the first recorded date and the record source are provided for each type separately.  

|Code| Description |PD |MSA|PSP|All cause<br>Parkinsonism|
|---|---|:---:|:---:|:---:|:---:|
|G20| Parkinson's disease                   |✓| | |✓|
|G21 <sup>a</sup> | Secondary parkinsonism  | | | |✓|
|G22 | Parkinsonism in diseases specified elsewhere  | | | |✓|
|G23.0 | Hallervorden-Spatz disease | | | |✓|
|G23.1 | Progressive Supranuclear Palsy | | |✓|✓|
|G23.2 | Multiple system atrophy, parkinsonian type [MSA-P]| |✓| |✓|
|G23.3 | Multiple system atrophy, cerebellar type [MSA-C]| |✓| |✓|
|G23.8 | Other specified degenerative diseases of basal ganglia | | | |✓|
|G23.9 | Degenerative diseases of basal ganglia, unspecified | | | |✓|
|G25.9 | Extrapyramidal and movement disorder, unspecified | | | |✓|
|G26 | Extrapyramidal and movement disorders in<br>diseases classified elsewhere | | | |✓|
|G90.3 | Multi-system degeneration | |✓| |✓|

<sup>a</sup> All ICD-10 codes beginning 'G21' are included  
</details>

#### Stroke
<details><summary>ICD-10 codes for stroke</summary>
UK Biobank's ADO for stroke events considers <b>ischaemic stroke (IS)</b>, <b>intracerebral haemorrhage (IH)</b>, and <b>subsrachnoid haemorrhage (SH)</b> separately. In UK LLC's derived stroke dataset, the first recorded date and the record source are provided for each type separately.  

|Code| Description |IS |IH|SH|Stroke |
|---|---|:---:|:---:|:---:|:---:|
|I60 <sup>a</sup>| Subarachnoid haemorrhage    | | |✓|✓|
|I61 <sup>b</sup>  | Intracerebral haemorrhage | |✓| |✓|
|I63 <sup>c</sup>  | Cerebral infarction       |✓| | |✓|
|I64.X             | Stroke, not specified as haemorrhage or infarction |✓| | |✓|

**Notes**  
<sup>a</sup> All ICD-10 codes beginning 'I60' are included  
<sup>b</sup> All ICD-10 codes beginning 'I61' are included  
<sup>c</sup> All ICD-10 codes beginning 'I63' are included  
</details>
