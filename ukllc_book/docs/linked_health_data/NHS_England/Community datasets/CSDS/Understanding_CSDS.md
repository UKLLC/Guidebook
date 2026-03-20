# Understanding the CSDS
>Last modified: 20 Mar 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px; "><strong>The Community Services Dataset (CSDS) is a secondary uses dataset containing information about adults and children supported by community-based health services.</strong></div>

## 1. Introduction
The CSDS comprises clinical and operational data for monitoring local and national service use and outcomes, reporting for commissioning, and to help address health inequalities. The CSDS is not used for direct patient care. Data are collected from publicly-funded community services in England such as health centres, day care facilities, schools, mobile facilities and patients' homes.

## 2. Strengths of CSDS

Although not designed for research, benefits of using the CSDS for research include: 

1. National consistency – standardised data collection enables comparisons across all publicly-funded community health services and all regions of England.

2. Comprehensive coverage of community care ensures the dataset provides a full picture of community service activity. 

3. The CSDS includes individual-level diagnostic, personal circumstance, screening and care event data, and can be used to supplement data recorded in primary and secondary care.

## 3. Limitations of CSDS

1.  Data completeness and consistency varies between, and within, organisations. Inconsistencies include missing data, variations in coding, and inconsistent adoption of national standards. Information about the quality of data submitted to the CSDS is available on the <strong><a href="https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/community-services-data-set/data-quality-dashboard" target="_blank" rel="noopener noreferrer">CSDS Data Quality Dashboard</a></strong>.  

2. Published statistics from CSDS are labelled 'experimental' as they are still being evaluated, which means that the dataset may not yet be truly reliable.  

3. Not all service providers submit data consistently, or submit complete returns, affecting representativeness and limiting comparative analyses.  

4. The CSDS has a complex multi-table structure, with variables spread across topic-specific tables such as 'care activities', 'referrals', etc. This is described more fully [below](#9-availability-in-the-uk-llc-tre).  

5. As a secondary uses dataset, the data in the CSDS has been ingested from multiple systems not necessarily designed for detailed analysis. Some clinically relevant data may not be captured with data quality dependent on local documentation practices.

## 4. Scope and coverage
The CSDS is a long-standing dataset which re-uses clinical and operational data for purposes other than direct patient care. It comprises data about care events occurring in community settings such as health centres, day care facilities, schools, mobile facilities and patients' own homes.

The CSDS includes patient-level data about adults and children including:
* personal and demographic information  
* social and personal circumstances  
* breastfeeding and nutrition  
* screening and assessments
* diagnoses, including long-term conditions and disabilities  
* weight management services

These are spread across **9 tables**, each focusing on an aspect of community care.

## 5. Data collection methodology
>No data are collected specifically for the CSDS.  

The dataset re-uses clinical and operational data extracted from electronic records held by providers such as community health trusts, mental health trusts, local authorities, and the independent sector. Providers are required to extract a structured set of data items and definitions from their Electronic Health Records (EHRs) or clinical systems according to the national <strong><a href="https://www.datadictionary.nhs.uk/data_sets/clinical_data_sets/community_services_data_set.html#dataset_community_services_data_set.specification" target="_blank" rel="noopener noreferrer">CSDS specifications</a></strong>. Data are collated and processed centrally by NHS England.

## 6. Structure of the dataset
The CSDS is comprised of multiple tables (i.e. individual datasets) which flow from NHS England to UK LLC grouped into **9 themed tables**: 
* care activities
* care plans
* coded scored assessments
* demographics and referral
* diagnoses
* group sessions
* immunisations
* onward referrals
* rrt (referrals to treatment)  

See ['Availability in the UK LLC TRE'](#9-availability-in-the-UK-LLC-TRE) below for more detail. All 9 tables contain multiple lines per participant.

## 7. Coding systems used
The CSDS uses four coding systems across the 9 tables: **ICD-10, SNOMED CT, National and Read Codes**.

Understanding which tables use which codes helps in identifying the appropriate coding system when working with the data. Table 1 shows some of the key coded variables and the coding system(s) used in each. 

The variables are grouped into four main categories to make the table easier to interpret. The categories and their descriptions are as follows.
* **Care / Contact Activity**: variables used to identify information about clinical activities, procedures, or observations captured during care contact.
* **Coded Assessment Tool**: variables used to identify information about clinical assessment tools used to measure patient outcomes.
* **Patient Demographics**: variables used to identify lifestyle or social factors captured during assessments.
* **Clinical Terminology / Diagnosis**: variables used to identify diagnosis codes used to record clinical information about the health-related conditions of patients.

<br>

 **Table 1: Key variables and the coding systems used**
| Table name (nhsd.CSDS_) | Variable name | Variable label | Coding system | Category |
|:---|:---|:---|:---|:---|
| care_activities_v0003 | codedfinding | Coded clinical entry for a finding | ICD-10, Read, SNOMED | Clinical Terminology / Diagnosis |
| care_activities_v0003 | codedobservation | Clinical terminology code for an observable entity | ICD-10, Read, SNOMED | Clinical Terminology / Diagnosis
| care_activities_v0003 | codedprocedure | Clinical terminology code for a procedure | Read, SNOMED |Clinical Terminology / Diagnosis |
| care_plans_v0003 | plan_type | Care plan type | National | Care / Contact Activity |
| demographics_and_referral_v0003 | employmentstatus | Current employment status of a person | National | Patient Demographics |
| coded_scored_assessments_v0003 | snomed_id | SNOMED CT concept ID used to identify an assessment | SNOMED | Coded Assessment Tool |
| demographics_and_referral_v0003 | accommstatus | Type of accommodation that a patient currently lives in | National | Patient Demographics |
| demographics_and_referral_v0003 | carecontact_attended_count | Cumulative count of the number of care contacts that were attended | n/a | Care / Contact Activity |
| immunisations_v003 | childhoodimmunisation_type | Type of childhood immunisation | National | Clinical Terminology / Diagnosis |
| onward_referrals_v0003 | onward_referralreason | Reason the patient was referred to another service| National | Care / Contact Activity |

<br>

>Further information about coding systems can be found in Guidebook's [coded variables guide](../../Coding/coding_intro.md). 

## 8. Evolution of the dataset
The CSDS has been collected since 2015, with the most recent version of the dataset (v1.6) introduced in January 2023. The uplift to v1.6 introduced the several changes to the dataset including:
* Demographics and referral table: a new variable **ethniccategory2021** was added for voluntary inclusion once the value list is available. 
* Care activities table: the variable **attendornot** was renamed to **attendancestatus** to align with other NHS England datasets. Both the old and new versions of the variable exist in the CSDS in the UK LLC TRE.

## 9. Availability in the UK LLC TRE
The UK LLC TRE currently holds an extract of the CSDS from **2015 onwards** organised into **9 linked tables**. An overview of these tables is provided in Table 2 below.  

The UK LLC TRE includes CSDS records for participants in partner LPS and only where individual or LPS permissions allow linkage to NHS data. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHS data not be shared via UK LLC.

**Table 2: CSDS tables available in the UK LLC TRE**
| Table name (nhsd.CSDS_)<sup>1</sup> | Summary of contents | No. variables |
|---|---|---:|
| care_activities | Appointments, referrals, patient observations and<br>measurements  | 98 |
| care_plans | Type and timings of care plans | 17 | 
| coded_scored_assessments | Type of assessment, age of participant | 19 |
| demographics_and_referral | Demographics, personal circumstances, summary of<br>care contacts, test results, physical examinations of infants  | 153 |
| diagnoses | Dates and clinical codes of diagnoses | 16 |
| group_sessions | Dates and types of group sessions | 19 |
| immunisations | Dates and clinical codes of immunisations | 21 |
| onward_referrals | Dates and reasons for referrals | 11 |
| rrt | Metrics on patient age groups, referral dates and waiting times  | 28|

<sup>1</sup> The number of LPS participants included in each table in the TRE is summarised on the [**Guidebook CSDS**](../../Community%20datasets/CSDS/CSDS.ipynb) page.

## 10. Missing information
* **Variable and value labels**  
UK LLC is infilling missing variable and value labels in the NHSE datasets in the TRE. Where variable labels have been added by UK LLC, rather than being found in NHSE documentation, this is made apparent by the phrase 'label added by UK LLC' being included in the variable label.  
* **Missing data**  
The amount of missing data varies widely between variables and across datasets. Throughout 2026, we will update this section with information about missingness in the CSDS.

## 11. Tips for researchers using the CSDS in the UK LLC TRE
1. Descriptions of the variables included in the dataset can be downloaded from the **Enhanced Technical Output Specification** available from [NHS England](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/community-services-data-set/implementing-the-community-services-data-set-csds-v1.6-tools-and-guidance). 
2. Use the individual identifer *cohortkey_e* to link participants across CSDS tables.  
3. Throughout the CSDS tables, variables suffixed **x_scheme** indicate which coding system is used in the associated variable **x** (e.g. diagnosis, procedure)

We will regularly update these tips as we gather more information. 

## 12. Useful syntax 
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the UK LLC Github repository where you can find the full scripts.

## 13. Further reading 
The interactive CSDS Data Quality Dashboard is available online: <a href="https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/community-services-data-set/data-quality-dashboard" target="_blank" rel="noopener noreferrer">CSDS Data Quality Dashboard</a>
