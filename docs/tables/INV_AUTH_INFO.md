# INV_AUTH_INFO

> This table will extract invoice level authorization information.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The invoice record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INV_AUTH_INV_NUM` | VARCHAR |  | The invoice number for the related group. |
| 4 | `INV_AUTH_CVG_ID` | NUMERIC |  | The coverage ID for the authorization. |
| 5 | `AUTH_NUM` | VARCHAR |  | The authorization number for the coverage. |
| 6 | `REF_NUM` | VARCHAR |  | The referral number for the coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

