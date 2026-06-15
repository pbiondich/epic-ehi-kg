# INVOICE_APC

> The INVOICE_APC table contains information on payment classifications.

**Primary key:** `INVOICE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | NUMERIC | PK FK→ | The unique ID of the invoice record. |
| 2 | `LINE` | INTEGER | PK | The line number of the payment classification type for this invoice record. |
| 3 | `PC_TYPE_C_NAME` | VARCHAR |  | The type of payment classification that appears on the invoice (i.e. CPT™, APC, etc.) |
| 4 | `PC_CODE` | VARCHAR |  | The payment classification code that appears on the invoice. |
| 5 | `PC_MODIFIER` | VARCHAR |  | The payment classification modifier that appears on the invoice. |
| 6 | `PC_SERVICE_DATE` | DATETIME |  | The service date the services were performed on. |
| 7 | `PC_PMT_STAT_IND_C_NAME` | VARCHAR |  | The status indicator for this payment classification. |
| 8 | `PC_ETR_LIST` | VARCHAR |  | The transaction record that appears on the invoice. |
| 9 | `PC_ORIG_REIMB_AMT` | NUMERIC |  | The payment classification reimbursement amount that appears on the invoice. |
| 10 | `PC_REIMB_AMT` | NUMERIC |  | The payment classification expected reimbursement amount that appears on the invoice. |
| 11 | `PC_QUANTITY` | NUMERIC |  | The payment classification quantity that appears on the invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |

