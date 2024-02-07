# NHS England datasets
## Introduction  
UK LLC has a data sharing agreement with NHS England to flow extracts of the **21 datasets** listed in Table 1 into the UK LLC TRE. Although NHS England is not the owner of all the datasets (acting as data controller or data processor on behalf of the owner for some), for ease, we refer to all the datasets in these guides as NHS England datasets.  

**Note**: Each LPS participant has the power to opt out of linkage to their NHS England records.  


## UK LLC documentation of NHS England datasets
We have organised our NHS England data documentation into four tiers as explained in Figure 1. This initial guide provides an overview of the NHS England datasets held in the UK LLC TRE. The [**Processing and linkage guide**](../NHS_England/Linkage%20and%20processing/) explains how LPS participants are linked to their health records and how they can opt out. The [**Coded variables guide**](../NHS_England/Coding/coding_intro.md) details the various classification systems used in NHS England datasets. The four **overview dataset guides** align with the dataset primary domains in Table 1 and provide an introduction to the hospital datasets, the COVID datasets, the registration datasets and the mental health datasets. Finally, there is a series of detailed **individual dataset guides**.  
</br>
<img src="../../images/NHSE_IntroDocumentation_Figure1.jpg" width="700"/>

**Figure 1** UK LLC documentation of the NHS England datasets is across four tiers, starting with this overview and culminating in the detailed individual dataset guides
## Overview of NHS England datasets
The NHS England datasets cover a **variety of domains and time periods** as summarised in Table 1. Their **geographic coverage is restricted to England**, apart from those listed in the footnotes. The UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE, apart from **SGSS** where we added COVID in front of it to distinguish it from the UK Health Security Agency's generalised Second Generation Surveillance System (SGSS). Some datasets have been renamed by NHS England, e.g. the **CHESS** dataset is now called the **Severe Acute Respiratory Infection (SARI-Watch) surveillance system**, but we still receive the data from NHS England as the CHESS dataset. Some datasets have alternative names, e.g. **NPEX** is also called **Covid-19 UK Non-hospital Antigen Testing Results** and **iELISA** is also called **Covid-19 UK Non-hospital Antibody Testing Results**. Further nomenclatural details are available in the individual dataset guides.     

**Table 1** Names, temporal coverage and availability of NHS England datasets in the UK LLC TRE (the datasets in italics are retired) 
|**Dataset name in TRE** | **Full dataset name**| **Primary  domain** | **Secondary domain** | **Data available in TRE<sup>1</sup>** |**Data owner** |
|---|:---:|:---:|:---:|:---:|:---:|
|**HESAPC**<sup>2</sup>| Hospital Episode Statistics Admitted Patient Care| Hospital | Admitted patients| 01/04/1998 onwards |NHSE|
|**HESOP**|Hospital Episode Statistics Outpatients|Hospital|Outpatients|01/04/2003 onwards |NHSE|
|**ECDS** | Emergency Care Data Set | Hospital | A & E patients |01/10/2017 onwards |NHSE|
|***HESAE***|*Hospital Episode Statistics Accident & Emergency*|*Hospital*|*A & E patients*|*01/04/2007 to 31/03/2020*|*NHSE*|
|**MSDS**|Maternity Services Data Set|Maternity|Hospital|01/04/2015 to 31/03/2019|NHSE| 
|**COVIDSGSS**| COVID-19 Second Generation Surveillance System|COVID|Testing|06/04/2020 onwards|NHSE|
|**IELISA**<sup>3</sup>| Enzyme-Linked Immunosorbent Assay| COVID |Testing| 01/09/2020 onwards |DHSC|
|**NPEX**<sup>3</sup>| National Pathology Exchange|COVID|Testing|17/04/2020 onwards|DHSC|
|**CHESS**|COVID-19 Hospitalisation in England Surveillance System|COVID|Hospital|12/03/2020 to 01/10/2022|NHSE|
|**CVAR** | COVID-19 Vaccination Adverse Reactions  | COVID |Vaccination|08/12/2020 onwards|NHSE|
|**CVS** | COVID-19 Vaccination Status| COVID|Vaccination|08/12/2020 onwards|NHSE|
|**GDPPR**|General Practice Extraction Service (GPES) Data for Pandemic Planning and Research | COVID | Primary care  | 01/06/2020 onwards|NHSE|
|**PCM**|Primary Care Medicines|COVID|Medicines|01/04/2015 onwards|NHSE| 
|**IAPT** | Improving Access to Psychological Therapies|Mental health |Talking therapies|01/04/2012 to 31/03/2023|NHSE|
|**MHSDS**| Mental Health Services Data Set |Mental health||01/04/2016 onwards|NHSE|
|***MHLDDS***|*Mental Health and Learning Disabilities Data Set*|*Mental health*| |*01/04/2015 to 31/03/2016*|*NHSE*|
|***MHMDS***|*Mental Health Minimum Data Set*|*Mental health*| |*01/04/2006 to 31/03/2015*|*NHSE*|
|**CSDS** | Community Services Data Set| Community|Mental health|01/04/2015 onwards|NHSE|                 |
|**CANCER**| Cancer Registration Data| Registration |Cancer|01/01/1971 onwards|NHSE|
|**DEMOGRAPHICS**<sup>4</sup>| Demographics Registration data| Registration|Demographics |01/06/2004 onwards|NHSE|
|**MORTALITY**<sup>4</sup>| Civil Registrations of  Death| Registration|Deaths|01/01/1993 onwards|ONS|     |
||||||||

<sup>1</sup>As documented in the data sharing agreement.  
<sup>2</sup>HESAPC includes critical care (HESAPC_ACP and HESCC) and maternity care (HESAPC_MAT).  
<sup>3</sup>NPEX and IELISA cover England, Northern Ireland, Scotland and Wales.  
<sup>4</sup>MORTALITY and DEMOGRAPHICS cover England and Wales.  
DHSC: Department of Health and Social Care; NHSE: NHS England; ONS: Office for National Statistics




