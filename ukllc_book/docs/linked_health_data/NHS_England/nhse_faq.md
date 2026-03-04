# FAQs about NHS England data
>Last modified: 27 Feb 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>Answers to researchers' questions about working with linked NHS England data.</strong></div style>  
<br>

<details>
<summary>Does UK LLC check the <B>accuracy</B> of health records?</summary>

No, the UK LLC Data Team can only see de-identified records in the TRE and does not amend any participant data. The UK LLC Data Team only performs the following data curation tasks:
- Clean and deduplicate data, dataset names and structures to enable data provisioning in an efficient manner while maintaining data integrity.
- Load and integrate variable and value labelling, where available from the NHS API and other web sources, into master metadata tables.
- Run the automated disclosure control risk assessment and manually review all flagged risks.
</details>

<details>
<summary>What <B>medical codes</B> are used in the NHS England data available in the TRE?</summary>

The main clinical classifications mandated by NHS England are SNOMED CT, ICD-10 and OPCS-4.
More information on codes used in Electronic Health Records (EHRs) is available here: [**Coded variables**](../NHS_England/Coding/coding_intro.md)
</details>

<details>
<summary>For which datasets do researchers need to provide <B>codelists</B>?</summary>

Researchers must provide codelists for their projects if they intend to use any of the following six datasets:
* [**HESOP**](../NHS_England/HES%20datasets/OP/HESOP.ipynb)
* [**HESAPC**](../NHS_England/HES%20datasets/APC/HESAPC.ipynb)
* [**HESAE**](../NHS_England/HES%20datasets/AE/HESAE.ipynb)
* [**GDPPR**](../NHS_England/Primary_care_datasets/GDPPR/GDPPR.ipynb)
* [**PCM**](../NHS_England/Primary_care_datasets/PCM/PCM.ipynb)
* [**CANCER**](../NHS_England/Registration%20datasets/CANCER/CANCER.ipynb)

The datasets use a range of clinical classifications, including:
* ICD-9 (HES & cancer registrations)  
* ICD-10 (HES)  
* SNOMED-CT (GDPPR)  
* OPCS-4 (HES)  
* ODS (cancer registrations and PCM)
* dm+d (PCM)
* NHS national codes (all datasets)  

More information creating a codelist is available here: [**Codelists**](../NHS_England/Coding/codelists.md)
</details>

<details>
<summary>How can I quantify the <b>effect of applying codelists</b> to my dataset?</summary> 

The file [**'NHSE patient service usage'**](../../ukllc_managed_data/UKLLC_generated/Datasets/Linked_derived/nhse_patient_service_usage.ipynb) contains the number of appearances and the date of the most recent appearance for each participant for each available NHS data source. Comparing LPS participants' presence in NHS data sources against the data provisioned to a project will identify which participants appear in the data source but are not included in the provisioned data. 
</details>

<details>
<summary>Why are there some <b>missing variable and value labels</b> in some datasets?</summary>

Variable labelling is primarily sourced from an NHS metadata API, but is not fully complete. Gaps in HES and MHSDS have been infilled from additional data dictionary sources. As part of ongoing work, we will be integrating additional sources to further complete the labelling and add value labels. We will inform users as these are updated. The approx. current variable label completeness is:
* HES, NPEX, COVIDSGSS: 100%
* MHSDS: 70-90% 
* GDPPR, CVS, CVAR: 70% 
* PCM: 40%
* DEMOGRAPHICS, CHESS, IELISA: not available.
</details>

<details>
<summary>Why do some variable labels include the phrase <b>‘label added by UK LLC’</b>?</summary>

A minority of the variables in NHSE datasets flowed into the UK LLC without labels. Where possible, UK LLC has infilled these from NHSE documentation available online. Where we have been unable to find variable labels, but where labels can be confidently inferred from the variable name, we have added them to the NHSE datasets. These labels derived from variable names include the phrase ‘label added by UK LLC’.
</details>

<details>
<summary>What <b>version</b> of NHS England data was I provisioned?</summary>

NHS England data provisioned to projects are locked to a specific extract. This is done using the extract_date variable found in the dataset, and is the date the data was extracted at NHS England.  

All projects are 'locked' to an NHS quarterly extract as well to as a fixed table, which controls permissions/consent. This locking is done based on the time of first provision of each project in the TRE. This locking prevents participant numbers from fluctuating during the course of a project (if, for example, more data or more participants are added to the TRE).  

Each fixed table is logged as a quarterly [**'freeze'**](../../ukllc_key_facts/Sample/UKLLC_sample.md). The freeze number, and freeze date, is provided in the 'documentation' folder in each TRE project space.
</details>

<details>
<summary>Why are some NHS England variables <b>excluded or encrypted</b>?</summary>

Prior to upload to the UK LLC TRE database, NHS data are assessed for disclosure risk. During this process, variables can be excluded from the upload if they are deemed to be disclosive. In cases where the variable has utility in an encrypted form, the variable is encrypted rather than excluded and an ***_e*** suffix is added to the end of the variable name e.g. *lsoa* ***_e***. Encryption is usually applied to variables which are, or provide, proxies for location information smaller than region. 
</details>

<details><summary>What does <b>nic_number</b> refer to?</summary>
The NIC number refers to UK LLC's Data Sharing Agreement (DSA) with NHSE. Particpants have different NIC numbers in the NHSE datasets depending on the legal basis for linking their data (consent or Section 251).  Participants who are in more than one LPS may have duplicated NHSE records if one study uses consent as its legal basis and one uses Section 251. UK LLC is working on a robust methodology for deduplicating participants who appear in multiple cohort studies, and will make this information available in Guidebook as soon as it is available.
</details>