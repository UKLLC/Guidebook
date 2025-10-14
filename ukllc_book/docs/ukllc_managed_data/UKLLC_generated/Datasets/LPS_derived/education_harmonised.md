# LPS harmonised education dataset
>Last modified: 13 Oct 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created a harmonised dataset of participants' highest educational qualifications.</strong></div>  

## 1. Summary
The LPS harmonised education dataset contains a variable for LPS participants' self-reported **highest educational qualification**, plus those of their parent(s) where that information is available.  Particpants' education has been harmonised into four groupings - depending on the level of information provided. Parent(s)' qualifications have been harmonised into two groupings. Further details are on the harmonisation methodology are available [here](../LPS_derived/LPS_derived.md#harmonisation-methodology).

## 2. Variables
<br>

| Variable name | Variable description |  
|---|---|
| LLC_xxxx_stud_id | Individual identifier (unique to each project in the TRE) |
| cohort | LPS name |
| source | LPS dataset holding the original education-level or qualification variable(s) for each participant (e.g. ALSPAC_wave1y) |
| object | Label indicating which of the harmonised variables is represented by the value (e.g. llc_educ_1, llc_educ_M1) |
| value | Numeric value for each of the objects |
| label | Description of what each of the values represents |  
| llc_timestamp | Date (month and year) on which the information was provided by the participant to the LPS |  

