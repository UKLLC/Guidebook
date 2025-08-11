# The Trusted Research Environment (TRE)
>Last modified: 11 Aug 2025

**Accessing the TRE**
<br>
<details>
  <summary>Can I access the TRE from home?</summary>
  
  Yes, as long as you're using a work provided laptop/desktop – see below the user security requirements in the [**Data Access and Acceptable Use Policy.**](https://ukllc.ac.uk/governance/) 

*All UK LLC users must:* 
* *Only access the UK LLC TRE using organisation owned/approved machines, which are automatically maintained so that they are fully patched and up to date with relevant virus protection.* 
* *Only access the UK LLC TRE from the UK and via a secure private or corporate network. Where using a private network, the user must make all reasonable efforts to ensure this is maintained and the equipment is secure (strong password) and kept patched and up to date.*
</details>

<details>
  <summary>Can I access the TRE from abroad?</summary>
No, you must only access the UK LLC TRE from the UK, in line with the user security requirements detailed in the question above.
</details>
<details>
  <summary>How do I unzip my QR code on a Mac?</summary>

  If you are using a Mac and therefore using “Archive Utility” rather than 7-Zip, you could experience issues. Archive Utility doesn't support the encryption 7zip uses. Therefore we suggest using a different extractor program called [**The Unarchiver**.](https://theunarchiver.com/) 
  </details>
  
<details>
<summary>What should I do if I have forgotten my password for the TRE?</summary>
You can request a new password from SeRP by by entering either your TRE username or email address at: <a href="https://portal.ukllc.ukserp.ac.uk/requestnewpassword" target="_blank" rel="noopener noreferrer">https://portal.ukllc.ukserp.ac.uk/requestnewpassword</a>  

</details>  

<details>
  <summary>What should I do if I can't connect to the TRE?</summary>
Some users may experience a blank screen after logging in. They may also see a message saying the connection has been timed out. This is a known issue with some network configurations. To address this issue, right click before logging into SeRP and you will see two options (VMware Blast and PCoIP). You may find that your home network works better with PCoIP, whereas your organisation network works better with VMware Blast.
  </details>
  <details>
<summary>How do I extend my access to the TRE?</summary>

To extend access beyond the agreed project end date, please submit an amendment to the UK LLC Access team. Information on how to submit an amendment is [**here**](../../user_guide/RequestingAnAmendment.md).
</details>

<br>

**Working in the TRE**
<br>
<details>
<summary>Can researchers work simultaneously in the TRE?</summary>

Yes, researchers can work with their approved project team simultaneously in the TRE. Each project is allocated a project folder, which is a shared area for storing all project-related workings. 
</details>

<details>
<summary>Can researchers share their screen in online meetings?</summary>

As long as the other researcher(s) is named on your project and has got valid ONS Accredited Researcher status and has completed a Data User Responsibilities Agreement (DURA), then yes, it is OK to share your screen on a conference call so that you can discuss your analyses.
</details>

<details>
<summary>Are there backups of researchers’ files in the TRE and how can I access these?</summary>
 
If you inadvertently delete or overwrite a file you can restore a previous version. To do this right click on the file/folder and choose ‘properties’ and then go to the ‘previous versions’ tab. Choose the version you want to restore.
</details>

<details>
<summary>What happens if I move organisation while working on a project in the TRE?</summary>

You must submit an amendment to notify UK LLC of a change in employer. Details of how to submit an amendment are available [**here**](../../user_guide/RequestingAnAmendment.md).
</details>

<details>
<summary>How do I add a researcher to an existing project in the TRE?</summary>

You must submit an amendment providing details of the new researcher so UK LLC can check whether they and their organisation meet UK LLC's [**access requirements**](https://ukllc.ac.uk/apply). Details of how to submit an amendment are available [**here**](../../user_guide/RequestingAnAmendment.md).
</details>

<details>
<summary>What should I do when a researcher leaves a project?</summary>

You must notify UK LLC when a researcher leaves a project so their access to the TRE can be terminated. This can be done by submitting an [**amendment**](../../user_guide/RequestingAnAmendment.md).
</details>
<br>

**Software in the TRE**  
  <details>
<summary>R helper – which method should I use to pull my data?</summary>

We advise using method A (one table at a time) or B (one LPS/data source at a time) for LPS-collected data. However, we advise using method A only for NHS data because of the size of some of the tables.
</details>

<details>
<summary>Why is my screen blank in RStudio?</summary>

If you encounter a blank screen when launching RStudio, please refer to this guide to fix the issue: [**https://docs.hiru.swan.ac.uk/display/HDK/RStudio+not+loading**](https://docs.hiru.swan.ac.uk/display/HDK/RStudio+not+loading)
</details>

<details>
<summary>Why isn’t Stata opening when I click on Stata files?</summary>

If logging into a fresh desktop, you have to launch Stata from the Windows start menu. It should then ‘deliver’ itself to your desktop and all Stata files should then associate themselves with Stata. 
</details>

<details>
<summary>Can I download Stata packages?</summary>

‘net’ downloads are blocked in the TRE because they require an internet connection. However, Stata package downloads via ssc have been whitelisted and are available. If what you need is not available via ssc you can request a file-in including the .do files using the file-in process. 
</details>

<details>
<summary>Can I download R packages from CRAN?</summary>

Yes, R packages available on CRAN can be installed on SeRP desktops. CRAN is a whitelisted connection for all approved users.
</details>
<br>

**Data in the TRE**


<details>
    <summary>What is study ID?</summary>

Each project is allocated a unique individual/participant-level ID system in the form llc_####_stud_id. This ID identifies a participant within an LPS, therefore if a participant exists in more than one LPS their records will exist in the UK LLC twice against 2 different study IDs. Study ID is specific to each project and must not be shared with users outside the project. If a researcher is named on more than one project in the TRE, separate identifiers are attached to each set of datasets relative to each project. Therefore, datasets cannot be combined between projects. 
</details>

<details>
  <summary>Can participants be linked between LPS?</summary>

Currently, participants who are in multiple LPS cannot be linked. However, this functionality has been factored into the design of the UK LLC TRE and will be implemented.
</details>

<details>
<summary>How much time is required for output clearance?</summary>

Output clearance can take 7-10 working days. We therefore recommend submitting outputs as early as possible and following the [**statisticial disclosure control (SDC) guidance**](../../user_guide/SDC.md) to increase the likelihood of them passing first time. 
</details>

<details>
<summary>Is there flexibility in the <10 rule?</summary>

No – due to the variability of statistical disclosure control (SDC) thresholds set by data providers, we are unable to be flexible. 
</details>

<details>
<summary>How can I request additional data for my project in the TRE?</summary>

Requests for new data should be submitted via an amendment to UK LLC. You may apply for additional data from already approved LPS, data from additional LPS, and/or additional linked data. N.B. each type of data [**amendment**](../../user_guide/RequestingAnAmendment.md)  requires a different level of review before being approved. 
</details>