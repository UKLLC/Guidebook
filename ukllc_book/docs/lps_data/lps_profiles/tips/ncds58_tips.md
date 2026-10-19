# NCDS58: tips and FAQs
>Last modified: 19 Oct 2026

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>Useful tips for working with NCDS58 data.</strong></div style>  
<br>

**Linking child-level tables**  

There are two child-level tables in the NCDS58 data:

* ncds58_ncds5_mother_child_vXXXX_1_YYYYMMDD
* ncds58_ncds5_mother_child_vXXXX_2_YYYYMMDD. 

These do not conform to the convention that tables split as part of the TRE loading process can be joined by the key identifier LLC_xxxx_stud_id alone. As the variable LLC_xxxx_stud_id is at the parent-level, these two tables require a **join on two fields**: 

* LLC_xxxx_stud_id, and 
* person

