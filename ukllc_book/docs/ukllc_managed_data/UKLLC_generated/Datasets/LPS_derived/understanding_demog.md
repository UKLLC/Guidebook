# Understanding harmonised (standardised) demographic variables
>Last modified: 02 Jul 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created a range of standardised (harmonised) demographic measures applicable to all LPS</strong></div>  

## 1. Introduction  
LPS collect data in different ways, using different variable names and values, so it is not always easy to make comparisons between studies. To enable UK LLC’s partners and data users to understand the profile of the UK LLC resource as a whole, UK LLC standardises (‘harmonises’) some key characteristics across all LPS.  

Currently available are harmonised variables for LPS participants’:  
* Sex  
* Gender
* Year of birth (as a proxy for age)  
* Ethnic group  
<br>
>N.B. UK LLC has not changed the original LPS data for these variables. The new variables are available as harmonised datasets which researchers can request in addition to LPS and linked data.  

## 2. Structure of datasets
The harmonised datasets are in long format. Table 1 shows the variables available in the datasets. More details on how the objects and values have been generated are on the pages for sex, gender and ethnicity.

**Table 1**  
| Variable name | Variable description |  
|---|---|
| LLC_xxxx_stud_id | Individual identifier (unique to each project in the TRE) |
| cohort | LPS name |
| source | LPS dataset holding the original demographic variable(s) for each participant (e.g. ALSPAC_wave1y) |
| object | Label indicating which of the harmonised variables is represented by the value (e.g. llc_sex, llc_gender) |
| value | Numeric value for each of the objects |
| label | Description of what each of the values represents |  
| llc_timestamp | Date (month and year) on which the information was provided by the participant to the LPS |  

## 3. Decision-making in UK LLC's harmonisation processes
Supplementary information on how the sex, gender, year of birth, and ethnicity variables have been harmonised by UK LLC are available here:

>[Sex](../../UKLLC_generated/README/sex_info.md)  
>[Gender](../../UKLLC_generated/README/gender_info.md)  
>[Year of birth](../../UKLLC_generated/README/yob_info.md)  
>[Ethnicity](../README/ethnicity_info.md)  


**These variables are available as single datasets in two formats:**  

### Full version of the dataset [link to dataset page]
The full dataset is in long format, retaining every relevant response provided by participant, e.g. if a participant was asked to confirm their ethnic group on five separate occasions, then that individual will have five occurrences of ethnicity in the harmonised dataset. For each occurrence of the value (indicated by the variable ‘object’), the most detailed available ethnicity grouping is provided.  
<br>
**Missing values**  
Participants are retained in the dataset if they were included in the dataset uploaded by the LPS irrespective of whether they responded to the question. Where a participant was included in the original dataset, but did not provide a response of any kind (not even ‘unknown’ or ‘prefer not to say’), their response is shown as a blank cell in the full [name] dataset.  
Researchers should be mindful of the fact that, for a single participant, data could be missing - either through omission or through a participant selecting e.g. "don’t know" from response options - for multiple waves of data collection.  

### Reduced version of the dataset [link to dataset page]
<span style="color:red">Missing values
In the reduced dataset, all missing values have been removed.
Need a note about missing data, and what to do when the most recent value for a participant is missing. Where the granularity of objects is hierarchical (i.e. ethnic group, gender), all possible levels are provided for each participant. </span>  

>**NOTE**  
>For some variables included in the harmonised datasets, it may be that UK LLC does not have the complete list of response options available to LPS participants. Where this is the case, the absence of a possible option (e.g. ‘prefer not to answer’) from the responses presented does not mean that option was not available to LPS participants. All that can be inferred is that, if that option was available, it was not selected by anyone included in the datasets shared with UK LLC.

## The future  
Whenever a new LPS joins UK LLC, their demographic variables wil be harmonised and added to the UK LLC demographic datasets. These Guidebook pages will be updated to reflect these changes.
