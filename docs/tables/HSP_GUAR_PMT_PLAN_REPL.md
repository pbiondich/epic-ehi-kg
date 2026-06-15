# HSP_GUAR_PMT_PLAN_REPL

> This table contains hospital guarantor payment plan information.

**Primary key:** `GUAR_ACCOUNT_ID`, `LINE`  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GUAR_ACCOUNT_ID` | NUMERIC | PK | The unique ID of the guarantor account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PP_START_DATE` | DATETIME |  | The Hospital Billing payment plan start date. |
| 4 | `PP_INIT_BAL` | NUMERIC |  | Hospital Billing Payment plan initial balance |
| 5 | `PP_AMT` | NUMERIC |  | Hospital Billing Payment plan monthly payment amount |
| 6 | `PP_NUM_PMTS` | INTEGER |  | Hospital Billing Payment plan number of payments |
| 7 | `PP_EFF_INST_DTTM` | DATETIME (UTC) |  | The instant the payment plan was set up (UTC). |
| 8 | `PP_TERMS_TYPE_C_NAME` | VARCHAR |  | The term type (monthly amount or number of payments) the payment plan was created with. |
| 9 | `PP_ORIG_PLAN_LINE` | INTEGER |  | Holds the original plan line in the related group if the current line is an update. If the current line is a new plan, the item is null. |
| 10 | `PP_STMT_DAY_OF_MO` | INTEGER |  | Stores the day of month to process statements for a payment plan with Auto Pay. |
| 11 | `CARD_ID` | NUMERIC |  | Stores the payment method ID for Hospital Billing payment plans on Auto Pay. |
| 12 | `PP_APAY_DAY_OF_MO` | INTEGER |  | Stores the day of month to charge the payment method on file and post a payment on the guarantor. This item forces statement cycle for monthly drop cycle. |
| 13 | `PP_CREATE_USER_ID` | VARCHAR |  | Stores the ID of the user in Epic who set up this payment plan. If this item is populated, then the system knows this plan was set up by a user via Hyperspace. |
| 14 | `PP_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `PP_CREATE_MYPT_ID` | VARCHAR |  | Stores the MyChart user who set up this payment plan. If this item is populated, then the system knows this plan was set up by a guarantor via MyChart rather than through customer service in Hyperspace. |
| 16 | `PP_SOURCE_C_NAME` | VARCHAR |  | Stores the source workflow that set up this payment plan. |
| 17 | `PP_INIT_DUE_AMT` | NUMERIC |  | Stores the payment plan due amount for the guarantor after the plan is setup. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

