# HSP_ACCT_EXTINJ_CD

> This table contains hospital account external injury codes information from the Hospital Accounts Receivable (HAR) master file.

**Primary key:** `HSP_ACCOUNT_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the hospital account. |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple external injury codes can be stored in one hospital account, each code will have a unique line number. |
| 3 | `EXT_INJURY_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `EXT_INJURY_POA_YNU` | VARCHAR | org | This column specifies whether each External Cause of Injury Code diagnosis was present on admission. ** Note: this column was deprecated in the Spring 2008 release. |
| 5 | `EXT_COMORBIDITY_YN` | VARCHAR |  | This column specifies whether the External Cause of Injury Code diagnosis is a non-complication/comorbidity ("N"), complication/comorbidity ("Y") or major complication/comorbidity ("Y"). Note that this column is extracted as an explicit "N" or "Y", where "Y" is used for both complication or comorbidity (CC) and major complication or comorbidity (MCC). The updated column EXT_COMORBIDITY_C can be used to distinguish between CC and MCC diagnoses. |
| 6 | `EXT_DX_AFF_DRG_YN` | VARCHAR |  | This column specifies whether the External Cause of Injury Code diagnosis affects the diagnosis-related group (DRG) associated with the hospital account. A null value for this column indicates no. |
| 7 | `ECODE_DX_SOI_C_NAME` | VARCHAR |  | External Cause of Injury Code diagnosis severity of illness |
| 8 | `ECODE_DX_ROM_C_NAME` | VARCHAR |  | External Cause of Injury Code diagnosis risk of mortality |
| 9 | `ECODE_DX_EXCLD_YN` | VARCHAR |  | External Cause of Injury Code diagnosis exclude from clinical reporting |
| 10 | `ECD_DX_AFCT_SOI_YN` | VARCHAR |  | External Cause of Injury Code diagnosis affects severity of illness |
| 11 | `ECD_DX_AFCT_ROM_YN` | VARCHAR |  | External Cause of Injury Code diagnosis affects risk of mortality |
| 12 | `ECODE_DX_POA_C_NAME` | VARCHAR |  | This column stores whether each External Cause of Injury Code diagnosis was present on admission. This column links to category table ZC_DX_POA. |
| 13 | `EXT_COMORBIDITY_C_NAME` | VARCHAR |  | Specifies if complication/comorbidity exists for each External Cause of Injury Code diagnosis on the hospital account. |
| 14 | `ECD_HAC_YN` | VARCHAR |  | Specifies if the External Cause of Injury Code diagnosis contributed to a Hospital Acquired Condition. |
| 15 | `DX_COF_C_NAME` | VARCHAR |  | The COF (Condition Onset Flag) for the diagnosis. This item describes whether the diagnosis is onset during the episode (on) or outside of the timeframe of the episode (not). |
| 16 | `DX_CLASS_C_NAME` | VARCHAR | org | The diagnosis classification. |
| 17 | `CAUSE_DEATH_YN` | VARCHAR |  | This field indicates whether the diagnosis is a cause of death for the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

