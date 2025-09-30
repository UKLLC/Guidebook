# Understanding the GDPPR dataset
>Last modified: 29 Sep 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>The General Practice Extraction Service (GPES) Data for Pandemic Planning and Research dataset contains an extract of coded data items from primary care (GP) records from General Practices across England.</strong></div>  


## Purpose  
The GDPPR dataset was established to fulfil the need for GP data for planning and research in response to the COVID-19 pandemic. It is an extract of data from GP systems (using the generic data extraction service 'GPES') and based on a set of business rules specifying the target group of patients, the coded record content and time period cut-offs.

GDPPR was established in 2020 with data extracted from GP systems fortnightly until March 2024, when it changed to a monthly extraction. Information on the recency of GDPPR data held by UK LLC is available [here](../GDPPR/GDPPR.ipynb).

## Scope  
Not all people registered with a GP in England have information about them included in the GDPPR extract. In order for an individual’s data to be included in an extract, each of these four conditions must be met:  
* The GP practice at which they are registered has to ‘opt in’ to inclusion in the GDPPR by accepting the offer to participate via the NHS’s online reporting and payments system for primary care (the Calculating Quality Reporting Service). The proportion of GP practices included in recent GDPPR extracts is not publicly available, however, the GDPPR Management Information (MI) report<sup>1</sup>, dated September 2020, indicates that 97.5% of GP practices and 93.5% of registered patients were included in the GDPPR extract.

* The patient must have an active, current registration at a participating GP practice or, for deceased patients, have a date of death after 31st October 2019.  

* The patient must not have ‘opted out’ of their information being shared outside their GP practice for purposes other than direct care (a Type 1 data opt-out). 

* The patient’s records are included only where they include medical (SNOMED) codes that match the codes defined by the [Code Clusters](#measures-code-clusters) applicable for the GDPPR extract. Patient information that is not relevant is excluded from the extract.  

>A participant’s **absence** from the GDPPR dataset is not an indication that they either are not registered with a GP or that they have not been diagnosed with a specific condition. 

## Measures (Code Clusters)  
The GDPPR dataset uses [SNOMED CT](../../Coding/coding_intro.md) codes. 

The coded information included in each GDPPR extract is specified by the **Code Clusters** specified for the COVID-19 planning and research extract. Similar SNOMED codes are grouped into 'clusters', with clusters being further grouped into **Cluster Categories**. (For example, the clusters BMI_COD (Body mass index codes) and ANXSCRN_COD (Anxiety screening codes) both fall within the cluster category ‘Observation measurement assessment and screening’.) 

>Most SNOMED codes are in more than one code cluster, but each cluster is only in one cluster category.

The rules and logic governing patient inclusion and extracted record content is provided by the 'GPES Extract for pandemic planning and research_business rules v2.0'<sup>2</sup> (or a more recent version). For some codes, the business rules document defines time-based cut offs (e.g. only occurrences in the last two years are included). Where there is no time-based cut off, all instances of a relevant code are included.

>The number of UK LLC participants included in the current GDPPR extract is summarised [elsewhere](../../Primary_care_datasets/GDPPR/GDPPR.ipynb) in Guidebook. 

## SNOMED CT codes included in the GDPPR  
All releases of the SNOMED CT code clusters are available online via the NHS [**TRUD**]([https://isd.digital.nhs.uk/trud/users/guest/filters/0/home) (Technology Reference Update Distribution). UK LLC has downloaded Release 51.0.0<sup>3</sup> and made it available as a [downloadable text file](https://apply.ukllc.ac.uk/apply/view_document/gdppr).  

>This material includes SNOMED Clinical Terms® (SNOMED CT®) which is used by permission of the International Health Terminology Standards Development Organisation (IHTSDO). All rights reserved. SNOMED CT®, was originally created by The College of American Pathologists. "SNOMED" and "SNOMED CT" are registered trademarks of the IHTSDO.      


Please note that code clusters and cluster categories are not currently included in the GDPPR dataset in the TRE. UK LLC is planning on making this information available later this year.  

## Additional information  
A GDPPR ‘Useful Information & DQ Notes’ can be accessed via the [NHS GDPPR guide for analysts and users of the data](https://digital.nhs.uk/coronavirus/gpes-data-for-pandemic-planning-and-research/guide-for-analysts-and-users-of-the-data). It should be noted that the document refers to full GDPPR extract, not just the subset available in the UK LLC TRE.

The full list of SNOMED CT code clusters - not just those included in the GDPPR dataset - can be explored via an NHS England dashboard: [**Microsoft Power BI**](https://app.powerbi.com/view?r=eyJrIjoiMjY4OTRhNmUtZDdiMy00NzVhLTkzMmMtZmRhMzAyOWFkZjc4IiwidCI6IjM3YzM1NGIyLTg1YjAtNDdmNS1iMjIyLTA3YjQ4ZDc3NGVlMyJ9). 

**Notes**  
<sup>1</sup> Available to download from: <https://digital.nhs.uk/coronavirus/gpes-data-for-pandemic-planning-and-research/guide-for-analysts-and-users-of-the-data>  

<sup>2</sup> Available to download from: <https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-collections/quality-and-outcomes-framework-qof#other-extracts>  

<sup>3</sup> N.B. Release 51.0.0 is dated 15.02.2024, while UK LLC’s GDPPR data was extracted on 26.04.2024. There is a chance that some of the drug cluster content may have changed slightly between the two dates because drug reference sets are released more frequently than the broader Primary Care Domain reference sets.