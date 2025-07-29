# LPS harmonised demographic dataset (full)
>Last modified: 17 Jul 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created a harmonised dataset of key demographic variables across the partner LPS.</strong></div>  
<br>

## 1. Summary
The full LPS harmonised demographic dataset contains harmonised variables for **sex, gender, year of birth** and **ethnic group**.  

>**Note** UK LLC has not changed the original LPS data for these variables.  

This dataset retains **every relevant response** provided by participants. For example, if a participant was asked to confirm their ethnic group on five separate occasions, then that individual will have five occurrences of ethnicity in the harmonised dataset.  

>Researchers are encouraged to use the **full dataset**:  
>* To investigate whether a participant’s self-reported demographic characteristics have changed over time  
>* To ensure that their research refers to participants' self-reported characteristics as recorded at a time point pertinent to the research question.  

The variables (objects) for which different levels of granularity can be derived, i.e. ethnicity and gender, are provided at the most detailed level available for each contributing dataset.  

**Missing data** are retained where a participant was included in a data sweep (i.e. other information is available about them in a dataset) but they did not answer the question(s) about one or more aspects of their sex, gender or ethnic group. This missing data is separate, and additional, to responses recorded as missing (e.g. 'prefer not to answer', 'no response').

Researchers should be mindful of the fact that, for a single participant, data could be missing - either through omission or through a participant selecting e.g. 'don’t know' from response options - for multiple waves of data collection. 

## 2. Variables
<br>

| Variable name | Variable description |  
|---|---|
| LLC_xxxx_stud_id | Individual identifier (unique to each project in the TRE) |
| cohort | LPS name |
| source | LPS dataset holding the original demographic variable(s) for each participant (e.g. ALSPAC_wave1y) |
| object | Label indicating which of the harmonised variables is represented by the value (e.g. llc_sex, llc_gender) |
| value | Numeric value for each of the objects |
| label | Description of what each of the values represents |  
| llc_timestamp | Date (month and year) on which the information was provided by the participant to the LPS |  

## 3. Updates to dataset  
Whenever a new LPS joins UK LLC, demographic variables provided by the LPS will be harmonised and added to the UK LLC demographic datasets. These Guidebook pages will be updated to reflect these changes.
