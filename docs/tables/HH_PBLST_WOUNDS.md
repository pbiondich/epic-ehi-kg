# HH_PBLST_WOUNDS

> Contains Home Health problem list wound information.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | Unique identifier for the problem list. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WOUND_STAGE_C_NAME` | VARCHAR | org | Wound stage. Links to category table ZC_WOUND_STAGE. |
| 4 | `WOUND_ODOR_C_NAME` | VARCHAR | org | Wound odor. Links to category table ZC_WOUND_ODOR. |
| 5 | `WOUND_LENGTH` | NUMERIC |  | Wound length. |
| 6 | `WOUND_WIDTH` | NUMERIC |  | Wound width. |
| 7 | `WOUND_DEPTH` | NUMERIC |  | Wound depth. |
| 8 | `WOUND_DRAINAGE_AMT` | VARCHAR |  | Wound drainage amount. |
| 9 | `WOUND_DRAINAGE_DES` | VARCHAR |  | Wound drainage description. |
| 10 | `WOUND_DESC_HNO_ID` | VARCHAR |  | Wound description note ID. |
| 11 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | Wound contact serial number. A unique serial number for this encounter. This number is unique across all patients and encounters in the system. Links to table PAT_ENC. |
| 12 | `WOUND_ENTRY_USR_ID` | VARCHAR |  | User ID of user who entered wound data. Links to table CLARITY_EMP. |
| 13 | `WOUND_ENTRY_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

