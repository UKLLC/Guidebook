# Study Permissions
>Last modified: 22 Aug 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created a study permissions dataset which serves as the UK LLC denominator or 'spine'</strong></div>  
<br>  

The **study permissions** dataset, formerly know as the **denominator** dataset, incorporates all participants across all LPS. 
Each project in the TRE is automatically provisioned a file named 'UKLLC_study_permissions_v0000_YYYYMMDD' (formerly known as 'CORE_denominator_file1_v0000_YYYYMMDD').  

The date in the dataset name relates to the "File 1" [**freeze**](../../../../ukllc_key_facts/Sample/UKLLC_sample.md) (permissions) to which each project is fixed. Participant permissions are correct and applied to each dataset as of this date. 

## What does the study permissions dataset include?
* one row per UK LLC participant 
* the name of the LPS to which the participant belongs
* all UK LLC configurable permissions for the different domains of data (e.g. NHS England, place-based). 
* the date the participant joined the UK LLC


## What does the study permissions dataset enable me to do?
* calculate linkage rates (when joined to linked datasets)
* contextualise LPS participants within UK LLC in relation to the LPS datasets. 

## Section 251 vs consent
When considering NHS England and Wales linkage permission flags *nhs_e_linkage_permission* and *nhs_w_linkage_permission* these have a second aspect to consider controlled by the *national_opt_out* flag. When *national_opt_out* is set to "0", this means that the participant has set **explicit consent** set with their LPS. Where *national_opt_out* is set to "1", this means that the participant has flowed for linkage under **Section 251**. Participants who flow under **Section 251** are filtered for **National Data Opt-Out**. If the participant has set a **National Data Opt-Out**, UK LLC will not receive their records. However, data on which participants have this set does not flow to UK LLC, and there are other reasons for participant data not flowing, such as failed linkage due to quality of identifiers.
<br>


