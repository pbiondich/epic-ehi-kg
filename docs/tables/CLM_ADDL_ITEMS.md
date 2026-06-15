# CLM_ADDL_ITEMS

> This table stores the additional item code and additional item types that are found at the header level of a claim.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLM_ADDL_ITEM_CODE` | VARCHAR |  | Stores the code associated with the additional item type of a claim. |
| 4 | `CLM_ADDL_ITM_TYPE_C_NAME` | VARCHAR | org | The Additional Data Type category ID for the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

