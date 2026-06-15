# V_EHI_PBI_PB_INVOICE_PMT_HX

> This view filters out invoice data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_INVC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_INVC_ID` | VARCHAR | PK FK→ | The unique ID of the premium billing invoice. |
| 2 | `LINE` | INTEGER | PK | Line counter for the payment on the invoice. |
| 3 | `PMT_AMT` | NUMERIC |  | Amount of payment towards the invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |

