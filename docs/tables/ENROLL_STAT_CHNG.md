# ENROLL_STAT_CHNG

> This table contains the enrollment status change of a participant in a research study and the effective date of the status change.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHNG_ENROLL_STATUS_C_NAME` | VARCHAR | org | The enrollment status category ID for a status change in an enrollment record. |
| 4 | `ENROLL_STAT_CHNG_DATE` | DATETIME |  | The date when an enrollment status became effective for an enrollment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

