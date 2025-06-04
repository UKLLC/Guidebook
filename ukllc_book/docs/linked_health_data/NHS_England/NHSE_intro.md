# NHS England data
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC has a data sharing agreement with NHS England to flow extracts of >20 datasets into the UK LLC database.</strong></div>  
<br>

>Last modified: 02 Jun 2025
## Introduction  
Although NHS England is not the owner of all the datasets (acting as data controller or data processor on behalf of the owner for some), for ease, we refer to the datasets as NHS England datasets.  

The datasets cover a **variety of domains and time periods**. Their **geographic coverage is restricted to England**, apart from those listed in the footnotes. 

**Note:**  
* The UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE, apart from **SGSS** where we added COVID in front of it to distinguish it from the UK Health Security Agency's generalised Second Generation Surveillance System (SGSS). 
* Some datasets have been renamed by NHS England, e.g. the **CHESS** dataset is now called the **Severe Acute Respiratory Infection (SARI-Watch) surveillance system** and the **IAPT** dataset is now called the **NHS Talking Therapies for Anxiety and Depression dataset**, but we still receive the data from NHS England as the CHESS and IAPT datasets, respectively. 
* Some datasets have alternative names, e.g. **NPEX** is also called **Covid-19 UK Non-hospital Antigen Testing Results** and **iELISA** is also called **Covid-19 UK Non-hospital Antibody Testing Results**. 
* Some datasets have been **retired** and therefore data only flows for the periods specified. 
* Further nomenclatural details are available in the individual dataset guides. 

<br>
> [**FAQs**](https://guidebook.ukllc.ac.uk/docs/faq/pages/faq_nhse) about working with NHS England data in the UK LLC TRE
<br>


## Overview of NHS England datasets
    

**Table 1** Names, availability and update frequency of NHS England datasets in the UK LLC TRE (datasets in italics are retired)
|**Dataset name in TRE** | **Full dataset name**| **Primary  domain** | **Secondary domain** | **Data available in TRE<sup>1</sup>** |**Data owner**|**Update frequency<sup>1</sup>**|
|---|:---:|:---:|:---:|:---:|:---:|:---:|
|[**HESOP**](../NHS_England/HES%20datasets/OP/HESOP.ipynb)|Hospital Episode Statistics Outpatients|Hospital|Outpatients|01/04/2003 onwards |NHSE|Quarterly|
|[**HESAPC**<sup>2</sup>](../NHS_England/HES%20datasets/APC/HESAPC.ipynb)| Hospital Episode Statistics Admitted Patient Care| Hospital | Admitted patients| 01/04/1998 onwards |NHSE|Quarterly|
|[**ECDS**](../NHS_England/HES%20datasets/ECDS/ECDS.ipynb) | Emergency Care Data Set | Hospital | A & E patients |01/10/2017 onwards |NHSE|Quarterly|
|[***HESAE***](../NHS_England/HES%20datasets/AE/HESAE.ipynb)|*Hospital Episode Statistics Accident & Emergency*|*Hospital*|*A & E patients*|*01/04/2007 to 31/03/2020*|*NHSE*|*Annually*|
|[***COVIDSGSS***](../NHS_England/COVID%20datasets/COVIDSGSS/COVIDSGSS.ipynb)| *COVID-19 Second Generation Surveillance System*|*COVID*|*Testing*|*06/04/2020 to Feb 2024*|*NHSE*|*Annually*|
|[***IELISA***<sup>3</sup>](../NHS_England/COVID%20datasets/IELISA/IELISA.ipynb)|*Enzyme-Linked Immunosorbent Assay*|*COVID*|*Testing*|*01/09/2020 to July 2022*|*DHSC*|*Annually*|
|[***NPEX***<sup>3</sup>](../NHS_England/COVID%20datasets/NPEX/NPEX.ipynb)|*National Pathology Exchange*|*COVID*|*Testing*|*17/04/2020 to Feb 2024*|*DHSC*|*Annually*|
|[***CHESS***](../NHS_England/COVID%20datasets/CHESS/CHESS.ipynb)|*COVID-19 Hospitalisation in England Surveillance System*|*COVID*|*Hospital*|*12/03/2020 to 01/10/2022*|*NHSE*|*Annually*|
|[**CVS**](../NHS_England/COVID%20datasets/CVS/CVS.ipynb)|COVID-19 Vaccination Status|COVID|Vaccination|08/12/2020 onwards|NHSE|Annually|
|[***CVAR***](../NHS_England/COVID%20datasets/CVAR/CVAR.ipynb)|*COVID-19 Vaccination Adverse Reactions*|*COVID*|*Vaccination*|*08/12/2020 to Sept 2023*|*NHSE*|*Annually*|
|[**GDPPR**](../NHS_England/COVID%20datasets/GDPPR/GDPPR.ipynb)|General Practice Extraction Service (GPES) Data for Pandemic Planning and Research | COVID | Primary care  | 1940s onwards|NHSE|Annually|
|[**CANCER**](../NHS_England/Registration%20datasets/CANCER/CANCER.ipynb)| Cancer Registration Data| Registration |Cancer|01/01/1971 onwards|NHSE|Quarterly|
|[**DEMOGRAPHICS**<sup>4</sup>](../NHS_England/Registration%20datasets/DEMOGRAPHICS/Demographics.md)| Demographics Registration data| Registration|Demographics |01/06/2004 onwards|NHSE|Quarterly|
|[**MORTALITY**<sup>4</sup>](../NHS_England/Registration%20datasets/MORTALITY/MORTALITY.ipynb)| Civil Registrations of  Death| Registration|Deaths|01/01/1993 onwards|ONS|Quarterly|
|[**MHSDS**<sup>5</sup>](../NHS_England/Mental%20health%20datasets/MHSDS/MHSDS.md)| Mental Health Services Data Set |Mental health||01/04/2006 onwards|NHSE|Annually|
|[**IAPT**](../NHS_England/Mental%20health%20datasets/IAPT/IAPT.ipynb)|NHS Talking Therapies for Anxiety and Depression|Mental health |Talking therapies|01/04/2012 onwards|NHSE|Annually|
|[**CSDS**](../NHS_England/Other%20datasets/CSDS/CSDS.ipynb)|Community Services Data Set|Other|Community|01/04/2015 onwards|NHSE|Quarterly|
|[**MSDS**](../NHS_England/Other%20datasets/MSDS/MSDS.md)|Maternity Services Data Set|Other|Maternity|01/04/2015 onwards|NHSE|Annually|
|[**PCM**](../NHS_England/Other%20datasets/PCM/PCM.ipynb)|Primary Care Medicines|Other|Medicines|01/04/2015 onwards|NHSE|Quarterly|
 

<sup>1</sup>As documented in the data sharing agreement.  
<sup>2</sup>HESAPC includes critical care (HESAPC_ACP and HESCC) and maternity care (HESAPC_MAT).  
<sup>3</sup>NPEX and IELISA cover England, Northern Ireland, Scotland and Wales.  
<sup>4</sup>MORTALITY and DEMOGRAPHICS cover England and Wales.  
<sup>5</sup>Within MHSDS we include its two precursors, the Mental Health and Learning Disabilities Data Set (MHLDDS) and the Mental Health Minimum Data Set (MHMDS).  
DHSC: Department of Health and Social Care; NHSE: NHS England; ONS: Office for National Statistics  
<br>
> [**FAQs**](https://guidebook.ukllc.ac.uk/docs/faq/pages/faq_nhse) about working with NHS England data in the UK LLC TRE