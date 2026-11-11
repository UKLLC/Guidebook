# NHS England linkage rates

>Last modified: 03 Nov 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>A comparison of the 2024 and 2026 linkages to NHSE records.</strong></div>

## Introduction  
>UK LLC has compared linkage rates across the two most recent UK LLC linkages:  
Version 3 ('v3') dated 4 July 2024 and Version 4 ('v4') dated 23 April 2026.

### Overview of LPS participant counts and linkage rates
**NHSE linkage v3**  
•	318,337 total LPS participants in the UK LLC TRE  
•	271,946 (85.4%) had permission to link to their NHSE records  
•	250,522 (92.1%) of those with permissions in place were linked to their NHS records.

**NHSE linkage v4**  
•	412,179 total LPS participants in the UK LLC TRE  
•	352,435 (85.5%) had permission to link to their NHSE records *  
•	311,863 (88.5%) of those with permissions in place were linked to their NHS records.  

<sup>*</sup> A total of n=363,030 LPS participants gave permission to link to their NHSE records. However, n=10,595 (2.9%) of these were removed from the linkage process by a change in study-level permissions.

### Increase in number of participants linked to NHSE data
The new linkage to v4 produced **an increase of n=61,341 LPS participants with linked NHSE data**, an uplift of 24.5% compared to v3 (Table 1). While LPS participants new to UK LLC comprised the vast majority of these new linkages, there were also n=2,232 participants who had not linked at v3 despite permissions being in place, and n=1,977 whose permissions were updated between the two linkages to facilitate successful linkage for v4.

**Table 1** LPS participants included in UK LLC at the point of NHSE linkage v4  
| v4 linkage status: | Consent & linkage | S251 & linkage | Permission in<br> place but not linked | No linkage permission | TOTAL |
|---|--:|--:|--:|--:|--:|
| Participants in the UK LLC TRE at v4 | 271,318 | 40,545 | 40,572 | 59,744 | 412,179 |
| Participants <b>added</b> to the TRE since v3 linkage | 75,639 | 439 | 13,171 | 4,593 | 93,842 |  
|
| Participants present in the TRE at v3 linkage | 195,679 | 40,106 | 27,401 | 55,151 | 318,337 |
| <b>v3 linkage status:</b> |
| Consent & linkage | <b>191,726 | 0 | 7,450 | 10,855 | 210,031 |
| S251 & linkage | 296 | <b>39,554 | 559 | 82 | 40,491 |
| Permission in place but not linked | 1,694 | 538 | <b>19,126 | 66 | 21,424 |
| No linkage permission | 1,963 | 14 | 266 | <b>44,148 | 46,391 |

### Comparison population: those with permission to link in both freezes
Among participants who were present in the TRE for the v3 linkage (shown in the lower half of Table 1), the number successfully linked to NHSE data fell from 250,522 to 235,785.

The linkage permissions and linkage status remained unchanged for the majority of participants (92.5%, n=294,554) as shown in bold. Among the 23,783 whose linkage status changed (i.e., from linked to not linked or vice versa), more than three-quarters (n=7,450) were not in linked to NHSE data in v4 despite having been successfully linked in v3 and their consent status being unchanged. 

While some of the reasons underpinning this change in linkage rates, cannot immediately be explained, there is one factor which explains nearly 30% of this discrepancy.

**LPS participants’ NHS number no longer present (29.5%, n=2,199)**  
NHS numbers included in n=2,199 LPS participants' identifiers in v3 were not included in v4. This primarily affected the four cohorts run by <a href="https://cls.ucl.ac.uk/" target="_blank" rel="noopener noreferrer">CLS (the Centre for Longitudinal Studies)</a>: BCS70, MCS, NCDS58 and NEXTSTEP. Sharing participants’ NHS numbers is not compatible with these LPS' existing Data Sharing Agreements (DSA) with NHSE.

**Table 2** Counts of participants where NHS numbers were removed from identifiers between v3 and v4 of the NHSE linkage
<div style="width:fit-content">

| LPS | n* |
|---| --:|
| [**NCDS58**](../../../lps_data/lps_profiles/ncds58.ipynb) | 830 |
| [**MCS**](../../../lps_data/lps_profiles/mcs.ipynb) | 650 |
| [**NEXTSTEP**](../../../lps_data/lps_profiles/nextstep.ipynb) | 440 |
| [**BCS70**](../../../lps_data/lps_profiles/bcs70.ipynb) | 280 |
|
| [**GLAD**](../../../lps_data/lps_profiles/glad.ipynb) | < 10 |
|
| Total | 2,200 |  

</div>

<sup>*</sup> <small>Figures rounded to the nearest 10 for disclosure control.</small>  


There is no clear pattern explaining why a further 5,251 participants were linked to their NHSE data in v3 but not in v4. UK LLC has examined changes in the validity of participants' address fields (e.g., address line 1, postcode) to see if there were any notable differences between the two linkages<sup>1</sup>. However, the number of valid address items provided by partner LPS increased between v3 and v4, so this in itself does not explain the discrepancy.  

It should be noted, however, that the validity flag provided by DCHW is binary and only indicates whether there is a value in each field; it provides no indication of the quality of the information provided. It may be, therefore, that provision of more address information could have a negative impact on linkage rates if the information provided is inaccurate.

### Conclusion
With the exception of the n=2,199 participants for whom NHS numbers were included as identifiers for v3 linkage but not for v4, it seems probable that the drop in linkage rates for this group is due to a change in NHSE’s linkage processes rather than any change in the identifiers supplied by partner LPS.  

UK LLC is working with NHSE to:  
•	Better understand the linkage process;  
•	Flow linkage quality metrics alongside the linked NHSE data to explain at what point in the linkage process a link was established; and  
•	Ingest NHSE validation reports into the TRE, indicating why some participants cannot be linked to NHSE data.

**Footnote**  
<sup>1</sup> LPS participants' NHS numbers and addresses, along with other personal identifiers, are used by DCHW to link to their NHSE records. UK LLC does not have any access to this identifiable information. DCHW shares with UK LLC only derived variables which indicate whether a field is valid.
