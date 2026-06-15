# INV_TX_PIECES

> This table contains Professional Billing charge transactions associated with invoice service lines.

**Primary key:** `INV_ID`, `LINE`, `TX_PIECE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INV_ID` | NUMERIC | PK | The unique identifier for the invoice record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `TX_PIECE` | INTEGER | PK | The position of the transaction ID in the comma-delimited list of transaction IDs for a given line. |
| 4 | `TX_ID` | NUMERIC | shared | The ID of the transaction associated with the claim line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

