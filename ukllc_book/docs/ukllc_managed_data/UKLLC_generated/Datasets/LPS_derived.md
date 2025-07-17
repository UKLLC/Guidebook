# LPS derived datasets
>Last modified: 17 Jul 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC is creating a range of derived datasets applicable to all Longitudinal Population Studies (LPS).</strong></div>  

## Introduction  
Longitudinal Population Studies (LPS) collect data in different ways, using different variable names and values, so it is not always easy to make comparisons between them. To help researchers understand the profile of the UK LLC resource as a whole, UK LLC standardises (‘harmonises’) key characteristics about participants across all partner LPS. UK LLC has so far harmonised the following variables: **sex, gender, year of birth and ethnic group**. These harmonised variables are available as either the full or reduced version of the LPS harmonised demographic dataset. UK LLC anticipates datasets with information about LPS participants' highest **education qualifications** to be available in late 2025.
 
 
>**Note** UK LLC has not changed the original LPS data for these variables.  


## Overview of LPS derived datasets

 Dataset | Dataset Name |Grouping| Data Available in TRE | Data Owner |
|---|---|---|---|---|
| [TBC - link] |LPS_harmonised_demog_full|Demographic |TBC | UK LLC |
| [TBC - link] |LPS_harmonised_demog_reduced|Demographic |TBC | UK LLC |

## Full vs. reduced demographic dataset
### Full dataset   
The [**full dataset**](../Datasets/LPS_derived/demo_harmonised_full.md) retains every relevant response provided by participants, e.g. if a participant was asked to confirm their ethnic group on five separate occasions, then that individual will have five occurrences of ethnicity in the dataset.  
>Researchers are encouraged to use the **full dataset**:  
>* To investigate whether a participant’s self-reported demographic characteristics have changed over time  
>* To ensure that their research refers to participants' self-reported characteristics as recorded at a time point pertinent to the research question.  
<br>

### Reduced dataset  
The [**reduced dataset**](../Datasets/LPS_derived/demo_harmonised_reduced.md) retains only the most recent response provided by a participant for each variable.  


>Researchers are encouraged to use the **reduced dataset**:  
>* To have the most recent, valid, definition of a participant’s demographic characteristics 
>* To have comparable data on ethnicity and gender for the maximum number of participants
>* To be able to compare LPS data with data from NHS England using the [**NHSE demographics dataset**](../../../linked_health_data/NHS_England/Registration%20datasets/DEMOGRAPHICS/DEMOGRAPHICS.ipynb).  
<br>

## Harmonisation methodology
Detailed information on how UK LLC generated the harmonised demographic dataset is available via the links below. These include downloadable files which show the mapping of LPS data to UK LLC's harmonised variables.  
| Detailed information on: |
|:---:|
[Sex](../../UKLLC_generated/README/sex_info.md) | 
[Gender](../../UKLLC_generated/README/gender_info.md) | 
[Year of birth](../../UKLLC_generated/README/yob_info.md) 
[Ethnicity](../README/ethnicity_info.md) |
<br>  

The level of detail provided by LPS about participants' **ethnic group** varies greatly. Consequently, UK LLC has harmonised data on ethnic group into three separate, hierarchical variables made up of six, five and two categories.

For **gender**, two hierarchical categories have been created. This enables the retention of the most detailed gender information while not losing data from LPS that collected less precise information. 
  
>**Note** For some variables included in the harmonised datasets, it may be that UK LLC does not have the complete list of response options available to LPS participants. Where this is the case, the absence of a possible option (e.g. ‘prefer not to answer’) from the responses presented does not mean that option was not available to LPS participants. All that can be inferred is that, if that option was available, it was not selected by anyone included in the datasets shared with UK LLC.
