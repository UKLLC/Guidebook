# FAQs about working with UK LLC-managed data
>Last modified: 19 Mar 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>Answers to researchers' questions about working with UK LLC-managed data.</strong></div style>  
<br>


<details>
<summary>Will more linked derived datasets be added to the UK LLC resource?</summary>

Once additional linked data is available (e.g. NHS Wales, HMRC), it is likely that new datasets will be derived from these and added to the TRE.
</details>

<details>
<summary>Where are the CORE datasets that UK LLC used to provision to all projects?
</summary>  

Prior to October 2025, UK LLC projects were provisioned 4 'CORE' datasets (outlined in column 1 of the table below). In response to feedback from LPS around participant permissions, and following internal review of our dataset naming conventions, these datasets were renamed and relocated into the UK LLC-managed schema as [**NHS England reference datasets**](../ukllc_managed_data/datasets/nhse_reference/nhse_reference.md).  

All projects that started before these changes, were updated to use the new naming conventions in October 2025.

| Previous dataset name | Current dataset name | Description |
|---|---|---|
| <i>CORE_denominator_file1 | [UKLLC_study_permissions](../ukllc_managed_data/datasets/nhse_reference/study_permissions.ipynb) | Cohort and linkage permission for each unique study participant | 
| <i>CORE_nhsd_presence | [UKLLC NHSE_patient_service_usage](../ukllc_managed_data/datasets/nhse_reference/nhse_patient_service_usage.ipynb) | Count of participants' appearances and last usage for NHSE datasets |
| <i>CORE_nhsd_derived_indicator | [UKLLC_nhse_patient_demo_mortality](../ukllc_managed_data/datasets/nhse_reference/nhse_patient_demo_mortality.ipynb) | Derived key demographic variables for participants with linkage to NHSE data | 
| <i>CORE_nhsd_lsoa11 | [UKLLC_nhse_lsoa11_dataset_mapping](../ukllc_managed_data/datasets/nhse_reference/nhse_lsoa11_dataset_mapping.ipynb) | LSOA11 lookup for participants with linkage to NHSE data | 

<br>
</details><br>

>**Further information will be added to this page as the UK LLC generated datasets become more widely available.**  
> Any queries about these datasets should be emailed to [support@ukllc.ac.uk](mailto:support@ukllc.ac.uk).

