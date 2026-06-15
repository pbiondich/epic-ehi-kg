# V_EHI_CVG_COVERAGE_HIST_ALL

> Filter view for loading coverage history filtered by all members on a view as EHI.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique ID assigned to the coverage record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of history information for a coverage record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | The category value associated with the change made to the coverage record (i.e. Create, Add Member, Change Covered Status, etc.) |
| 4 | `CHANGE_DATE` | DATETIME |  | The date on which each change was added to the coverage record. |
| 5 | `EDIT_INFO` | VARCHAR |  | The original information associated with the change. |
| 6 | `EFF_DT_CHNG_RSN_C_NAME` | VARCHAR | org | The effective date change reason in the Coverage History. |
| 7 | `INFO_RCVD_DT` | DATETIME |  | The information received date associated with the change. |
| 8 | `MC_EDIT_HX_TIME` | DATETIME (Local) |  | Coverage history time of change. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

