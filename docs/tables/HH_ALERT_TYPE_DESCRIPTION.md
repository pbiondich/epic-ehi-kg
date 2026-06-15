# HH_ALERT_TYPE_DESCRIPTION

> This tables stores the description of an alert type.

**Primary key:** `ALERT_TYPE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_TYPE_ID_ALERT_TYPE_NAME` | VARCHAR |  | The name of the home health alert type. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALERT_DESCRIPTION` | VARCHAR |  | The description of the alert type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

