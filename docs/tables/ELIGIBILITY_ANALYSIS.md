# ELIGIBILITY_ANALYSIS

> This table contains information regarding eligibility analysis executions for a patient-study combination.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INCL_CRITERIA_NA_COUNT` | INTEGER |  | Number of inclusion criteria that were not applicable to the patient in this run. |
| 4 | `EXCL_CRITERIA_NA_COUNT` | INTEGER |  | Number of exclusion criteria that were not applicable to the patient in this run. |
| 5 | `EXECUTION_IDENT` | VARCHAR |  | The execution ID of the eligibility analysis run. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

