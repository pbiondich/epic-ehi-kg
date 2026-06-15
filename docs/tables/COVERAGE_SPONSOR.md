# COVERAGE_SPONSOR

> This table contains information about who is sponsoring this coverage for the subscriber, such as current employment. Changes to this information are tracked over time for informational purposes, though just the latest values are actively used. Each row in this table for a coverage represents one date range with the values of the sponsor information fields effective during that date range.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique ID of the coverage record for this row. This column is frequently used to link to the COVERAGE table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPONSR_EFF_FROM_DT` | DATETIME |  | Covered through (I CVG 206) and Employer Size (I CVG 207) are tracked over time since they can affect filing order and MSP logic. When either of those items are changed, a new line is added to this related group using today's date for this item and the new values for the other two items. |
| 4 | `COVERED_THROUGH_C_NAME` | VARCHAR | org | Covered through current employment, retirement, COBRA, or other. Affects filing order calculation and is used for Medicare Secondary Payor. |
| 5 | `EMPLOYER_SIZE_C_NAME` | VARCHAR |  | Number of employees for the employer that sponsors this coverage. Used as part of Medicare Secondary Payor determination. |
| 6 | `SPONSOR_EFF_TO_DT` | DATETIME |  | Covered through (I CVG 206) and Employer Size (I CVG 207) are tracked over time since they can affect filing order and MSP logic. When either of those items are changed, a new line is added to this related group, and the previous line is given yesterday's date as the effective to date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

