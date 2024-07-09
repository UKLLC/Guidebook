# NHS England hospital datasets
>Last modified: 05 Jul 2024
## Introduction
The NHS England hospital datasets comprise the **Hospital Episode Statistics (HES) datasets** and the **Emergency Care Data Set (ECDS)**. The hospital datasets **do not include** all mental health or maternity-specific hospital activity. Much of this information is included in the Mental Health Services Data Set (MHSDS) and Maternity Services Data Set (MSDS), respectively. 

As detailed in Figure 1, the three primary hospital datasets are the **HES Outpatients (HESOP) dataset**; the **HES Admitted Patient Care (HESAPC) dataset**; and the **Emergency Care Data Set (ECDS)**. The **HESAPC** dataset encompasses two further datasets: the **HES Critical Care (HESCC) minimum dataset**; and the **HES Maternity (HESAPC_MAT) dataset**. 

<img src="../../../images/Hospital_datasets_Figure1.jpg" width="600"/>


**Figure 1** The five datasets that make up NHS England's hospital datasets  

**OPCS** and **ICD-10 codes** are used in the HESOP and HESAPC datasets, while **SNOMED CT codes** are used in the ECDS. See the [**Coded variables guide**](../Coding/coding_intro.md) for further details. 


## Coverage of hospital datasets
The hospital datasets cover **inpatient admissions, outpatient appointments** and **accident & emergency attendances** at **hospitals in England**.     

The hospital datasets **include** private patients treated in NHS hospitals; patients resident outside England; and care delivered by treatment centres funded by the NHS (this includes those in the independent sector).  



The hospital datasets date back to 1989, although **hospital data in the UK LLC TRE are only available from 1998**, when the use of unique 10-digit NHS numbers was mandated; this made linkage much more accurate. Two datasets have been retired and replaced by others; **all seven hospital datasets are available in the UK LLC TRE**. 
  
**Table 1** Names, temporal coverage and availability of hospital datasets in the UK LLC TRE (the datasets in italics are retired)

| **Name in TRE**|**Full name**|**Domain**|**From**|**Until**|**Data available in TRE<sup>1</sup>** |
|---|:---:|:---:|:---:|:---:|:---:|
|[**HESOP**](../HES%20datasets/OP/HESOP.ipynb)|HES Outpatients|Outpatients|01/04/2003|Ongoing|01/04/2003 onwards|
|[**HESAPC**<sup>2</sup>](../HES%20datasets/APC/HESAPC.ipynb)|HES Admitted Patient Care|Inpatients|01/04/1989|Ongoing |01/04/1998 onwards|
|- **HESAPC_MAT**|HES APC Maternity|Maternity|01/04/2000|Ongoing|01/04/2000 onwards|
|[- **HESCC**](../HES%20datasets/CC/HESCC.ipynb)|HES Critical Care|Critical care| 01/04/2008|Ongoing|01/04/2008 onwards|
|- ***HESAPC_ACP***|*HESAPC Augmented Care Periods*|*Critical care*|*01/04/1997*|*31/03/2006*|*01/04/1997 to 31/03/2006*|
|[**ECDS**](../HES%20datasets/ECDS/ECDS.ipynb)|Emergency Care Data Set|A & E patients|01/10/2017|Ongoing|01/10/2017 onwards|
|[***HESAE***](../HES%20datasets/AE/HESAE.ipynb)|*HES Accident & Emergency*|*A & E patients*|*01/04/2007*|*31/03/2020*|*01/04/2007 to 31/03/2020*| |

<sup>1</sup>As documented in the data sharing agreement.  
<sup>2</sup>The HESAPC dataset encompasses HESAPC_MAT, HESCC and HESAPC_ACP.

HES: Hospital Episode Statistics  

For further details see the [**NHS England monthly provisional and annual reports**](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics#hes-publications), [**HES processing cycle and data quality checks**](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics/hes-processing-cycle-and-data-quality-checks) and [**Processing cycle and ECDS data quality**](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/emergency-care-data-set-ecds/data-quality) webpages.

## Background
<details>
  <summary>Production of hospital datasets for research purposes</summary>
Secondary uses of the hospital datasets, including research, are accommodated within the system as detailed below and summarised in Figure 2. 


<img src="../../../images/Hospital_processing_Figure2.jpg" width="600"/>

**Figure 2** The compilation of the hospital datasets via NHS England’s Secondary Uses Service (SUS)  

**Stage 1: Collection of the Commissioning Data Sets (CDS)**:
The NHS Standard Contract requires all providers of NHS hospital care in England to collect clinical and administrative information as part of the [**Commissioning Data Sets (CDS)**](https://digital.nhs.uk/services/data-services-for-commissioners/commissioning-datasets). These data are used by regional commissioners of healthcare for NHS patients – Integrated Care Boards (ICBs)  – for payment and monitoring purposes. 
    \
**Stage 2: Submission of the CDS to the Secondary Uses Service (SUS)**:
NHS secondary care providers electronically submit their CDS to the Secondary Uses Service (SUS), a national data warehouse located within NHS England. Data from the SUS are made available to the ICBs who use the data to pay hospitals for the care they delivered. These same data can also be processed and used for non-clinical purposes, such as research. Data for these purposes are stored in the SUS Secure Data Warehouse.
  \
**Stage 3: Extraction of hospital datasets from the SUS Secure Data Warehouse**:
On a monthly basis, NHS England takes a provisional extract from the SUS Secure Data Warehouse and carries out basic data checks and cleaning, adds geographical fields and attaches pseudonymised patient identifiers (Person_ID) to each episode of care. Each extract is cumulative and contains data submitted for the financial year so far, i.e. month 6 will contain data from April to September. At the end of each financial year, providers have the opportunity to revise and update their submissions for the year via the 'Annual Refresh'. The finalised hospital datasets are published and made available for research purposes and to NHS England statisticians around September each year. 



</details>
 
