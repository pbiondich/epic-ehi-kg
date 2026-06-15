# CUST_SERVICE_TRANS_DX

> The CUST_SERVICE_TRANS_DX table contains diagnosis-related information collected for a transfer patient in both free text and coded form.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the customer service communication. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TRANS_DX_TEXT` | VARCHAR |  | Free text diagnoses for the transfer patient. |
| 4 | `TRANS_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 5 | `TRANS_DX_CATEGORY_C_NAME` | VARCHAR | org | Enter the diagnosis category for the transfer patient. If an encounter is created from this request, data from this item will be copied to I EPT 10151. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

