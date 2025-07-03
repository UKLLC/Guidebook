# Harmonised (standardised) demographic variables
>Last modified: 03 Jul 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created a range of harmonised demographic measures applicable to all LPS</strong></div>  

## 1. Introduction  
LPS collect data in different ways, using different variable names and values, so it is not always easy to make comparisons between studies. To enable UK LLC’s partners and data users to understand the profile of the UK LLC resource as a whole, UK LLC standardises (‘harmonises’) some key characteristics across all LPS.  

**Harmonised variables for sex, gender, year of birth, and ethnic group are available**  

>N.B. UK LLC has not changed the original LPS data for these variables. The new variables are available as harmonised datasets which researchers can request in addition to LPS and linked data.  

## 2. Structure of datasets
There are two harmonised datasets (a 'full' and a 'reduced' version), both in long format. Table 1 shows the variables available in the datasets. The difference between the two datasets is outlined in [Section 4](#4-the-full-and-reduced-datasets) below.

**Table 1: variables in the harmonised demographic datasets**  
| Variable name | Variable description |  
|---|---|
| LLC_xxxx_stud_id | Individual identifier (unique to each project in the TRE) |
| cohort | LPS name |
| source | LPS dataset holding the original demographic variable(s) for each participant (e.g. ALSPAC_wave1y) |
| object | Label indicating which of the harmonised variables is represented by the value (e.g. llc_sex, llc_gender) |
| value | Numeric value for each of the objects |
| label | Description of what each of the values represents |  
| llc_timestamp | Date (month and year) on which the information was provided by the participant to the LPS |  

## 3. UK LLC's harmonisation process
Detailed information on how UK LLC generated the derived, demographic variables is available via the links below. These also include downloadable files which show the mapping of LPS data to UK LLC's harmonised variables.  
| Additional information on: |
|:---:|
[Sex](../../UKLLC_generated/README/sex_info.md) | 
[Gender](../../UKLLC_generated/README/gender_info.md) | 
[Ethnicity](../README/ethnicity_info.md) |
[Year of birth](../../UKLLC_generated/README/yob_info.md) | 
<br>

The level of detail provided by LPS about participants' **ethnic group** varies greatly. Consequently, UK LLC has harmonised data on ethnic group into three separate, hierarchical variables made up of six, five and two categories.

For **gender**, two hierarchical categories have been created. This enables the retention of the most detailed gender information while not losing data from LPS that collected less precise information. 
 
>**NOTE**  
>For some variables included in the harmonised datasets, it may be that UK LLC does not have the complete list of response options available to LPS participants. Where this is the case, the absence of a possible option (e.g. ‘prefer not to answer’) from the responses presented does not mean that option was not available to LPS participants. All that can be inferred is that, if that option was available, it was not selected by anyone included in the datasets shared with UK LLC.

## 4. The full and reduced datasets
### **The full dataset** <span style="color:red">[add link to dataset page]</span>  
This retains every relevant response provided by participants. E.g. if a participant was asked to confirm their ethnic group on five separate occasions, then that individual will have five occurrences of ethnicity in the harmonised dataset.  

The variables (objects) for which different levels of granularity can be derived, i.e. ethnicity and gender, are provided at the most detailed level available for each contributing dataset.  

**Missing data** are retained where a participant was included in a data sweep (i.e. other information is available about them in a dataset) but they did not answer the question(s) about one or more aspects of their sex, gender or ethnic group. This missing data is separate, and additional, to responses recorded as missing (e.g. 'prefer not to answer', 'no response').
Researchers should be mindful of the fact that, for a single participant, data could be missing - either through omission or through a participant selecting e.g. 'don’t know' from response options - for multiple waves of data collection. 

>**Researchers are encouraged to use the full dataset**:  
>* to investigate whether a participant’s self-reported demographic characteristics have changed over time  
>* to ensure that their research refers to participants' self-reported characteristics as recorded at a time point pertinent to the research question


### **The reduced dataset** <span style="color:red">[add link to dataset page]</span>  
This retains only the most recent response provided by participant for relevant variable.  

 Where different levels of granularity can be derived for variables (objects), i.e. ethnic group and gender, all possible levels of the variables have been derived and included in the dataset.

**Missing data** have been removed from the reduced dataset.

>**Researchers are encouraged to use the reduced dataset**:  
>* to have the most recent, valid, definition of a participant’s demographic characteristics 
>* to have comparable data on ethnicity and gender for the maximum number of participants
>* to be able to compare LPS data with linked data from NHS England using the <span style="color:red">[NHSE demographic dataset]</span>

## 5. The future  
Whenever a new LPS joins UK LLC, demographic variables provided by the LPS will be harmonised and added to the UK LLC demographic datasets. These Guidebook pages will be updated to reflect these changes.
