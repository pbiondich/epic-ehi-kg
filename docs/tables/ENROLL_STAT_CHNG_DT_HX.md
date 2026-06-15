# ENROLL_STAT_CHNG_DT_HX

> This table contains the history of enrollment status change effective dates for a patient in a research study.

**Primary key:** `ENROLL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the enrollment record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the enrollment status change date in the enrollment record. Together with ENROLL_ID, this forms the foreign key to the ENROLL_STAT_CHNG_DT_HX table |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple enrollment status change dates associated with the enrollment record and the ENROLL_STAT_CHNG_HX_C from the ENROLL_STAT_CHNG_HX table |
| 4 | `HX_ENROLL_STAT_CHNG_DATE` | DATETIME |  | The effective date of an enrollment status change in the history of an enrollment record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

