# HSP_BFH_ACT_DATA_PBA

> This table stores billing activity history action-specific data. Every time a billing activity (ATM) is performed on a record or group of records, an activity history record (BFH) is logged. These activity history records store specific data related to each action that was performed on the activity. Each action (and its related data) is logged as a line in related group BFH 300. This table is specifically for actions performed on Premium Billing Accounts (PBA).

**Primary key:** `BFH_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the activity history record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | Stores what system actions were actually performed on the account. |
| 4 | `PBA_ACTION_CARD_ID` | NUMERIC |  | The payment method that was selected when the PBA action was performed. |
| 5 | `DELINQUENT_STATUS_C_NAME` | VARCHAR | org | The delinquency status the Premium Billing Account was set to when an action was performed. |
| 6 | `DELINQUENT_PB_INVC_ID` | VARCHAR |  | The invoice that caused the Premium Billing account to become delinquent. |
| 7 | `INDIV_PB_INVC_ID` | VARCHAR |  | The invoice created from reinvoicing an account using the Reinvoice Account action. |
| 8 | `GRP_PB_INVC_ID` | VARCHAR |  | The invoice created for the group account on a split-billing accounts from using the Reinvoice Account action. |
| 9 | `PB_ACT_TX_ID` | VARCHAR | shared | The Ad Hoc transaction ID generated from the Ad Hoc Adjustment action. |
| 10 | `COLL_PROCESS_IDENT` | INTEGER |  | Stores billing activity history of the id of the process modified by the billing action. |
| 11 | `COLL_MODIFICATION_OPT_C_NAME` | VARCHAR |  | Stores billing activity history for which modification option the user chooses with the Modify Collections Step action. |
| 12 | `ACTION_COMP_PB_COLL_STEP_C_NAME` | VARCHAR | org | Billing activity history item to store step completed by Modify Collections Step. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

