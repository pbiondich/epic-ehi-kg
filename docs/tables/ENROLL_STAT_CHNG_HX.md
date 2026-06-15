# ENROLL_STAT_CHNG_HX

> This table contains the enrollment status change history of a participant in a research study.

**Primary key:** `ENROLL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier for the enrollment record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the enrollment status change history in the enrollment record.Together with ENROLL_ID, this forms the foreign key to the ENROLL_STAT_CHNG_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple enrollment status changes associated with the enrollment record and the ENROLL_STAT_CHNG_DT_HX_DATE from the ENROLL_STAT_CHNG_DT_HX table |
| 4 | `HX_CHNG_ENROLL_STATUS_C_NAME` | VARCHAR | org | The enrollment status category ID of a status change in the enrollment history. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

