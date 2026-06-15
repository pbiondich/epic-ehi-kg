# ARPB_TX_REFUND_HX

> This table contains refund request activity history information for payments that have been refunded.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | Payment transaction (ETR) ID that was refunded. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REF_REQ_HX_USER_ID` | VARCHAR |  | The user who performed the refund request activity. |
| 4 | `REF_REQ_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REF_REQ_HX_ACT_C_NAME` | VARCHAR |  | The refund request activity performed. |
| 6 | `REF_REQ_HX_COMMENT` | VARCHAR |  | The comment associated with the refund request activity. |
| 7 | `REF_REQ_HX_REF_NUM` | NUMERIC |  | The refund number of the refund request. |
| 8 | `REF_REQ_HX_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the refund request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

