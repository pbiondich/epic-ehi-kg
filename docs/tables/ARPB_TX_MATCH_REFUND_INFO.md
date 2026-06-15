# ARPB_TX_MATCH_REFUND_INFO

> Clarity table for refund's matching transaction information.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MATCH_HX_LINE` | INTEGER |  | This data is populated exclusively on the refund. This item holds a pointer to the matching line number in the refund ETR's 800 table. |
| 4 | `MATCH_CHARGE_ID` | NUMERIC |  | This data is populated exclusively on a refund. This item holds the matched charge ids. |
| 5 | `MATCH_CHARGE_AMT` | NUMERIC |  | This data is populated exclusively on a refund. This item holds the matched charge amounts. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

