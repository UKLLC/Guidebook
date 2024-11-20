# Working with NHS England data
>Last modified: 20 Nov 2024

<details>
<summary>Does UK LLC check the accuracy of health records?</summary>

No, the UK LLC Data Team can only see de-identified records in the TRE and does not amend any participant data. The UK LLC Data Team only performs the following data curation tasks:
- Clean and deduplicate data, dataset names and structures to enable data provisioning in an efficient manner while maintaining data integrity.
- Load and integrate variable and value labelling, where available from the NHS API and other web sources, into master metadata tables.
- Run the automated disclosure control risk assessment and manually review all flagged risks.
</details>
<br>
<details>
<summary>Why are some NHS E datasets missing variable or value labels?</summary>

Variable labelling is primarily sourced from an NHS metadata API, but is not fully complete. Gaps in HES and MHSDS have been infilled from additional data dictionary sources. As part of ongoing work, we will be integrating additional sources to further complete the labelling and add value labels. We will inform users as these are updated. Approx current variable label completeness:
* HES, NPEX, COVIDSGSS: 100%
* MHSDS: 70 - 90% 
* GDPPR, CVS, CVAR: 70% 
* PCM: 40%
* DEMOGRAPHICS, CHESS, IELISA: not available.
</details>
<br>
<details>
<summary>What version of NHS E data was I provisioned?</summary>

NHS E data provisioned to projects are locked to an extract. This is done using the extract_date variable found in the dataset. This is the date the data was extracted at NHS E. All projects are locked to an NHS quarterly extract as well as a fixed table, which controls permissions/consent. This is done based on time of first provision. This prevents participant numbers from fluctuating during the course of the project.
</details>
<br>
<details>
<summary>Why are some NHS E variables excluded or encrypted?</summary>

Prior to upload to the UK LLC TRE database, NHS data are disclosure risk assessed. During this process variables can be excluded from the upload if they are deemed to be disclosive. In cases where the variable has utility in an encrypted form, the variable is encrypted rather than excluded and an ***_e*** suffix is added to the end of the variable name e.g. *lsoa* ***_e***. Encryption is usually applied to variables which are or provide proxies for location information smaller than region/strategic health authority. 
</details>
<br>
<details>
<summary>Why are records limited by codelists?</summary>

HES data provisions are limited by medical codes provided by researchers. This means that the extent to which specific coding is used in these data is important. For example, you may observe more records in your HESAPC (admitted patients) than in HESOP (outpatients) despite the national volume of HESOP being typically ~5x greater per year. This is because HESAPC has meaningful diagnoses codes consistently provided. Whereas with HESOP often generic codes are given. This means when codes are matched, fewer hits will be made on datasets with non-specific codes and thus fewer records will be included in your minimised project-specific view. Examples of these include “R69=Not known” for diagnoses and “X997=Not known” for operations. These non-specific codes are used extensively in HESOP, but far less so in HESAPC.  

Going forward, we are looking at changing the way we make linked health records available, by initially making available unfiltered views to researchers (with particularly sensitive records removed) rather than asking for codelists upfront. This will allow codelists to be developed whilst working with the data, but will also allow exploration of records which do not have specific codes assigned.
</details>
<br>
<details>
<summary>What do “_OTR”, “_ACP” and “_MAT” suffixes relate to in HES data?</summary>

* “_OTR” is short for ‘Other’ and is an extension of the HES record. There should be a 1:1 relationship between the main record found in HESAPC for example and its extension in HESAPC_OTR
* “_ACP” is short for ‘Augmented care period’. This was collected from 1997–2006 and was replaced by HESCC (critical care in 2008)
* “_MAT” is short for ‘Maternity’ and contains variables associated with maternity related admissions.  

See below for data and sub table lookup relationships. Note: HESCC is a subset of HESAPC 

<img src="../../images/user_guide/Picture2.png" width="400"/>  

</details>
<br>


<details>
<summary>How to link “HESCC”, “..._OTR”, “..._ACP”, “..._MAT” data to their main record?</summary>

These sub tables do not contain an individual-level identifier. Therefore, they need to be linked to the main HESAPC/HESOP/HESAE. See below for the linkage keys for each dataset: 

<img src="../../images/user_guide/Picture3.png" width="400"/>

</details>
<br>

<details>
<summary>How to find test results in covid datasets?</summary>

* **NPEX and IELISA**: Use testresult variable. Result is SNOMED (SCT) coded. There are 6 codes used e.g. “SCTID: 1240581000000104”: “Severe acute respiratory syndrome coronavirus 2 detected (finding)”. A lookup will be available shortly in the TRE with linkage guidance.
* **COVIDSGSS**: This dataset does not contain a test results field. We are awaiting confirmation from NHS England about how to interpret the presence of records in this dataset.
</details>
<br>
<details>
<summary>How can I request additional NHS E data for my project?</summary>

Requests for new data should be submitted via an amendment to UK LLC. You may apply for additional data from already approved LPS, data from additional LPS, and/or additional linked data. N.B. each type of data [**amendment**](https://guidebook.ukllc.ac.uk/docs/user_guide/6.requestinganamendment)  requires a different level of review before being approved. 

</details>
