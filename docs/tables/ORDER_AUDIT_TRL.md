# ORDER_AUDIT_TRL

> This table contains orders that are being audited and their current audit status.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique ID of the order record. |
| 2 | `LINE` | INTEGER | PK | The line count for this table as determined by the number of users who audited the order. |
| 3 | `AUDIT_TRL_AUTH_ID` | VARCHAR |  | The user who authorized the audit. |
| 4 | `AUDIT_TRL_AUTH_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

