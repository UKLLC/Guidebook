# Understanding the GDPPR dataset
>Last modified: 09 Feb 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The General Practice Extraction Service (GPES) Data for Pandemic Planning and Research dataset contains an extract of coded data items from primary care (GP) records from General Practices across England.</strong></div>  

## 1. Introduction
The GDPPR dataset was established to fulfil the need for GP data for planning and research in response to the **COVID-19 pandemic**. It is an extract of data from GP systems (using the generic data extraction service 'GPES') and based on a set of business rules specifying the target group of patients, the coded record content and time period cut-offs.

<aside class="admonition danger"><p class="admonition-title">The GDPPR dataset can only be used for research related to COVID-19</p>For all restrictions and examples of research purposes acceptable to NHS England see the <strong><a href="https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/secretary-of-state-directions/covid-19-public-health-directions-2020" target="_blank" rel="noopener noreferrer">COVID-19 Public Health Directions 2020</a></strong></aside>

## 2. Strengths of GDPPR
* The dataset is relatively simple, comprising just one table with 23 variables
* It includes coded information on diagnoses, test results and demographics from the majority of GP practices in England
* Although not comprehensive, the GDPPR does contain some 43,000 unique SNOMED codes, grouped into over 400 clusters
* The use of SNOMED codes ensures consistency and enables international comparisons

## 3. Limitations of GDPPR
* The GDPPR extract can currently only be used for research related to COVID-19
* Not all people registered with a GP in England have information about them included in the GDPPR extract  
* Because of GDPPR's strict [inclusion criteria](#4-scope-and-coverage), a participant's **absence** from the GDPPR dataset is not an indication that they either are not registered with a GP or that they have not been diagnosed with a specific condition 

## 4. Scope and coverage
Individuals' data are included in a GDPPR extract if each of these **four conditions** are met:  
* The **GP practice** at which they are registered has ‘opted in’ to inclusion in the GDPPR by accepting the offer to participate via the NHS’s online reporting and payments system for primary care (the Calculating Quality Reporting Service).  
The proportion of GP practices included in recent GDPPR extracts is not publicly available, however, the GDPPR Management Information (MI) report<sup>1</sup>, dated September 2020, indicates that 97.5% of GP practices and **93.5% of registered patients** were included in the GDPPR extract.

* Patients must have an active, current registration at a participating GP practice or, for deceased patients, have a date of death after 31st October 2019.  

* Patients must not have ‘opted out’ of their information being shared outside their GP practice for purposes other than direct care (a Type 1 data opt-out). 

* Patients' records are included only where they include medical (SNOMED) codes that match the codes defined by the [Code Clusters](#code-clusters) applicable for the GDPPR extract. Patient information that is not relevant is excluded from the extract.  
 
The **rules and logic governing patient inclusion and extracted record content** is provided by the 'GPES Extract for pandemic planning and research_business rules v2.0'<sup>2</sup> (or a more recent version). For some codes, the business rules document defines time-based cut offs (e.g. only occurrences in the last two years are included). Where there is no time-based cut off, all instances of a relevant code are included.  

## 5. Data collection methodology
GPES data are extracted automatically from GP's clinical systems (such as EMIS and TPP) where GPs and other practice staff record interactions with patients (e.g. appointments, medical conditions, test results). This system collects coded information from the majority of GP practices across England, and is used for a range of purposes including GP payments, service planning and monitoring, and research.  

## 6. Structure of the dataset
The GDPPR dataset comprises one row per primary care 'event', such as a diagnosis, test result or blood pressure measurement. Each time an individual is in contact with their GP, at least one line of data is added to the underlying GPES dataset. One GP visit (or phonecall) can generate multiple lines of data when more than one health issue is addressed as part of a single interaction.

## 7. Coding systems used
The GDPPR dataset uses [**SNOMED CT**](../../Coding/coding_intro.md) (Systematized Nomenclature of Medicine Clinical Terms), usually abbreviated to just **SNOMED**. It is an international system used to classify many types of medical data, including diagnoses, procedures, symptoms, family history, assessment tools, observations and medications.  

The **UK edition** of SNOMED CT contains the UK extensions, which include UK-specific screening procedures and assessment scales. SNOMED CT is designed for direct management and care of patients. The codes are numeric, typically between 6 and 18 digits long, and do not follow a pattern or hierarchy.

### Code Clusters  
The coded information included in each GDPPR extract is specified by the **Code Clusters** identified for the COVID-19 planning and research extract. Similar SNOMED codes are grouped into 'clusters', with clusters being further grouped into **Cluster Categories**. (For example, the clusters BMI_COD (Body mass index codes) and ANXSCRN_COD (Anxiety screening codes) both fall within the cluster category ‘Observation measurement assessment and screening’.) 

**Most SNOMED codes are in more than one code cluster, but each cluster is only in one cluster category.**

## 8. Evolution of the dataset
The GDPPR dataset was established in 2020 to support immediate COVID-19 planning and research. Data were extracted from GP systems fortnightly until March 2024, when it changed to a monthly extraction.  

The **[code clusters](#code-clusters) are updated regularly** to refine definitions, add new COVID‑19 related measures, and improve consistency across GP practices. All releases code clusters are available online via the NHS [**TRUD**]([https://isd.digital.nhs.uk/trud/users/guest/filters/0/home) (Technology Reference Update Distribution). UK LLC has downloaded Release 51.0.0<sup>3</sup> and made it available as a [downloadable text file](https://apply.ukllc.ac.uk/apply/view_document/gdppr).  

>This material includes SNOMED Clinical Terms® (SNOMED CT®) which is used by permission of the International Health Terminology Standards Development Organisation (IHTSDO). All rights reserved. SNOMED CT®, was originally created by The College of American Pathologists. "SNOMED" and "SNOMED CT" are registered trademarks of the IHTSDO.      

## 9. Availability in the UK LLC TRE
The UK LLC TRE holds an extract of the GDPPR dataset, going back to the 1940s. The GDPPR records of participants in UK LLC’s partner LPS, where individual or LPS permissions allow linkage to NHS data, are included in the TRE. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHSE data not be shared via UK LLC.

**Note**: information on code clusters and cluster categories is not currently included in the GDPPR dataset in the TRE. UK LLC is planning on making this information available early in 2026. 

## 10. Missing information
* **Variable and value labels**  
UK LLC is infilling missing variable and value labels in the NHSE datasets in the TRE. Where variable labels have been added by UK LLC, rather than being found in NHSE documentation, this is made apparent in the variable label.  
* **Missing data**  
The amount of missing data varies widely between variables and across datasets. Throughout 2026, we will update this section with information about missingness in GDPPR.  

## 11. Tips for researchers using GDPPR in the UK LLC TRE
Researchers should be mindful of the fact that GDPPR is not a complete record of an LPS participant's interaction with their GP practice. The records included are restricted to the codes included in the GDPPR business rules applicable at the time of data extraction.  

>When applying to access GDPPR data in the UK LLC TRE, researchers must [**submit a codelist**](../../Coding/codelists.md) specifying the **SNOMED** codes which are relevant to their research question. 

**Note**: Information about medicines prescribed in primary care is available in the [PCM](../PCM/PCM.ipynb) dataset. Using the two datasets together will provide a more comprehensive picture of participants' interactions with primary care providers than will using GDPPR alone.  

## 12. Useful syntax
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the <a href="https://github.com/UKLLC" target="_blank" rel="noopener noreferrer">UK LLC Github</a> repository where you can find the full scripts.

The <a href="https://github.com/NHSDigital/GDPPR_Analytical_Code" target="_blank" rel="noopener noreferrer">NHS England Github</a> also makes code publicly available to prevent duplication of work and to increase consistency of methodology between users of the datasets.


## 13. Further reading
A GDPPR **‘Useful Information & DQ Notes’** can be accessed via the [NHS GDPPR guide for analysts and users of the data](https://digital.nhs.uk/coronavirus/gpes-data-for-pandemic-planning-and-research/guide-for-analysts-and-users-of-the-data). It should be noted that the document refers to full GDPPR extract, not just the subset available in the UK LLC TRE.

The full list of SNOMED CT code clusters - not just those included in the GDPPR dataset - can be explored via an NHS England dashboard: [**Microsoft Power BI**](https://app.powerbi.com/view?r=eyJrIjoiMjY4OTRhNmUtZDdiMy00NzVhLTkzMmMtZmRhMzAyOWFkZjc4IiwidCI6IjM3YzM1NGIyLTg1YjAtNDdmNS1iMjIyLTA3YjQ4ZDc3NGVlMyJ9). 

<br>  

**NOTES**  
<sup>1</sup> Available to download from: <https://digital.nhs.uk/coronavirus/gpes-data-for-pandemic-planning-and-research/guide-for-analysts-and-users-of-the-data> 

<sup>2</sup> Available to download from: <https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof#other-extracts>  

<sup>3</sup> N.B. Release 51.0.0 is dated 15.02.2024, while UK LLC’s GDPPR data was extracted on 26.04.2024. There is a chance that some of the drug cluster content may have changed slightly between the two dates because drug reference sets are released more frequently than the broader Primary Care Domain reference sets.