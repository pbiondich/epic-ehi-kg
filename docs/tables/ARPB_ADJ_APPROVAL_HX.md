# ARPB_ADJ_APPROVAL_HX

> This table extracts information about adjustments in PB Adjustment Review workqueues that have been approved or denied.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADJ_APRV_DTTM` | DATETIME (UTC) |  | The instant the adjustment record was approved or declined. |
| 4 | `ADJ_APRV_STATUS_C_NAME` | VARCHAR | org | The category value indicating the adjustment record's approval status. The matching category title can be found in the table ZC_ADJ_APRV_STATUS. |
| 5 | `ADJ_APRV_USER_ID` | VARCHAR |  | The unique ID of the user who approved the adjustment record. |
| 6 | `ADJ_APRV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ADJ_APRV_COMMENT` | VARCHAR |  | The comment left by the user who approved or declined the adjustment record. |
| 8 | `ADJ_DECLINE_RSN_C_NAME` | VARCHAR | org | The category value indicating the reason the adjustment record was declined. The matching category title can be found in the table ZC_ADJ_DECLINE_RSN. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

