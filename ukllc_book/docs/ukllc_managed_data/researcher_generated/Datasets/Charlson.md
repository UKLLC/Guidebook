# Charlson & Elixhauser Comorbidity Scores
>Last modified: 18 Aug 2025
<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC worked with researchers to derive comorbidity scores for a number of LPS using the Admitted Patient Care dataset</strong></div>  

## Overview
The dataset **UKLLC_rtn_comorbidity_scores_mar19feb20_v0001_20230420** contains comorbidity measures derived from the **NHS England Hospital Episode Statistics (HES) Admitted Patient Care (APC)** dataset for the period **1 March 2019 to 29 February 2020**.

The comorbidity indices included are **Charlson** and **Elixhauser** scores, each in multiple variants based on published weighting schemes. These measures are widely used in health services research for risk adjustment, mortality prediction, and burden of disease studies.

All scores have been calculated using the comorbidity R package, based on diagnoses recorded in the [**HESAPC dataset**](../../../linked_health_data/NHS_England/HES%20datasets/APC/HESAPC.ipynb)

Code used to create the scores can be found on [**GitHub**]( (<a href="https://github.com/UKLLC/LLC_0002/tree/main/comorbidity_scores" target="_blank" rel="noopener noreferrer">GitHub</a>)

---

## Variables

| Variable name | Description | Weighting scheme / Source |
|---------------|-------------|----------------------------|
| `unw_cci` | Number of Charlson comorbidity categories present for each patient, without weighting. | Unweighted count |
| `char_cci` | Charlson score calculated using the original weights proposed by Charlson et al. (1987). | (<a href="https://pubmed.ncbi.nlm.nih.gov/3558716/" target="_blank" rel="noopener noreferrer">Charlson ME et al., 1987</a>) |
| `quan_cci` | Charlson score calculated using the revised weights proposed by Quan et al. (2011). | (<a href="https://pubmed.ncbi.nlm.nih.gov/21330339/" target="_blank" rel="noopener noreferrer">Quan H et al., 2011</a>) |
| `unw_eci` | Number of Elixhauser comorbidity categories present for each patient, without weighting. | Unweighted count |
| `vw_eci` | Elixhauser score calculated using the weights proposed by van Walraven et al. (2009). | (<a href="https://pubmed.ncbi.nlm.nih.gov/19433995/" target="_blank" rel="noopener noreferrer">van Walraven C et al., 2009</a>) |
| `swiss_eci` | Elixhauser score calculated using the Swiss hospital weights proposed by Sharma et al. (2021). | (<a href="https://pubmed.ncbi.nlm.nih.gov/33407455/" target="_blank" rel="noopener noreferrer">Sharma N et al., 2021</a>) |

---

## Inclusion & Data Source
- **Inclusion criteria:** All admitted patient care episodes recorded in HES for NHS England hospitals between 1 March 2019 and 29 February 2020 where LPS in the following list: ["ALSPAC", "BCS70", "BIB", "ELSA", "EPICN", "EXCEED", "FENLAND", "GLAD", "MCS", "NCDS58", "NEXTSTEP", "NIHRBIO_COPING", "NSHD46", "TWINSUK", "UKHLS"]
- **Data source:** NHS England Hospital Episode Statistics (HES) – Admitted Patient Care. 

---

## Interpretation
- **Higher scores** indicate greater comorbidity burden.
- **Unweighted scores** simply count the number of comorbidity categories present.
- **Weighted scores** apply coefficients to comorbidities to reflect their relative impact on mortality or other outcomes, as estimated in the cited publications.

