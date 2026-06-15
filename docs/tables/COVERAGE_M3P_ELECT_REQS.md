# COVERAGE_M3P_ELECT_REQS

> Clarity table for related group CVG 940 - M3P Election Requests.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `M3P_ELECT_REQ_UTC_DTTM` | DATETIME (UTC) |  | The date and time in which a member submits an election request for the Medicare Prescription Payment Plan. |
| 4 | `M3P_REQ_STATUS_C_NAME` | VARCHAR |  | The Request Status category ID for the Medicare Prescription Payment Plan election request. |
| 5 | `M3P_STATUS_REASON_C_NAME` | VARCHAR | org | The Status Reason category ID for the Medicare Prescription Payment Plan election request. |
| 6 | `M3P_SOURCE_TYPE_C_NAME` | VARCHAR | org | The Source Type category ID for the Medicare Prescription Payment Plan election request. |
| 7 | `M3P_PLAN_YEAR` | INTEGER |  | The plan year the member is electing to opt into the Medicare Prescription Payment Plan for. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

