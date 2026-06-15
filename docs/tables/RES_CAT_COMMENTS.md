# RES_CAT_COMMENTS

> This table contains test-level result category comments.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RES_COMMENT_C_NAME` | VARCHAR | org | The category number of the test-level result category comment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

