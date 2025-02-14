# NHSD LSOA11

>Last modified: 25 Jul 2024


CORE_nhsd_lsoa11_v0000_YYYYMMDD has one row per health interaction where the project has selected the LPS and where participant permissions are in place. The indicator picks from the following NHS datasets where Lower Super Output Area 2011 (LSOA11) is routinely available:
* General Practice Extraction Service (GPES) Data for Pandemic Planning and Research (GDPPR)
* HES Accident & Emergency (HESAE)
* HES Admitted Patient Care (HESAPC)
* HES Outpatients (HESOP).

LSOA11 is encrypted in the dataset, because geographical units smaller than region are not permitted ‘in-the-clear’ in the UK LLC TRE. The dataset contains the following variables:
* record_date: date stamp from health record 
* lsoa11cd_e: encrypted LSOA 2011 from health record
* origin: NHS dataset the LSOA originated from 
This dataset can be linked to CORE_LSOA11_geo_indicators (documented in next subsection) to add in geographical indicator variables asscoiated with encrypted LSOA11 (lsoa11cd_e).
