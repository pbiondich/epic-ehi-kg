# AP_CLAIM_INVOICE_RESP

> The AP_CLAIM_INVOICE_RESP table contains billing information for self-funded claims, including the invoice amount, pay cycle recovered amount, and billing cycle recovered amount, categorized by responsibility class.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLAIM_INV_RESP_CLASS_ID` | NUMERIC |  | The responsibility class of the current line. |
| 4 | `CLAIM_INV_RESP_CLASS_ID_RECORD_NAME` | VARCHAR |  | The name of the responsibility class record. |
| 5 | `CLAIM_INV_RESP_INVOICE_AMT` | NUMERIC |  | Amount invoiced through AP Claim billing cycles |
| 6 | `CLAIM_INV_RESP_AP_RCVD_AMT` | NUMERIC |  | Amount previously recovered through the AP Claim Pay Cycle. |
| 7 | `CLAIM_INV_RESP_AR_RCVD_AMT` | NUMERIC |  | Amount previously recovered through the AP Claim billing cycles. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

