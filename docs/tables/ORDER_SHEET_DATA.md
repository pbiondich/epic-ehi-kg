# ORDER_SHEET_DATA

> This table stores order and scheduling info for active and historical therapy protocols.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The unique identifier for the plan record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_OTP_ID` | NUMERIC |  | Identifiers for order templates (OTP) present in this plan. |
| 4 | `SESS_INTER_C_NAME` | VARCHAR |  | Category value representing the plan level interval of an order. |
| 5 | `SESS_INIT_CNT` | NUMERIC |  | Planned treatment count for an order scheduled for a fixed number of treatments. |
| 6 | `TX_ORD_RELEASE_CNT` | NUMERIC |  | The number of times an order has been generated from the associated order template (OTP). |
| 7 | `SESS_START_DATE` | DATETIME |  | Stores the first date on which treatment with the associated order is planned (user entered or calculated from a relative offset in the protocol). |
| 8 | `ORDER_CAT` | NUMERIC |  | Category associated with the general type of order. |
| 9 | `ORDER_ADDED_DTTM` | DATETIME (Local) |  | Instant at which this order was added to the plan. |
| 10 | `SESS_ORDER_STAT_C_NAME` | VARCHAR | org | Status of the order template. |
| 11 | `LAST_RELEASE_DTTM` | DATETIME (Local) |  | Instant at which the linked order template was last released as an order. |
| 12 | `LAST_RELEASE_ORD_ID` | NUMERIC |  | Identifier for the order (ORD) created on the last release of this order template. |
| 13 | `MIN_TREAT_SEP` | INTEGER |  | The minimum number of days expected between treatments with the affected order. |
| 14 | `TREAT_DIST_C_NAME` | VARCHAR |  | Stores the initial treatment distribution type. This item determines how a treatment is distributed from a chosen interval. If weekly is the chosen interval, only two distribution types are available for selection: any day or specific days. If any day is selected, then user's value in interval details description determine how many times a week this treatment is to be released. If specific days is selected, interval details description displays which days are selected. If another interval type is chosen, then other treatment distribution types are available. Currently this category only has items supporting a weekly interval. |
| 15 | `INTER_DETAILS_DESC` | VARCHAR |  | Stores information on how treatments are distributed in a specified interval. |
| 16 | `DUE_DATE` | VARCHAR |  | Stores the next due date of the linked order. |
| 17 | `OTP_DISPLAY_SEQ` | INTEGER |  | Stores the display order of an order template (OTP) within the therapy plan. |
| 18 | `OTP_GROUP_PRL_CSN` | NUMERIC |  | Stores the contact serial number (CSN) of the protocol contact that this order was associated with for grouping purpose. |
| 19 | `END_DATE` | DATETIME |  | Stores the end date for an order after which the order should be completed. |
| 20 | `DEFAULT_SELECTION_C_NAME` | VARCHAR |  | Stores the default selection status of the order during ordering workflow. |
| 21 | `ORDER_GROUP_CSN` | NUMERIC |  | Stores the source order group contact serial number (CSN) from where the order came from. |
| 22 | `ORDER_GROUP_NUM` | INTEGER |  | Stores a unique number for orders that came from the same order group. |
| 23 | `ORDER_GROUP_DFLT_SELECTION_C_NAME` | VARCHAR |  | Stores the default selection status of the order group during ordering workflow. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

