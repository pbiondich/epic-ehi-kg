# RES_MICRO_WORKUP_U

> This table contains data for microbiology workup results.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple users that are associated with the line from the RES_MICRO_WORKUP table. |
| 4 | `WORKUP_USER_ID` | VARCHAR |  | Resulting user of each value. |
| 5 | `WORKUP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

