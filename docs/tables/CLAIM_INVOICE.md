# CLAIM_INVOICE

> Stores information about AP claim invoices.

**Primary key:** `CLAIM_INVC_ID`  
**Columns:** 9  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_INVC_ID` | VARCHAR | PK | The unique identifier (.1 item) for the invoice record. |
| 2 | `CREATION_DATE` | DATETIME |  | Stores the date the invoice was created. |
| 3 | `DUE_DATE` | DATETIME |  | Stores the date when the invoice is due. |
| 4 | `INV_STAT_C_NAME` | VARCHAR |  | Stores the category identifier of the invoice's status. |
| 5 | `CLAIM_ACCT_ID` | VARCHAR |  | Stores the unique identifier of the AP claim billing account for this invoice. |
| 6 | `INVOICE_NUMBER` | VARCHAR |  | Stores the invoice number. |
| 7 | `INVOICE_TYPE_C_NAME` | VARCHAR |  | The category identifier of the invoice type. |
| 8 | `RESP_CLASS_TYPE_C_NAME` | VARCHAR |  | The category identifier of the responsibility class for this invoice. |
| 9 | `BATCH_RUN_CSN_ID` | NUMERIC |  | The contact serial number of the batch run that creates this invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [CLAIM_INVOICE_STATUS_HX](CLAIM_INVOICE_STATUS_HX.md) | `CLAIM_INVC_ID` | high |

