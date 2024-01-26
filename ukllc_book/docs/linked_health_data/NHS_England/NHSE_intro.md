# NHS England datasets
## Introduction  
UK LLC has a data sharing agreement with NHS England to flow extracts of the **19 datasets** listed in Table 1 into the UK LLC TRE. Although NHS England is not the owner of all the datasets (acting as data controller on behalf of the owner for some), for ease, we refer to all the datasets in these guides as NHS England datasets. **Each LPS participant has the power to opt out of linkage to their NHS England records**.  


## UK LLC documentation of NHS England datasets
We have organised our NHS England data documentation into four tiers as explained in Figure 1. This initial guide provides an overview of the NHS England datasets held in the UK LLC TRE. The [**Processing and linkage guide**](../NHS_England/Linkage%20and%20processing/) explains how LPS participants are linked to their health records and how they can opt out. The [**Coded variables guide**](../NHS_England/Coding/coding_intro.md) details the various classification systems used in NHS England datasets. The four **overview dataset guides** align with the dataset primary domains in Table 1 and provide an introduction to the hospital datasets, the COVID datasets, the registry datasets and the mental health datasets. Finally, there is a series of detailed **individual dataset guides**.  
</br>
<img src="../../images/NHSE_IntroDocumentation_Figure1.jpg" width="700"/>

**Figure 1** UK LLC documentation of the NHS England datasets is across four tiers, starting with this overview and culminating in the detailed individual dataset guides
## Overview of NHS England datasets
The NHS England datasets cover a **variety of domains and time periods** as summarised in Table 1. Their **geographic coverage is restricted to England**, apart from those listed in the footnotes. The UK LLC Data Team does **not change the names of the datasets** when they are ingested to the UK LLC TRE, apart from **SGSS** where we added COVID in front of it to distinguish it from the UK Health Security Agency's generalised Second Generation Surveillance System (SGSS). Some datasets have been renamed by NHS England, e.g. the **CHESS** dataset is now called the Severe Acute Respiratory Infection (SARI-Watch) surveillance system, but we still receive the data from NHS England as the CHESS dataset. Some datasets have alternative names, e.g. **NPEX** is also called the Covid-19 UK Non-hospital Antigen Testing Results and **iELISA** is also called the Covid-19 UK Non-hospital Antibody Testing Results. Further nomenclatural details are available in the individual dataset guides.     

**Table 1** Names, temporal coverage and availability of NHS England datasets in the UK LLC TRE (the dataset in italics is retired) 
| **Dataset name in TRE** | **Full dataset name**| **Primary  domain** | **Secondary domain** | **Data available in TRE** |**Data owner** |
|---|:---:|:---:|:---:|:---:|:---:|
| **HESOP** | Hospital Episode Statistics Outpatients| Hospital | Outpatients | 01/04/2003 onwards |NHSE|
| **HESAPC**<sup>1</sup>  | Hospital Episode Statistics Admitted Patient Care| Hospital | Admitted patients  | 01/04/1997 onwards |NHSE|
| ***HESAE*** | *Hospital Episode Statistics Accident & Emergency* | *Hospital* | *A & E patients* | *01/04/2007 to 31/10/2021* |NHSE   |
| **ECDS** | Emergency Care Data Set | Hospital | A & E patients |01/01/2020 onwards |NHSE|
| **MSDS**| Maternity Services Data Set |Maternity | Hospital | None|NHSE| 
| **NPEX**<sup>2</sup> | National Pathology Exchange (Pillar 2) |COVID |Testing| 01/06/2020 onwards|?   |
| **COVIDSGSS** | COVID-19 Second Generation Surveillance System (Pillars 1 & 2)  | COVID|Testing| 01/03/2020 onwards|NHSE|
| **IELISA**| Enzyme-Linked Immunosorbent Assay (Pillar 3) | COVID |Testing| 1/09/2020 onwards |?|
| **CHESS** | COVID-19 Hospitalisation in England Surveillance System  | COVID |Hospital| 12/03/2020 onwards |NHSE|
| **CVS** | COVID-19 Vaccination Status| COVID|Vaccination| 01/10/2020 onwards |NHS E|
| **CVAR** | COVID-19 Vaccination Adverse Reactions  | COVID |Vaccination| 08/12/2020 onwards|NHSE|
| **GDPPR**| General Practice Extraction Service (GPES) Data for Pandemic Planning and Research | COVID | Primary care  | 01/06/2020-?|NHSE|
| **PCM**| Primary Care Medicines | COVID | Medicines  | 01/04/2018 onwards|NHSE| 
| **MHSDS**<sup>3</sup> | Mental Health Services Data Set | Mental health| |? |NHSE|
| **IAPT** | Improving Access to Psychological Therapies | Mental health |Talking therapies|?|NHSE|
| **CSDS** | Community Services Data Set| Community| Mental health| ? |NHSE|                 |
| **CANCER**| Cancer Registration Data| Registry |Cancer|?|NDRS  |
| **MORTALITY**<sup>4</sup>| Civil Registrations of  Death| Registry|Deaths| ?|    |      |
| **DEMOGRAPHICS**<sup>4</sup>| Demographics Registration data| Registry| |?| ?   |
||||||||

<sup>1</sup>HESAPC includes critical care (HESAPC_ACP and HESCC) and maternity care (HESAPC_MAT).  
<sup>2</sup>NPEX covers England, Northern Ireland, Scotland and Wales.  
<sup>3</sup>Other mental health datasets that will be available are (i) Mental Health Minimum Data Set (MHMDS; 01/04/2006-31/08/2014); and (ii) Mental Health and Learning Disabilities Data Set (MHLDDS; 01/09/2014-31/12/2015).  
<sup>4</sup>MORTALITY and DEMOGRAPHICS cover England and Wales.  
NDRS: National Disease Registration Service; NHSE: NHS England




