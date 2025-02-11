# Working with NHS England data
>Last modified: 11 Feb 2025

<details>
<summary>Does UK LLC check the <B>accuracy</B> of health records?</summary>

No, the UK LLC Data Team can only see de-identified records in the TRE and does not amend any participant data. The UK LLC Data Team only performs the following data curation tasks:
- Clean and deduplicate data, dataset names and structures to enable data provisioning in an efficient manner while maintaining data integrity.
- Load and integrate variable and value labelling, where available from the NHS API and other web sources, into master metadata tables.
- Run the automated disclosure control risk assessment and manually review all flagged risks.
</details>
<br>
<details>
<summary>What <B>medical codes</B> are used in the NHS England data available in the TRE?</summary>

The main clinical classifications mandated by NHS England are SNOMED CT, ICD-10 and OPCS-4.
More information on codes used in Electronic Health Records (EHRs) is available here: [**Coded variables**](../../linked_health_data/NHS_England/Coding/coding_intro.md)
</details>
<br>
<details>
<summary>For which datasets do researchers need to provide <B>codelists</B>?</summary>

Researchers must provide codelists for their projects if they intend to use any of the following datasets:
* [HES](../../linked_health_data/NHS_England/HES%20datasets/) (Hospital Episode Statistics)
* [GDPPR](../../linked_health_data/NHS_England/Primary_care_datasets/primary_intro.md) (General Practice Extraction Service (GPES) Data for Pandemic Planning and Research)
* [Cancer registrations](../..//linked_health_data/NHS_England/Registration%20datasets/CANCER/)
* [PCM](../../linked_health_data/NHS_England/Other%20datasets/PCM/PCM.ipynb) (Primary Care Medicines)

The datasets use a range of clinical classifications, including:
* ICD-9 (HES & cancer registrations)  
* ICD-10 (HES)  
* SNOMED-CT (GDPPR)  
* OPCS-4 (HES)  
* ODS (cancer registrations and PCM)
* dm+d (PCM)
* NHS national codes (all datasets)  

More information on codes used in Electronic Health Records (EHRs) is available here: [**Coded variables**](../../linked_health_data/NHS_England/Coding/coding_intro.md)
</details>
<br>
<details>
<summary>What impact do the <B>different levels of coding</B> have on HES data?</summary>

The extent to which specific coding is used in HES data is important. For example, you may observe more records in your HESAPC (admitted patients) than in HESOP (outpatients) dataset, despite the national volume of HESOP records being typically ~5x greater per year. This is because HESAPC has meaningful diagnoses codes consistently provided, whereas generic codes are more often used in HESOP. This means when codes provided by a researcher are matched with HES data in the TRE, fewer matches ('hits') will be made on datasets with non-specific codes. Thus fewer records will be included in the project.  
<br>
Examples of non-specific codes include “R69=Not known” for diagnoses and “X997=Not known” for operations. These are used extensively in HESOP, but far less so in HESAPC.  

UK LLC is considering the way it makes linked health records available, by initially making unfiltered views available to researchers (with particularly sensitive records removed) rather than asking for codelists upfront. This will allow codelists to be developed whilst working with the data, but will also allow exploration of records which do not have specific codes assigned.
</details>
<br>
<details>
<summary>Why are there some <b>missing variable and value labels</b> in some datasets?</summary>

Variable labelling is primarily sourced from an NHS metadata API, but is not fully complete. Gaps in HES and MHSDS have been infilled from additional data dictionary sources. As part of ongoing work, we will be integrating additional sources to further complete the labelling and add value labels. We will inform users as these are updated. The approx. current variable label completeness is:
* HES, NPEX, COVIDSGSS: 100%
* MHSDS: 70 - 90% 
* GDPPR, CVS, CVAR: 70% 
* PCM: 40%
* DEMOGRAPHICS, CHESS, IELISA: not available.
</details>
<br>
<details>
<summary>What <b>version</b> of NHS England data was I provisioned?</summary>

NHS England data provisioned to projects are locked to a specific extract. This is done using the extract_date variable found in the dataset, and is the date the data was extracted at NHS England.  
All projects are 'locked' to an NHS quarterly extract as well to as a fixed table, which controls permissions/consent. This locking is done based on the time of first provision of each project in the TRE. This locking prevents participant numbers from fluctuating during the course of a project (if, for example, more data or more participants are added to the TRE).  
Each fixed table is logged as a quarterly [**'freeze'**](../../introduction/Sample/freezes/freeze1.ipynb). The freeze number, and freeze date, is provided in the 'documentation' folder in each TRE project space.
</details>
<br>
<details>
<summary>Why are some NHS England variables <b>excluded or encrypted</b>?</summary>

Prior to upload to the UK LLC TRE database, NHS data are assessed for disclosure risk. During this process, variables can be excluded from the upload if they are deemed to be disclosive. In cases where the variable has utility in an encrypted form, the variable is encrypted rather than excluded and an ***_e*** suffix is added to the end of the variable name e.g. *lsoa* ***_e***. Encryption is usually applied to variables which are, or provide, proxies for location information smaller than region. 
</details>
<br>
<details>
<summary>What do the <B><i>_ACP</i>, <i>_MAT</i> and <i>_OTR</i></B> suffixes refer to in HES data?</summary>

* *_OTR* is short for **Other** and is an extension of the HES record. There should be a 1:1 relationship between the main record found in HESAPC for example and its extension in HESAPC_OTR
* *_ACP* is short for **Augmented care period**. This was collected from 1997–2006. It was replaced by HESCC (critical care) in 2008
* *_MAT* is short for **Maternity** and contains variables associated with maternity-related admissions.  

See below for data and sub table lookup relationships. Note: HESCC is a subset of HESAPC 

<img src="../../images/user_guide/Picture2.png" width="400"/>  

</details>
<br>


<details>
<summary>How can I link <B>_ACP</B>, <B>_MAT</B>, <B>_OTR</B>”, and <B>HESCC</B> data to their main record?</summary>

These sub tables do not contain an individual-level identifier. They therefore need to be linked to the main HESAPC / HESOP / HESAE datsets. See below for the linkage keys for each dataset: 

<img src="../../images/user_guide/Picture3.png" width="400"/>

</details>
<br>

<details>
<summary>How to find test results in <B>COVID-19</B> datasets?</summary>

* **NPEX and IELISA**: Use the variable "testresult". The result is SNOMED (SCT) coded. There are 6 codes used, e.g. “SCTID: 1240581000000104”: “Severe acute respiratory syndrome coronavirus 2 detected (finding)”.
* **COVIDSGSS**: This dataset does not contain a test results field. We are awaiting confirmation from NHS England about how to interpret the presence of records in this dataset.
</details>
<br>
<details>
<summary>How can I request <b>additional data</b> for my project?</summary>

Requests for new data should be submitted via an [**amendment**](../../user_guide/RequestingAnAmendment.md) to UK LLC. You may apply for additional linked data, additional data from already approved LPS, and/or data from additional LPS.  
N.B. each type of data amendment requires a different level of review before being approved. 

</details>
