# HSP_CLP_CMS_TX_PIECES

> This table contains the hospital transactions that were used in the creation of CMS claim lines in Hospital Billing.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`, `TX_PIECE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number of the claim line in the claim record. |
| 3 | `TX_PIECE` | INTEGER | PK | The index of the transaction for the claim line. |
| 4 | `TX_ID` | NUMERIC | shared | ID of the hospital transaction used in the creation of this claim line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

