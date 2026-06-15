# FIN_ASST_CASE_ASSET

> This table contains information related to assets of a patient mentioned in a financial assistance case record.

**Primary key:** `FIN_ASST_CASE_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_CASE_ID` | NUMERIC | PK FK→ | The unique identifier for the financial assistance case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSET_TYPE_C_NAME` | VARCHAR | org | The category ID of the asset type. |
| 4 | `ASSET_VALUE` | NUMERIC |  | The amount the asset is worth. |
| 5 | `AST_BLNG_PAT_RELATIONSHIP_ID` | NUMERIC |  | The patient contact of one of the patients on the case for whom the asset information in the current row belongs to. If the information belongs to a patient on the case, ASSET_BELONGS_TO_PAT_ID column will be set instead. |
| 6 | `ASSET_COMMENT` | VARCHAR |  | A brief comment about the asset information in the current row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

