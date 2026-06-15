# SPEC_MATERIAL_TREATMENT

> This table contains information about the treatment of the specimen material.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MATERIAL_TREATMENT_C_NAME` | VARCHAR | org | The treatment of the specimen material. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

