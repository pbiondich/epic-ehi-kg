# INDICATOR_REL_VARIANT_SRC

> This table extracts the variants' link source for the results stored in INDICATOR_REL_ORD_VAR.

**Primary key:** `PAT_INDICATOR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_INDICATOR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the pt indicators record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PAT_GENOMICS_IND_SRC_C_NAME` | VARCHAR |  | If the corresponding variant in the VARIANT_ID column of the INDICATOR_REL_ORD_VARIANT table was added manually or by the translation engine. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_INDICATOR_ID` | [PAT_INDICATOR](PAT_INDICATOR.md) | sole_pk | high |

