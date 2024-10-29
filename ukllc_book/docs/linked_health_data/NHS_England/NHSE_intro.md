# NHS England datasets
>Last modified: 29 Oct 2024
## Introduction  
UK LLC has a data sharing agreement with NHS England to flow extracts of the **19 datasets** listed in Table 1 into the UK LLC TRE. Although NHS England is not the owner of all the datasets (acting as data controller or data processor on behalf of the owner for some), for ease, we refer to all the datasets in these guides as NHS England datasets.  

**Note**: Each LPS participant can opt out of linkage to their NHS England records.  


## UK LLC documentation of NHS England datasets
We have organised our NHS England data documentation into four tiers as explained in Figure 1. This initial guide provides an overview of the NHS England datasets held in the UK LLC TRE. The [**Processing and linkage guide**](../NHS_England/Linkage%20and%20processing/linkage_processing.md) explains how LPS participants are linked to their health records and how they can opt out. The [**Coded variables guide**](../NHS_England/Coding/coding_intro.md) details the various classification systems used in NHS England datasets. The five **overview dataset guides** align with the dataset primary domains in Table 1 and provide an introduction to the hospital datasets, the COVID datasets, the registration datasets, the mental health datasets and the 'other' datasets, which is a collection of datasets that do not fit neatly into one of the other four groups. Finally, there is a series of more detailed **individual dataset guides**.  
</br>
<img src="../../images/NHSE_IntroDocumentation_Figure1.jpg" width="900"/>

**Figure 1** UK LLC documentation of the NHS England datasets is across four tiers, starting with this overview and culminating in the individual dataset guides
## Overview of NHS England datasets
The NHS England datasets cover a **variety of domains and time periods** as summarised in Table 1 and Figure 2. Their **geographic coverage is restricted to England**, apart from those listed in the footnotes.   
Note:  
* The UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE, apart from **SGSS** where we added COVID in front of it to distinguish it from the UK Health Security Agency's generalised Second Generation Surveillance System (SGSS). 
* Some datasets have been renamed by NHS England, e.g. the **CHESS** dataset is now called the **Severe Acute Respiratory Infection (SARI-Watch) surveillance system** and the **IAPT** dataset is now called the **NHS Talking Therapies for Anxiety and Depression dataset**, but we still receive the data from NHS England as the CHESS and IAPT datasets, respectively. 
* Some datasets have alternative names, e.g. **NPEX** is also called **Covid-19 UK Non-hospital Antigen Testing Results** and **iELISA** is also called **Covid-19 UK Non-hospital Antibody Testing Results**. 
* Further nomenclatural details are available in the individual dataset guides.     

**Table 1** Names, availability and update frequency of NHS England datasets in the UK LLC TRE (datasets in italics are retired)
|**Dataset name in TRE** | **Full dataset name**| **Primary  domain** | **Secondary domain** | **Data available in TRE<sup>1</sup>** |**Data owner**|**Update frequency<sup>1</sup>**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|
|[**HESOP**](../NHS_England/HES%20datasets/OP/HESOP.ipynb)|Hospital Episode Statistics Outpatients|Hospital|Outpatients|01/04/2003 onwards |NHSE|Quarterly|
|[**HESAPC**<sup>2</sup>](../NHS_England/HES%20datasets/APC/HESAPC.ipynb)| Hospital Episode Statistics Admitted Patient Care| Hospital | Admitted patients| 01/04/1998 onwards |NHSE|Quarterly|
|[**ECDS**](../NHS_England/HES%20datasets/ECDS/ECDS.ipynb) | Emergency Care Data Set | Hospital | A & E patients |01/10/2017 onwards |NHSE|Quarterly|
|[***HESAE***](../NHS_England/HES%20datasets/AE/HESAE.ipynb)|*Hospital Episode Statistics Accident & Emergency*|*Hospital*|*A & E patients*|*01/04/2007 to 31/03/2020*|*NHSE*|Annually|
|[**COVIDSGSS**](../NHS_England/COVID%20datasets/COVIDSGSS/COVIDSGSS.ipynb)| COVID-19 Second Generation Surveillance System|COVID|Testing|06/04/2020 onwards|NHSE|Annually|
|[***IELISA***<sup>3</sup>](../NHS_England/COVID%20datasets/IELISA/IELISA.ipynb)|*Enzyme-Linked Immunosorbent Assay*|*COVID*|*Testing*|*01/09/2020 to 2022*|*DHSC*|*Annually*|
|[**NPEX**<sup>3</sup>](../NHS_England/COVID%20datasets/NPEX/NPEX.ipynb)| National Pathology Exchange|COVID|Testing|17/04/2020 onwards|DHSC|Annually|
|[***CHESS***](../NHS_England/COVID%20datasets/CHESS/CHESS.ipynb)|*COVID-19 Hospitalisation in England Surveillance System*|*COVID*|*Hospital*|*12/03/2020 to 01/10/2022*|*NHSE*|Annually|
|[**CVS**](../NHS_England/COVID%20datasets/CVS/CVS.ipynb)|COVID-19 Vaccination Status|COVID|Vaccination|08/12/2020 onwards|NHSE|Annually|
|[**CVAR**](../NHS_England/COVID%20datasets/CVAR/CVAR.ipynb)| COVID-19 Vaccination Adverse Reactions  | COVID |Vaccination|08/12/2020 onwards|NHSE|Annually|
|[**GDPPR**](../NHS_England/COVID%20datasets/GDPPR/GDPPR.ipynb)|General Practice Extraction Service (GPES) Data for Pandemic Planning and Research | COVID | Primary care  | 01/06/2020 onwards|NHSE|Annually|
|[**CANCER**](../NHS_England/Registration%20datasets/CANCER/CANCER.ipynb)| Cancer Registration Data| Registration |Cancer|01/01/1971 onwards|NHSE|Quarterly|
|[**DEMOGRAPHICS**<sup>4</sup>](../NHS_England/Registration%20datasets/DEMOGRAPHICS/Demographics.md)| Demographics Registration data| Registration|Demographics |01/06/2004 onwards|NHSE|Quarterly|
|[**MORTALITY**<sup>4</sup>](../NHS_England/Registration%20datasets/MORTALITY/MORTALITY.ipynb)| Civil Registrations of  Death| Registration|Deaths|01/01/1993 onwards|ONS|Quarterly|
|[**MHSDS**<sup>5</sup>](../NHS_England/Mental%20health%20datasets/MHSDS/MHSDS.md)| Mental Health Services Data Set |Mental health||01/04/2006 onwards|NHSE|Annually|
|[**IAPT**](../NHS_England/Mental%20health%20datasets/IAPT/IAPT.ipynb)|NHS Talking Therapies for Anxiety and Depression|Mental health |Talking therapies|01/04/2012 to 31/03/2023|NHSE|Annually|
|[**CSDS**](../NHS_England/Other%20datasets/CSDS/CSDS.ipynb)|Community Services Data Set|Other|Community|01/04/2015 onwards|NHSE|Quarterly|
|[**MSDS**](../NHS_England/Other%20datasets/MSDS/MSDS.md)|Maternity Services Data Set|Other|Maternity|TBC|NHSE|Annually|
|[**PCM**](../NHS_England/Other%20datasets/PCM/PCM.ipynb)|Primary Care Medicines|Other|Medicines|01/04/2015 onwards|NHSE|Annually|
 

<sup>1</sup>As documented in the data sharing agreement.  
<sup>2</sup>HESAPC includes critical care (HESAPC_ACP and HESCC) and maternity care (HESAPC_MAT).  
<sup>3</sup>NPEX and IELISA cover England, Northern Ireland, Scotland and Wales.  
<sup>4</sup>MORTALITY and DEMOGRAPHICS cover England and Wales.  
<sup>5</sup>Within MHSDS we include its two precursors, the Mental Health and Learning Disabilities Data Set (MHLDDS) and the Mental Health Minimum Data Set (MHMDS).  
DHSC: Department of Health and Social Care; NHSE: NHS England; ONS: Office for National Statistics  




<img src="../../images/Graph_Availability_NHSE_data_29102024.jpg" width="900"/>

**Figure 2** A summary of the temporal coverage of each NHS England dataset in the UK LLC TRE
