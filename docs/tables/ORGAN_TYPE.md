# ORGAN_TYPE

> Table of organ descriptors.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this contact. |
| 3 | `ORG_ID` | NUMERIC |  | Type of organ, such as right kidney or left lung. |
| 4 | `ORG_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

