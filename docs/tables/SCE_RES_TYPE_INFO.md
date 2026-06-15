# SCE_RES_TYPE_INFO

> This table stores resource type availability info.

**Primary key:** `RESRC_AVAIL_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESRC_AVAIL_ID` | NUMERIC | PK | The unique ID number of the record used to store scheduling availability information for a provider. |
| 2 | `RESRC_AVAIL_ID_RECORD_NAME` | VARCHAR |  | The name of an Area, Department or Location based on type of record. |
| 3 | `RECORD_NAME` | VARCHAR |  | The name of an Area, Department or Location based on type of record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

