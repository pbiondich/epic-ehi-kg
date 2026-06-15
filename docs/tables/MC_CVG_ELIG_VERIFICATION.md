# MC_CVG_ELIG_VERIFICATION

> This table contains information about the eligibility verification status of coverage members.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEMBER_PAT_ID` | VARCHAR | FK→ | The unique ID of the member for this row. |
| 4 | `VERIFICATION_RECORD_ID` | NUMERIC |  | The unique ID of the member's eligibility verification record (VRX). |
| 5 | `GRACE_PERIOD_START_DATE` | DATETIME |  | This start date of the member's eligibility grace period. |
| 6 | `GRACE_PERIOD_END_DATE` | DATETIME |  | This end date of the member's eligibility grace period. |
| 7 | `MC_VERIFICATION_TYPE_C_NAME` | VARCHAR | org | The verification status type for the verification record on this line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `MEMBER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

