# Hospital datasets
## Introduction
The NHS England hospital datasets comprise the **Hospital Episode Statistics (HES)** datasets and the **Emergency Care Data Set (ECDS)**, which replaced the HES Accident & Emergency dataset (HESAE) in 2017. We haven't included other datasets in this overview guide, such as the Maternity Services Data Set (MSDS) and the Mental Health Services Data Set (MHSDS), because their coverage extends beyond secondary care. 

As detailed in Figure 1, the three primary hospital datasets are the **HES Outpatients (HESOP) dataset**; the **HES Admitted Patient Care (HESAPC) dataset**; and the **Emergency Care Data Set (ECDS)**. The **HESAPC** dataset encompasses two further datasets: the **HES Critical Care (HESCC) minimum dataset** ; and the **HES Maternity (HESAPC_MAT) dataset**. 

<img src="../../../images/Hospital_datasets_Figure1.jpg" width="600"/>


**Figure 1** The five datasets that make up NHS England's hospital datasets  

It is well recognised that these datasets are challenging because of their complexity. We suggest you familiarise yourself with the hospital datasets as a whole before delving into our dataset-specific guides.  

The **primary purpose** of these datasets is to facilitate **financial reimbursement to hospitals** from NHS England and to **support local service planning**. Secondary uses, including research, are permitted as detailed below.
## Coverage of hospital datasets
The hospital datasets cover **inpatient admissions, outpatient appointments** and **accident & emergency attendances** at **hospitals in England**.     

**The hospital datasets include** private patients treated in NHS hospitals; patients resident outside England; and care delivered by treatment centres funded by the NHS (this includes those in the independent sector).  

**The hospital datasets do not include** all mental health or maternity-specific hospital activity – see the Mental Health Services Data Set (MHSDS) guide and Maternity Services Data Set (MSDS) guide, respectively.  

The hospital datasets date back to 1989, although **hospital data in the UK LLC TRE are only available from 1998**, when the use of unique 10-digit NHS numbers was mandated; this made linkage much more accurate. Two datasets have been retired and replaced by others; **all seven hospital datasets are available in the UK LLC TRE**. 
  
**Table 1** Names, temporal coverage and availability of hospital datasets in the UK LLC TRE (the datasets in italics are retired)

| **Dataset name in TRE** | **Domain** |**From**   | **Until**  | **Data available in TRE<sup>1</sup>** |
|---|:---:|:---:|:---:|:---:|
|**HESOP**|Outpatients|01/04/2003|Ongoing|01/04/2003 onwards|
|**HESAPC**|Admitted patients|01/04/1989|Ongoing |01/04/1998 onwards|
|- **HESAPC_MAT**|- Maternity|01/04/2000|Ongoing|01/04/2000 onwards|
|- **HESCC**|- Critical care| 01/04/2008|Ongoing|01/04/2008 onwards|
|- ***HESAPC_ACP***<sup>2</sup>|*- Critical care*|*01/04/1997*|*31/03/2006*|*01/04/1997 to 31/03/2006*|
|**ECDS**|A & E patients|01/10/2017|Ongoing|01/10/2017 onwards|
|***HESAE***<sup>3</sup>|*A & E patients*|*01/04/2007*|*31/03/2020*|*01/04/2007 to 31/03/2020*|
 |

<sup>1</sup>As documented in the data sharing agreement.  
<sup>2</sup>Data about critically ill patients were previously collected in the HES Augmented Care Periods (HESAPC_ACP) dataset.  
<sup>3</sup>Emergency care data were previously collected in the HES Accident & Emergency (HESAE) dataset.  


## Clinical classifications in hospital datasets
**OPCS** and **ICD-10 codes** are used in the HESOP and HESAPC datasets, while **SNOMED CT codes** are used in the ECDS. See the [**Coded variables guide**](../NHS_England/Coding/coding_intro.md) for further details.

## Production of hospital datasets for research purposes

Secondary uses of the hospital datasets, including research, are accommodated within the system as detailed below and summarised in Figure 2. 


<img src="../../../images/Hospital_processing_Figure2.jpg" width="600"/>

**Figure 2** The compilation of the hospital datasets via NHS England’s Secondary Uses Service (SUS)  

**Stage 1: Collection of the Commissioning Data Sets (CDS)**:
The NHS Standard Contract requires all providers of NHS hospital care in England to collect clinical and administrative information as part of the [Commissioning Data Sets (CDS)](https://digital.nhs.uk/services/data-services-for-commissioners/commissioning-datasets). These data are used by regional commissioners of healthcare for NHS patients – Integrated Care Boards (ICBs)  – for payment and monitoring purposes. 
    \
**Stage 2: Submission of the CDS to the Secondary Uses Service (SUS)**:
NHS secondary care providers electronically submit their CDS to the Secondary Uses Service (SUS), a national data warehouse located within NHS England. Data from the SUS are made available to the ICBs who use the data to pay hospitals for the care they delivered. These same data can also be processed and used for non-clinical purposes, such as research. Data for these purposes are stored in the SUS Secure Data Warehouse.
  \
**Stage 3: Extraction of hospital datasets from the SUS Secure Data Warehouse**:
On a monthly basis, NHS England takes a provisional extract from the SUS Secure Data Warehouse and carries out basic data checks and cleaning, adds geographical fields and attaches pseudonymised patient identifiers (Person_ID) to each episode of care. Each extract is cumulative and contains data submitted for the financial year so far, i.e. month 6 will contain data from April to September. At the end of each financial year, providers have the opportunity to revise and update their submissions for the year via the 'Annual Refresh'. The finalised hospital datasets are published and made available for research purposes and to NHS England statisticians around September each year. 

For further details see the [NHS England monthly provisional and annual reports](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics#hes-publications), [HES processing cycle and data quality checks](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics/hes-processing-cycle-and-data-quality-checks) and [Processing cycle and ECDS data quality](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/emergency-care-data-set-ecds/data-quality) webpages.


## Structure of hospital datasets
The structure of the **HESOP, HESAE** and **ECDS** datasets is relatively **straightforward**, with each line representing one patient per hospital visit. In contrast, the **HESAPC** datasets are organised into **episodes** and **spells**. Most patients in the HESAPC datasets are represented by one row of data (i.e. a spell comprising one episode), but others may be represented by multiple rows if they move between consultants within or between hospitals. Furthermore, in the **HESAPC_MAT** dataset, each birth generates at least two episodes, one recording details of the delivery (relating to the mother) and one episode per child delivered (relating to the child). See the individual **HESAPC dataset guides** for further details.  

## Data quality of hospital datasets
**Data Quality Notes** are published alongside the finalised [HES datasets](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics/the-processing-cycle-and-hes-data-quality#hes-data-quality-notes) and [ECDS](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/emergency-care-data-set-ecds/data-quality#further-a-e-and-ecds-data-quality-reports). These highlight any specific known issues with the data that should be considered when analysing them. 



 
