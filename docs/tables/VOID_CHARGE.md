# VOID_CHARGE

> This table contains the Specimens (OVS) void charge table.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOURCE_INI` | VARCHAR |  | Source database (INI) of the charge that should not be dropped. |
| 4 | `SOURCE_ID` | VARCHAR |  | Source identifier of the charge that shouldn't be dropped |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

