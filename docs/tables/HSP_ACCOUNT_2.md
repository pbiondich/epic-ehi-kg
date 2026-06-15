# HSP_ACCOUNT_2

> This table contains hospital account information from the Hospital Accounts Receivable (HAR) master file. This second hospital account table has the same basic structure as HSP_ACCOUNT, but was created as a second table to prevent HSP_ACCOUNT from getting any larger. This table will exclude professional billing accounts in classic PB self-pay service areas.

**Overflow of:** [HSP_ACCOUNT](HSP_ACCOUNT.md)  
**Primary key:** `HSP_ACCOUNT_ID`  
**Columns:** 57  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCOUNT_ID` | NUMERIC | PK | This column stores the unique identifier for the hospital account. |
| 2 | `HH_AGENCY_C_NAME` | VARCHAR | org | The home health agency associated with the hospital account. |
| 3 | `EXPIRATION_REASON` | VARCHAR |  | The reason for expiration (anesthesia, operation, etc.). If the discharge disposition is not "expired," this field will not be populated. |
| 4 | `DECEASED_DT` | DATETIME |  | Date of patient's death. |
| 5 | `DECEASED_TIME` | DATETIME |  | The date and time for the death of the patient that is associated with this hospital account. |
| 6 | `DURATIONS_HYPERAL` | NUMERIC |  | This column stores the number of days patient is on Hyperal. Hyperal is the same as Total Parenteral Nutrition (TPN) regarding diet and nutrition management. |
| 7 | `OPEN_DENIAL_BDC_YN` | VARCHAR |  | This column stores whether the hospital account has an open denial record. |
| 8 | `OPEN_RMK_BDC_YN` | VARCHAR |  | This column stores whether the hospital account has an open remark record. |
| 9 | `OPEN_COR_BDC_YN` | VARCHAR |  | This column stores whether the hospital account has an open correspondence record. |
| 10 | `ECMO` | NUMERIC |  | This column stores the number of days the patient has been using the ECMO (extracorporeal membrane oxygenation) equipment. |
| 11 | `MECHANICAL_VENT` | NUMERIC |  | The number of days the patient has been using the mechanical ventilator. |
| 12 | `ARCHIVE_ID` | VARCHAR |  | This column stores the unique identifier for the archive record of the hospital account. |
| 13 | `ARCHIVE_DT` | DATETIME |  | The date the hospital account was archived. |
| 14 | `REC_CREATE_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who created the hospital account. |
| 15 | `REC_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `REGIONAL_STUDY_1` | VARCHAR |  | This column stores the Regional study 1, which is one of the coding info items. |
| 17 | `REGIONAL_STUDY_2` | VARCHAR |  | This column stores the Regional study 2, which is one of the coding info items. |
| 18 | `FACILITY_STUDY_A` | VARCHAR |  | Facility study A is one of the coding info items. The abstract info tab in account maintenance can be configured to display these items. |
| 19 | `FACILITY_STUDY_B` | VARCHAR |  | Facility study B is one of the coding info items. The abstract info tab in account maintenance can be configured to display these items. |
| 20 | `DECUBITIS_C_NAME` | VARCHAR | org | Decubitis is one of the coding info items. The abstract info tab in account maintenance can be configured to display these items. |
| 21 | `TRAUMA_C_NAME` | VARCHAR |  | Trauma is one of the coding info items. The abstract info tab in account maintenance can be configured to display these items. |
| 22 | `GEST_AGE_DAYS` | NUMERIC |  | Gestational age days is one of the coding info items. The abstract info tab in account maintenance can be configured to display these items. |
| 23 | `GEST_AGE_BABY_DAYS` | NUMERIC |  | Gestational (baby) age days is one of the coding info items. The abstract info tab in account maintenance can be configured to display these items. |
| 24 | `ESOP_PAYOR_C_NAME` | VARCHAR | org | This column stores the expected source of payment payer, which is a coding info item that stores the payer that is expected to pay for the services. This item is necessary for regulatory reporting in some states. The abstract info tab in account maintenance can be configured to display this item. |
| 25 | `ESOP_PLAN_NAME_C_NAME` | VARCHAR | org | Expected source of payment plan name is one of the coding info items. It stores the plan that is expected to pay for the services. This item is necessary for regulatory reporting in some states. The abstract info tab in account maintenance can be configured to display coding items. |
| 26 | `ESOP_PLAN_TYPE_C_NAME` | VARCHAR | org | Expected source of payment plan type is one of the coding info items. It stores the type of plan that is expected to pay for the services. This item is necessary for regulatory reporting in some states. The abstract info tab in account maintenance can be configured to display coding items. |
| 27 | `CODING_USER` | VARCHAR |  | This column stores the unique identifier for the user who last changed the coding status of the hospital account. This is frequently used to join to the CLARITY_EMP table. |
| 28 | `CODING_USER_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 29 | `APGAR_10_MIN` | FLOAT |  | The Apgar score at ten minutes for the newborn associated with the hospital account. This is an abstracting item. |
| 30 | `FRST_PRO_STMT_DT` | DATETIME |  | This field contains the date of the first non-demand enterprise statement to be sent with a self-pay proration balance. |
| 31 | `LST_PRO_STMT_DT` | DATETIME |  | This field contains the date of the most recent non-demand enterprise statement to be sent with a self-pay proration balance. |
| 32 | `NUM_PRO_STMTS` | INTEGER |  | This field contains the total number of non-demand enterprise statements sent with a self-pay proration balance. |
| 33 | `FRST_PRO_D_STMT_DT` | DATETIME |  | This field contains the date of the first demand enterprise statement to be sent with a self-pay proration balance. |
| 34 | `LST_PRO_D_STMT_DT` | DATETIME |  | This field contains the date of the most recent demand enterprise statement to be sent with a self-pay proration balance. |
| 35 | `NUM_PRO_D_STMTS` | INTEGER |  | This field contains the total number of demand enterprise statements sent with a self-pay proration balance. |
| 36 | `FRST_FULL_STMT_DT` | DATETIME |  | This field contains the date of the first non-demand enterprise statement to be sent where the remaining account balance is completely self-pay. |
| 37 | `LST_FULL_STMT_DT` | DATETIME |  | This field contains the date of the most recent non-demand enterprise statement to be sent where the remaining account balance is completely self-pay. |
| 38 | `NUM_FULL_STMTS` | INTEGER |  | This field contains the total number of non-demand enterprise statements sent where the remaining account balance is completely self-pay. |
| 39 | `FST_FULL_D_STMT_DT` | DATETIME |  | This field contains the date of the first demand enterprise statement to be sent where the remaining account balance is completely self-pay. |
| 40 | `LST_FULL_D_STMT_DT` | DATETIME |  | This field contains the date of the most recent demand enterprise statement to be sent where the remaining account balance is completely self-pay. |
| 41 | `NUM_FULL_D_STMTS` | INTEGER |  | This field contains the total number of demand enterprise statements sent where the remaining account balance is completely self-pay. |
| 42 | `FIRST_SELF_PAY_DT` | DATETIME |  | This field contains the date of the first self-pay balance for this account. |
| 43 | `FIRST_FULL_SP_DT` | DATETIME |  | This field contains the first date when the self-pay balance equaled the full account balance for this account. |
| 44 | `STILLBORN_YN` | VARCHAR |  | Indicates whether a pregnancy resulted in a stillbirth. This is an abstracting item. |
| 45 | `NUM_LIVE_BIRTHS` | INTEGER |  | This column contains the abstracted number of children that were born alive for the hospital account encounter. |
| 46 | `FIRST_INFO_STMT_DT` | DATETIME |  | This field contains the date of the first non-demand enterprise statement to be sent with no self-pay balance (only insurance balance). |
| 47 | `LAST_INFO_STMT_DT` | DATETIME |  | This field contains the date of the most recent non-demand enterprise statement to be sent with no self-pay balance (only insurance balance). |
| 48 | `LAST_D_INFO_STM_DT` | DATETIME |  | This field contains the date of the most recent demand enterprise statement to be sent with no self-pay balance (only insurance balance). |
| 49 | `NUM_D_INFO_STMTS` | INTEGER |  | This field contains the total number of demand enterprise statements sent with no self-pay balance (only insurance balance). |
| 50 | `FARM_ACCIDENT_YN` | VARCHAR |  | This column stores whether or not the hospital account was abstracted as a farm accident. 0-No or 1-Yes. |
| 51 | `EXTERN_AR_FLAG_YN` | VARCHAR |  | External A/R Flag. This flag determines if an account's A/R is to be counted as belonging to an external agency (i.e., as bad debt). This flag is set by a collections action and can be unset by another action. This flag is only used if external agency A/R has been enabled. |
| 52 | `PRIMARY_CONTACT` | VARCHAR |  | This column stores the primary contact date (DAT) of the hospital account. It's used in many places, such as in determining the admission/discharge date of the account. |
| 53 | `NUM_STILLBORNS` | INTEGER |  | This column contains the abstracted number of stillborns for the hospital account. |
| 54 | `HOSP_INFECTION_YN` | VARCHAR |  | Indicates whether the patient developed a hospital infection during the hospital account encounter. |
| 55 | `RAPID_RESP_TEAM_YN` | VARCHAR |  | Indicates whether a rapid response team was needed during the hospital account encounter. |
| 56 | `RETURN_TO_OR_YN` | VARCHAR |  | Indicates whether the patient was returned to operating room. This is an abstracting item. |
| 57 | `NONCVRD_SNF_STAY_YN` | VARCHAR |  | This column stores whether the Skilled Nursing Facility (SNF) stay billed on this account is non-covered due to not having a prior qualifying inpatient stay. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [HSP_ACCOUNT](HSP_ACCOUNT.md).

