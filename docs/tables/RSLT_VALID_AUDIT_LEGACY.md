# RSLT_VALID_AUDIT_LEGACY

> This table contains legacy validation audit information for the result.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VALIDATION_PERSON` | VARCHAR |  | The user who validated the legacy result. |
| 4 | `VALIDATION_DTTM` | DATETIME (Local) |  | The date and time when the legacy result was validated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

