# ASSOCIATED_COSD_EPISODES

> This table contains cancer pathways and their associated Cancer Outcomes and Services Dataset (COSD) episodes.

**Primary key:** `ADMIN_PWY_PERIOD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ADMIN_PWY_PERIOD_ID` | NUMERIC | PK | The unique identifier (.1 item) for the admin pathway episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ASSOCIATED_COSD_EPISODE_ID` | NUMERIC |  | The COSD episode record associated with the admin pathway period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

