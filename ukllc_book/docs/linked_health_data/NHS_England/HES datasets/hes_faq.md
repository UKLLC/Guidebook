# FAQs about HES data
>Last modified: 03 Dec 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>Answers to researchers' questions about working with linked hospital data.</strong></div style>  
<br>

<details>
<summary>Does HES data include any information about medicines prescribed in hospitals?</summary>

No, HES does not contain any information about medications. Data on prescriptions can be found in the **Primary Care Medicines** ([PCM](../Primary_care_datasets/PCM/PCM.ipynb)) dataset which includes information about prescriptions issued in general practice, community and hospital clinics, and by dentists and community nursing services.

</details>

<details>
<summary>What impact do the <B>different levels of coding</B> have on HES data?</summary>
The extent to which specific coding is used in HES data is important. For example, you may observe more records in your HESAPC (admitted patients) than in HESOP (outpatients) dataset, despite the national volume of HESOP records being typically ~5x greater per year. This is because HESAPC has meaningful diagnoses codes consistently provided, whereas generic codes are more often used in HESOP. This means when codes provided by a researcher are matched with HES data in the TRE, fewer matches ('hits') will be made on datasets with non-specific codes. Thus fewer records will be included in the project.  
<br>
Examples of non-specific codes include “R69=Not known” for diagnoses and “X997=Not known” for operations. These are used extensively in HESOP, but far less so in HESAPC.  

UK LLC is considering the way it makes linked health records available, by initially making unfiltered views available to researchers (with particularly sensitive records removed) rather than asking for codelists upfront. This will allow codelists to be developed whilst working with the data, but will also allow exploration of records which do not have specific codes assigned.
</details> 

<details>
<summary>What do the <B><i>_ACP</i> and <i>_MAT</i> </B> suffixes refer to in HES data?</summary>

* *_ACP* is short for **Augmented Care Period**. This dataset was collected from 1997–2006. It was replaced by HESCC (critical care) in 2008
* *_MAT* is short for **Maternity** and contains variables associated with maternity-related admissions.  

See below for data and sub table lookup relationships. Note: HESCC is a subset of HESAPC 

<img src="../../../images/user_guide/Picture2.png" width="400"/>  

</details>

<details>
<summary>How can I link <B>_ACP</B>, <B>_MAT</B> and <B>HESCC</B> data to their main record?</summary>

These sub tables do not contain an individual-level identifier. They therefore need to be linked to the main HESAPC / HESOP / HESAE datsets. See below for the linkage keys for each dataset: 

<img src="../../../images/user_guide/Picture3.png" width="400"/>

</details>