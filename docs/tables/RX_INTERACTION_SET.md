# RX_INTERACTION_SET

> This table contains basic information on interaction setting records. These settings control the context in which warnings are seen by users. Interaction settings can be either system-level or user-level.

**Primary key:** `SETTING_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SETTING_ID` | NUMERIC | PK shared | The unique record ID (.1) for this FIS record. |
| 2 | `SETTING_ID_SETTING_NAME` | VARCHAR |  | The name of the interaction setting. |
| 3 | `SETTING_NAME` | VARCHAR |  | The name of the interaction setting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

