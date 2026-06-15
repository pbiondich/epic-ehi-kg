# IRFPAI_ABSTRACTIONS

> IRFPAI_ABSTRACTIONS stores information for RDI records with a type of IRF-PAI.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `IRFPAI_CMG_CODE` | VARCHAR |  | Stores CMG code associated with IRF-PAI RDI record. |
| 3 | `IRFPAI_CMG_DATE` | DATETIME |  | Stores the CMG date. CMG date is the date IRF-PAI is accepted by CMS. |
| 4 | `PRES_COMPLIANCE_ADM_YN` | VARCHAR |  | Stores if the patient qualifies as presumptive compliant or not based on the admission date. |
| 5 | `ADJ_COMPLIANCE_YN` | VARCHAR |  | Stores if the patient qualifies as adjusted compliant or not. |
| 6 | `PRES_COMPLIANCE_DIS_YN` | VARCHAR |  | Stores if the patient qualifies as presumptive compliant or not based on the discharge date. |
| 7 | `MEDICARE_PAT_YN` | VARCHAR |  | Stores whether the IRF-PAI is for a Medicare patient. This is determined by what is entered in the Payer Information section of the IRF-PAI. |
| 8 | `PAT_ADMISSION_DATE` | DATETIME |  | Stores the date that the patient was admitted to the IRF. This is determined by what is entered in the Identification Information section of the IRF-PAI. |
| 9 | `REHAB_IMPAIRMENT_CATEGORY_C_NAME` | VARCHAR |  | This is the Rehab Impairment Category (RIC) for this IRF-PAI abstraction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

