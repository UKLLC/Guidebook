# Datasets derived from linked data
>Last modified: 03 Jul 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>Understanding a UK LLC project's sample and denominator</strong></div>  

## Introduction  
UK LLC has derived three datasets based predominantly on NHS England data sources. These datasets enable researchers to understand their sample and define the denominator for their project. Each of these files contains **one row per participant**.

>These datasets are made available to all researchers using linked data in the TRE.

The datasets are:
* **UK LLC Denominator**
* **NHSE Presence**
* **NHSE Derived indicator**

The datasets are updated each quarter as part of the UK LLC data [**freeze**](../../../../ukllc_key_facts/Sample/UKLLC_sample.md).

For each approved research project, these derived datasets are filtered both on the LPS selected and on individual participants' NHS England permissions. Researchers' views of these data are locked to permissions at the time of a project's first data provision.

<div style="background-color: rgba(255, 218, 185, 0.5); padding: 5px; border-radius: 5px;"><strong>The Denominator file</strong></div>  

This incorporates all participants across all LPS and serves as **UK LLC's 'spine'**. Each project in the TRE is automatically provisioned a file named: <span style="color:red"> **CORE_denominator_file1_yyyymmdd**.</span> The date in the file name refers to the freeze date. Particpant permissions are correct and applied to each LPS and linked dataset as of this date.

The denominator file includes:
* the name of the LPS to which each participant belongs
* all UK LLC configurable permissions for the different domains of data (e.g. NHS England, place-based)

It enables users to 
* calculate linkage rates (when joined to linked datasets)
* contextualise LPS participants within UK LLC in relation to LPS datasets

<div style="background-color: rgba(255, 218, 185, 0.5); padding: 5px; border-radius: 5px;"><strong>The Presence file</strong></div>  

For each NHSE data source in the UK LLC TRE, this file contains, for each participant, the number of appearances and the date of the most recent appearance in that data source. Each project in the TRE is automatically provisioned a file named: <span style="color:red">CORE_NHSD_Presence_v0000_YYYYMMDD</span>.  

The file also includes a **'last seen date'** for each participant, being the most recent record across all NHSE data sources. N.B. Some NHSE data sources do not include record dates, so the Presence file may include counts of participants' appearances in a data source without an associated date.  

The Presence file can be used to **identify a project's control group** or denominator by comparing LPS participants' presence in NHS data sources against the NHS data provisioned to a project. For datasets that have to be **minimised by codelists<sup>1</sup>**, this comparison will identify which participants appear in the full dataset in the TRE but are not included in the provisioned data.  

<div style="background-color: rgba(255, 218, 185, 0.5); padding: 5px; border-radius: 5px;"><strong>The Derived Indicator file</strong></div>  

 This file contains the most recent and most reliable record for certain key variables found in NHSE data sources in the UK LLC database. Each project in the TRE is automatically provisioned a file named: <span style="color:red">CORE_derived_indicator_v0000_YYYYMMDD</span>. The file pulls data from the following datasets and preferentially uses data from the datasets in this order:  

1. Demographics
2. General Practice Extraction Service (GPES) Data for Pandemic Planning and Research (GDPPR)
3. HES Admitted Patient Care (HESAPC)
4. HES Outpatients (HESOP)
5. HES Accident & Emergency (HESAE).

The following variables are included in the Derived Indicator file:
* sex
* Deceased: from NHSD.mortality
* Date of death: from NHSD.mortality
* ethnic: NHS ethnicity coding system
* dob_year_month: year and month of birth 
* last_seen_date: last date record in any NHS England dataset.  
<br>

>**Note 1**  
>The NHSE datasets listed below must be minimised by codelists prior to linked data being made available in the TRE.  
More information on using codelists can be found [here](../../../../linked_health_data/NHS_England/Coding/codelists.md).
> * HES (Hospital Episode Statistics)
> * GDPPR(General Practice Extraction Service (GPES) Data for Pandemic Planning and Research)
> * Cancer registrations
> * PCM (Primary Care Medicines)  
> 

