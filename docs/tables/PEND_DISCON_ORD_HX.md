# PEND_DISCON_ORD_HX

> This table contains history of information about pending discontinued orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PEND_DISC_ACTION_C_NAME` | VARCHAR |  | The category number for the pending discontinue action for the order. - 1 means the order is still pending discontinued. |
| 4 | `PEND_DISCON_USER_ID` | VARCHAR |  | The user who entered pend discontinue for the order. |
| 5 | `PEND_DISCON_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `PEND_DISC_REASON_C_NAME` | VARCHAR | org | The category number for the reason for discontinue entered by the user who pend discontinued the order. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 7 | `PEND_DISC_INST_DTTM` | DATETIME (Local) |  | Instant at which order was marked as pending discontinued. |
| 8 | `PEND_DISC_VERBAL_LN` | INTEGER |  | This column stores the line index for the Verbal Order Type Flag item in the order record(SI ORD 34800). It tells which line of data in the Verbal Order Type Flag corresponds to the lines of data in the Pending Discontinue Action item (SI ORD 34892). (SIGNED_TYPE_C column in tables ORDER_SIGNED_MED and PRDER_SIGNED_PROC). |
| 9 | `PEND_DC_RES_USER_ID` | VARCHAR |  | User who took action, i.e., verified or rejected the pending discontinued order. |
| 10 | `PEND_DC_RES_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `PENDDC_RES_INS_DTTM` | DATETIME (Local) |  | Instant at which an the pending discontinued order was accepted or rejected. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

