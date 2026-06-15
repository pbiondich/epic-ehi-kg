# OR_LOG_ANESTLOC

> The OR_LOG_ANESTLOC table contains OR management system log anesthesia locations.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the log record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the anesthesia location information for the log. |
| 3 | `ANESTH_TYPE_C_NAME` | VARCHAR | org | The category value of the type of anesthesia used in the log. |
| 4 | `ANESTH_LOC_C_NAME` | VARCHAR | org | The category value of the anesthesia location in the log. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

