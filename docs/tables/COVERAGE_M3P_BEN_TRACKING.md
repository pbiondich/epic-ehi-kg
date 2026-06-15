# COVERAGE_M3P_BEN_TRACKING

> Clarity table for CVG related group 930 - M3P Benefit Tracking.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `M3P_BEN_DETRM_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the member is determined to be likely to benefit from the Medicare Prescription Payment Plan. |
| 4 | `M3P_BEN_PLAN_YEAR` | INTEGER |  | The plan year for when the member is identified as Likely to Benefit. |
| 5 | `M3P_BEN_REASON_C_NAME` | VARCHAR | org | The M3P Likely to Benefit Reason category ID for the coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

