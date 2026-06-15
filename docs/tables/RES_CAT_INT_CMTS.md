# RES_CAT_INT_CMTS

> This table contains test-level result internal category comments.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RES_INT_CMT_C_NAME` | VARCHAR | org | The category number of the test-level result internal category comment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

