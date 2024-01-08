# Processing and linkage to NHS England datasets
## Submission and general processing of NHS England datasets
Datasets are submitted by health and social care organisations via a range of pathways, including upload to the [Seconday Uses Service (SUS)](https://digital.nhs.uk/services/secondary-uses-service-sus), the [Strategic Data Collection Service in the cloud (SDCS Cloud)](https://digital.nhs.uk/services/strategic-data-collection-service-in-the-cloud-sdcs-cloud) or the [Message Exchange for Social Care and Health (MESH)](https://digital.nhs.uk/services/message-exchange-for-social-care-and-health-mesh). The degree of data validation and derivation of variables depends on the dataset, as described in the individual dataset guides (where this information is available from NHS England).  

## Flow of LPS participants' NHS England data into the UK LLC TRE
Flows of data from contributing Longitudinal Population Studies (LPS) and NHS England are conducted through a ‘split file’ protocol where the **flow of LPS participants' identifiers (File 1s)** is entirely separate from the **flow of LPS participants' NHS England data (File 2s)** - see figure 1. Updates to NHS England datasets flow on a **quarterly basis** into the UK LLC TRE. 

<img src="../../../images/Linkage_UKLLCDataFlows_Figure1.jpg" width="600"/>

**Figure 1** An overview of the flow of LPS participants' NHS England data into the UK LLC TRE  

### 1. Each LPS sends a File 1 to DHCW

Each LPS generates a **File 1**, containing only **participant identifiers** (NHS number, name, date of birth, sex and address) and **permission flags** (set at the LPS or participant level) and sends it securely to UK LLC's Trusted Third Party, **NHS Digital Health and Care Wales (DHCW)**. As detailed below in the opt out section, LPS can send updated File 1s prior to each quarterly flow of NHS England data.  

### 2. DHCW acts as UK LLC's linkage broker

DHCW encrypts the STUDY_IDs and sends an ID mapping file, containing the encrypted STUDY_IDs, to Swansea University. DHCW acts as UK LLC's **linkage broker** by sending a permission-filtered file of unique identifiers and encrypted STUDY_IDs (the NHS Output) to NHS England for linkage and extraction of datasets. 

### 3. NHS England's MPS links LPS participants to their health records 
As described below, NHS England's [**Master Person Service (MPS)**](https://digital.nhs.uk/services/personal-demographics-service/master-person-service) uses each LPS participant's information in the NHS output from DHCW to derive a unique **Person_ID** to standardise linkage across all the different NHS England datasets.   

The MPS first tries to match the participant to their record in the [**Personal Demographics Service (PDS) database**](https://digital.nhs.uk/services/personal-demographics-service) - the national database of all NHS patients in England, Wales and the Isle of Man, which holds NHS numbers and basic demographic details such as date of birth, name, sex and address. If a perfect match of NHS number and date of birth cannot be found, more complex algorithms are used to try to identify the most likely PDS record based on other information. If the similarity is acceptable, the matched record is returned. If not, the algorithm proceeds instead to look for similarities with previously unmatched records stored in the **MPS record bucket**, a separate dataset. An MPS-ID is generated if a matching record is found or if there is sufficient information to generate a new MPS-ID. If neither search is successful, a one-time-use ID is generated.   

The unique **Person_ID** derived by the MPS for each LPS participant therefore corresponds to: (i) their **NHS number** from the PDS; or (ii) the **MPS-ID** from the MPS record bucket; or (iii) a **one-time-use ID**.  

See [The Person_ID Handbook for HES users](https://digital.nhs.uk/binaries/content/assets/website-assets/services/mps/the-person_id-handbook-for-hes-users-v1.0.4.pdf) for more details about the algorithms MPS uses to derive a Person_ID. The accuracy of matching will be higher for datasets that reliably have accurate NHS numbers attached, compared to those that rely on other personal identifiers, which may be incomplete, inconsistently recorded or not unique.

NHS England uses the Person_ID to create extractions of datasets and sends these as **File 2s containing LPS participants' de-identified health data** and the encrypted STUDY_ID, to Swansea University for re-encryption of the STUDY_IDs and preparation of the data for **ingest into the UK LLC TRE**. 

NHS England is developing a product called **MPS Diagnostics** which will document how the Person_ID was created for each LPS participant. When this is available, we will update this guide.   

### 4. Swansea University receives and uploads data according to UK LLC specifications
While the linkage process is the same for all datasets, the subsequent data pipelines are bespoke for each of the datasets according to UK LLC specifications.   

The Population Data Science Development Team at Swansea University receives and uploads LPS participants' deidentified NHS England records to the UK LLC database following **variable-level rules** detailed in specification documents provided by UK LLC. The rules require Swansea to **encrypt or exclude particular variables** to protect the anonymity of LPS participants. Geographical units smaller than region or strategic health authority are routinely encrypted - this includes Lower-layer Super Output Areas (LSOAs). These encrypted variables are useful because they can be used in grouping/multi-level modelling. Other variables deemed to pose a risk to disclosure that don't have value in an encrypted form are excluded.

### 5. Management and curation of data by the UK LLC Data Team
The UK LLC Data Team checks that all the NHS England data that are uploaded to the UK LLC database align with the data sharing agreement between NHS England and the University of Bristol. They also perform the following tasks:   
* **Clean and deduplicate data, table names and structures** to enable data provisioning in an efficient manner while maintaining data integrity.    
* **Load and integrate variable and value labelling**, where available from the NHS API and other web sources, into master metadata tables.  
* **Run the automated disclosure control risk assessment** and manually review all flagged risks.  

## LPS participants can opt out of linkage to their NHS England data
LPS can send **quarterly updates** of their File 1s (participant identifiers and permission flags) to DHCW. If a participant has decided to **opt out** of UK LLC altogether or to opt out of linkage to their NHS records, or conversely has decided to **opt into** linkage to their NHS records, their instructions are communicated to **NHS England** in a **delta file**, which is based on the permission flags in the File 1. If a participant opts out, no further data about them will flow into the UK LLC TRE and the participant’s data will not be provisioned to new research projects. However, researchers who already have access to that individual’s information will be permitted to retain that access until the end of the project, but they will not obtain any new data about that individual.   

While some LPS that contribute data to UK LLC’s TRE only use consent to determine inclusion of participants in the UK LLC TRE, other LPS operate a blended consent/section 251 (for English and Welsh participants) model to reduce bias and to improve research inclusivity. **NHS National Data Opt Out** is applied to all NHS data extractions, which means that any participant included using s251 as a legal basis is excluded if they have set a national data opt-out. 