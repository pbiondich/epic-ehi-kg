# INDICATOR_REL_ORD_RSLT

> This table extracts the result components for the order stored in INDICATOR_REL_ORD_TBL. The corresponding value for this result component can be found in INDICATOR_REL_ORD_VAL for matching values of PAT_INDICATOR_ID, GROUP_LINE, and VALUE_LINE.

**Primary key:** `PAT_INDICATOR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_INDICATOR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the pt indicators record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `COMPONENT_ID` | NUMERIC | shared | If a lab result triggered this patient genomic indicator to be added, the result components causing this PGI to be added are stored in this item, grouped by the order which contains the result. |
| 5 | `COMPONENT_ID_NAME` | VARCHAR |  | The name of the component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_INDICATOR_ID` | [PAT_INDICATOR](PAT_INDICATOR.md) | sole_pk | high |

