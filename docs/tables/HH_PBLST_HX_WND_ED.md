# HH_PBLST_HX_WND_ED

> Contains Home Health problem list wound history information.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | Unique identifier for the problem list. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_WOUND_STAGE_C_NAME` | VARCHAR | org | Wound stage history. Links to category table ZC_WOUND_STAGE. |
| 4 | `HX_WOUND_ODOR_C_NAME` | VARCHAR | org | Wound odor history. Links to category table ZC_WOUND_ODOR. |
| 5 | `HX_WOUND_LENGTH` | NUMERIC |  | Wound length history. |
| 6 | `HX_WOUND_WIDTH` | NUMERIC |  | Wound width history. |
| 7 | `HX_WOUND_DEPTH` | NUMERIC |  | Wound depth history. |
| 8 | `HX_WND_DRAIN_AMT` | VARCHAR |  | Wound drainage amount history. |
| 9 | `HX_WND_DRAIN_DESC` | VARCHAR |  | Wound drainage description history. |
| 10 | `HX_WND_DESC_HNO_ID` | VARCHAR |  | Wound drainage description note ID. |
| 11 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 12 | `HX_WND_ADDEND_NUM` | INTEGER |  | Wound history addendum number. |
| 13 | `HX_WND_ENTR_USR_ID` | VARCHAR |  | User ID of user who entered historical wound data. Links to table CLARITY_EMP. |
| 14 | `HX_WND_ENTR_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

