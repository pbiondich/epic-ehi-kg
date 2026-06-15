# RAD_THP_VOLUME_MORPH

> This table is used to hold Radiotherapy Volume Morphology information.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

