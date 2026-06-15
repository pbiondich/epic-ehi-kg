# PB_INVOICE

> The PB_INVOICE table contains information about premium billing invoices.

**Primary key:** `PB_INVC_ID`  
**Columns:** 12  
**Joined by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_INVC_ID` | VARCHAR | PK | The unique ID of the premium billing invoice. |
| 2 | `INV_CREATE_DATE` | DATETIME |  | Date invoice was created. |
| 3 | `INV_DUE_DATE` | DATETIME |  | Due date for the invoice. |
| 4 | `INV_STAT_C_NAME` | VARCHAR |  | Indicates the current status of the invoice (printed, payment received, etc.) |
| 5 | `PB_ACCT_ID` | VARCHAR | FK→ | The unique ID of the premium billing account associated with the invoice. |
| 6 | `EFF_MONTH` | DATETIME |  | Effective period for the invoice. This date will correspond to the cycle date of the billing cycle used to generate this invoice. |
| 7 | `INV_NUM` | VARCHAR |  | Invoice number generated using the account ID and the account invoicing sequence number. |
| 8 | `CYL_DATE` | DATETIME |  | Cycle date for the invoice. |
| 9 | `UPDATE_DATE` | DATETIME (Local) |  | The extract date and time of the record for this table. |
| 10 | `PRESUMED_PAYMENT_ID` | VARCHAR |  | The ID of the payment that pays this invoice. |
| 11 | `GRACE_EXCLUSION_YN` | VARCHAR |  | Controls whether an invoice is considered an exception to the FFM grace period rules |
| 12 | `REFUND_INVOICE_YN` | VARCHAR |  | This item is set to yes when the invoice that has been generated was done through refunding. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

## Joined in — referenced by (11)

| From | Column | Confidence |
|------|--------|------------|
| [MC_NOTIFICATIONS](MC_NOTIFICATIONS.md) | `PB_INVC_ID` | high |
| [PB_ACCT_TX_INV_NUM](PB_ACCT_TX_INV_NUM.md) | `PB_INVC_ID` | high |
| [PB_DTL_TX_INVC_NUM](PB_DTL_TX_INVC_NUM.md) | `PB_INVC_ID` | high |
| [PB_INVOICE_NOTIF_HX](PB_INVOICE_NOTIF_HX.md) | `PB_INVC_ID` | high |
| [PB_INVOICE_PMT_HX](PB_INVOICE_PMT_HX.md) | `PB_INVC_ID` | high |
| [PB_INVOICE_PREV](PB_INVOICE_PREV.md) | `PB_INVC_ID` | high |
| [PB_TX_SET_INVOICE](PB_TX_SET_INVOICE.md) | `PB_INVC_ID` | high |
| [V_EHI_PAX_PB_ACCT_TX_INV_NUM](V_EHI_PAX_PB_ACCT_TX_INV_NUM.md) | `PB_INVC_ID` | high |
| [V_EHI_PBI_PB_INVOICE_GRP_TTL](V_EHI_PBI_PB_INVOICE_GRP_TTL.md) | `PB_INVC_ID` | high |
| [V_EHI_PBI_PB_INVOICE_PMT_HX](V_EHI_PBI_PB_INVOICE_PMT_HX.md) | `PB_INVC_ID` | high |
| [V_EHI_PTS_PB_TX_SET_INVOICE](V_EHI_PTS_PB_TX_SET_INVOICE.md) | `PB_INVC_ID` | high |

