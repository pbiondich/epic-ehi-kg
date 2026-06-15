# ANATOMY_NOADD

> This table contains the items for dental teeth records.

**Primary key:** `FINDING_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `DENTAL_TOOTH_STAT_C_NAME` | VARCHAR |  | Current status of the tooth |
| 3 | `ANATOMY_ACTIVE_FLAG_C_NAME` | VARCHAR |  | Indicates whether a tooth should be shown in the tooth chart. |
| 4 | `ANATOMY_TEMPL_ID` | NUMERIC |  | Identifier of the anatomy template associated with this record. |
| 5 | `ANATOMY_TEMPL_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

