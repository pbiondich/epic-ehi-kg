# COVERAGE_STATUS

> This table stores information about the current coverage statuses of a coverage record.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COVERAGE_STATUS_TYPE_C_NAME` | VARCHAR |  | The coverage status type category ID for the coverage record. |
| 4 | `COVERAGE_STATUS_RESOLUTION_C_NAME` | VARCHAR | org | The coverage status resolution category ID for the coverage record. This column's associated ZC table is ZC_CVD_STAT_OUTST_ACT_RES. |
| 5 | `CREATION_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the coverage gained the coverage status. |
| 6 | `RESOLUTION_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time when the resolution had its state for this coverage status set. |
| 7 | `CREATION_DTTM` | DATETIME (Local) |  | The local date and time when the coverage gained the coverage status. |
| 8 | `RESOLUTION_DTTM` | DATETIME (Local) |  | The local date and time when the coverage had its resolution for this coverage status set. |
| 9 | `COVERAGE_STATE_CHANGE_REASON_C_NAME` | VARCHAR | org | The coverage status set reason category ID for the coverage record. This column's associated ZC table is ZC_CVG_STAT_CHNG_RSN. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

