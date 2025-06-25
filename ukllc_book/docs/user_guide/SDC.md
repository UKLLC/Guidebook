# Statistical Disclosure Control (SDC)
>Last modified: 25 Jun 2025


<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>UK LLC enforces strict SDC rules on all data leaving the TRE</strong></div style>  
<br>

Statistical Disclosure is defined as information about an identifiable individual being released, either directly or indirectly, through a statistical output from a secure environment. 

UK LLC’s SDC threshold is **10 data subjects**. Any output (including tables, charts, and text) which include counts <10, including zero, cannot be removed from the TRE. File Out requests which include counts <10 will be rejected by the SDC reviewers, and the researcher asked to resubmit their request. 


>The most common reasons for a File Out request being rejected are:  
>1. **Low counts** (counts <10 included in the output)  
>2. **Masking issues** (low counts have been suppressed but can be derived from the information presented)  
>3. **Insufficient information** provided (so the reviewer is unable to fully understand the output)  


***
**Low counts** can be avoided by:  

* Aggregating / combining categories (so each category includes 10+ observations) 

* Averaging values (so outliers are modified) 

* Rounding values (to reduce specificity) 

* Suppressing or masking values  

N.B. Low counts also include percentages referring to <10 individuals, even if the actual counts are not presented. In all outputs means, media, modes, standard deviations and variances should only be reported where they are based on a count of at least 10.

***

**Masking (suppression)** can be used to avoid combining categories, or using rounded or averaged figures.  
When suppressing figures in a table or chart: 

* Usually two or more categories should be suppressed so original counts cannot be deduced 

* In tables, masking will need to be done both row-wise and column-wise so counts cannot be back-calculated  
<br>

To ensure File Out requests meet SDC requirements, all counts <10 should be masked. For masking to be effective: 
* It should be impossible for a reader to deduce any value <10 from the information provided  

* A distinctive symbol (~ * $) needs to be used to indicate where counts have been masked 

* A zero (0) is an ambiguous value of suppression and should be avoided 

* There should be a clear note regarding what the masking symbol indicates (e.g. “counts <10 including zero”) 

***

It is important that **sufficient information** is provided with a File Out for SDC reviewers to make sense of the outputs: 

* provide definitions of variable names and acronyms, and enough information to put the outputs in context 

* If outputs include numbers <10 that are not disclosive, e.g. if they are part of a correlation coefficient, it is helpful to add an explanation of why the information is not disclosive. This should be made explicit as the reader may not be familiar with the statistical techniques used. 

***

**Further information** is available from: 
* The [**SDC Handbook**](https://securedatagroup.org/sdc-handbook/) produced by the Safe Data Access Professionals network 

* The [**SRS Output Checking Guidance Document Work strand: Statistical Disclosure Control**](https://www.ons.gov.uk/aboutus/whatwedo/statistics/requestingstatistics/secureresearchservice/gettingyourresearchoutputsapproved) produced by the ONS.   

 