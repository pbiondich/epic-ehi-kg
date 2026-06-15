# SPEC_BIOPSY_FLUID_INFO

> Stores the biopsy fluid added to the specimen.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BIOPSY_FLUID_C_NAME` | VARCHAR | org | Type of biopsy fluid added to the specimen. |
| 4 | `BIOPSY_FLUID_DATE` | DATETIME |  | Date that biopsy fluid was added to the specimen. |
| 5 | `BIOPSY_FLUID_TM` | DATETIME (Local) |  | Time that biopsy fluid was added to the specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

