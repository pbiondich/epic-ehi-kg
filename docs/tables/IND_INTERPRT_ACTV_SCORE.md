# IND_INTERPRT_ACTV_SCORE

> This table extracts the interpreted activity score for each variant on the order stored in INDICATOR_REL_ORD_TBL. The corresponding variant can be found in INDICATOR_REL_ORD_VARIANT for matching values of PAT_INDICATOR_ID, GROUP_LINE, and VALUE_LINE.

**Primary key:** `PAT_INDICATOR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_INDICATOR_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the patient indicator record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `INTERPRT_ACTIVITY_SCORE` | VARCHAR |  | This item represents the variant activity score when it is calculated from a genotype-activity score mapping table using the variant genotype. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_INDICATOR_ID` | [PAT_INDICATOR](PAT_INDICATOR.md) | sole_pk | high |

