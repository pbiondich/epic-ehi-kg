# OR_LOG_PREOP_LVLS

> The table stores the details about the Pre-op acuity levels documented for a patient in a surgical log.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique identifier for the log record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREOP_LEVEL_C_NAME` | VARCHAR | org | The Pre-op acuity level category value for a given time interval in the surgical log. |
| 4 | `PREOP_TIME` | INTEGER |  | The amount of time a patient was documented as having a Pre-op acuity level in a surgical log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

