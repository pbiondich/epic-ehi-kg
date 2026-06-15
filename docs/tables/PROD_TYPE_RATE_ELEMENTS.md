# PROD_TYPE_RATE_ELEMENTS

> This table contains information about the product type assigned to a specific premium rate element used in commission calculation for the transaction.

**Primary key:** `TX_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `RATE_ELEMENT_PROD_TYPE_C_NAME` | VARCHAR | org | The product type of the premium rate element used in the formula. This item is only used in conjunction with a Premium Rate Element Identifier value to find premiums paid for plans of a specific product type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

