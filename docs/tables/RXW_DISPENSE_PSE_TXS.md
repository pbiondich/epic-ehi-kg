# RXW_DISPENSE_PSE_TXS

> This table contains the list of pseudoephedrine sales compliance database transactions associated with a point of sale transaction.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PSE_SALE_TX_IDENT` | VARCHAR |  | The pseudoephedrine sales compliance system transaction IDs. The first ID will always be the initial Pseudoephedrine Transaction ID from the initial purchase. For returns, the Pseudoephedrine Return ID will be stored on the subsequent lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

