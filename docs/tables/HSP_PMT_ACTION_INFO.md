# HSP_PMT_ACTION_INFO

> This table will hold the actions that were attempted to be performed for a payment. There will also be a result and reason if the action was not performed.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PMT_ACTION_C_NAME` | VARCHAR |  | Stores the actions that were attempted to be performed on the payment |
| 4 | `PMT_ACTION_DONE_C_NAME` | VARCHAR |  | Stores the result of the action that was attempted. |
| 5 | `PMT_ACTION_CMT` | VARCHAR |  | Stores the reason why this action was or was not performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

