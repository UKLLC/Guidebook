
# UK LLC database design
>Last modified: 08 Jul 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The UK LLC database holds all LPS and linked data available to researchers as a vast collection of SQL tables.</strong></div>

##  Summary

> The UK LLC Database, named *UKSERPUKLLC* in the TRE, is a **relational database** that contains all datasets provided to us by our partner data owners as **SQL** tables. These tables are organised by different database schemas, where **one schema corresponds to each each data owner** (e.g. ALSPAC, NHSE, SABRE). The main software used in the TRE to manage and explore the database is **Microsoft SQL Server management Studio (SSMS)**.

A **relational database** refers to one that stores and organises data in a structured format using tables of rows and columns that relate to one another. In the context of the UKSERPUKLLC database, the unique ID of the participants, i.e. study_id_e (LPS data) or cohortkey_e (linked NHS England health records) are the key variables (columns) that allow for relationships between the tables to be established. In other words, almost all tables of LPS data will have the study_id_e column, thereby allowing multiple data points to be held across many tables for a given study participant. For example, the table [UKHLS].[a_indresp] contains questionnaire data for UKHLS participants from the study’s first wave in 2009-11, while [UKHLS].[l_indresp] holds questionnaire data from the study’s twelfth wave in 2020-22. However, both tables relate to each other with a common study_id_e column which corresponds to the study participants. Tables containing LPS data (via study_id_e) and linked health records (via cohortkey_e) are also related to each other owing to the linking process, as UKSERPUKLLC contains a table called [Linkage].[File4], which maps each study participant (study_id_e) to their unique health record identifier (cohortkey_e). Further information about the linkage process with NHS England records can be found here.

**SQL** stands for Structured Query Language and is a standardized programming language widely used to organise and query relational databases. It allows users of the language to *retrieve*, *insert*, *update* and *delete* data using declarative syntax. More specifically, **T-SQL** (Transact-SQL) is Microsoft’s extension to SQL, used in SQL Server. It includes extra features that make it easier to perform more advanced tasks such as creating user-defined functions and error handling.

Researchers in the TRE will almost exclusively be *retrieving* data from the database, with SELECT statements. e.g. to retrieve all records from a specific ALSPAC view:

```
SELECT * FROM [ALSPAC].[DATASET_VIEW]
```

So, while researchers in the TRE will not be inserting or updating data to *UKSERPUKLLC*, they will be retrieving data from the **Views** built for their research projects, and so some familiarity with SQL is recommended. **Note:** If any datasets arising from research in the TRE needs to be stored, we recommend saving them as .csv files either in the P:\ drive or the project folder in the S:\ drive for later use.

**Microsoft SQL Server management Studio (SSMS)** is a free and powerful program used to communicate with and manage the UK LLC database. With it, researchers can view and explore the data provisioned to them. When a researcher is set up in the TRE, SSMS is made available by default as the primary tool to access the data provisioned to their projects, using “views” (see below).

##  Provisioning Data to Researchers as Views

Rather than provisioning datasets by granting direct read access to the tables, they are made available to researchers as Views in the database. This allows us to adhere to principes of *Data Minimization*, where researchers only have access to the data they need for their specific research question. Moreover, datasets in the UK LLC TRE are made available to researchers in the same format as they are provided to UK LLC by the data owners.

**The UK LLC naming convention** ensures the name of each View includes the project number, source/owner, dataset name, version number, and the date the file was last updated. For example, Views provisioned to project LLC_9999 might include:
•	LLC_9999.CORE_denominator_file1_v0001_yyyymmdd
•	LLC_9999.LPSNAME_COVID_W1_v0001_yyyymmdd
•	LLC_9999.nhsd_HESAPC_v0003<sup>1</sup>
•	LLC_9999.RETURNED_sociodemo_harmonised_selfreport_v0004_yyyymmdd<sup>1</sup>
<br>
<sup>1</sup>The schema 'nhsd' incorporates linked data from NHS England (previously called NHS Digital)

**Dates and updates**
The date suffix (yyyymmdd) for each View, refers to the date on which the data were shared with UK LLC, rather than the date on which the data were collected. Many LPS datasets contain variables indicating the date of data collection (e.g. questionnaire completion, clinic visit), which may pre-date the LPS joining UK LLC.
