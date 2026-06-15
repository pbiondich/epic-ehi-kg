# ORD_CV_F_WALL_MOTN

> This table stores the wall motion data - segment, value and modifier.

**Primary key:** `CV_FINDING_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CV_FINDING_ID` | NUMERIC | PK FK→ | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WALL_SEGMENT_C_NAME` | VARCHAR | org | The wall segment being scored. |
| 4 | `WALL_VALUE_C_NAME` | VARCHAR | org | The disease value for a wall segment. |
| 5 | `WALL_MODIFIER_C_NAME` | VARCHAR | org | The location modifier for the wall segment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CV_FINDING_ID` | [ORD_CV_FINDING](ORD_CV_FINDING.md) | sole_pk | high |

