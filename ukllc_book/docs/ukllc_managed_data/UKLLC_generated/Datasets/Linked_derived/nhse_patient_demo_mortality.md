# NHS England Patient Demo Mortality
>Last modified: 22 Aug 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created a demographic and mortality dataset dervived from NHS England datasets</strong></div>  

## What does the dataset include?
'UKLLC_nhse_patient_demo_mortality_v0000_YYYYMMDD' (formerly known as 'CORE_derived_indicator_v0000_YYYYMMDD') contains the most recent and most reliable record for certain key demographic variables sourced from NHS data sources in the UK LLC database. There is one row per participant. The dataset will include all **NHS England** linked participants who have permissions from the longitudinal population studies selected and approved as part of your project. The dataset is built from the following datasets and preferentially uses data in this order where complete:
1. Demographics
2. General Practice Extraction Service (GPES) Data for Pandemic Planning and Research (GDPPR)
3. HES Admitted Patient Care (HESAPC)
4. HES Outpatients (HESOP)
5. HES Accident & Emergency (HESAE).

Currently included are the following variables:
* sex
* Deceased: from the NHS England Mortality dataset
* Date of death: from the NHS England Mortality dataset
* ethnic: NHS England ethncity coding system, see values table for coding lookup
* dob_year_month: year and month of birth 
* last_seen_date: last date record in any NHS England dataset.

## What does the dataset enable me to do?
* Ascertain whether a participant is alive or dead based on NHSE Mortality records and see their recorded date of death 
* Quickly retrieve basic demographic information such as Sex, Ethnicity and Age (via date of birth) of participants from their NHSE record 
* See the date when a participant last used an NHS England service
* Enables quick filtering and/or grouping of participant demographic data to be integrated into analytical pipelines
