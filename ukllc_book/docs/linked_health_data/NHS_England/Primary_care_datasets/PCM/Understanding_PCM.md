# Understanding the Primary Care Medicines (PCM) Dataset
>Last modified: 09 Feb 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>PCM is a record of prescriptions dispensed and fulfilled in community settings in England.</strong></div>  

## 1. Introduction
The Primary Care Medicines (PCM) Dataset was introduced in April 2015, and comprises patient-level data about prescriptions submitted to the NHS Business Services Authority (NHSBA) for reimbursement. It includes all prescriptions dispensed in England, including those written elsewhere in the U.K. and vice versa.  

<aside class="admonition warning"><p class="admonition-title">PCM is primarily a financial dataset; data are collected for the reimbursement of medicines dispensed</p>As with all NHS England datasets, it is not designed to be used for research.</aside>

## 2. Strengths of PCM  
1) It provides complete coverage of all prescriptions dispensed in community settings in England
2) It includes data from GPs, dentists, hospital clinics and community clinics
3) It contains detailed information about medicines prescribed, including codes (BNF and dm+d), quantities and costs
4) It is longitudinal making it possible for researchers to study cohorts over time

## 3. Limitations of PCM
1) The dataset does not include prescriptions dispensed by hospitals
2) It captures medicines dispensed rather than medicines prescribed, so any variation from the prescriber's intention is lost
3) It does not include prescriptions that were written but not dispensed
4) There are coding inconsistencies both between organisations and over time
5) PCM does not contain any information on diagnoses
6) Non-prescription ('over the counter') medications are not included in PCM

## 4. Scope and coverage
The dataset contains patient-level information about:  
* name of medicines dispensed (and whether proprietory or generic)
* medicine formulation, strength and quantity
* costs
* date of precription processing
* type of dispenser (e.g. community pharmacy, GP, dentist)

## 5. Data collection methodology
The NHSBSA extracts information for the PCM dataset based on reimbursement claims. These claims are submitted by primary care dispensers. Only prescriptions submitted for reimbursement are included in the dataset. 
  
## 6. Structure of the dataset
Each record (line) represents a single dispensed item. Information available for each item includes:
* codes for the dispensing pharmacy and LSOA (encrypted in the UK LLC TRE)
* costs: including amount paid, any exemptions from payment, and actual cost to the NHS
* information about the dispensed medicine: including [BNF and dm+d codes](#7-coding-systems-used), name, strength and quantity
* the patient's age and gender

## 7. Coding systems used
The PCM dataset uses coding systems from both the **dm+d** (NHS Dictionary of Medicines and Devices) and the **BNF** (British National Formulary). 

The **dm+d** is a subset of **SNOMED** codes, and is currently limited to medicines licensed for use in the UK. Codes are in numeric format, e.g. ‘39732311000001104’ represents ‘Amoxicillin 250mg capsules’. 

The **BNF** is used by healthcare professionals as a reference when prescribing medications. BNF codes are hierarchical and alphanumeric, reflecting the BNF chapter and section structure.

## 8. Evolution of the dataset
The PCM data has been collected consistently since 2015. It is a very stable dataset, having comprised the same 57 variables since its inception. 

## 9. Availability in the UK LLC TRE
The UK LLC TRE holds an extract of the PCM, going back to 2015. The PCM records of participants in UK LLC's partner LPS, where individual or LPS permissions allow linkage to NHS data, are included in the TRE. UK LLC does not hold any information about people who are not part of a partner LPS or about LPS participants who have requested that their NHSE data not be shared via UK LLC.

More detailed information about the UK LLC's PCM extract is [here](../PCM/PCM.ipynb).

## 10. Missing information
* **Variable and value labels**  
UK LLC is infilling missing variable and value labels in the NHSE datasets in the TRE. Where variable labels have been added by UK LLC, rather than being found in NHSE documentation, this is made apparent in the variable label.  
* **Missing data**  
The amount of missing data varies widely between variables and across datasets. Throughout 2026, we will update this section with information about missingness in the PCM dataset.


## 11. Tips for researchers using PCM in the UK LLC TRE
>When applying to access linked PCM data in the UK LLC TRE, researchers must [**submit a codelist**](../../Coding/codelists.md) specifying the **BNF** codes which are relevant to their research question. 


**Key variables in the PCM dataset**
| Variable name | Variable label |
|---|---|
| prescribedbnfcode | BNF code of the medicine or appliance prescribed 
| prescribedbnfname | Name of the prescribed medicine or appliance
| prescribeddmdcode | dm+d code of the medicine prescribed
| prescribedformulation | Formulation of the medicine prescribed
| prescribedquantity | Quantity of medicine prescribed

**Note:** Information about conditions diagnosed in primary care is available in the [GDPPR](../GDPPR/GDPPR.ipynb) dataset. Although GDPPR is restricted to COVID-19 research only, using the two datasets together will provide a more comprehensive picture of participants’ interactions with primary care providers than will using PCM alone.  

## 12. Useful syntax
Below we will include syntax that may be helpful to other researchers in the UK LLC TRE. For longer scripts, we will include a snippet of the code plus a link to the <a href="https://github.com/UKLLC" target="_blank" rel="noopener noreferrer">UK LLC Github</a> repository where you can find the full scripts.

## 13. Further reading  
Information in this section will be added in due course.