# RES_MICRO_WORKUP

> This table contains data for microbiology workup results.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WORKUP_ISOLATE` | NUMERIC |  | Stores unique organism identifier (CUID) of the isolate for each line. |
| 4 | `WORKUP_PLATE_C_NAME` | VARCHAR | org | Plate tested for each line. |
| 5 | `WORKUP_COMP_ID` | NUMERIC |  | Component tested for each line. |
| 6 | `WORKUP_COMP_ID_NAME` | VARCHAR |  | The name of the component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

