# SPEC_ACCESS_TIER

> This table contains a list of labs that should have access to a specimen. The first line is the accessioning lab. An additional line is added each time the specimen is received into a new lab.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique ID of the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACCESS_TIER_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

