# FIN_ASST_CASE_PAT_ASSET

> This table contains information related to assets reported by the patient in a financial assistance case record.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ASSET_TYPE_C_NAME` | VARCHAR | org | Type of asset entered by the patient. |
| 4 | `PAT_ASSET_VALUE` | NUMERIC |  | How much an asset is worth, as entered by the patient. |
| 5 | `PAT_ASSET_COMMENT` | VARCHAR |  | Comment entered by a patient for the current asset row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

