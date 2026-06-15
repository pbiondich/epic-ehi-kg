# TC_REQUEST_STATUS_MOD_HX

> This table stores information related to the request status modifier change history for Transfer Center requests.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TC_REQUEST_STATUS_MOD_C_NAME` | VARCHAR | org | This item stores the audit trail for the request status modifier changes to the Transfer Center request. |
| 2 | `REQUEST_MOD_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | This item specifies the instant when the Transfer Center request's status modifier changed. |
| 3 | `TRANS_AUD_TC_FUTURE_RSN_C_NAME` | VARCHAR | org | This item stores the audit trail for the future reason changes to the Transfer Center request. |
| 4 | `TRANSFER_AUDIT_FUTURE_UTC_DTTM` | DATETIME (UTC) |  | This item stores the audit trail for the future date changes to the Transfer Center request. |
| 5 | `COMM_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the communication record. |
| 6 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 7 | `TRANS_MOD_AUD_USER_ID` | VARCHAR |  | This item stores the user who changed the request status modifier for the Transfer Center request. |
| 8 | `TRANS_MOD_AUD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `TRANSFER_RETURN_FROM_F_C_NAME` | VARCHAR |  | Stores the reason why a Transfer Center request got moved from the future tab into another status tab. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

