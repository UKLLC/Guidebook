# Understanding: Townsend Deprivation Index 


>Last modified: 09 Jun 2025

<div style="background-color: rgba(0, 178, 169, 0.3); padding: 5px; border-radius: 5px;"><strong>UK LLC provides a 2021 version of the Townsend Deprivation Index, developed by Jephcote and Gulliver, covering the Census Output Areas across England and Wales.</strong></div>  
<br>

## Townsend Index 

### Methodology

A 2021 version of the [Townsend Index (1989)](https://doi.org/10.4324/9781003368885) has been created by [Jephcote and Gulliver (2025)](https://doi.org/10.1016/j.envint.2025.109304) for the 188,879 Census Output Area (COA) communities across England and Wales.  

The Townsend index is a relative indicator of material deprivation, which has been widely used to identify socio‐economic confounding in crime, education, and health research in England. This deprivation index is constructed from four unweighted UK Census variables, which describe the level of total unemployment, overcrowding, private vehicle ownership, and home ownership in each community.  

[Census 2021 tables:](https://www.nomisweb.co.uk/sources/census_2021) RM024, TS052, TS045, and TS054 provided information on the four required measures, in 188,880 Output Area communities across England and Wales: 

**Variable 1: Proportion of “Total Unemployment” (RM024)** * 
| **Description**                | **Formula**                                                                 |
|-------------------------------|------------------------------------------------------------------------------|
| "Total Unemployment" | “Unemployed Persons Age 16–74y” ÷ “Economically Active Age 16–74y”          |

 * ***All students are considered as economically active by the original Index.***

 **Variable 2: "Proportion of “Overcrowded Households” (TS052)**
| **Description**                          | **Calculation** **                                                                |
|------------------------------------------|----------------------------------------------------------------------------------|
| “Overcrowded Households” | (“Households with a negative Bedroom Standard” ÷ “All Households”)              |

** ***The original index measured overcrowding in terms of ‘persons per room’, with any household with a number over 1 defined as overcrowded. In the 2021 UK Census, ‘persons per room’ was replaced with the ‘Bedroom Standard’ occupancy rating, where the following should have their own bedroom:***

***1. Married or cohabiting couple;***

***2. Single parent;*** 

***3. Person aged 16 years and over;***  

***4. Pair of same‐sex persons aged 10 to 15 years;***  

***5. Person aged 10 to 15 years paired with a person under 10 years of the same sex;***  

***6. Pair of children aged under 10 years, regardless of their sex;***  

***7. Person aged under 16 years who cannot share a bedroom with someone in 4, 5 or 6 above.***

***An occupancy rating of:***  

***- ‐1 or less: Implies that a household has fewer bedrooms than is required (overcrowded).***  

***- +1 or more: Implies that a household's accommodation is under‐occupied.***  

***- 0: suggests that a household's accommodation has an ideal number of bedrooms***  

***Although it is a more accurate measurement, it prevents the direct comparison with previous census years.***

**Variable 3: Proportion of “Households without Vehicle Ownership” (TS045)**
| **Description**                  | **Calculation**                                                       |
|----------------------------------|------------------------------------------------------------------------|
| “Households without Vehicle Ownership” | “Households without a Car or Van” ÷ “All Households”                   |

**Variable 4: Proportion of “Households that are not owner occupied” (TS054)**
 | **Description**                             | **Calculation**                                                                                   |
|---------------------------------------------|----------------------------------------------------------------------------------------------------|
| “Households that are not owner occupied”   | (“Social rented” + “Private rented” + “Living rent free”) ÷ “All Households”                      |

The four variables are converted in percentages, with the overcrowding and unemployment dimensions then experiencing a log transformation to reduce skewness within the distributions: 
- Unemployment:    LN ((Variable 1 * 100) + 1)  
- Overcrowding:    LN ((Variable 2 * 100) + 1)  
- Vehicle Ownership: Variable 3 * 100    
- Home ownership: Variable 4 * 100 

Each of these variables was then converted into z‐scores and summed to return an index value measuring the relative level of material deprivation in each community. The index values are then ranked and converted to deciles and quintiles. 

## Caveats: 

- The Townsend Index focuses on the actual as opposed to the perceived needs of individuals, and determines key indicators of actual standards of living in the sense of prevailing patterns whose absence indicates deprivation [(Eroğlu, 2007)](https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/content/pdf/10.1007/s11205-006-0004-0.pdf&casa_token=XrOeTxnIuD0AAAAA:oreku47tgBEEu_hOTmCtsTFKlnlTrDso2S4ImCNOu6OTQZcEyClMvDcYnzTwd4kGJO8noOHmxzLBCBqzTQ).  

- The index broadens the scope of the concept of poverty to mean being deprived of the living standards ‘which are customary or at least widely accepted by the societies to which they belong’ (Townsend, 1979: 31)*, and it attaches importance to the actual assessment of individuals’ standards of living [(Eroğlu, 2007)](https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/content/pdf/10.1007/s11205-006-0004-0.pdf&casa_token=XrOeTxnIuD0AAAAA:oreku47tgBEEu_hOTmCtsTFKlnlTrDso2S4ImCNOu6OTQZcEyClMvDcYnzTwd4kGJO8noOHmxzLBCBqzTQ).   


\* ***Townsend, Peter. Poverty in the United Kingdom: a survey of household resources and standards of living. University of California Press, 1979.***


## Limitations:  

- The ability of the Townsend Index to objectively and scientifically measure deprivation has been questioned, due to the value-laden judgments involved in the determination of socially acceptable standards of living [(Piachaud, 1987)](https://doi.org/10.1017/S0047279400020353).  

- The index does not separate choice from constraints and does not consider the element of taste as an explanation for a particular response such as not owning a car due to environmental reasons [(Piachaud, 1987)](https://doi.org/10.1017/S0047279400020353).   

 

 