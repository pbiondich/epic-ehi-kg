# IP_CP_TIMEMARK

> This table no longer contains accurate information about Care Plan Review / Documentation data. Table CAREPLAN_TIMEMARK can be used instead of this table.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. |
| 3 | `EDIT_TIME` | DATETIME (Local) |  | The instant Care Plan was edited ( e.g. Document or Review ) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

