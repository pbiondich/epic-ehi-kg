# CLM_PMT_HISTORY

> The CLM_PMT_HISTORY table contains claim level history for how a payment was processed.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique ID for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLM_PMT_HISTORY_C_NAME` | VARCHAR |  | Contains an action that was taken for the payment. |
| 4 | `CLM_PMT_COMMENT` | VARCHAR |  | Contains a comment for an action that was taken for the payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

