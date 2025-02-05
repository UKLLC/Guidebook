# Working with LPS data
>Last modified: 05 Feb 2025

<details>
<summary>Why are there duplicate study IDs in my LPS dataset?</summary>

In most cases LPS data is one row per person. However, there are a few exceptions. Please check the relevant LPS documentation associated with the dataset you are working on.
</details>

<details>
<summary>Are there quirks in some datasets?</summary>

This section is work-in-progress and will be updated as further quirks are brought to our attention – if you identify quirks, please notify the UK LLC Data Team [**support@ukllc.ac.uk**](mailto:support@ukllc.ac.uk)

#### Quirk 1: ncds58_ncds5_mother_child_v0001
Datasets which are >1000 variables wide are split on loading to the UKSERPUKLLC database due to SQL field limit of 1024. Where this is the case the table name will contain a _1_, _2_ etc nested between the version and date in the table name. In most cases the 2 (or more) parts can be merged/joined on LLC_XXXX_stud_id. This can be done when the table has a 1-row per participant structure.   

The following table(s) is/are an exception to this:
* ncds58_ncds5_mother_child_vXXXX_1_YYYYMMDD
* ncds58_ncds5_mother_child_vXXXX_2_YYYYMMDD. 

These data require a join on 2 fields, LLC_XXXX_stud_id and person, because this table is at the child-level whereas the key ID LLC_XXXX_stud_id is at the parent-level.  
</details>

<details>
<summary>What is the relationship between participants in NIHRBIO_COPING and GLAD?</summary>

As an overview, consider the diagram below. GLAD in the UK LLC TRE contains participants in the Green AND Orange. NIHRBIO_COPING in the UK LLC TRE only contains those in the RED but NOT the orange:   

<img src="../images/user_guide/COPING_GLAD.png" width="300"/>

Work is ongoing to create a ‘true’ individual-level ID in the UK LLC TRE. This is known as Anonymous Linking Field (ALF2), and used in conjunction with llc_XXXX_stud_id, it will be possible to unpick these relationships.
</details>

<details>
<summary>Do LPS have weighting variables in the TRE?</summary>



|LPS name|Weighting variables in the TRE?|Further information
|:--|:--:|:--|
|AIRWAVE|TBC|TBC|
|ALSPAC|No|Published paper with missing data: [The Avon Longitudinal Study of Parents and Children - a resource for COVID-19 research: questionnaire data capture July 2021 to December 2021, with a focus on long COVID](https://wellcomeopenresearch.org/articles/8-292). You can also find other papers on the Welcome Open Research site (search for ALSPAC and COVID) that explain how to deal with missing data.|
|BCS70|Yes|Search for weighting variables (e.g. 'design weight') using the Variables search in [Explore](https://ukllc-data-catalogue-96b71e84a70e.herokuapp.com/) and use the Advanced Options to filter on BCS70.|
|BIB|No|The BIB cohort recruited people during pregnancy who attended a 28-week antenatal appointment at the hospital. The aim was to invite all attendees to participate in the BIB cohort. BIB didn’t use any sample frame or weighting during recruitment and the population is broadly representative of people having babies in Bradford during this time. Compared to other LPS in UK LLC, the Bradford cohort falls into the highest deprivation groups and is more ethnically diverse (c. 50% South Asian). |
|ELSA|Yes|Search for weighting variables (e.g. 'cross-sectional weight') using the Variables search in [Explore](https://ukllc-data-catalogue-96b71e84a70e.herokuapp.com/) and use the Advanced Options to filter on ELSA.|
|EPICN|No|Eligible participants were recruited by post. Individuals were requested to provide detailed dietary, biological and other health data, and to be followed up over a few years, and so the response rate was c. 45%. Therefore participants were not a random population sample, but they were [closely similar to UK population samples](https://pubmed.ncbi.nlm.nih.gov/10466767/) with respect to many characteristics, including anthropometry, blood pressure, and lipids, although with a lower proportion of smokers.|
|EXCEED|No|Published paper with missing data: [Extended Cohort for E-health, Environment and DNA (EXCEED) COVID-19 focus](https://wellcomeopenresearch.org/articles/6-349) |
|FENLAND|No|TBC|
|GENSCOT|No|Published paper with missing data: [Generation Scotland: an update on Scotland's longitudinal family health study](https://bmjopen.bmj.com/content/bmjopen/14/6/e084719.full.pdf) |
|GLAD|No|Published paper with missing data: [Comparison of depression and anxiety symptom networks in reporters and non-reporters of lifetime trauma in two samples of differing severity](https://www.sciencedirect.com/science/article/pii/S266691532100127X)|
|MCS|Yes|See the [MCS User Guide](https://cls.ucl.ac.uk/wp-content/uploads/2020/09/MCS1-5_User_Guide_ed9_2020-08-07.pdf) to understand how the weighting variables are named. Search for weighting variables (e.g. 'weight1') using the Variables search in [Explore](https://ukllc-data-catalogue-96b71e84a70e.herokuapp.com/) and use the Advanced Options to filter on MCS.|
|NCDS58|Yes|Search for weighting variables (e.g.  ‘design weight’) using the Variables search in [Explore](https://ukllc-data-catalogue-96b71e84a70e.herokuapp.com/) and use the Advanced Options to filter on NCDS58.|
|NEXTSTEP|Yes|Search for weighting variables (e.g.  ‘design weight’) using the Variables search in [Explore](https://ukllc-data-catalogue-96b71e84a70e.herokuapp.com/) and use the Advanced Options to filter on NEXTSTEP.|
|NICOLA|No|Weighting is explained in [Early key findings from a study of older people in Northern Ireland](https://www.qub.ac.uk/sites/NICOLA/FileStore/Filetoupload,783215,en.pdf)|
|NIHRBIO_COPING|No|Published paper with missing data: [Risk and protective factors for new onset binge eating, low weight, and self-harm symptoms in over 25,000 individuals in the UK during the COVID-19 pandemic](https://osf.io/preprints/psyarxiv/qsbwf/)|
|NSHD46|Yes|Search for weighting variables (e.g. ‘design weight’) using the Variables search in [Explore](https://ukllc-data-catalogue-96b71e84a70e.herokuapp.com/) and use the Advanced Options to filter on NSHD46.|
|SABRE|No|Published paper with further information: [Ethnic differences in associations between fat deposition and incident diabetes and underlying mechanisms: The SABRE study](https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/oby.20997)|
|TEDS|No|TBC|
|TRACKC19|No|TRACKC19 has not calculated sampling weights.|
|TWINSUK|No|Most of the data in the TRE is derived from the CoPE questionnaires. For more details on how to deal with missing data visit: [Wellcome Open Research Gateways.](https://wellcomeopenresearch.org/gateways/twinsuk)|
|UKHLS|Yes|See UKHLS's guidance on [selecting the correct weight for your analysis](https://www.understandingsociety.ac.uk/documentation/mainstage/user-guides/main-survey-user-guide/selecting-the-correct-weight-for-your-analysis/0). Search for weighting variables (e.g. ‘xw’) using the Variables search in [Explore](https://ukllc-data-catalogue-96b71e84a70e.herokuapp.com/) and use the Advanced Options to filter on UKHLS.|
</details>

<details>
<summary>How can I request additional LPS data for my project?</summary>

Requests for new data should be submitted via an amendment to UK LLC. You may apply for additional data from already approved LPS, data from additional LPS, and/or additional linked data. N.B. each type of data [**amendment**](../../user_guide/RequestingAnAmendment.md)  requires a different level of review before being approved. 
</details>