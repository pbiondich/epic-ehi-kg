# ORD_CV_INV_LOG

> Table ORD_CV_INV_LOG allows users to report on orders which have intraprocedure log information filed by an external system.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record |
| 2 | `LINE` | INTEGER | PK | The line number for information associated with this record. |
| 3 | `INTERV_FROM_EXT_ID` | VARCHAR |  | Stores a pointer to a note record which was filed via an interface. |
| 4 | `INTERV_FROM_EXT_DAT` | VARCHAR |  | Stores the contact date (DAT) of the last contact on the note record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

