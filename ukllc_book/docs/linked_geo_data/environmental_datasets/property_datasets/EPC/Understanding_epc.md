# Understanding: Energy Performance Certificates (EPC)

>Last modified: 16 Jun 2025

The concept for Energy Performance Certificates (EPCs) were first introduced by the EU’s Energy Performance of Buildings Directive in 2002. The directive was established to improve energy efficiency across European Union (EU) member states by implementing mandatory energy certificates of buildings.

The Energy Performance of Buildings Directive (EPBD) officially  introduced EPCs in 2007. By 2008 it became mandatory in England and Wales to issue an EPC when a dwelling is sold or rented, creating a large historic database. EPC's contain detailed property level information including floor area, environmental impact and fuel type. EPCs serve as a key policy tool for improving building energy efficiency and reducing environmental impact. Since their introduction they have been implemented in different ways across Member States. 

### Policy timeline

**2002:** Introduction of the European Union’s Energy Performance of Buildings Directive (EPBD), aiming to improve energy efficiency across Europe with measures such as energy certification. 

**August 2007:** In England and Wales, EPCs became mandatory for properties being sold with 4+ bedrooms.

**October 2007:** In England and Wales, EPCs became mandatory for all properties being sold regardless of size.

**2008:** In England and Wales, EPCs became mandatory for rental properties when they were put up for rent.

**2012:** The European Union updated the EPBD, introducing [stricter requirements](https://assets.publishing.service.gov.uk/media/5ec2b3d8d3bf7f5d3defffb7/EPBD_consultation.pdf) for energy performance standards such as increasing the inspection threshold for heating systems.  

**March 2015:** In the UK, the government introduced the [Energy Efficiency (Private Rented Property) (England and Wales) Regulations 2015](https://www.legislation.gov.uk/uksi/2015/962/contents/made), which set [Minimum Energy Efficiency Standards (MEES)](https://www.gov.uk/guidance/domestic-private-rented-property-minimum-energy-efficiency-standard-landlord-guidance).

**October 2015:** New rules were introduced which gave Local Authorities the option to set a minimum space standard for new homes. Under the new standard, a new one bed, one person flat would have to be a minimum of 37m² while a three bed, five person home would be a minimum of 93m². 

**April 2018:** As set out by the MEES, landlords could no longer grant new leases on properties with an EPC band below E unless they had a valid exemption.

**April 2020:** As set out by the MEES, landlords had to obtain at least an EPC E rating, could no longer let or continue to let properties if they have an EPC rating below E, unless they have a valid exemption in place.

**April 2021:** In England, all new homes delivered through permitted development rights must now meet the nationally described space standards as published by the Department of Communities and Local Government, 2015.  

### Methodology

A property's energy performance is calculated using the [Standard Assessment Procedure (SAP)](https://www.gov.uk/guidance/standard-assessment-procedure). SAP is the current methodology used by the government whereby an algorithm makes assumptions about the thermal properties of a building's fabric and occupancy in order to calculate the theoretical heat loss of the property. New properties being built are required to have a full SAP assessment, whereas existing properties are only required to have a reduced Standard Assessment Procedure (rdSAP). 

The SAP methodology calculates an energy efficiency rating out of 100 and assigns a corresponding EPC band, where A is the most energy efficient and G is the least:
| Energy Efficiency Rating | EPC Band |
|--------------------------|----------|
| ≥ 92                     | A        |
| 81–91                    | B        |
| 69–80                    | C        |
| 55–68                    | D        |
| 39–54                    | E        |
| 21–38                    | F        |
| 1–20                     | G        |

An EPC is created following an EPC survey of a property conducted by a Domestic Energy Assessor (DEA). The DEA records key building characteristics which are then uploaded into SAP software to generate an Energy Efficiency Rating and EPC band. All of the EPC information submitted from DEA's across the UK is consolidated into one database. 

The Energy Performance of Buildings Register (the register) is the official place for all Energy Performance Certificates (EPCs) and is 
published by the [Department for Levelling Up, Housing & Communities](https://epc.opendatacommunities.org/). The department has chosen only to publish data from 1 October 2008. 


## Caveats:

- Records were removed with an inspection date prior to 1st August 2007 which was when EPCs were introduced in England and Wales and also removed where inspection date was prior to 1st October 2008 as the department stated then have chosen only to publish data from this date. This is inline with GOV.UK data tables on Energy Performance of Buildings Certificates which report on Q4 2008 onwards due to [data quality issues](https://assets.publishing.service.gov.uk/media/5eaaab78d3bf7f6526f8d742/EPB_Cert_Statistics_Release_Q1_2020.pdf).

- There are some instances where houses have been converted into flats and the EPC record states the habitable room number and floor area of the entire building rather than the singular flats (Scott et al., [2015](https://doi.org/10.23889/ijpds.v8i2.2927)). 

- The records contain many duplicate entries. In this dataset, variables have been transformed to minimise disclosure risk such as inspection date has been transformed to inspection year to minimise disclosure risk. Duplicates were therefore removed following transformation, where all parameters were equal. Hardy and Glew [(2019)](https://doi.org/10.1016/j.enpol.2019.03.022) have suggested that duplicate entries are most likely due to a software or network fault which leads to EPC's being lodged multiple times.

- The records also contain EPCs that have the same inspection date but the rest of the values are different, suggesting two different inspections. Hardy and Glew [(2019)](https://doi.org/10.1016/j.enpol.2019.03.022) suggests that this is possibly due to human error as an inspector can manually set an inspection date or due to a failed audit. Desk-based audits are required for a minimum of 2% of EPCs lodged by each DEA. When an EPC fails an audit, the DEA has to re-submit the EPC with the required corrections. While the assessor is meant to request for the EPC that failed the audit to be removed from the records, they might not always carry out this required step.

- While EPC energy efficiency ratings may increase, they should typically not decrease. Nevertheless, variation in EPC rating can be expected due to DEAs disagreeing on specific variables such as floor area even if no changes have actually been made to the property. 
As part of the EPC quality assurance process, the score should be within ± 5 points 95% of the time, or within ± 10 points 99.99% of the time where an EPC is conducted on an identical property. If the EPC rating for a property decreases by more than 10, it is therefore potentially an error. Nevertheless, there are instances where a decrease may be legitimate such as the addition of an extension (Hardy and Glew [(2019)](https://doi.org/10.1016/j.enpol.2019.03.022)).


## Limitations:

- The records contain discrepancies in building characteristics over time such as for some flats there are differences across records for 'built form' such as discrepancies in 'built form' classifications for some flats - e.g., one inspection may list a property as ‘End-Terrace’ and another as ‘Semi-Detached’. 

- There are potential errors in instances of buildings changing their property type. Hardy and Glew [(2019)](https://doi.org/10.1016/j.enpol.2019.03.022) suggest that while a building may change its property type, such as converting a house into a flat, the rate of conversions is low in the UK (around 5000 per year which would only account for 0.5% of lodged EPCs in a typical year). Consequently, it is not very likely for a property type to change and may therefore be due to error.

- For flats and maisonettes, there are instances where there are discrepancies in the exact 'floor level' recorded in EPCs (Hardy and Glew [(2019)](https://doi.org/10.1016/j.enpol.2019.03.022)).

- There are potential errors where EPCs indicate that energy efficiency products have been removed. Removal of such products is unlikely as it is difficult to do so and there is no real incentive to do so (Hardy and Glew [(2019)](https://doi.org/10.1016/j.enpol.2019.03.022)).

- There are potential errors where EPCs indicate that a property changes its window glazing type to be less energy efficient such as conversion from double glazing to single glazing (Hardy and Glew [(2019)](https://doi.org/10.1016/j.enpol.2019.03.022)).

- There are some instances where values are outside the expected range of the data for example, where values fall outside expected ranges - for example, a floor area recorded as 1 m² or where the number of habitable rooms is less than number of heated rooms (Scott et al., [2015](https://doi.org/10.23889/ijpds.v8i2.2927)).


  

 

 