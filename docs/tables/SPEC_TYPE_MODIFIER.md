# SPEC_TYPE_MODIFIER

> Contains order specimen type modifier data.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPEC_TYPE_MOD_C_NAME` | VARCHAR | org | Modifiers associated with the order specimen type |
| 4 | `SPEC_TYPE_MOD_SNOCD` | VARCHAR |  | SNOMED codes associated with specimen modifiers |
| 5 | `SPEC_TYPE_MOD_SNO_C_NAME` | VARCHAR |  | Details whether the associated SNOMED code was Reported discretely or Inferred |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

