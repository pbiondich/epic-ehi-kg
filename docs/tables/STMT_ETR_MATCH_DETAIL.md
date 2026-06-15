# STMT_ETR_MATCH_DETAIL

> This table contains information about Professional Billing transaction matching for a given statement.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement print or detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_ID` | NUMERIC | shared | Professional Billing transaction ID in matched transaction table. |
| 4 | `MATCH_TX_ID` | NUMERIC |  | Matched Professional Billing transaction ID in matched transaction table. |
| 5 | `MATCH_DATE` | DATETIME |  | Matched date in matched transaction table. |
| 6 | `UNMATCH_DATE` | DATETIME |  | Unmatched date in matched transaction table. |
| 7 | `AMOUNT` | NUMERIC |  | Amount (self pay + insurance) matched or unmatched in matched transaction table. |
| 8 | `INS_AMT` | NUMERIC |  | Insurance amount matched or unmatched in matched transaction table. |
| 9 | `SP_AMT` | NUMERIC |  | Self-pay amount matched or unmatched in matched transaction table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

