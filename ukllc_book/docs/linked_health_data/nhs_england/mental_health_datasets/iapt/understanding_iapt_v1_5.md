# Understanding the IAPT V1.5 dataset
>Last modified: 15 Oct 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px; "><strong>IAPT includes adults who are referred in England for depression, anxiety, or related conditions under the NHS Talking Therapies for Anxiety and Depression Service. The IAPT V1.5 dataset covers referrals received during the period from April 2013 to September 2019.</strong></div>

## 1. Introduction
The IAPT dataset contains information about adults in England referred to the NHS Talking Therapies for Anxiety and Depression service. This service offers **psychological therapy for anxiety and/or depression as well as other related mental health conditions (e.g. obsessive compulsive disorder, body dysmorphic disorder).** It was launched in **2008** as **Improving Access to Psychological Therapies (IAPT)** and was rebranded in **January 2023** though the associated dataset retains the IAPT name until its next formal revision. We therefore continue to refer to this dataset as IAPT.     

The NHS Talking Therapies for Anxiety and Depression service offers evidence-based psychological treatments delivered using a **stepped-care model**. People with less severe depression and anxiety are typically offered a course of **low-intensity treatment** (e.g. guided self-help) delivered by a Psychological Wellbeing Practitioner over 6-8 sessions. Those who do not respond at this level can be stepped up to a course of **high-intensity treatment.** People with more severe depression and/or anxiety may receive high-intensity treatment from the outset. People with specific disorders (e.g. post-traumatic stress disorder or social anxiety) should also receive high-intensity treatment. High-intensity treatment (e.g. cognitive behavioural therapy) is delivered by an accredited therapist, involves more intensive clinician input and a greater number of sessions (e.g. 15-20). Following initial assessment some patients are not considered suitable for a course of treatment and will instead be signposted onto another service. 

**Employment advice and support** is also provided as part of the service to help support the patient’s employment goals.  

Central data collection has been in place for IAPT since **2012** by which time the service had been rolled out nationally across England. 

<aside class="admonition warning"><p class="admonition-title">The IAPT dataset is designed to support service delivery and inform clinical decision-making and has secondary uses related to commissioning, service improvement and service design.</p>As with all NHS England datasets, it is not designed to be used for research.</aside>


## 2. Strengths of IAPT V1.5

Although not designed for research, the IAPT V1.5 dataset can be a useful research resource as its strengths include: 

1. Comprehensive coverage – captures care pathway (e.g. referral, appointments, treatment type), sociodemographic information (e.g. age, gender, ethnicity), and patient outcomes (e.g. recovery, improvement, deterioration). 

2. Standardised and validated measures of depression, anxiety, and functional impairment. Specific thresholds are used for the symptom measures to calculate key outcomes such as reliable recovery and reliable improvement.   

3. Some use of standardised [coding systems](#coding-systems-used) – for example ICD-10 codes.

4. Repeated assessment of symptoms – patients complete measures of symptoms at every session rather than only at the start and end of treatment. This design provides a last available score to calculate outcome metrics even if treatment ends earlier than expected. Outcome data has been obtained for more than 98% of all patients who have a course of treatment.

5. Large-scale naturalistic data about psychological treatment which enhances generalisability.

6. National consistency – standardised data collection enables comparison across services and geographical areas of England. 

## 3. Limitations of IAPT V1.5

1. Scope – limited to NHS-funded talking therapies for anxiety, depression and related conditions. Does not capture private mental health care, other NHS mental health services, or treatment outside of England.

2. Selection bias – includes only those people who are referred (by GP, other professional) or who self-refer. Excludes people whose problems are not recognised by referring professionals, those unaware of the service, lacking motivation or capacity to self-refer  or seek help, or facing other barriers to access including perceived stigma. Treatment access barriers affect some sociodemographic groups disproportionately.

3. Missing data – while outcome data completion is high, incomplete date may arise due to patient distress or objection to its collection, language or literacy barriers, perceived administrative burden, or data collection errors. 

4. Self-report data – many items, including concurrent medication use and long term conditions, rely on self-reported information without clinical verification. 

5. Absence of formal diagnoses – patients are not formally diagnosed so they may not meet clinical criteria for their treated condition or may  have unrecognised comorbidities.

6. Coverage – the data collected in IAPT V1.5 is more limited than later versions of the dataset (see [Evolution of the dataset](#8-evolution-of-the-dataset) below for more detail).



## 4. Scope and coverage
Population: The IAPT dataset includes adults referred for NHS psychological therapies for anxiety, depression and related conditions in England. A formal diagnosis is not required and therefore the dataset **includes patients who may or may not meet clinical criteria for their treated condition.** The IAPT dataset includes some people under the age of 18 who access adult services. It **does not include** activity related to the provision of Children and Young People’s (CYP) IAPT services which is included in [**MHSDS**.](../MHSDS/MHSDS.ipynb) Please also see [**FAQs**](../mh_faq.md) for information about the differences between IAPT and MHSDS.

Included conditions: Anxiety, depression and other related conditions such as post-traumatic stress disorder, obsessive-compulsive disorder and body dysmorphic disorder. These conditions may occur in the context of comorbid long-term physical health conditions or symptoms such as irritable bowl syndrome, as well as some drug or alcohol use.

Excluded conditions: The service is not designed to treat other conditions including psychosis, bipolar disorder, 'personality disorders' or severe eating disorders ([**MHSDS**](../MHSDS/MHSDS.ipynb) captures these). However, individuals with these conditions may be accepted if their primary presenting problem is an included condition and they have no active symptoms that would interfere with treatment. 

Referral routes: Patients can **self-refer** to the service or be **referred by a health professional or voluntary organisation.**  

Data collected: 

The IAPT dataset contains patient-level information about:
-	Sociodemogrphics including age, gender, ethnicity, religious affiliation
-	Area level deprivation, employment status, sick pay receipt status  
-	Clinical presentation - problem descriptor (informal diagnosis), long term physical health conditions, disabilities, use of medication for mental health problems 
-	Care pathway - referral source and dates, appointment dates/times/type, waiting time pauses, attendance
-	Treatment - therapy type (e.g. cognitive behavioural therapy) 
-	Clinical measures - symptom and impairment scpres from each appointment, and derived outcomes such as recovery

Coverage of specific items is dependant on whether the item is mandatory or optional in the dataset specification.

## 5. Data collection methodology
Patients complete self-report measures of their symptoms at every session, typically before or at the beginning. Depression is measured using the [**Patient Health Questionnaire-9 (PHQ-9)**](https://www.apa.org/depression-guideline/patient-health-questionnaire.pdf). Anxiety is measured with the [**Generalised Anxiety Disorder 7-item assessment (GAD-7)**](https://adaa.org/sites/default/files/GAD-7_Anxiety-updated_0.pdf) or an **anxiety disorder specific measure** where available and appropriate for the patient's problem descriptor. The PHQ-9 and GAD-7 assess the frequency of symptoms over the previous two weeks. Patients also complete the [**Work and Social Adjustment Scale**](https://greenspacehealth.com/en-us/work-and-social-functioning-wsas/) to measure how their anxiety and depression symptoms impair their social, work and private life functioning. At the end of assessment and of treatment patients complete **patient experience questionnaires (PEQs)** about the quality of their care.  

NHS England collects data for the IAPT dataset through monthly submissions from service providers via the Strategic Data Collection Service (SDCS) Cloud. Providers send data on referrals (received, seen or closed), contacts, and patient outcomes for that reporting period. NHS England carries out validation checks to ensure data quality, pseudonymisation to protect patient confidentiality, and linkage to previous months’ submissions.


## 6. Structure of the dataset
Version 1.5 of the IAPT dataset is comprised of 7 linked tables which capture details about the person, disability, referrals, appointments, assessments, treatments and waiting time pauses. See [Availability in the UK LLC TRE](#9-availability-in-the-UK-LLC-TRE) below for more detail. 


## 7. Coding systems used
The IAPT V1.5 dataset uses **ICD-10** codes according to the [**NHS Data Model and Dictionary**.](https://archive.datadictionary.nhs.uk/DD%20Release%20May%202024/data_sets/clinical_data_sets/improving_access_to_psychological_therapies_data_set.html) 

Further information about coding systems can be found in the [coded variables guide.](../../Coding/coding_intro.md) 

## 8. Evolution of the dataset
The IAPT dataset has been collected **since 2012** and has evolved through incremental changes over time (summarised in Table 1). These have included: mandating previously optional items, introducing or discontinuing variables, alterations to response options, incorporating pilot datsets, and aligning with NHS-wide standards such as SNOMED CT coding and the [NHS data model and dictionary.](https://archive.datadictionary.nhs.uk/DD%20Release%20May%202024/data_sets/clinical_data_sets/improving_access_to_psychological_therapies_data_set.html) 

The current version of the IAPT dataset is **v2.1** which was **released 20 July 2021** and **implemented in 2022.** 

**Important:** When working with IAPT data spanning multiple years, researchers should ensure they check for differences in variables availability, coding and response options. For full details of the changes across versions see NHS Engalnd's [Change Specification documents](https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dapb-1520-improving-access-to-psychological-therapies-data-set) published by NHS England for current and previous versions. 


**Table 1** A summary of IAPT dataset versions since 2012.

|**Version**|**Year released<sup>1</sup>**|**Year implemented**|**Summary of major changes from previous version**|
|:---|:---|:---|:---|
|1.0|2012|2012|Initial version developed to support consistent data collection and reporting across IAPT services. It was mandated for central return from April 2012|
|1.5|2013|2014|Addition of waiting time pauses, time from patient opt-in to treatment and patient experience questionnaires (PEQs) for assessment and treatment, appointment purpose made mandatory, new code list for reason for end of treatment|
|2.0|2019|2020| Major structural changes to align with other NHS datasets (e.g. [MHSDS](../MHSDS/MHSDS.ipynb). See [NHS data model and dictionary](https://archive.datadictionary.nhs.uk/DD%20Release%20May%202024/data_sets/clinical_data_sets/improving_access_to_psychological_therapies_data_set.html)) including expanded use of clinical terminology (e.g. SNOMED CT). Added/updated variables relating to internet-enabled therapies, language, qualifications of care personnel, treatment location, and group treatment delivery. Changes to anxiety disorder specific measures. Incorporated the Employment Advisors Pilot Data Set<sup>2</sup> and items from the Long Term Conditions and Medically Unexplained Symptoms Pilot Data Set<sup>3</sup>. Clarified scope regarding the inclusion of under-18s who access adult IAPT services|
|2.1|2021|2022| Updated the recording of gender to align with MHSDS, addition of medical history (previous diagnosis), accommodation type information, and added/updated items relevant to employment support activity|

<sup>1</sup> The year of release is the date specified in the guidance reports.

<sup>2</sup> This pilot increased the number of Employment Advisors embedded in IAPT services. Collection of Employment Advisors in IAPT pilot data from those services involved in the pilot started in October 2017 and was submitted alongside the core IAPT dataset v1.5. Version 2.0 incorporated this into the main dataset. 

<sup>3</sup>  This pilot integrated IAPT care into existing medical pathways and services for patients with long term conditions and/or medically unexplained symptoms. Collection of IAPT integrated services pilot data from those services involved in the pilot started in January 2017 and was submitted alongside the core IAPT dataset v1.5. Version 2.0 incorporated this into the main dataset. 

## 9. Availability in the UK LLC TRE

The UK LLC TRE holds an extract of the IAPT V1.5 dataset which covers referrals received during the period from **April 2013 to September 2019** organised into **7 linked tables**. A detailed overview of these tables is provided below **(Table 2)**.  

The UK LLC TRE includes IAPT V1.5 records for participants in partner LPS and only where individual or LPS permissions allow linkage to NHS data. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHS data not be shared via UK LLC.

**Table 2** IAPT V1.5 tables available in the UK LLC TRE, including summary and key variables.

|**Table name**|**Summary of constituent tables**|**Key variables**|
|--------------|-----------|-----------------|
|IAPT_person_V1_5|Personal details of the patient| Age, Religion, Gender, Ethnicity, Sexual orientation, Indicator of long-term physical health condition| 
|IAPT_referral_clear_V1_5|Details of patients' referrals|Date referral received, Source of referral, Indicator of service request acceptance, Provisional diagnoses, Date of symptom onset, Indicator of previous symptoms, Reason for end of care pathway, Date of service discharge, Mental health care cluster code|
|IAPT_appointment_clear_V1_5|Details of interactions between the patient and a health care professional| Appointment date and time, Appointment type, Attendance indicator, Therapy type, Appointment medium (e.g. face-to-face, telephone, email), Intensity of treatment delivered (e.g. low, high, stepped up, stepped down), Care professional role, Employment status, Employment support referral date, Indicator of statutory sick pay receipt, PHQ9 total score, GAD7 score, WSAS scores, Specific anxiety disorder measures scores (e.g. agoraphobia score, OCS score, panic disorder severity score)|
|IAPT_disability_V1_5|Details of the patients' disability (when applicable)|Disability type|
|IAPT_assessments_clear_V1_5|Details of Patient Experience Questionnaire (PEQ) completed at the first assessment session|PEQ (assessment) completion date and time, PEQ (assessment) item scores|
|IAPT_treatments_clear_V1_5|Details of Patient Experience Questionnaire (PEQ) completed at the end of treatment|PEQ (treatment) completion date and time, PEQ (treatment) item scores|
|IAPT_waitingtimes_clear_V1_5|Details of breaks in activity for a patient|Pause start date, Pause end date, Pause reason|

For guidance in managing item changes across IAPT version 1.5 and version 2.1 please refer to [NHS England mapping guidance documentation](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/improving-access-to-psychological-therapies-data-set/iapt-data-set-v2.0-archived-guidance-documents)


## 10. Missing information
* **Variable and value labels**  
UK LLC is infilling missing variable and value labels in the NHSE datasets in the TRE. Where variable labels have been added by UK LLC, rather than being found in NHSE documentation, this is made apparent by the phrase 'label added by UK LLC' being included in the variable label.  
* **Missing data**  
The amount of missing data varies widely between variables and across datasets. Throughout 2026, we will update this section with information about missingness in the IAPT dataset.

## 11. Tips for researchers using IAPT V1.5 in the UK LLC TRE
Please also see the list of [**mental health FAQs**](../mh_faq.md)
1. Descriptions of the variables included in the V1.5 dataset can be downloaded from the **Technical Output Specification** available from [**NHS England.**](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/improving-access-to-psychological-therapies-data-set/iapt-data-set-v1.5-archived-guidance-documents) 
2. Linking between tables: Use the cohort key variable (cohortkey_e) to link patients across IAPT V1.5 tables and use the pathway ID variable (ic_pathway_id) to link pathways (i.e. distinct referrals/episodes of care for a patient) across tables.  
3. Multiple referrals per patient: Some patients have been referred on more than one occasion and therefore have records for multiple referrals (each referral has its own unique pathway ID). It may be appropriate for your analysis to select one per patient (e.g. first referral, most recent referral, or meeting other specific criteria).
4. Defining a course of treatment: A patient is deemed to have had a ‘course’ of treatment if they had at least two clinical sessions before discharge. Patients with only one session or assessment-only contacts are not considered to have received a course of treatment. Inspecting the type of contact that occured in each session is therefore important for understanding a patient's care pathway.
5. Interpreting problem descriptors: Problem descriptors in IAPT use ICD-10 diagnotic codes but do not represent formal diagnoses. They are used to assign patients to appropriate treatment protocols, as specified by NICE guidelines. A patient may not meet full clinical criteria for for the condition they are treated for and it is possible that they could meet diagnostic criteria for other conditions not captured by their problem descriptor.
6. Understanding outcome metrics: Key outcomes including recovery are calculated based on symptom scores at a patient's first and final sessions using specific thresholds. Not all participants are eligible for all outcome calculations. For example, a patient who scores below the clinical thresholds on both the PHQ-9 and GAD-7 at baseline cannot be assessed for recovery as they were not in the 'caseness' range to begin with.

We will regularly update these tips as we gather more information. 

## 12. Useful syntax 
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the UK LLC Github repository where you can find the full scripts.

## 13. Further reading 
Information in this section will be added in due course.