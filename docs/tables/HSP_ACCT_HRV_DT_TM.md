# HSP_ACCT_HRV_DT_TM

> This table holds the abstracted organ harvest date(s) for the organ(s) donated by the patient. Note: The information in this table cannot be guaranteed to be accurate and complete unless the programming point 41273 - Organ Harvest Info Missing is set as an abstract validation check.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The ID of the hospital account associated with the abstracted organ harvest date(s). |
| 2 | `LINE` | INTEGER | PK | This column stores the line number in the results of a query. Because multiple organs may be donated by a patient, there may be multiple organ harvest dates stored on one hospital account. Therefore, each abstracted organ harvest date will have a unique line number. |
| 3 | `HARVEST_DATE_TIME` | DATETIME (UTC) |  | This abstracting item indicates the organ harvest date(s) and time(s) associated with the organ(s) donated by the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

