# BILL_SCHED_PMT

> This table contains information about scheduled payments. This can include payment plan agreements and payments, Visit Auto Pay payment plans and payments, and trust transfers and payments.

**Overflow family:** [BILL_SCHED_PMT_2](BILL_SCHED_PMT_2.md)  
**Primary key:** `SCHED_PMT_ID`  
**Columns:** 83  
**Org-specific columns:** 2  
**Joined by:** 14 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SCHED_PMT_ID` | NUMERIC | PK | This column stores the unique identifier for the scheduled payment record. |
| 2 | `RECORD_NAME` | VARCHAR |  | Record name |
| 3 | `EXTERNAL_IDENT` | VARCHAR |  | This column stores the external identifier for the scheduled payment. |
| 4 | `SCHED_PMT_TYPE_C_NAME` | VARCHAR |  | Stores the scheduled payment record type. |
| 5 | `SCHED_PMT_STATUS_C_NAME` | VARCHAR |  | Stores the status of the scheduled payment. |
| 6 | `IS_ACTIVE_YN` | VARCHAR |  | Indicates whether the scheduled payment record is considered active. 'Y' indicates that the payment record is active. 'N' indicates that it is inactive. |
| 7 | `PARENT_SCHED_PMT_ID` | NUMERIC |  | Stores the parent scheduled payment record associated with the current scheduled payment record. |
| 8 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 9 | `ACCOUNT_ID` | NUMERIC | FK→ | Stores the guarantor account associated with the scheduled payment. |
| 10 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | Stores the hospital account associated with the scheduled payment. |
| 11 | `CARD_ID` | NUMERIC |  | This column stores the unique identifier for the payment method record of the scheduled payment. |
| 12 | `PMT_PROCESS_MODE_C_NAME` | VARCHAR |  | Stores the processing mode of the scheduled payment. |
| 13 | `PMT_PROCESS_MODE_AMT` | NUMERIC |  | Stores the amount associated with the payment processing mode for the scheduled payment. |
| 14 | `RECUR_TYPE_C_NAME` | VARCHAR |  | Stores the recurrence type of the scheduled payment. |
| 15 | `RECUR_DAY_OF_MONTH` | INTEGER |  | Stores the recurrence day of month if it is a monthly scheduled payment. |
| 16 | `RECUR_DAY_OF_WEEK_C_NAME` | VARCHAR |  | Stores the recurrence day of week if it is a bi-weekly or weekly scheduled payment. |
| 17 | `START_DATE` | DATETIME |  | Stores the start date of the scheduled payment. |
| 18 | `EXP_DATE` | DATETIME |  | Stores the expiration date of the scheduled payment. |
| 19 | `CREATION_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant at which the scheduled payment record is created. |
| 20 | `CREATION_SRC_C_NAME` | VARCHAR |  | Stores the source from which the payment schedule was created. For example, it will tell if the scheduled payment was setup through Hyperspace, or MyChart Web etc. |
| 21 | `CREATION_USER_ID` | VARCHAR |  | Stores the user who set up the scheduled payment. |
| 22 | `CREATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 23 | `CREATION_MYPT_ID` | VARCHAR |  | Stores the MyChart account that set up the scheduled payment. |
| 24 | `NEXT_PMT_DATE` | DATETIME |  | Stores the next date on which the payment will be processed. |
| 25 | `NEXT_PMT_AMT` | NUMERIC |  | Stores the amount that will be processed on the next scheduled date. |
| 26 | `POSTED_PMT_AMT` | NUMERIC |  | Stores the total amount processed and posted in the system by the scheduled payment. |
| 27 | `REMAINING_AMT` | NUMERIC |  | This column stores the remaining amount that can be processed to the payment method if the payment processing mode is "Up To Amount." |
| 28 | `LAST_PROCESS_DATE` | DATETIME |  | Stores the date when the payment method was last processed. |
| 29 | `LAST_PROCESS_PMT_AMT` | NUMERIC |  | Stores the amount that was processed during the last attempt. |
| 30 | `LAST_PROCESS_CARD_TX_STS_C_NAME` | VARCHAR |  | Stores the status of the last processing attempt. |
| 31 | `LAST_PROCESS_USER_ID` | VARCHAR |  | Stores the user who attempted the last processing of the payment method. |
| 32 | `LAST_PROCESS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 33 | `LAST_STATUS_DATE` | DATETIME |  | Shows the date on which the payment schedule was set to the current status. |
| 34 | `EMAIL_ADDRESS_OVRIDE` | VARCHAR |  | If set, this email will be used when sending notifications for this scheduled payment instead of the guarantor's email. |
| 35 | `MOBILE_PHONE_OVRIDE` | VARCHAR |  | If set, this mobile phone number will be used when sending notifications for this scheduled payment instead of the guarantor's mobile phone number. |
| 36 | `TRANSFER_FROM_GUAR_ID` | NUMERIC |  | Stores the source guarantor account associated with the scheduled trust transfer. |
| 37 | `LAST_BSP_CONSENT_TYPE_C_NAME` | VARCHAR |  | The type of the most current consent for the Visit Auto Pay agreement represented by this scheduled payment. |
| 38 | `LAST_CONSENT_USER_ID` | VARCHAR |  | The user that collected or updated the most current consent for the Visit Auto Pay agreement represented by this scheduled payment. |
| 39 | `LAST_CONSENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 40 | `LAST_CONSENT_DOCUMENT_ID` | VARCHAR |  | The document representing the most current consent for the Visit Auto Pay agreement represented by this BSP. |
| 41 | `CONSENT_DATE` | DATETIME |  | The date the patient consented to the terms for this scheduled payment. |
| 42 | `CREATION_DATE` | DATETIME |  | The date at which the scheduled payment record was created. |
| 43 | `RESOLUTION_DTTM` | DATETIME (Local) |  | The instant (local, guarantor's time zone) in which the scheduled payment record was resolved, either by completing successfully or being cancelled. |
| 44 | `RESOLUTION_DATE` | DATETIME |  | The date in which the scheduled payment record was resolved, either by completing successfully or being cancelled. |
| 45 | `RESOLUTION_STATUS_C_NAME` | VARCHAR |  | The resolution status category ID for this scheduled payment record. Use this to indicate the extent to which a the agreement was successful in collecting a payment. |
| 46 | `RESOLUTION_REASON_C_NAME` | VARCHAR |  | The resolution reason category ID for this scheduled payment. Use this to indicate the specific path-to-arrival to a resolution status (RESOLUTION_STATUS_C). |
| 47 | `CANCELLATION_REASON_C_NAME` | VARCHAR | org | The cancelation reason category ID for this scheduled payment. This column can be used to see the user-specified reason that a patient is canceling the agreement. |
| 48 | `TOTAL_SP_RESP_AMT` | NUMERIC |  | This column contains the total self-pay responsibility on a Visit Auto Pay agreement, regardless of the agreement being cancelled. |
| 49 | `ALL_HAR_BAL_IN_FULL_SP_DATE` | DATETIME |  | This column contains the most recent date in which all balances were on self-pay for all associated hospital accounts. |
| 50 | `LAST_CONSENT_DTTM` | DATETIME (Local) |  | The consent date and time for the Visit Auto Pay agreement. |
| 51 | `CUR_ACTIVE_SCHED_PMT_ID` | NUMERIC |  | This column contains the current active agreement (Visit Auto Pay or Payment Plans) in a replacement chain for any given agreement. If the agreement is not in a replacement chain, this column will match the agreement ID. |
| 52 | `CANCELLATION_USER_ID` | VARCHAR |  | This column contains the user who canceled the scheduled payment. |
| 53 | `CANCELLATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 54 | `CANCELLATION_MYPT_ID` | VARCHAR |  | This column contains the MyChart account that canceled the scheduled payment. |
| 55 | `FINAL_RESOLUTION_DATE` | DATETIME |  | This column contains the date when the agreement was resolved and all charges were in full self-pay for all accounts. - If the agreement is not resolved, this column will be empty. - If the agreement has not ever been in a state where all charges were in full self-pay, this column will be empty - If both the agreement is resolved and all charges on all visits were in full self-pay at least once in the agreement's lifetime, this column will contain the later of Resolution Date (I BSP 155) and All Hospital Account Balances in Full Self-Pay Date (I BSP 1752). By comparing this item with the Resolution Date, reports can find cases where VAP-eligible balances are dropping to self pay after the agreement was completed. |
| 56 | `FINAL_VAP_SCHED_PMT_ID` | NUMERIC |  | This column contains the final Visit Auto Pay agreement for a visit. This is determined by finding either the current active Visit Auto Pay agreement or finding the agreement that was most recently resolved. This uses the associated hospital account for Hospital Billing and the associated visit for Professional Billing. |
| 57 | `VISIT_DATE` | DATETIME |  | This column stores the visit date of the primary visit at the time of consent. |
| 58 | `VISIT_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 59 | `CREATION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 60 | `PAT_PMT_COLL_WKFL_C_NAME` | VARCHAR |  | This column contains the workflow category ID performed to collect a patient payment from the point of view of the user. For example, MyChart eCheck-in vs. MyChart One-Touch. |
| 61 | `MYC_SIGNIN_METHOD_C_NAME` | VARCHAR |  | This column denotes how the patient or guarantor logged in to MyChart to create the agreement. Only populated for agreements made via MyChart. |
| 62 | `GUAR_MYC_STATUS_C_NAME` | VARCHAR | org | This column stores the MyChart account status for the guarantor at the time the agreement is created or updated. An active MyChart account status is defined as whether a MyChart user could log into the account with a user name and password. Accounts that are not yet active, deactivated, or are proxy accounts are considered inactive. |
| 63 | `CREATION_MYC_STATUS_C_NAME` | VARCHAR |  | This column stores the MyChart account status for the MyChart account who created or last updated the agreement. An active MyChart account status is defined as whether a MyChart user could log into the account with a user name and password. Accounts that are not yet active, deactivated, or are proxy accounts are considered inactive. |
| 64 | `PREV_SCHED_PMT_ID` | NUMERIC |  | Stores the previous record that was replaced with the current scheduled payment record. |
| 65 | `PMT_TRACKER_SCHED_PMT_ID` | NUMERIC |  | The unique ID of the expected payment tracker record associated with this scheduled payment. This is currently only used for payment plans to track each month's Auto Pay. |
| 66 | `REPLACEMENT_REASON_C_NAME` | VARCHAR |  | The reason a BSP was replaced. For example, if a payment plan had new balances added, the Agreement BSP will be replaced with one representing the new terms. The previous BSP will be marked as "Replaced" and have a replacement reason of "Principal Edit". |
| 67 | `REMAINING_NUMBER_PAYMENTS` | INTEGER |  | The number of payments remaining if this agreement has a recurring payment cycle. |
| 68 | `PP_INITIAL_BALANCE` | NUMERIC |  | The total initial balance on the payment plan agreement. |
| 69 | `PP_MONTHLY_AMT` | NUMERIC |  | The amount agreed to be paid each month on the payment plan. |
| 70 | `PP_INITIAL_NUMBER_PAYMENTS` | INTEGER |  | The initial number of payments on a payment plan agreement. |
| 71 | `PP_DUE_DAY_OF_MONTH` | INTEGER |  | The recurring day of month on which payment will be due for this payment plan. |
| 72 | `PP_NEXT_DUE_DATE` | DATETIME |  | The upcoming due date for this month's payment. |
| 73 | `PP_TOTAL_DEFER_MONTHS` | INTEGER |  | The total number of payments that have been delayed as a result of a deferral over the course of the plan. This is only incremented if the deferred months have elapsed. |
| 74 | `PP_CURRENT_DEFER_MONTHS` | INTEGER |  | The number of months that a payment plan is currently deferred. |
| 75 | `PP_IS_AUTO_PAY_YN` | VARCHAR |  | Indicates whether the payment plan is set up as an Auto Pay agreement. 'Y' indicates that the payment plan is Auto Pay. 'N' indicates that the payment plan does not have a payment method attached and therefore isn't Auto Pay. NULL indicates that this agreement is not a payment plan. |
| 76 | `PP_IS_OVERDUE_YN` | VARCHAR |  | Indicates whether the payment plan has a balance overdue from the previous cycle. 'Y' indicates that the payment plan has an overdue balance. 'N' indicates that the payment plan does not have an overdue balance. NULL indicates that this agreement is not a payment plan. |
| 77 | `PP_AUTO_PAY_SUSPENDED_YN` | VARCHAR |  | Indicates whether the payment plan's Auto Pay is suspended due to a payment error or declined payment. 'Y' indicates that the payment plan has suspended Auto Pay. 'N' indicates the payment plan's Auto Pay is not suspended. NULL indicates that this is not a payment plan agreement or does not have Auto Pay. |
| 78 | `ORIGINAL_PARENT_SCHED_PMT_ID` | NUMERIC |  | The unique ID of the original agreement record in a replacement chain of agreement records. |
| 79 | `VAP_RESOLUTION_SP_AMT` | NUMERIC |  | The difference between the remaining self-pay balance of all accounts on a Visit Auto Pay agreement on its resolution date (BSP-155) and posted payments from the agreement (BSP-161). |
| 80 | `VAP_RESOLUTION_SP_DATE` | DATETIME |  | The latest date on which all accounts associated with the Visit Auto Pay agreement reached full self-pay, as of the Visit Auto Pay's resolution date (BSP-155). This date can be any time before or equal to the agreement's resolution date. If all of the accounts on the agreement were not fully in self-pay by the resolution date of the agreement, this column is blank. |
| 81 | `SIGN_UP_USER_ID` | VARCHAR |  | The user who setup or last edited this agreement. |
| 82 | `SIGN_UP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 83 | `SIGN_UP_MYPT_ID` | VARCHAR |  | The MyChart user who setup or last edited this agreement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

## Joined in — referenced by (14)

| From | Column | Confidence |
|------|--------|------------|
| [ARPB_TRANSACTIONS2](ARPB_TRANSACTIONS2.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_CONSENT_HX](BILL_SCHED_PMT_CONSENT_HX.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_NOTIF_HX](BILL_SCHED_PMT_NOTIF_HX.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_PAT_CSN](BILL_SCHED_PMT_PAT_CSN.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_PP_EST](BILL_SCHED_PMT_PP_EST.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_PP_HAR](BILL_SCHED_PMT_PP_HAR.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_PP_HAR_EST](BILL_SCHED_PMT_PP_HAR_EST.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_PROCESS_HX](BILL_SCHED_PMT_PROCESS_HX.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_REC_STS_HX](BILL_SCHED_PMT_REC_STS_HX.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PMT_STS_HX](BILL_SCHED_PMT_STS_HX.md) | `SCHED_PMT_ID` | high |
| [BILL_SCHED_PP_ACTION_HX](BILL_SCHED_PP_ACTION_HX.md) | `SCHED_PMT_ID` | high |
| [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | `SCHED_PMT_ID` | high |
| [HSP_TRANSACTIONS_2](HSP_TRANSACTIONS_2.md) | `SCHED_PMT_ID` | high |
| [STMT_EB_SCHED_AUTO_PAY](STMT_EB_SCHED_AUTO_PAY.md) | `SCHED_PMT_ID` | high |

