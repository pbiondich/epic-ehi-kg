# ADVERSE_EVENT_REVIEW_INFO

> The ADVERSE_EVENT_REVIEW_INFO table contains information about the reviews of the adverse events for a given study association.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AE_REVIEW_HX_UTC_DTTM` | DATETIME (UTC) |  | The date and time of a historical review of the adverse events for a study association. |
| 4 | `AE_REVIEW_HX_USER_ID` | VARCHAR |  | The unique ID of a reviewing user for a historical review of the adverse events for a study association. |
| 5 | `AE_REVIEW_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

