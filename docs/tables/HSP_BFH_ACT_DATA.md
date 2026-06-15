# HSP_BFH_ACT_DATA

> Actions performed during the billing activity.

**Overflow family:** [HSP_BFH_ACT_DATA_2](HSP_BFH_ACT_DATA_2.md)  
**Primary key:** `BFH_ID`, `LINE`  
**Columns:** 70  
**Org-specific columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the billing activity history record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | Stores what actions were actually performed on the account. |
| 4 | `ACTION_NOTE_ID` | VARCHAR |  | This column stores the unique identifier for the resultant hospital account note record from this activity. |
| 5 | `ACTION_COMMENT` | VARCHAR |  | The user entered comment for the action. |
| 6 | `ACTION_AGENCY_ID` | NUMERIC |  | This column stores the unique identifier for the user-entered agency for the action. |
| 7 | `ACTION_AGENCY_ID_COLL_AGENCY_NAME` | VARCHAR |  | The name of the collection agency. |
| 8 | `ACTION_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `ACTION_DATE` | DATETIME |  | The user entered date for the action. |
| 10 | `ACTION_ASGN_RSN_C_NAME` | VARCHAR | org | The agency assign reason category number that is set as a result of this action. |
| 11 | `ACTION_WD_RSN_C_NAME` | VARCHAR |  | The agency withdraw reason category number that is set as a result of this action. |
| 12 | `ACTION_PAPRLS_RSN_C_NAME` | VARCHAR | org | Stores the reason the paperless billing status was changed for the associated action |
| 13 | `ACTION_TX_ID` | NUMERIC |  | Stores the associated transaction created as a result of a billing activity action. |
| 14 | `ACTION_AMOUNT` | NUMERIC |  | Stores an amount associated with a performed billing activity action. |
| 15 | `ACT_NOT_ALLOWED_AMT` | NUMERIC |  | Stores a not allowed amount associated with a performed billing activity action. |
| 16 | `ACCT_RMV_FROM_TRACKER_ID` | NUMERIC |  | Stores the financial assistance tracker from which the hospital account is removed as part of the billing action. |
| 17 | `ACCT_ADD_TO_TRACKER_ID` | NUMERIC |  | Stores the financial assistance tracker to which the hospital account is added as part of the billing action. |
| 18 | `ACTION_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 19 | `ACT_RELATED_HAR_TYPE_C_NAME` | VARCHAR | org | The related account type this action changed the account to. |
| 20 | `ACTION_ADMIT_DATE` | DATETIME |  | Stores the admit date set through a billing activity action. |
| 21 | `ACTION_DISCHRG_DATE` | DATETIME |  | Stores the discharge date set through a billing activity action. |
| 22 | `ACT_RELATED_HAR_ID` | NUMERIC |  | This column stores the unique identifier for the related hospital account created through the Create Related Account billing action. |
| 23 | `ACT_COMB_HSP_ACCOUNT_ID` | NUMERIC |  | This column stores the unique identifier for a hospital account that was combined or uncombined through a billing activity action. |
| 24 | `ACT_COMBINE_RSN_C_NAME` | VARCHAR |  | This item tracks the reason that an account was combined |
| 25 | `COMM_MODE_C_NAME` | VARCHAR |  | History of the communication mode used in an account activity. |
| 26 | `ACT_HH_DISCHRG_DISP_C_NAME` | VARCHAR | org | This column stores the patient status (I CLM 1021) value entered for the Override Home Health Discharge Disposition action in an account activity. |
| 27 | `ACTION_ACCT_CLASS_C_NAME` | VARCHAR | org | The account class this action changed the account to. |
| 28 | `ACTION_START_DATE` | DATETIME |  | History of start date used in a date range of an action. |
| 29 | `ACTION_END_DATE` | DATETIME |  | History of end date used in a date range of an action. |
| 30 | `ACT_CODABS_STAT_C_NAME` | VARCHAR | org | The Coding or Abstracting status change made by the action. |
| 31 | `ACT_CDI_STAT_C_NAME` | VARCHAR | org | This column stores the clinical documentation improvement (CDI) status change made by the action. |
| 32 | `ACT_CHNG_STAT_CMT` | VARCHAR |  | The comment associated with the change made by the action. |
| 33 | `ACT_ASGN_USER_ID` | VARCHAR |  | This column stores the Coding, Abstracting, or Clinical Documentation Improvement user assignment made by the action. |
| 34 | `ACT_ASGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 35 | `ACTION_DAY_OF_MONTH` | INTEGER |  | The day of month that was selected when the action was performed. |
| 36 | `ACTION_CARD_ID` | NUMERIC |  | The payment method that was selected when the action was performed. |
| 37 | `ACT_BILL_TYPE_C_NAME` | VARCHAR |  | Indicates how the account was billed. (Date Range, Cumulative, Part A Final) |
| 38 | `ACT_CONTEST_RSN_C_NAME` | VARCHAR | org | Shows why the account was contested. |
| 39 | `ACT_CONTEST_RESOLUTION_RSN_C_NAME` | VARCHAR | org | Holds why the account's contested status was resolved. |
| 40 | `ACTION_COVERAGE_ID` | NUMERIC |  | This column stores the unique identifier for the new coverage for the Professional Billing Next Responsible Party (PB NRP) action and the unique identifier for the current coverage for the PB Transfer to Insurance action. |
| 41 | `ACTION_NAA_WRITE_OFF_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 42 | `ACTION_BASE_AMOUNT` | NUMERIC |  | This item stores the base amount set through by a billing activity (ATM) action (for actions with a second, calculated amount). |
| 43 | `ACTION_PERCENT` | NUMERIC |  | This item stores the percent used by a billing activity (ATM) action. |
| 44 | `ACT_LATE_CHG_OPTION_C_NAME` | VARCHAR |  | The late charge processing type that was performed on an account |
| 45 | `ACTION_NUM_OF_PMTS` | INTEGER |  | The number of payments entered into the billing activity. |
| 46 | `ACTION_STMT_DAY_OF_MONTH` | INTEGER |  | The statement day of the month entered into the billing activity. |
| 47 | `ACT_ACCT_MAN_SPLIT_RSN_C_NAME` | VARCHAR | org | The manual split account reason that a billing action set for the account. |
| 48 | `ACTION_RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 49 | `ACTION_NUM_OF_CHGS` | INTEGER |  | The number of charges associated with the action. |
| 50 | `ACTION_SP_DSCNT_OV_RSN_C_NAME` | VARCHAR | org | This column stores the billing follow-up history item for tracking the self-pay discount override reason if the account is not insured. |
| 51 | `ACTION_SP_DSNT_IOV_RSN_C_NAME` | VARCHAR | org | This column stores the billing follow-up history item for tracking the self-pay discount override reason if the account is insured. |
| 52 | `ACT_WRITE_OFF_BALANCE_YN` | VARCHAR |  | Whether to write off the entire balance |
| 53 | `ACT_REFERENCE_NUMBER` | VARCHAR |  | Stores the reference number |
| 54 | `ACTION_EMAIL` | VARCHAR |  | Stores the email from the activity when the notification was sent. |
| 55 | `ACTION_PHONE_NUMBER` | VARCHAR |  | Stores the phone number from the activity when the notification was sent. |
| 56 | `ACT_DATE_FLTR_TYPE_C_NAME` | VARCHAR |  | This item describes how the start and end dates were interpreted when filtering transactions on a detail bill. |
| 57 | `ACTION_PRINT_ID` | NUMERIC |  | The statement or detail bill ID created by the action. For example, for Send Statement this is the statement that was printed. For Send Detail Bill, this is the detail bill that was printed. If the user chooses to print later, then this will be blank until the statement/detail bill run is accepted. This may never be set if the statement/detail bill is removed from the queue before it is printed. |
| 58 | `ACT_SELF_PAY_EXEMPT_RSN_C_NAME` | VARCHAR | org | The self-pay charge exemption reason category ID for the hospital account. |
| 59 | `ACT_CONS_SP_WITHDRAWAL_RSN_C_NAME` | VARCHAR | org | The consolidated self-pay account withdrawal reason that is set as the result of this action. |
| 60 | `ACT_SP_LEVEL_CHANGE_C_NAME` | VARCHAR |  | Stores the self-pay follow-up level change (increment/decrement) for the associated action. |
| 61 | `ACT_INTERIM_START_DT_TYPE_C_NAME` | VARCHAR |  | The start date category used for interim billing |
| 62 | `ACT_INTERIM_END_DT_TYPE_C_NAME` | VARCHAR |  | The end date category used for interim billing |
| 63 | `ACT_INTERIM_DAYS_NUM` | INTEGER |  | The number of days used for interim billing |
| 64 | `ACT_INTERIM_CATCHUP_YN` | VARCHAR |  | Whether or not catch up was performed for interim billing |
| 65 | `ACT_SELECTIVE_BILLING_RULE_ID` | VARCHAR |  | The Hospital Transaction rule used for Selective Billing |
| 66 | `ACT_SELECTIVE_BILLING_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 67 | `ACT_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 68 | `ACT_NUM_DAYS` | INTEGER |  | The number of days used in the billing action |
| 69 | `FIN_ASST_CASE_ID` | NUMERIC | FK→ | The financial assistance case that was created by the action. |
| 70 | `ADDR_QUERY_NOTE_ID` | VARCHAR |  | The note containing the address verification query as a result of this action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |

