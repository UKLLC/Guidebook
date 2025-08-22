# NHS England LSOA11 Dataset Mapping
>Last modified: 22 Aug 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created a LSOA11 mapping table enabling linkage of lsoa11 level data such as IMD to NHS England records</strong></div>  

## What does the dataset include?
**UKLLC_nhse_lsoa11_dataset_mapping_v0000_YYYYMMDD** has one row per health interaction where the project has selected the LPS and where participant permissions are in place. The indicator picks from the following NHS datasets where **Lower Super Output Area 2011 (LSOA11)** is routinely available:
* General Practice Extraction Service (GPES) Data for Pandemic Planning and Research [**(GDPPR)**](../../../../linked_health_data/NHS_England/Primary_care_datasets/GDPPR/GDPPR.ipynb)
* HES Accident & Emergency [**(HESAE)**](../../../../linked_health_data/NHS_England/HES%20datasets/AE/HESAE.ipynb)
* HES Admitted Patient Care [**(HESAPC)**](../../../../linked_health_data/NHS_England/HES%20datasets/APC/HESAPC.ipynb)
* HES Outpatients [**(HESOP)**](../../../../linked_health_data/NHS_England/HES%20datasets/OP/HESOP.ipynb)

**LSOA11** is encrypted in the dataset, because geographical units smaller than English region or devolved nation are not permitted ‘in-the-clear’ in the UK LLC TRE. The dataset currently contains the following variables:

* **record_date**: date stamp from health record
* **lsoa11cd_e**: encrypted LSOA 2011 from health record
* **origin**: NHS England dataset the LSOA 2011 originated from. 

## What does the dataset enable me to do?
The **UKLLC_nhse_lsoa11_dataset_mapping** dataset can be linked to placed-based datasets at the LSOA-level such as IMD e.g. **PLACE_IMD_XXX_v0000_YYYYMMDD**. This will add in geographical indicator variables associated with encrypted **LSOA11** (lsoa11cd_e) from health records. See the additional information provided for the [**IMD dataset**](../../../../linked_geo_data/population_datasets/IMD/Understanding_IMD.md) for an example of how to do this.