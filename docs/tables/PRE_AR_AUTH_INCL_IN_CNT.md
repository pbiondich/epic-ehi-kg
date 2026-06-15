# PRE_AR_AUTH_INCL_IN_CNT

> This table extracts indicators for which charge lines are included in authorization counts.

**Primary key:** `TAR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the charge session record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `INCL_IN_AUTH_CHG_CNT_YN` | VARCHAR |  | This item indicates whether the charge line contributes to the used count of the authorization linked to it. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

