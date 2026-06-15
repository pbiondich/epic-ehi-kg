# INDICATOR_REL_ORD_DOC

> This table extracts the media related to the orders in INDICATOR_REL_ORD_TBL.

**Primary key:** `PAT_INDICATOR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_INDICATOR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the patient indicators record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `DOCUMENT_ID` | VARCHAR | shared | The unique ID of a document linked to an order linked to a patient genomic indicator. Which order can be found by joining to INDICATOR_REL_ORD_TBL ON INDICATOR_REL_ORD_DOC.PAT_INDICATOR_ID = INDICATOR_REL_ORD_TBL.PAT_INDICATOR_ID and INDICATOR_REL_ORD_DOC.GROUP_LINE = INDICATOR_REL_ORD_TBL.LINE |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_INDICATOR_ID` | [PAT_INDICATOR](PAT_INDICATOR.md) | sole_pk | high |

