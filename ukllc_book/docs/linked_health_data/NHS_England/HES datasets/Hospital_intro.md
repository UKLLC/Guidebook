# NHS England hospital datasets
>Last modified: 20 Jun 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The hospital datasets cover all NHS funded hospital activity in England. This includes inpatient, outpatient and accident & emergency.</strong></div>  
<br>

>## Summary:
>* UK LLC holds **seven NHS England hospital datasets**. The four primary datasets are [**Hospital Episode Statistics (HES) Outpatients**](../HES%20datasets/OP/HESOP.ipynb), [**HES Admitted Patient Care**](../HES%20datasets/APC/HESAPC.ipynb), [**HES Accident & Emergency** (retired)](../HES%20datasets/AE/) and [**Emergency Care**](../HES%20datasets/ECDS/).  
<br>
>* **HES Admitted Patient Care** encompasses three further datasets: [**HES Critical Care**](../HES%20datasets/CC/), **HES Augmented Care Periods** (retired) and **HES Maternity**.  
<br>
> * The datasets in the UK LLC TRE span **1998 onwards**.  
<br>
> * The datasets **do not** include all mental health or maternity-specific hospital activity. Much of this information is included in the [**Mental Health Services Data Set (MHSDS)**](../Mental%20health%20datasets/MHSDS/MHSDS.ipynb) and [**Maternity Services Data Set (MSDS)**](../Community%20datasets/MSDS/), respectively.  
<br>    
> * **OPCS** and **ICD-10 codes** are used in the HESOP and HESAPC datasets, while **SNOMED CT codes** are used in the ECDS. See the [**Coded variables guide**](../Coding/coding_intro.md) for further details. 
<br>

<img src="../../../images/Hospital_datasets.jpg" width="900"/>

**Figure 1** The seven NHS England hospital datasets, including their temporal coverage  

For further details see the [**NHS England monthly provisional and annual reports**](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics#hes-publications), [**HES processing cycle and data quality checks**](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/hospital-episode-statistics/hes-processing-cycle-and-data-quality-checks) and [**Processing cycle and ECDS data quality**](https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/emergency-care-data-set-ecds/data-quality) webpages.

## Purpose of data collection
The datasets were set up for the **management and planning** of hospital services and for the **financial reimbursement** to hospitals for the care they have provided to patients. Secondary uses of the hospital datasets, including **research**, are accommodated within the system. 

## Processing cycle and frequency of data collection


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
 
