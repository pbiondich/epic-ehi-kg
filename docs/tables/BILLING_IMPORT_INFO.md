# BILLING_IMPORT_INFO

> This table stores items that contain billing details.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BILL_INVOICE_NUM` | VARCHAR |  | This item stores the invoice number. |
| 4 | `BILL_ICN` | VARCHAR |  | This item stores the ICN. |
| 5 | `BILL_PMT_DPST_DATE` | DATETIME |  | This item stores the payment deposit date. |
| 6 | `BILL_PMT_AMT` | NUMERIC |  | This item stores the payment amount. |
| 7 | `BILL_PAGE_NUM` | INTEGER |  | This item stores the document page number. |
| 8 | `BILL_PAYER_NM` | VARCHAR |  | This item stores the payer name in the scanned document. |
| 9 | `BILL_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 10 | `BILL_ACCT_ID` | NUMERIC |  | This item stores the guarantor ID. |
| 11 | `BILL_HSP_ACCOUNT_ID` | NUMERIC |  | This item stores the hospital account ID. |
| 12 | `BILL_REF_NUM` | VARCHAR |  | This item stores the payment reference number on the scanned document. |
| 13 | `BILL_STMT_NUM` | VARCHAR |  | This item stores the statement number. |
| 14 | `BILL_BDC_ID` | NUMERIC |  | This item stores the BDC ID for lines associated with follow-up records. |
| 15 | `BILL_IMPORT_ERRORS` | VARCHAR |  | This item stores list of errors for the given line of the import document received from import. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

