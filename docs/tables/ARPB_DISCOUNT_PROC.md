# ARPB_DISCOUNT_PROC

> This table contains discount procedure related information for Professional Billing transactions.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DISCOUNT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `DISCOUNT_AMOUNT` | NUMERIC |  | Stores the amount being discounted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

