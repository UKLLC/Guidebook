# FAQs about codes used in Electronic Health Records (EHRs)
>Last modified: 24 Nov 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>Answers to researchers' questions about diagnostic and procedural codes.</strong></div style>  
<br>

<details>
<summary>How can I find out which codes refer to the condition I am interested in?</summary>  
There are online resources for each medical coding system, enabling you to search on **key words**:  

* ICD-10: <a href="https://icd.who.int/browse10/2019/en" target="_blank" rel="noopener noreferrer">https://icd.who.int/browse10/2019/en</a>  
* SNOMED-CT: <a href="https://termbrowser.nhs.uk/?" target="_blank" rel="noopener noreferrer" >https://termbrowser.nhs.uk/?</a>
* OPCS-4: <a href="https://classbrowser.nhs.uk/#/book/OPCS-4.10" target="_blank" rel="noopener noreferrer">https://classbrowser.nhs.uk/#/book/OPCS-4.10</a>  
</details>  

<details>
<summary>Why does NHS England use SNOMED, ICD-10 and OPCS-4 codes?</summary>
The different coding systems serve different purposes in the NHS. SNOMED codes (used in primary care and mental health) are used to record the detailed information needed by health care professionals providing care. ICD-10 and OPCS-4 codes (found in hospital and registration datasets) are used to enumerate conditions and procedures as required for reimbursement and healthcare planning.
</details>  

<details>
<summary>What do ICD-10 codes look like?</summary>

ICD-10 codes are **alphanumeric**. They begin with a single letter, referring to 1 of 22 'chapters' in the classification, followed by two or more numbers. ICD-10 codes are hierarchical, with the level of detail being increased by the addition of more characters. For example:
| Code | Description |
|:---|:---|
| J | Diseases of the respiratory system |
| J4 | Chronic lower respiratory diseases |
| J45 | Asthma |
| J45.1 | Nonallergic asthma|

N.B. ICD-10 data in the TRE is provided without the decimal point, so e.g. nonallergic asthma appears as: J451.  
</details>  

<details>
<summary>What do OPCS-4 codes look like?</summary>

OPCS-4 codes are **alphanumeric**. They begin with a single letter, referring to 1 of 24 'chapters' in the classification, followed by two or more numbers. OPCS-4 codes are hierarchical, with the level of detail being increased by the addition of more characters. For example:
| Code | Description |
|:---|:---|
| F | Mouth |
| F09 | Surgical removal of tooth |
| F09.1 | Surgical removal of impacted wisdom tooth |

N.B. OPCS-4 data in the TRE is provided without the decimal point, so the example above appears as: F091.  
</details>  

<details>
<summary>What do SNOMED codes look like?</summary>

SNOMED codes are **numeric** and look very different from the short, alphanumeric ICD-10 and OPCS-4 codes. They are typically between 6 and 18 digits long, and do not follow a pattern or hierarchy. This means SNOMED codes cannot be as readily understood as ICD-10 and OPCS-4 codes. 
</details>

<details>
<summary>Can ICD-10 codes be translated into SNOMED codes (and vice versa)?</summary>
There is not a a 1:1 relationship between the two coding systems, but there are tools which enable researchers and clinicians to map one system onto the other, e.g. <a href="https://www.nlm.nih.gov/research/umls/mapping_projects/snomedct_to_icd10cm.html" target="_blank" rel="noopener noreferrer">https://www.nlm.nih.gov/research/umls/mapping_projects/snomedct_to_icd10cm.html</a>.  

**Note:** As SNOMED codes provide far more detail than ICD-10, a single SNOMED code is likely to map to multiple ICD-10 codes.
</details>

<details>
<summary>Which medical coding systems are used in the NHS England datasets in the UK LLC TRE?</summary>

A summary of which datasets use which codes is on Guidebook's [Coded variables](../Coding/coding_intro.md#classification-systems) page.
</details>
