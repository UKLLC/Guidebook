# Harmonised sociodemographic datasets
>Last modified: 21 Oct 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has created a range of harmonised datasets applicable across Longitudinal Population Studies (LPS).</strong></div>

## Introduction
Longitudinal Population Studies (LPS) collect data in different ways, using different variable names and values, so it is not always easy to make comparisons between them. To help researchers understand the profile of the UK LLC resource as a whole, UK LLC standardises ('harmonises') key characteristics about participants across all partner LPS.  

UK LLC has harmonised the following demographic variables: **sex, gender, year of birth** and **ethnic group**. UK LLC has also harmonised information about LPS participants' **highest educational qualifications**. Table 1 below lists the LPS that are included in each of the harmonised datasets.

>**Note**: UK LLC has not changed the original LPS data for these variables.

## 1. Demographic data
<details><summary>There are two versions of the harmonised demographic dataset: full and reduced.</summary>
<br>

[**The full dataset**](../harmonisation/demo_harmonised_full.ipynb) retains every relevant response provided by participants, e.g. if a participant was asked to confirm their ethnic group on five separate occasions, then that individual will have five occurrences of ethnicity in the dataset.
>Researchers are encouraged to use the **full dataset**:
>* To investigate whether a participant’s self-reported demographic characteristics have changed over time
>* To ensure that their research refers to participants' self-reported characteristics as recorded at a time point pertinent to the research question.

[**The reduced dataset**](../harmonisation/demo_harmonised_reduced.ipynb) retains only the most recent response provided by a participant for each variable.

>Researchers are encouraged to use the **reduced dataset**:
>* To have the most recent, valid, definition of a participant’s demographic characteristics
>* To have comparable data on ethnicity and gender for the maximum number of participants
>* To be able to compare LPS data with data from NHS England using the [**NHSE demographics dataset**](../ukllc_managed_data/datasets/nhse_reference/nhse_patient_demo_mortality.ipynb).
</details>

## 2. Education data
<details><summary>LPS participants' highest educational qualification has been harmonised.</summary>

Seventeen LPS contributing to UK LLC have deposited information educational qualifications of either their participants, their participants' parents, or both. Because of changes in qualifications awarded in the UK over time, and differences between the four nations, UK LLC has harmonised data about education into four categories for LPS participants and two categories for participants' parents. Harmonised education information is provided for each LPS at the most granular level available.

</details>

## Table 1: LPS included in each dataset
<details><summary>The majority of LPS have deposited relevant demographic or educational information.</summary>  
<br>
The figures in the Table below show, for each LPS, what percentage of participants in the UK LLC are included in the harmonised variables. The ✗ indicates that UK LLC does not currently have any relevant information from that LPS.  

<br>  
 
<aside class="admonition note"><p class="admonition-title">N.B. This table reflects only the LPS datasets currently available in the UK LLC TRE.</p>Due to a delay between LPS uploading datasets to the TRE and them being incorporated into the harmonised datasets, these figures may under-represent the proportion of participants for whom sociodemographic information is available.</aside>


| LPS | Sex | Gender | Year of birth | Ethnicity | Education:<br>participant | Education:<br> parent(s) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| AIRWAVE | 75-95% | ✗ | 75-95% | ✗ | <25% | ✗ |
| ALSPAC | 50-74% | ✗ | 25-49% | <25% | ✗ | 25-49% |
| BCS70 | 25-49% | ✗ | 50-74% | 50-74% | 25-49% | 50-74% |
| BIB | >95% | ✗ | >95% | >95% | ✗ | 75-95% |
| <small>CAPS<sup>1</sup> | - | - | - | - | - | - |
| <small>CSSBIO<sup>1</sup> | - | - | - | - | - | - |
| ELSA | 25-49% | ✗ | 25-49% | 25-49% | 25-49% | ✗ |
| EPICN | >95% | ✗ | >95% | >95% | >95% | ✗ |
| EXCEED | <25% | 75-95% | 75-95% | 75-95% | ✗ | ✗ |
| FENLAND | >95% | ✗ | >95% | >95% | >95% | ✗ |
| GENSCOT | >95% | <25% | >95% | 75-95% | ✗ | ✗ |
| GLAD | 25-49% | 25-49% | 25-49% | 25-49% | 25-49% | ✗ |
| <small>INTERVAL<sup>1</sup> | - | - | - | - | - | - |
| MCS | 25-49% | ✗ | 50-74% | >95% | 25-49% | ✗ |
| NCDS58 | 25-49% | ✗ | 50-74% | 50-74% | 25-49% | ✗ |
| NEXTSTEP | 25-49% | ✗ | 50-74% | >95% | 50-74% | ✗ |
| NICOLA | >95% | ✗ | >95% | ✗ | >95% | ✗ |
| NIHRBIO_COPING | 75-95% | 75-95% | 75-95% | 50-74% | ✗ | ✗ |
| NSHD46 | >95% | ✗ | >95% | ✗ | >95% | ✗ |
| SABRE | >95% | ✗ | <25% | <25% | <25%> | ✗ |
| TEDS | 75-95% | 50-74% | 50-74% | 50-74% | 50-74% | 25-49% |
| TRACKC19 | >95% | ✗ | >95% | >95% | ✗ | ✗ |
| TWINSUK | 75-95% | ✗ | 75-95% | 50-74% | ✗ | ✗ |
| UKHLS | <25% | ✗ | <25% | <25% | <25% | ✗ |
| <small>UKREACH<sup>1</sup> | - | - | - | - | - | - |

**Notes:**  
<sup>1</sup> Data from these partner LPS are not yet available in the TRE.
</details>  
<br>

>UK LLC-managed datasets are available for selection via the **UKLLC** schema in <strong><a href="https://explore.ukllc.ac.uk/" target="_blank" rel="noopener noreferrer">UK LLC Explore</a></strong>.

## Harmonisation methodology
Detailed information on how UK LLC generated the harmonised datasets is available via the links below. These include downloadable files which show the mapping of LPS data to UK LLC's harmonised variables.
| Detailed information on: |
|:---:|
|[Sex](../harmonisation/readme/sex_info.md)|
|[Gender](../harmonisation/readme/gender_info.md)
|[Ethnicity](../harmonisation/readme/ethnicity_info.md) |
|[Education](../harmonisation/readme/education_info.md) |


>**Note** For some variables included in the harmonised datasets, it may be that UK LLC does not have the complete list of response options available to LPS participants. Where this is the case, the absence of a possible option (e.g. ‘prefer not to answer’) from the responses presented does not mean that option was not available to LPS participants. All that can be inferred is that, if that option was available, it was not selected by anyone included in the datasets shared with UK LLC.
