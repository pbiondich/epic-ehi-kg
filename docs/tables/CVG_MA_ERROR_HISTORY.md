# CVG_MA_ERROR_HISTORY

> The history of Medicare Advantage errors that have been removed from a coverage. Each row represents an error that has been resolved. CVG_MA_ERRORS has the errors currently present on coverages.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MA_ERR_CODE_C_NAME` | VARCHAR |  | The Medicare Advantage error code that was previously on the coverage |
| 4 | `MA_ERR_DATA` | VARCHAR |  | The data from the CMS file associated with the Medicare Advantage error |
| 5 | `MA_ERR_DATE` | DATETIME |  | The date that the error was reported. |
| 6 | `MA_ERR_CODE_FILE_C_NAME` | VARCHAR |  | The type of CMS file that caused this error to be logged. |
| 7 | `MA_ERR_RESOLUTION_C_NAME` | VARCHAR |  | The reason the error was resolved. |
| 8 | `MA_ERR_RESOLUTION_USER_ID` | VARCHAR |  | The user who resolved the error. |
| 9 | `MA_ERR_RESOLUTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `MA_ERR_RESOLUTION_DATE` | DATETIME |  | The date on which the error was resolved. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

