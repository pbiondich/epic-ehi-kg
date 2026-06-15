# HSP_ACCT_DX_LIST

> This table contains hospital account final diagnosis list information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | The ID number of a hospital account. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Since multiple final ICD diagnoses can be stored in one hospital account, each diagnosis will have a unique line number. The record associated with line 1 represents the principal final coded diagnosis. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `DX_AFFECTS_DRG_YN` | VARCHAR |  | Specifies if the diagnosis affects the diagnosis-related group (DRG) associated with the hospital account. 1-yes, 2-no |
| 5 | `DX_COMORBIDITY_YN` | VARCHAR |  | Specifies if the diagnosis is a non-complication/comorbidity ("N"), complication/comorbidity ("Y"), or major complication/comorbidity ("Y"). Note that this column is extracted as an explicit "N" or "Y", where "Y" is used for both CC and MCC. The updated column DX_COMORBIDITY_C can be used to distinguish between CC and MCC diagnoses. |
| 6 | `FINAL_DX_SOI_C_NAME` | VARCHAR |  | Stores the final diagnosis severity of illness |
| 7 | `FINAL_DX_ROM_C_NAME` | VARCHAR |  | Stores the final diagnosis risk of mortality |
| 8 | `FINAL_DX_EXCLD_YN` | VARCHAR |  | Stores whether the final diagnosis should be excluded from clinical reporting |
| 9 | `FNL_DX_AFCT_SOI_YN` | VARCHAR |  | Stores whether the diagnosis affects severity of illness. |
| 10 | `FNL_DX_AFCT_ROM_YN` | VARCHAR |  | Stores whether the diagnosis affects risk of mortality. |
| 11 | `FINAL_DX_POA_C_NAME` | VARCHAR | org | Specifies whether each diagnosis was present on admission. |
| 12 | `DX_COMORBIDITY_C_NAME` | VARCHAR |  | Specifies if complication / comorbidity exists for each diagnosis on the hospital account. |
| 13 | `DX_HAC_YN` | VARCHAR |  | Specifies if the diagnosis contributed to a Hospital Acquired Condition. |
| 14 | `DX_COF_C_NAME` | VARCHAR |  | The COF (Condition Onset Flag) for the diagnosis. This item describes whether the diagnosis is onset during the episode (on) or outside of the timeframe of the episode (not). |
| 15 | `DX_COMPLEXITY_LVL` | INTEGER |  | The diagnosis complexity level - the complexity weight assigned to the diagnosis in relation to the DRG. |
| 16 | `COMPLEX_DX_C_NAME` | VARCHAR |  | The complex diagnosis indicator for the diagnosis code. |
| 17 | `DX_CLASS_C_NAME` | VARCHAR | org | The diagnosis classification. |
| 18 | `CAUSE_DEATH_YN` | VARCHAR |  | This field indicates whether the diagnosis is a cause of death for the patient. |
| 19 | `DX_CLUSTER` | VARCHAR |  | This item stores the diagnosis cluster identifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

