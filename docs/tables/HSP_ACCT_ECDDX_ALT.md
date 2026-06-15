# HSP_ACCT_ECDDX_ALT

> This table contains the hospital account alternate external cause of injury diagnoses from the hospital account (HAR) master file. Alternate external cause of injury diagnoses will be specified if hospital accounts are coded with two sets of ICD codes.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ECD_DX_ALT_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `ECD_DX_ALT_EXCLD_YN` | VARCHAR |  | The alternate external cause of injury diagnosis exclude from clinical reporting data. |
| 5 | `ECD_DX_ALT_POA_C_NAME` | VARCHAR | org | The alternate external cause of injury diagnosis present on admission data. |
| 6 | `ECD_DX_ALT_CC_C_NAME` | VARCHAR |  | The alternate external cause of injury diagnosis complication / comorbidity data. |
| 7 | `ECD_DX_ALT_HAC_YN` | VARCHAR |  | The alternate external cause of injury diagnosis hospital acquired condition data. |
| 8 | `ECD_DX_ALT_AFDRG_YN` | VARCHAR |  | The alternate external cause of injury diagnosis affects DRG data. |
| 9 | `ECD_DX_ALT_SOI_C_NAME` | VARCHAR |  | The alternate external cause of injury diagnosis severity of illness data. |
| 10 | `ECD_DX_ALT_ROM_C_NAME` | VARCHAR |  | The alternate external cause of injury diagnosis risk of mortality data. |
| 11 | `ECD_DX_ALT_AFSOI_YN` | VARCHAR |  | The alternate external cause of injury diagnosis affects severity of illness data. |
| 12 | `ECD_DX_ALT_AFROM_YN` | VARCHAR |  | The alternate external cause of injury diagnosis affects risk of mortality data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

