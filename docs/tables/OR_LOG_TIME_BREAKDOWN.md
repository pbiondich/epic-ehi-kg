# OR_LOG_TIME_BREAKDOWN

> This table contains documentation regarding the breakdown of the case time.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LOG_TIME_CLASS_C_NAME` | VARCHAR | org | This item is used to document the classification of the case time. |
| 4 | `LOG_TIME_DURATION` | INTEGER |  | This item is used to document the duration of a specified classification of the case time. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

