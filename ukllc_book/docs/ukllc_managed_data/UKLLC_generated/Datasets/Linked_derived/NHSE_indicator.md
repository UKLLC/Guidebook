# NHSD derived indicator
>Last modified: 18 Jul 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created an NHS England derived indicator dataset ...</strong></div>  

COPIED from the live version of Guidebook - needs to be updated asap

CORE_derived_indicator_v0000_YYYYMMDD contains the most recent and most reliable record for certain key variables sourced from NHS data sources in the UK LLC database. There is one row per participant. The table sources data from the following tables and preferentially uses data from datasets in this order:
1. Demographics
2. General Practice Extraction Service (GPES) Data for Pandemic Planning and Research (GDPPR)
3. HES Admitted Patient Care (HESAPC)
4. HES Outpatients (HESOP)
5. HES Accident & Emergency (HESAE).

Currently included are the following variables:
* sex
* Deceased: from NHSD.mortality
* Date of death: from NHSD.mortality
* ethnic: NHS ethncity coding system, see values table for coding lookup
* dob_year_month: year and month of birth 
* last_seen_date: last date record in any NHS England dataset.
