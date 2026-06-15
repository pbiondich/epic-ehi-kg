# OB_DEL_PROC

> This table contains the category values which correspond to procedures that occur during or immediately following the delivery. This data is documented in the Delivery Summary.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the summary block record. The delivery record ID on which the data is stored. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEL_PROC_C_NAME` | VARCHAR | org | The category values which correspond to procedures that occur during or immediately following the delivery. This data is documented in the Delivery Summary. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

