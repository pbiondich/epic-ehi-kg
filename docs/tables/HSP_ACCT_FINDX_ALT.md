# HSP_ACCT_FINDX_ALT

> This table contains the hospital account alternate final diagnoses from the hospital account (HAR) master file. Alternate final diagnoses will be specified if hospital accounts are coded with two sets of ICD codes.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the hospital account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FIN_DX_ALT_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `FIN_DX_ALT_EXCLD_YN` | VARCHAR |  | The alternate final diagnosis exclude from clinical reporting data. |
| 5 | `FIN_DX_ALT_POA_C_NAME` | VARCHAR | org | The alternate final diagnosis present on admission data. |
| 6 | `FIN_DX_ALT_CC_C_NAME` | VARCHAR |  | The alternate final diagnosis complication / comorbidity data. |
| 7 | `FIN_DX_ALT_HAC_YN` | VARCHAR |  | The alternate final diagnosis hospital acquired condition data. |
| 8 | `FIN_DX_ALT_AFDRG_YN` | VARCHAR |  | The alternate final diagnosis affects DRG data. |
| 9 | `FIN_DX_ALT_SOI_C_NAME` | VARCHAR |  | The alternate final diagnosis severity of illness data. |
| 10 | `FIN_DX_ALT_ROM_C_NAME` | VARCHAR |  | The alternate final diagnosis risk of mortality data. |
| 11 | `FIN_DX_ALT_AFSOI_YN` | VARCHAR |  | The alternate final diagnosis affects severity of illness data. |
| 12 | `FIN_DX_ALT_AFROM_YN` | VARCHAR |  | The alternate final diagnosis affects risk of mortality data. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

