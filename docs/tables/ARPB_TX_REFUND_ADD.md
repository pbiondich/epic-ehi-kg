# ARPB_TX_REFUND_ADD

> This table contains the refund address entered on the Refund Request Slip form. Use this table in conjunction with ARPB_TX_REFUND to display the full address entered on the Refund Request Slip form.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REFUND_ADDR_ADDRESS` | VARCHAR |  | This column contains the refund address entered on the Refund Request Slip form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

