# Why are there multiple rows of data for the same participant within an IAPT data table?
>Last modified: 09 Mar 2026
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px; "><strong>

In the IAPT dataset, multiple rows of data per participant are expected because:
- One person can have many pathway IDs (episodes of care) over time (see section 1)
- One pathway ID can have many associated events (see section 3)
- Data are structured by extract periods (see sections 2 and 3)

For researchers working with IAPT, it is key that they decide how to appropriately de-duplicate the data prior to analysis.</strong></div>
<br>

There are several inter-related reasons why there are multiple rows of data for the same participant in the IAPT dataset tables:

## 1. Different rows represent different pathways (i.e. different episodes of care)
The variable **pathwayid** identifies an episode of continuous care that a person has (from referral through to discharge). If the same person is discharged and then subsequently referred again, they will have a different pathwayid. Participants can therefore have multiple rows of data reflecting their multiple episodes of care (see Example 1).
- The variable cohortkey_e links participants across IAPT data tables
- The variable pathwayid links participants' pathways (distinct episodes of care) across IAPT data tables

**Example 1:** 
Participant 1 has 2 rows of data reflecting their 2 episodes of care (indicated by 2 distinct pathway IDs). Participant 2 has 3 rows of data representing their 3 episodes of care (indicated by 3 distinct pathway IDs)

|**Participant number**|**cohortkey_e**|**Pathwayid**|
|:---|:---|:---|
|1|1996749|8065n|
|1|1996749|1657f|
|2|7892964|6912l|
|2|7892964|9484e|
|2|7892964|5357s|

## 2. Different rows represent different ‘extract periods’
In addition, from September 2020 onwards (i.e. IAPT version 2.0) the IAPT metadata includes fields that mark exactly which period a given extract covers. This is labelled with the variables **‘extract start date’** and **‘extract end date’.**
The extract start date is always 01 April (i.e. the start of the UK financial year), except for the very first extract which started on 01 September 2020 when these fields were introduced. Care providers report IAPT data to NHS England on a monthly basis. The extract end dates therefore identify the month that the extract was taken. In the IAPT dataset each participant will have multiple extract periods (typically 2-3 per financial year) and the time periods covered by these will overlap (see Example 2).  A pathway ID will appear in an extract period until it is closed and so the same pathway ID can appear in multiple rows as it is included in multiple extracts (see Example 2).

**Example 2:**
Participant 1 has 4 rows of data reflecting their 2 episodes of care (indicated by the 2 distinct pathway IDs). The first extract period covers 01 September 2020 until the end of that financial year (31 Mar 2021) in which there was a single episode of care. Their subsequent episode of care appears in the extract period 01 April 2022 – 31 Mar 2023. Note that this second episode of care appears in 3 rows because the referral remained open when the Sep 2022 extract was taken, when the January 2023 extract was taken, and when the March 2023 extract was taken. Information about events associated with that episode of care – such as the number of contacts attended – has been updated over time. Here, participant 1 has attended 5 contacts in the period 01 April 2022 – 31 January 2023 and by 31 March 2023 this total has increased to 7 (the totals are cumulative across extract periods).      

|**Participant number**|**cohortkey_e**|**Pathwayid**|**Extract start date**|**Extract end date**|**Number of contacts attended**|
|:---|:---|:---|:---|:---| :---|
|1|1996749|8065n|01 Sep 2020|31 Mar 2021|5|
|1|1996749|1657f|01 Apr 2022|30 Sep 2022|2|
|1|1996749|1657f|01 Apr 2022|31 Jan 2023|5|
|1|1996749|1657f|01 Apr 2022|31 Mar 2023|7| 

## 3. Different rows within an extract period represent different events associated with a pathway  
It gets even more complex than this because in some IAPT tables there are multiple rows of data per participant (and per pathway ID) for a given extract period. These multiple rows represent different events associated with a particular pathway ID within the same extract period. For example, within a particular extract period there may have been multiple contacts (appointments) recorded for a particular pathway ID (see Example 3).

**Example 3:**
Participant 1 has 5 contact dates recorded during the period 01 Sep 2020-31 Mar 2021. Each contact is represented by a different row and they are all associated with the same episode of care (indicated by the same pathway ID). 

|**Participant number**|**cohortkey_e**|**Pathwayid**|**Extract start date**|**Extract end date**|**Contact date**|
|:---|:---|:---|:---|:---| :---|
|1|1996749|8065n|01 Sep 2020|31 Mar 2021|05 Sep 2020|
|1|1996749|8065n|01 Sep 2020|31 Mar 2021|10 Sep 2020|
|1|1996749|8065n|01 Sep 2020|31 Mar 2021|20 Oct 2020|
|1|1996749|8065n|01 Sep 2020|31 Mar 2021|03 Dec 2020|
|1|1996749|8065n|01 Sep 2020|31 Mar 2021|09 Jan 2021|

## 4. What does this mean for researchers?

<aside class="admonition warning"><p class="admonition-title">Researchers will need to do some de-duplicating by pathwayid prior to conducting analysis. </p>If researchers include all extract periods given per participant they will overcount referrals and their associated events.</aside>


Which rows researchers keep and which they remove may depend somewhat on their specific research question (e.g. they maybe interested in a specific date/time period). But we provide some general guidance as follows:

**Step 1:**
For each pathway ID, select the extract period which contains the latest (most recent) extract end date and do this once per financial year to give the most complete view for that financial year.

- In Example 2 that would mean selecting row 1 for pathway ID 8065n and row 4 for pathway ID 1657f
- In the ‘Demographics & Referral’ IAPT table a pathway ID may appear across multiple financial years. Examining which row has had the service discharge date filled in (if the referral has been closed) may be a helpful way to help reduce to one row per pathway.

**Step 2:**
Remember, if there are multiple events (e.g. contacts dates, assessment scores) recorded within the same extract period, then step 1 will still result in there being multiple rows per pathway ID (as per Example 3). Examining clinical/event dates will help researchers to determine which of these rows is the most relevant for what they are interested in. For example:

Interested in **completion** → look at row with latest discharge date

Interested in **last contact** → look at row with latest appointment date

Interested in **clinical outcome** → look at first and last valid scores

Interested in whether referral is **open/closed** → look for presence of discharge date

