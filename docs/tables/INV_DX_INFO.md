# INV_DX_INFO

> Stores claim-level diagnosis information sent on Resolute Professional Billing claims. Diagnosis information is coming from the INV 350 related group. The Group 100 column corresponds to claims that were sent.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The unique ID of the invoice. |
| 2 | `LINE` | INTEGER | PK | The line count value of the invoice related group. |
| 3 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `INV_NUM` | VARCHAR |  | The external ID of the invoice that is associated with the claim. |
| 5 | `INV_NUM_100_GRP_LN` | INTEGER |  | Claim line number that the diagnosis entry applies to. This is the line number that links the INV_DX_INFO table with the LINE column in the INV_BASIC_INFO table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

