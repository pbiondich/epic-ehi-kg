# FEE_SCHEDULE_MAP

> The FEE_SCHEDULE_MAP table contains basic information about the fee schedule map that is used to select a fee schedule and conversion factor table per geographic area.

**Primary key:** `FEE_SCHEDULE_MAP_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FEE_SCHEDULE_MAP_ID` | NUMERIC | PK | The unique identifier for the fee schedule map record. |
| 2 | `FEE_SCHEDULE_MAP_ID_FEE_SCHEDULE_MAP_NAME` | VARCHAR |  | The name for the fee schedule map record. |
| 3 | `FEE_SCHEDULE_MAP_NAME` | VARCHAR |  | The name for the fee schedule map record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

