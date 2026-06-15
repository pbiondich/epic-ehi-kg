# ARPB_TX_MODIFIERS

> This table contains multiple response information for modifiers associated with A/R (ETR) transactions.

**Primary key:** `ETR_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ETR_ID` | NUMERIC | PK | The unique ID of the transaction (ETR) record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_MODIFIER` | VARCHAR |  | The external ID of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

