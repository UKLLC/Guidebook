# FAQs about working with mental health data
>Last modified: 13 Jan 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>Answers to researchers' questions about working with mental health data.</strong></div style>  
<br>

<details>
<summary>What is the difference between MHMDS, MHLDDS and MHSDS?</summary>

The **Mental Health Minimum Dataset (MHMDS)** was introduced in 2000 to collect data about adults with mental health issues. It was published in 2008 and retired in 2014. In 2014, the dataset was expanded to include individuals receiving learning disabilities services and was subsequently renamed the **Mental Health and Learning Disabilities Dataset (MHLDDS)**. Then, in 2016, the scope was further broadened to include services such as Children’s Mental Health Services (CAMHS), Children and Young People’s Improving Access to Psychological Therapies (CYP-IAPT), Eating Disorders in Children and Young People, and Problem Gambling Services. With this expansion, the dataset was renamed the **Mental Health Services Dataset (MHSDS)**. Currently, UK LLC only receives MHSDS data. 

</details>

<details>
<summary>In the MHSDS, why are there records that pre-date April 2016 (when the dataset was established)?</summary>

The data which pre-date the MHSDS indicate referral starts etc. which were open before the MHSDS was established. These data submissions were only made for open referrals. No closed referrals are submitted through MHSDS and no data has been brought across from previous datasets (e.g Mental Health Minimum Data Set).
</details>

<details>
<summary>What is a 'referral' in the context of the MHSDS?</summary>

A referral occurs when a person is directed or recommended to a service for support, assessment, or treatment. In the context of the MHSDS, referrals can originate from a wide range of sources or settings, including:
- General Practitioners (GPs)
- Health visitors
- Maternity services
- Self-referrals
- Social services
- Local authorities or public services
- The justice system (e.g. police, courts, probation services, prisons)
- Employers
- Independent services
- Other services (including voluntary services, asylum services, school nurse etc.).
</details>

<details>
<summary>What are the conditions under which a referral is rejected in the MHSDS?</summary>

The most common reasons for rejection of a referral are:
- Duplicate referral request (the patient is already undergoing treatment with the same or different care provider)
- Inappropriate referral request (the request is inappropriate for the services offered by the healthcare provider)
- Incomplete referral request (the request does not contain all the required information).
</details>

<details>
<summary>What is the difference between the MHSDS and IAPT datasets in terms of information about anxiety and depression?</summary>

Both the MHSDS and IAPT datasets include people who have been diagnosed with anxiety or depression. However, the information in the MHSDS is only adequate for counts of people with these diagnoses. If you are interested in performing more detailed analyses about people with anxiety and/or depression, you should include the [**NHS Talking Therapies dataset (IAPT)**](../Mental%20health%20datasets/IAPT/IAPT.ipynb) in your data request/analyses.
</details>

<details>
<summary>Why do some variables in the MHSDS appear to be identical?</summary>

In the referrals table (MSH101), the following pairs of variables have the same content, with the second one being the de-identified ('deid') version of the first:  
* pservcierequestid & servicerequestedid_deid 
* puniqservreqid & uniqservreqid_deid  
</details>

<details>
<summary>What is the purpose of Unique Month ID in the MHSDS?</summary>

MHSDS is submitted on a monthly basis by providers. The Unique Month ID (UniqMonthID) indicates the month of submission. Month 1 is April of each year, with the value increasing every month thereafter.
</details>

<details>
<summary>What is the difference between the information captured by tables 201 and 202 in the MHSDS?</summary>

The 201 Care Contact table provides details about the type of clinical activity or intervention delivered to the service user. The 202 Care Activity table contains information about the location, duration of the care contact and the schemes used.
</details>

<details>
<summary>How does information in table 201 vary from table 204 in the MHSDS?</summary>

The 201 Care Contact table records information about direct care contact services where the patient (or sometimes their carer/family) is in contact with the service. The 204 Indirect Activity table records information where the patient is not present, but the activity still supports their care. 
</details>

<details>
<summary>What is the difference between HES and MHSDS ?</summary>

The Hospital Episode Statistics [**HES**](https://guidebook.ukllc.ac.uk/docs/linked_health_data/nhs_england/hes%20datasets/hospital_intro) collects information on secondary care activity within NHS hospitals including inpatient admissions, outpatient appointments, and Accident & Emergency attendances. In contrast, the Mental Health Services Data Set (MHSDS) provides comprehensive information about mental health and learning disabilities, including both community and inpatient care. It contains details on referrals, assessments, care plans, contacts with mental health professionals, and clinical outcomes.
</details>

<details>
<summary>What information about mental health conditions can be obtained from HES OP and HES APC and what additional details are available only in MHSDS?</summary>

Information about study participants diagnosed with mental health conditions, including schizophrenia, bipolar disorder, and psychotic disorders, can be obtained from HES OP and HES APC. These datasets record only the diagnosis details found in MHSDS tables such as MHS601 (Previous Diagnosis), MHS603 (Provisional Diagnosis), MHS604 (Primary Diagnosis), and MHS605 (Secondary Diagnosis). More comprehensive information suitable for in-depth analysis, such as referrals, services referred to, or care activities, can instead be obtained from MHSDS.
</details>

<details>
<summary>What does the term “in contact with mental health services” mean in the context of reporting? </summary>

The term refers to individuals who have an active referral to mental health services during the reporting period. An active referral means the case remains open at the end of the reporting month, regardless of whether the person has received any appointments, interventions, or recorded care activities under that referral. 
</details><br>

