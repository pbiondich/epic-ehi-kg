# HSP_CLP_UB_TX_PIECES

> This table contains the hospital transactions that were used in the creation of UB claim lines in Hospital Billing.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`, `TX_PIECE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number of the claim line in the claim print record. |
| 3 | `TX_PIECE` | INTEGER | PK | The hospital transaction IDs used for the claim line. |
| 4 | `TX_ID` | NUMERIC | shared | ID of the hospital transaction used in the creation of this claim line. |
| 5 | `CLAIM_LINE_NUM` | INTEGER |  | The ordinal position of the claim line. This can be different than the line number in the claim print record for claim print records that include summary lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

