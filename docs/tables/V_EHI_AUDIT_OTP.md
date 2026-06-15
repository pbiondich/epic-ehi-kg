# V_EHI_AUDIT_OTP

> Translates OTP_AUDIT_TRAIL.

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 31  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOURCE_OTP_ID` | NUMERIC |  | Holds the order template ID that is the source for this audit line. |
| 4 | `UPDATE_ACTION_C_NAME` | VARCHAR | org | Action taken on the order. |
| 5 | `UPDATE_COMMENT` | VARCHAR |  | Any additional comment for the updating the order. |
| 6 | `UPDATE_DTTM` | DATETIME (Local) |  | Time instant at which the order was updated. |
| 7 | `UPDATE_ORDER_ID` | NUMERIC |  | This item contains the ID of the order that this action refers to. |
| 8 | `UPDATE_REASON_C_NAME` | VARCHAR | org | Reason for updating the order. |
| 9 | `UPDATED_BY_ID` | VARCHAR |  | User who updated the order. |
| 10 | `UPDATED_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `UPDATE_OLD_START_DAY` | VARCHAR |  | Stores the old start date of the order. |
| 12 | `UPDATE_OLD_START_TIME` | DATETIME (Local) |  | Stores the old start time of the order. |
| 13 | `UPDATE_NEW_START_DAY` | VARCHAR |  | Stores the new start date of the order. |
| 14 | `UPDATE_NEW_START_TIME` | DATETIME (Local) |  | Stores the new start time of the order. |
| 15 | `UPDATED_FREE_TEXT_SIG` | VARCHAR |  | Stores the value of the updated free text sig of the order. |
| 16 | `UPDATED_TARGET_AUC` | NUMERIC |  | Stores the value of the updated target AUC of the order. |
| 17 | `UPDATED_SELECTED_CRCL_SRC_C` | INTEGER |  | Stores the value of the updated GFR source of the order. |
| 18 | `UPDATED_GFR_FORMULA_LPP_ID` | NUMERIC |  | Stores the value of the updated GFR formula of the order. |
| 19 | `UPDATED_GFR_FORMULA_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 20 | `UPDATED_GFR_ORDER_SPECIFIC_VAL` | NUMERIC |  | Stores the value of the updated GFR order specific value. |
| 21 | `UPDATED_SELECTED_SCR_SRC_C` | INTEGER |  | Stores the value of the updated SCR source of the order. |
| 22 | `UPDATED_SCR_ORDER_SPECIFIC_VAL` | NUMERIC |  | Stores the value of the updated SCR order specific value. |
| 23 | `UPDATED_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 24 | `UPDATED_MAX_BSA` | NUMERIC |  | Stores the value of the updated maximum BSA of the order. |
| 25 | `UPDATED_USES_AUC_DOSE_C` | INTEGER |  | Stores if the order uses AUC dosing after the update. |
| 26 | `UPDATED_PHARMACY` | VARCHAR |  | Stores the value of the updated pharmacy of the order. |
| 27 | `UPDATE_OLD_MLSIG_SIGTYPE_C` | INTEGER |  | Stores the old sig type of the order. |
| 28 | `UPDATE_NEW_MLSIG_SIGTYPE_C` | INTEGER |  | Stores the new sig type of the order. |
| 29 | `UPDATED_SCHEDULING_DURATION` | INTEGER |  | Stores the value of the updated scheduling duration (in minutes) of the order. |
| 30 | `UPDATED_MEDICATION_NAME` | VARCHAR |  | The name of the medication. |
| 31 | `UPDATE_ORDER_NAME` | VARCHAR |  | The name of the medication as it appears on the medication record itself. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

