# RATE_TBL

> The RATE_TBL table contains rate tables used for capitation, broker commissions, and premium billing.

**Primary key:** `RATE_TABLE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RATE_TABLE_ID` | VARCHAR | PK | The unique ID of the capitation rate table. |
| 2 | `RATE_TABLE_ID_RATE_TABLE_NAME` | VARCHAR |  | Name of the capitation rate table. |
| 3 | `RATE_TABLE_NAME` | VARCHAR |  | Name of the capitation rate table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

