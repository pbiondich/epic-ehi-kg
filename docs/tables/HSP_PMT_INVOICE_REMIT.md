# HSP_PMT_INVOICE_REMIT

> Invoice level remittance information for a payment.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INV_GRP_CODE_C_NAME` | VARCHAR | org | Stores the group code corresponding to the reason code at the invoice level. |
| 4 | `INV_REMIT_CODE_ID` | VARCHAR |  | Stores the invoice level reason code or remark codes. |
| 5 | `INV_REMIT_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 6 | `INV_RSN_CODE_EXTL` | VARCHAR |  | Stores the invoice level external reason code or remark codes. |
| 7 | `INV_RMT_AMT` | NUMERIC |  | Stores the amount associated with the reason code at the invoice level. |
| 8 | `INV_RMK_CODES` | VARCHAR |  | Stores information about the remark codes that are associated with specific reason codes. This is a comma delimited list of remark codes. The system will associate all remark codes present at the invoice level to every reason code at the invoice level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

