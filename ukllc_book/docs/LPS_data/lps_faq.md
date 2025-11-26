# FAQs about working with LPS data
>Last modified: 26 Nov 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 10px; border-radius: 5px;"><strong>Answers to researchers' questions about working with LPS data.</strong></div style>  
<br>
<details>
<summary>What should I do if I don't use data from an LPS provisioned to my project?</summary>

UK LLC's [**publication policy**](https://ukllc.ac.uk/governance) requires researchers to complete a checklist to confirm which LPS data they used in their research. Before publications are submitted, and at the end of a project, UK LLC will let LPS know whether their data was used in each research project. It is helpful if researchers share their reasons for not using some datasets so UK LLC can share this information with future potential users.
</details>
<details>
<summary>How can I request additional LPS data for my project?</summary>

Requests for new data should be submitted via an amendment to UK LLC. You may apply for additional data from already approved LPS, data from additional LPS, and/or additional linked data. **Note**: each type of data [**amendment**](../user_guide/RequestingAnAmendment.md)  requires a different level of review before being approved. 
</details>

<details>
<summary>When is more LPS data going to be available via UK LLC?</summary>

UK LLC is currently working with our partner LPS to increase the both the number of datasets, and the number of study participants, included in the UK LLC resource. Information about new datasets will be provided to the UK LLC TRE user group as soon as they become available, and this will be reflected on the [individual LPS pages](../LPS_data/LPS_introduction.md) in Guidebook and in <strong><a href="https://explore.ukllc.ac.uk" target="_blank" rel="noopener noreferrer">UK LLC Explore</a></strong>, UK LLC's data catalogue.
</details>

<details>
<summary>Is UK LLC planning on increasing the number of LPS with data in the TRE?</summary>
Yes, we are encouraging more LPS to become part of UK LLC. Updates will be added to Guidebook and the <a href="https://ukllc.ac.uk" target="_blank" rel="noopener noreferrer">UK LLC website</a> whenever new data are deposited into the TRE.
</details>

<details>
    <summary>What is study ID?</summary>

Each project is allocated a unique individual/participant-level ID system in the form llc_####_stud_id. This ID identifies a participant within an LPS, therefore if a participant exists in more than one LPS their records will exist in the UK LLC twice against 2 different study IDs. Study ID is specific to each project and must not be shared with users outside the project. If a researcher is named on more than one project in the TRE, separate identifiers are attached to each set of datasets relative to each project. Therefore, datasets cannot be combined between projects. 
</details>

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
  <summary>Can participants be linked between LPS?</summary>

Currently, participants who are in multiple LPS cannot be linked. However, this functionality has been factored into the design of the UK LLC TRE and will be implemented.
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
