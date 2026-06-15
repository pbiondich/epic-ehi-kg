# V_EHI_PBI_PB_INVOICE

> This view filters out invoice data that is not appropriate for member level EHI exports when group billing or claims invoicing is used.

**Primary key:** `INVOICE_ID`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | VARCHAR | PK FK→ | The unique ID of the premium billing invoice. |
| 2 | `INV_BAL_DUE` | NUMERIC |  | Balance due for the invoice. |
| 3 | `LAST_INV_AMT` | NUMERIC |  | Amount of the last invoice for the premium billing account. |
| 4 | `BAL_FWD_AMT` | NUMERIC |  | Total balance forward from the last invoice. |
| 5 | `NEW_ACTV_AMT` | NUMERIC |  | Total amount for new activity included on the invoice, including new credits. |
| 6 | `NEW_CHRG` | NUMERIC |  | Total new charges included on the invoice. |
| 7 | `THIS_CYL_AMT` | NUMERIC |  | Total amount of new premium charges for this invoice. This amount does not include retroactive transactions. |
| 8 | `RETRO_PREM_AMT` | NUMERIC |  | Amount of retroactive premium on the invoice. |
| 9 | `PREM_ADJ_AMT` | NUMERIC |  | Amount of premium adjustments on the invoice. |
| 10 | `OTHER_ADJ_AMT` | NUMERIC |  | Amount of other adjustments included on the invoice. |
| 11 | `TOTAL_PAID_AGAINST` | NUMERIC |  | Total paid against the invoice to date. |
| 12 | `OUTSTAND_AMT` | NUMERIC |  | Amount outstanding for the invoice. This amount includes unused credits associated with the invoice. |
| 13 | `OUT_NEW_CHRG` | NUMERIC |  | Outstanding new charges for the invoice. This represents the amount of charge transactions left to be closed in payment posting related to this invoice. |
| 14 | `OVERPOST_AMT` | NUMERIC |  | Total amount of overposts that appear for the first time on this invoice. |
| 15 | `AMT_IN_OPEN_PTS` | NUMERIC |  | Amount of payment against this invoice that is currently included in uncommitted payment transaction sets. |
| 16 | `THIS_CYL_APTC_AMT` | NUMERIC |  | The APTC amount for the current billing cycle. |
| 17 | `THIS_CYL_LEP_AMT` | NUMERIC |  | This field contains the amount of the Medicare Part D late enrollment penalty for this invoice. |
| 18 | `SEC_INV_BAL_DUE` | NUMERIC |  | The amount due on the secondary invoice. |
| 19 | `SEC_INV_NEW_ACTV_AMT` | NUMERIC |  | The amount of charges on the secondary invoice that are new. This includes both the amount for the current cycle, as well as any new charges from retro. |
| 20 | `SEC_INV_THIS_CYL_AMT` | NUMERIC |  | The amount of premium charges on the secondary invoice. This does not include retro. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

