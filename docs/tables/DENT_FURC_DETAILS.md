# DENT_FURC_DETAILS

> Contains location and classification details for furcation findings.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENT_FURC_LOC_C_NAME` | VARCHAR |  | Stores the locations where furcation is present on a tooth. |
| 4 | `DENT_FURC_CLASS_C_NAME` | VARCHAR |  | Stores the classification of furcation present on a tooth. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

