
# Introduction

>Last modified: 03 Sep 2024

Welcome to **UK LLC Guidebook**, the home of UK LLC’s **data documentation** and **user guide**.

UK Longitudinal Linkage Collaboration (UK LLC) is the **national Trusted Research Environment (TRE)** for the **UK's longitudinal research community**. UK LLC brings together **de-identified data** from **Longitudinal Population Studies (LPS)** and systematically links these data to participants' **health, non-health administrative** (e.g. education, employment, tax and benefits) and **geospatial** records in the UK LLC TRE.

Currently, researchers can request access to data from more than **20 LPS**, with participants' records linked to **NHS England** and **geospatial datasets**, where permissions allow. We anticipate NHS Wales and further geospatial datasets being available by the end of 2024. 

We invite researchers to work **collaboratively** on UK LLC Guidebook to build content and maximise use - see instructions below.

Please visit [**UK LLC Explore**](https://explore.ukllc.ac.uk/), UK LLC's metadata catalogue to discover the breadth of data held in the UK LLC TRE.

# Contribute to UK LLC Guidebook 
We welcome all contributions to UK LLC Guidebook.

As detailed in the flow diagram there are several steps that contributors must follow. You will need to have Git installed on your computer [**https://git-scm.com/**](https://git-scm.com/) and you need to be familiar with Git ways of working - see the [**Using Git guide**](../docs/user_guide/4.TeamDataScience.md) and [**GitHub Docs**](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) for further details.   




<img src="images/Contributor_Guidebook2.jpg" width="900"/>



**Figure 1** How to contribute to UK LLC Guidebook using Git

We suggest you read the summary below and then, if need be, follow the more detailed instructions on the [**GitHub Docs Contributing to a project guide**](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project). Below we include some details not specifically covered in the GitHub Docs guide. 

1. Go to the UK LLC Guidebook repo: [**https://github.com/UKLLC/Guidebook**](https://github.com/UKLLC/Guidebook) and **fork the repository**. The repo will be created in your own account. 
2. Use GitBash to **clone the repository** into a local folder of your choice (we recommend the HTTPS method) - click on the green Code button. You need to type 'git clone' into GitBash followed by the https path.   
3. Go to your forked repo and **create a branch**, giving it a meaningful name. To switch to the branch you need to type 'git branch' into GitBash followed by the branch name [Enter] and then type 'git checkout' followed by the branch name [Enter].  
4. **Make changes** to a guide(s) using e.g. [**MS Visual Studio Code**](https://code.visualstudio.com/Download).
5. If you make many changes to a guide(s) it is a good idea to build a local version of Guidebook in an **Anaconda test environment**. You need to install [**Anaconda**](https://www.anaconda.com/download/success) and then open Anaconda Prompt where you will see your base environment. Enter cd followed by the file path to your Guidebook. Type conda create --name jupbook [Enter]; press y when asked if you want to proceed; type conda activate jupbook [Enter]; type conda install pip [Enter]; press y when asked if you want to proceed; type pip install jupyter-book [Enter]; type pip install pandas [Enter]. You are then ready to build a local version of Guidebook. Open Anaconda Prompt and type cd followed by the file path to your Guidebook; type conda activate jupbook; type jb build ukllc_book. Then click on the index.html file which is in the html folder within the _build folder. Guidebook will open in your browser.
6. When you're happy with the changes you've made you then **prepare to submit a pull request** to UK LLC. Type 'git add .' in GitBash [Enter] and then type 'git commit -m " " (add a short description of the change between " "). Then type 'git push'. If the push doesn't work and there is a message saying the current branch has no upstream branch, copy the suggested text (git push --set-upstream origin 'File name') and [Enter]. 
7. Go to your forked repo and **submit a pull request**. Click on 'Contribute' and then submit your request. 
8. Your request will be **reviewed by UK LLC** and you will be notified by email of the outcome. 

