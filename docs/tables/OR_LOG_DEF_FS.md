# OR_LOG_DEF_FS

> The OR_LOG_DEF_FS table contains the default Flowsheets used in the log.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log record. |
| 2 | `LINE` | INTEGER | PK | The line number of the defaulted flowsheet templates used for this log. |
| 3 | `DEFAULT_FLOWSHEETS` | VARCHAR |  | The default flowsheet templates used for this log. |
| 4 | `DEFAULT_FLOWSHEETS_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

