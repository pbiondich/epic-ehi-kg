# AUTHORIZATION_TYPE

> This table identifies whether the authorization number for the claim is a referral number or a prior authorization number.

**Primary key:** `INVOICE_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the invoice record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AUTHORIZATION_TYPE_C_NAME` | VARCHAR |  | The authorization type category ID identifying whether the authorization number on the row is a referral number or prior authorization number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

