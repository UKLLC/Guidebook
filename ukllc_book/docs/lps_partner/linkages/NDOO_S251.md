# Legal bases for linkage to NHSE records (Draft Nov26)
>Last modified: 17 Nov 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>How National Data Opt Outs affect the linkage of participants' health records.</strong></div>
<br>

NHS England’s <a href="https://digital.nhs.uk/services/national-data-opt-out" target="_blank" rel="noopener noreferrer">National Data Opt-Out (NDOO)</a> scheme enables individuals to request that their health records are not shared for research purposes. The national <a href="https://digital.nhs.uk/dashboards/national-data-opt-out-open-data" target="_blank" rel="noopener noreferrer">NDOO rate</a> is currently 5.7% of the adult population. 


In UK LLC, existing NDOOs are over-ridden in cases where people have given **explicit consent** to data linkage, meaning that their health records can be shared for research. This applies to the vast majority of LPS participants whose data are included in the UK LLC Trusted Research Environment (TRE).  

However, participants from some LPS<Sup>1</sup> have not consented to NHSE record linkage but are included via <a href="https://www.hra.nhs.uk/about-us/committees-and-services/confidentiality-advisory-group/confidential-patient-information-and-regulations/" target="_blank" rel="noopener noreferrer">Section 251</a> (S251) support.  

<aside class="admonition note"><p class="admonition-title">Section 251 allows the disclosure of confidential patient information for medical purposes in the public interest where it is not possible to use anonymised information and not practical to obtain consent.</p></aside> 

For those who have **not explicitly consented** to linkage<sup>2</sup>, and who have an NDOO in place, the NDOO is respected and no health records are linked. These participants are filtered out by NHS England ensuring that their health records will not flow to UK LLC. This application of the NDOO means that linkage rates are likely to be lower for 'S251 participants' than for others. 

**Identifying NDOO participants in the UK LLC TRE**  
UK LLC's reference dataset ['Study Permissions'](../../ukllc_managed_data/datasets/nhse_reference/study_permissions.ipynb) contains the binary variable 'national_opt_out': 
* A value of '0' means the participant has explicitly consented to health record linkage and, if they have an NDOO in place, the NDOO is over-ridden. 
* A value of '1' means that the participant's data have flowed for linkage under S251 and, if they have an NDOO in place, it is respected and health records are not linked. 

<br> 

>**Notes**  
<sup>1</sup> ALSPAC, CaPS, EPICN, NSHD46, TEDS AND TWINSUK include 'S251 participants'.   
<sup>2</sup> e.g. participants who may have been asked to 'opt-out' of linkage rather than to 'opt-in'. 
