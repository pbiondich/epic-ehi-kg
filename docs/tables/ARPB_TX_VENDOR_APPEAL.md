# ARPB_TX_VENDOR_APPEAL

> Status of Vendor Appeals.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VENDOR_APPEAL_FLG_C_NAME` | VARCHAR | org | The APPEAL_FLAG category number for this row. This determines the type of response represented by this row. |
| 4 | `VENDOR_RESPONSE_DT` | DATETIME |  | The date when this response was received. |
| 5 | `VENDOR_REIMB` | NUMERIC |  | The reimbursement amount associated with the response. |
| 6 | `VENDOR_VARIANCE` | NUMERIC |  | The variance amount associated with the response. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

