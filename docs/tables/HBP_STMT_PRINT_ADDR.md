# HBP_STMT_PRINT_ADDR

> This table stores the billing address of the guarantor for a given Hospital Billing statement print record.

**Primary key:** `HBP_PRINT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HBP_PRINT_ID` | NUMERIC | PK FK→ | The unique identifier for the bill print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BILL_ADDR` | VARCHAR |  | The billing address of the guarantor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HBP_PRINT_ID` | [HBP_STMT_PRINT](HBP_STMT_PRINT.md) | sole_pk | high |

