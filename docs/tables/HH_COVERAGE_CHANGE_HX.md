# HH_COVERAGE_CHANGE_HX

> This table contains audit information about a patient's coverage change.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HH_COVERAGE_CHANGE_DATE` | DATETIME |  | Auditing history of the date a coverage change was indicated on a patient's Home Health episode. |
| 4 | `HH_COVCHG_REASON_C_NAME` | VARCHAR |  | Auditing history of the reason a coverage change was indicated on a patient's Home Health episode. |
| 5 | `EDIT_USER_ID` | VARCHAR |  | Auditing history of the ID of the user who edited the coverage change indication. |
| 6 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | Auditing history of the instant at which edits were made to the coverage change indication. |
| 8 | `PAT_STATUS_C_NAME` | VARCHAR | org | Auditing history of the discharge disposition recorded for a truncated hospital account following a coverage change. |
| 9 | `PRIM_CVG` | INTEGER |  | Auditing history of the primary coverage for a Home Health episode before a coverage change. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

