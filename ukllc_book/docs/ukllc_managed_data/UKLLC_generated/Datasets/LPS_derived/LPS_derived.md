# LPS derived datasets
>Last modified: 03 Nov 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC is creating a range of derived datasets applicable across Longitudinal Population Studies (LPS).</strong></div>

## Introduction
Longitudinal Population Studies (LPS) collect data in different ways, using different variable names and values, so it is not always easy to make comparisons between them. To help researchers understand the profile of the UK LLC resource as a whole, UK LLC standardises (‘harmonises’) key characteristics about participants across all partner LPS. UK LLC has so far harmonised the following demographic variables: **sex, gender, year of birth and ethnic group**. UK LLC has also harmonised information about LPS participants' **highest educational qualifications**. Table 1 below lists the LPS that are included in each of the harmonised datasets.

>**Note**: UK LLC has not changed the original LPS data for these variables.



## 1. Demographic data
<details><summary>There are two versions of the harmonised demographic dataset: full and reduced.</summary>
<br>

[**The full dataset**](../Datasets/LPS_derived/demo_harmonised_full.ipynb) retains every relevant response provided by participants, e.g. if a participant was asked to confirm their ethnic group on five separate occasions, then that individual will have five occurrences of ethnicity in the dataset.
>Researchers are encouraged to use the **full dataset**:
>* To investigate whether a participant’s self-reported demographic characteristics have changed over time
>* To ensure that their research refers to participants' self-reported characteristics as recorded at a time point pertinent to the research question.

[**The reduced dataset**](../Datasets/LPS_derived/demo_harmonised_reduced.ipynb) retains only the most recent response provided by a participant for each variable.

>Researchers are encouraged to use the **reduced dataset**:
>* To have the most recent, valid, definition of a participant’s demographic characteristics
>* To have comparable data on ethnicity and gender for the maximum number of participants
>* To be able to compare LPS data with data from NHS England using the [**NHSE demographics dataset**](../Linked_derived/nhse_patient_demo_mortality.ipynb).
</details>

## 2. Education data
<details><summary>LPS participants' highest educational qualification has been harmonised.</summary>

Fifteen LPS contributing to UK LLC have deposited information educational qualifications of either their participants, their participants' parents, or both. Because of changes in qualifications awarded in the UK over time, and differences between the four nations, UK LLC has harmonised data about education into four categories for LPS participants and two categories for participants' parents. Harmonised education information is provided for each LPS at the most granular level available.
<br>

</details>

## Table 1: LPS included in each dataset
<details><summary>The majority of LPS have deposited relevant demographic or educational information.</summary>

| LPS | Sex | Gender | Year of birth | Ethnicity | Education:<br>participant | Education:<br> parent(s) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| AIRWAVE<sup>*</sup> | n/a | n/a | n/a | n/a | n/a | n/a |
| ALSPAC | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| BCS70 | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ |
| BIB | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| ELSA | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |
| EPICN | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |
| EXCEED | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| FENLAND | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |
| GENSCOT | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| GLAD | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| MCS | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| NCDS58 | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |
| NEXTSTEP | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |
| NICOLA | ✓ | ✗ | ✓ | ✗ |✓ | ✗ |
| NIHRBIO_COPING | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ |
| NSHD46 | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ |
| SABRE | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |
| TEDS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| TRACKC19 | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ |
| TWINSUK | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| UKHLS | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ |
| UKREACH<sup>*</sup> | n/a | n/a | n/a | n/a | n/a | n/a |

<sup>*</sup> Data from  AIRWAVE and UKREACH are not yet available in the TRE.
</details>


## Harmonisation methodology
Detailed information on how UK LLC generated the harmonised datasets is available via the links below. These include downloadable files which show the mapping of LPS data to UK LLC's harmonised variables.
| Detailed information on: |
|:---:|
|[Sex](../../README/sex_info.md)|
|[Gender](../../README/gender_info.md)|
|[Year of birth](../../README/yob_info.md)
|[Ethnicity](../../README/ethnicity_info.md) |
|[Education](../../README/education_info.md) |


>**Note** For some variables included in the harmonised datasets, it may be that UK LLC does not have the complete list of response options available to LPS participants. Where this is the case, the absence of a possible option (e.g. ‘prefer not to answer’) from the responses presented does not mean that option was not available to LPS participants. All that can be inferred is that, if that option was available, it was not selected by anyone included in the datasets shared with UK LLC.
