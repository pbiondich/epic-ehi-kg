# SPEC_PLACED_IN_SOLN

> Stores whether the specimen was placed in solution after collection.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPEC_PLACED_IN_SOLN_C_NAME` | VARCHAR | org | Stores whether the specimen was placed in solution after collection. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

