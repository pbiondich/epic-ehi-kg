# ORDER_SPECIMEN_CONDITION

> Indicates the condition of the specimen that was collected.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPEC_CONDITION_C_NAME` | VARCHAR | org | The specimen condition category ID for the order. |
| 4 | `SPEC_CONDITION_CMT` | VARCHAR |  | A free text comment associated with each specimen condition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

