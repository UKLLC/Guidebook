# FAQs about working with COVID-19 datasets
>Last modified: 28 Oct 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>Answers to researchers' questions about working with linked COVID-19 datasets.</strong></div style>  
<br>

<details>
<summary>Are data on COVID-19 testing still be collected?</summary>

No, NHS England stopped receiving data from [Pillar 2](../covid_datasets/npex/npex.ipynb) (NPEX) and [SGSS](../covid_datasets/covidsgss/covidsgss.ipynb) in 2024, and from [Pillar 3](../covid_datasets/ielisa/ielisa.ipynb) (IELISA) in 2022.
</details>

<details>
<summary>How can I find test results in <B>COVID-19</B> datasets?</summary>

* **NPEX and IELISA**: Use the variable "testresult". The result is SNOMED coded. There are 6 codes used, e.g. “SCTID: 1240581000000104”: “Severe acute respiratory syndrome coronavirus 2 detected (finding)”.
* **COVIDSGSS**: This dataset does not contain a test results field. We are awaiting confirmation from NHS England about how to interpret the presence of records in this dataset.
</details>
