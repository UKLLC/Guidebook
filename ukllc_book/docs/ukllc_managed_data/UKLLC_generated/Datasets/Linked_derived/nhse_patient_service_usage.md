# NHS England Patient Service Usage
>Last modified: 22 Aug 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created an summary dataset of patient service usage using NHS England data</strong></div>  
<br>

## What does the dataset include?
The dataset 'UKLLC_nhse_patient_service_usage_v0000_YYYYMMDD' (formerly know as 'CORE_NHSD_Presence_v0000_YYYYMMDD') contains the number of appearances and the date of the most recent appearance for each participant for each available **NHS England** data source in the UK LLC database. There is one row per participant. The table also includes a ‘last seen date’ for each participant as the most recent record across all NHS data sources. Some NHS data sources do not include record dates. Therefore the presence table may include the counts of each participant’s appearances in a data source without an associated date. The dataset will include all **NHS England** linked participants who have permissions from the longitudinal population studies selected and approved as part of your project.

## What does the dataset enable me to do?
The dataset can be used to identify a project's control group or denominator by comparing LPS participants' overall usage of **NHS England** services against the usage apparent in the data provisioned to a project. For datasets that have to be minimised by codelists<sup>1</sup>, this comparison will establish which participants appear in the dataset but are not included in the provisioned data. Further to this, to what extent do the codelist definitions provided cover the overall participant usage of a service. 

<sup>1</sup> Codelists are required for the following NHS England datasets:

 * [HES](../../../../linked_health_data/NHS_England/HES%20datasets/Hospital_intro.md) (Hospital Episode Statistics)
 * [GDPPR](../../../../linked_health_data/NHS_England/Primary_care_datasets/GDPPR/understanding_GDPPR.md) (General Practice Extraction Service (GPES) Data for Pandemic Planning and Research)
 * [Cancer registrations](../../../../linked_health_data/NHS_England/Registration%20datasets/CANCER/CANCER.ipynb)
 * [PCM](../../../../linked_health_data/NHS_England/Primary_care_datasets/PCM/PCM.ipynb) (Primary Care Medicines)
