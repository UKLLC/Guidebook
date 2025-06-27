
# UK LLC database design
>Last modified: 27 Jun 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The UK LLC database ...... </strong></div>  
<br>

>##  Summary: 
>* Datasets in the UK LLC TRE are made available to researchers in the same format as they are provided to UK LLC by the data owners. The content and structure of each dataset in the TRE is determined by the data owners (LPS or linked data source). These are stored in the TRE Database organised by schema, with **one schema for each data owner** (e.g. ALSPAC, NHSE). Datasets are made available to researchers as **MS SQL Server** database Views.  
<br>
>* **The UK LLC naming convention** ensures the name of each View includes the project number, source/owner, dataset name, version number, and the date the file was last updated. For example, Views provisioned to project LLC_9999 might include:  
•	LLC_9999.CORE_denominator_file1_v0001_yyyymmdd  
•	LLC_9999.LPSNAME_COVID_W1_v0001_yyyymmdd  
•	LLC_9999.nhsd_HESAPC_v0003<sup>1</sup>  
•	LLC_9999.RETURNED_sociodemo_harmonised_selfreport_v0004_yyyymmdd<sup>1</sup>   
<br> 
<sup>1</sup>The schema 'nhsd' incorporates linked data from NHS England (previously called NHS Digital)

**Dates and updates**  
The date suffix (yyyymmdd) for each View, refers to the date on which the data were shared with UK LLC, rather than the date on which the data were collected. Many LPS datasets contain variables indicating the date of data collection (e.g. questionnaire completion, clinic visit), which may pre-date the LPS joining UK LLC.

**Data freezes**  
To account for changes in the LPS samples (e.g. when participants withdraw from studies or update their linkage preferences), UK LLC implements a quarterly **'freeze'** based on the most recent information provided by LPS. This freeze is linked to all datasets requested by a researcher, enabling up-to-date permission filtering. Researchers are informed which freeze has been applied to their research data by a freeze information file dropped into their TRE project area. There is more information on UK LLC’s freeze process in the introduction: https://guidebook.ukllc.ac.uk/docs/introduction/sample/ukllc_sample#. 

**Refreshes**  
Linked data providers aim to provide updates to UK LLC at least twice a year. Whenever updates are received, the summary in this Guidebook will be updated and researchers working in the TRE notified by email.

New or updated datasets are not automatically shared with ongoing projects, because doing so would potentially alter the sample size. An exception is made to this rule in cases of disclosure risk being identified retrospectively or data deletion requests from data owners.  If researchers would like their project data to be updated to include the most recent records (either LPS or linked data), they should submit a project amendment via the UK LLC [amendment process](../../user_guide/RequestingAnAmendment.md). It should be noted that requesting new data for a project will update all the project’s provisioned datasets to the most recent figures.

