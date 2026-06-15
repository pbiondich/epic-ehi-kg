# HSP_PMT_REMIT_DETAIL

> This is a type of summary level of the remittance actions associated with a payment transaction. This table will summarize remittance information from Electronic Remittance and manual payment posting as stored on the transaction. This table extracts the information that displays in the remittance grid in payment posting as the end user sees it.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DTL_GRP_CODE_C_NAME` | VARCHAR | org | This column stores the group code for the reason code that is entered in the remittance grid when this batch is opened in payment posting. |
| 4 | `DTL_REMIT_CODE_ID` | VARCHAR |  | This column stores the remit code that is entered in the remittance grid when this batch is opened in payment posting. |
| 5 | `DTL_REMIT_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 6 | `DTL_RSN_CODE_EXTL` | VARCHAR |  | This column stores the external reason code that is entered in the remittance grid when this batch is opened in payment posting. |
| 7 | `DTL_REMIT_AMT` | NUMERIC |  | This column stores the amount associated with the reason code that is entered in the remittance grid when this batch is opened in payment posting. |
| 8 | `DTL_ACTION_STRING` | VARCHAR |  | This column stores the actions associated with the reason code that is entered in the remittance grid when this batch is opened in payment posting. This is a comma delimited string of actions for reason codes with multiple actions associated with them. |
| 9 | `DTL_CREATE_BDC_YN` | VARCHAR |  | This column stores whether a denial or remark record should be created with the reason code. If any action on the reason code creates a denial or remark, this column will be set to Yes, otherwise this column will be set to No. |
| 10 | `DTL_SERVICE_LINE` | INTEGER |  | This column stores the service line this reason code was entered in on the remittance grid when this batch was opened in payment posting. If any reason code was entered at the claim level this row will be set to -1. |
| 11 | `DTL_DFLTCD_MAPCOL_C_NAME` | VARCHAR |  | This column contains the mapped column of the defaulted remit code. |
| 12 | `DTL_AUTO_CLOSE_YN` | VARCHAR |  | This field contains whether the follow-up record should be auto-closed after being created. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

