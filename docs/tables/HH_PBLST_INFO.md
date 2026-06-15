# HH_PBLST_INFO

> Contains Home Health problem list noadd single items information.

**Primary key:** `PROBLEM_LIST_ID`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | Unique identifier for the problem list. |
| 2 | `X_COORD_WOUND_POS` | INTEGER |  | Wound position x-coordinate. |
| 3 | `Y_COORD_WOUND_POS` | INTEGER |  | Wound position y-coordinate. |
| 4 | `WOUND_LOCATION_C_NAME` | VARCHAR | org | Wound location. Links to category table ZC_WOUND_LOCATION. |
| 5 | `WOUND_TYPE_C_NAME` | VARCHAR | org | Wound type. Links to category table ZC_WOUND_TYPE. |
| 6 | `WOUND_IS_ACTIVE_YN` | VARCHAR |  | Is the wound active? Yes or no. |
| 7 | `WOUND_IS_DELETE_YN` | VARCHAR |  | Has the wound been deleted? Yes or no. |
| 8 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | Wound deletion contact serial number. A unique serial number for this encounter. This number is unique across all patients and encounters in the system. Links to table PAT_ENC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

