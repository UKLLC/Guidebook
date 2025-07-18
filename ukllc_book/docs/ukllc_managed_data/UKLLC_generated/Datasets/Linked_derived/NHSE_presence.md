# NHS England presence dataset
>Last modified: 18 Jul 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created an NHS England presence dataset ...</strong></div>  
<br>

COPIED from the live version of Guidebook - needs to be updated asap

CORE_NHSD_Presence_v0000_YYYYMMDD contains the number of appearances and the date of the most recent appearance for each participant for each available NHS data source in the UK LLC database. There is one row per participant. The table also includes a ‘last seen date’ for each participant as the most recent record across all NHS data sources. Some NHS data sources do not include record dates. Therefore the presence table may include the counts of each participant’s appearances in a data source without an associated date. 

NHSD_presence can be used to identify a project's control group or denominator by comparing LPS participants' presence in NHS data sources against the NHS data provisioned to a project. For datasets that have to be minimised by codelists<sup>1</sup>, this comparison will establish which participants appear in the dataset but are not included in the provisioned data.  

<sup>1</sup> Codelists are required for the following NHS England datasets:

 * [HES](../HES%20datasets/HES_intro.md) (Hospital Episode Statistics)
 * [GDPPR](../../linked_health_data/NHS_England/Primary_care_datasets/primary_intro.md) (General Practice Extraction Service (GPES) Data for Pandemic Planning and Research)
 * [Cancer registrations](../Registration%20datasets/CANCER/CANCER.ipynb)
 * [PCM](../../linked_health_data/NHS_England/Other%20datasets/PCM/PCM.ipynb) (Primary Care Medicines)
