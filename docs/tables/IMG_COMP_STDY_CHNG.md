# IMG_COMP_STDY_CHNG

> This stores comparison study change amounts. It is related to table IMG_COMP_STUDIES and can be joined to using the ORDER_ID and the LINE columns.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STUDY_CHNG_AMT_C_NAME` | VARCHAR | org | Contains the amount of change from a comparison study. The comparison order record can be obtained by joining this table to IMG_COMP_STUDIES using the ORDER_ID and LINE columns. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

