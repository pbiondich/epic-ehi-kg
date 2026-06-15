# PAT_ENC_ANTICOAG

> This table contains information related to anticoagulation monitoring encounters. It includes dosing information for the encounter (columns that contain the word DOSE or PILL with the exception of WEEKLY_MAX_DOSE and DOSE_DESC), information for the INR selected in the encounter (LAST_INR, LAST_INR_DATE, LATE_INR_ORDER_ID, LAST_INR_LINE_NUM), information from the anticoagulation episode values at the time of the encounter (INR_GOAL_C, INR_GOAL_HIGH, INR_GOAL_LOW, TARGET_END_DATE, WEEKLY_MAX_DOSE, ANTICOAG_DX, INDEFINITE_TREAMENT_YN), and other encounter details (DOSE_DESC, RETURN_DATE, ANTICOAG_TREND_C, AC_LAST_CHANGE_USER_ID, AC_LAST_CHANGE_IN_DTTM, ANTICOAG_NO_CHAN_YN, MANAGEMENT_TYPE_C) The dosing columns do not apply when using the calendar tracking section (LVN 617) for the anticoagulation encounter. The following columns only apply when using the calendar tracking section (LVN 617) for the anticoagulation encounter: ANTICOAG_TREND_C, AC_LAST_CHANGE_USER_ID, AC_LAST_CHANGE_IN_DTTM, ANTICOAG_NO_CHAN_YN, and MANAGEMENT_TYPE_C. There is a related table, EPI_ANTICOAG, for the most recent anticoagulation episode information.

**Overflow family:** [PAT_ENC_ANTICOAG_2](PAT_ENC_ANTICOAG_2.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 95  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_DATE_REAL` | FLOAT |  | The date for the patient encounter in internal format. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 4 | `INR_GOAL_C_NAME` | VARCHAR | org | The patient's INR goal, which is a range, at time of the encounter. The current INR goal is in the EPI_ANTICOAG table. |
| 5 | `INR_GOAL_HIGH` | FLOAT |  | The high value for the INR goal range. The column represents the high value portion of the category title at the time of extract. If application administrators change the meaning of a category value's title, this column could get out of sync. It is recommended to use INR_GOAL_C to link to ZC_INR_GOAL to look up the category title for the complete INR goal range (low and high). |
| 6 | `INR_GOAL_LOW` | FLOAT |  | The low value for the INR goal range. The column represents the low value portion of the category title at the time of extract. If application administrators change the meaning of a category value's title, this column could get out of sync. It is recommended to use INR_GOAL_C to link to ZC_INR_GOAL to look up the category title for the complete INR goal range (low and high). |
| 7 | `TARGET_END_DATE` | DATETIME |  | Target end date at the time of the visit. |
| 8 | `LAST_INR` | VARCHAR |  | The most recent INR result as of the encounter. |
| 9 | `LAST_INR_DATE` | DATETIME |  | The date of most recent INR result as of the encounter. |
| 10 | `WEEKLY_MAX_DOSE` | NUMERIC |  | Weekly max dose at the time of the visit. |
| 11 | `PT_DEVIATE_DOSE_YN` | VARCHAR |  | Indicates if the patient deviated from dose instructions. If so, the 'taken' columns have been manually updated with the actual doses the patient reported taken. |
| 12 | `DOSE_SUN` | NUMERIC |  | Sunday dose in mg |
| 13 | `DOSE_MON` | NUMERIC |  | Monday dose in mg |
| 14 | `DOSE_TUE` | NUMERIC |  | Tuesday daily dose in mg |
| 15 | `DOSE_WED` | NUMERIC |  | Wednesday dose in mg |
| 16 | `DOSE_THU` | NUMERIC |  | Thursday dose in mg |
| 17 | `DOSE_FRI` | NUMERIC |  | Friday dose in mg |
| 18 | `DOSE_SAT` | NUMERIC |  | Saturday dose in mg |
| 19 | `PILL_SZ_SUN` | VARCHAR |  | Sunday pill size in mg |
| 20 | `PILL_SZ_MON` | VARCHAR |  | Monday pill size in mg |
| 21 | `PILL_SZ_TUE` | VARCHAR |  | Tuesday pill size in mg |
| 22 | `PILL_SZ_WED` | VARCHAR |  | Wednesday pill size in mg |
| 23 | `PILL_SZ_THU` | VARCHAR |  | Thursday pill size in mg |
| 24 | `PILL_SZ_FRI` | VARCHAR |  | Friday pill size in mg |
| 25 | `PILL_SZ_SAT` | VARCHAR |  | Saturday pill size in mg |
| 26 | `PILLS_SUN` | NUMERIC |  | Sunday number of pills |
| 27 | `PILLS_MON` | NUMERIC |  | Monday number of pills |
| 28 | `PILLS_TUE` | NUMERIC |  | Tuesday number of pills |
| 29 | `PILLS_WED` | NUMERIC |  | Wednesday number of pills |
| 30 | `PILLS_THU` | NUMERIC |  | Thursday number of pills |
| 31 | `PILLS_FRI` | NUMERIC |  | Friday number of pills |
| 32 | `PILLS_SAT` | NUMERIC |  | Saturday number of pills |
| 33 | `WEEKLY_DOSE` | NUMERIC |  | Total dose for the week in mg. |
| 34 | `PILL_DISTRIBUTION` | INTEGER |  | How the pills were distributed (0=single pill,1=additional pill,2=alternate pill) |
| 35 | `RETURN_DATE` | DATETIME |  | Date the patient should return for their next INR as of this encounter. The most recent return date is in the table EPI_ANTICOAG. |
| 36 | `WEEKLY_DOSE_TAKEN` | FLOAT |  | Patient reported weekly dose taken |
| 37 | `DOSE_TAKEN_SUN` | FLOAT |  | Dose taken Sunday in mg |
| 38 | `DOSE_TAKEN_MON` | FLOAT |  | Dose taken Monday in mg |
| 39 | `DOSE_TAKEN_TUE` | FLOAT |  | Dose taken Tuesday in mg |
| 40 | `DOSE_TAKEN_WED` | FLOAT |  | Dose taken Wednesday in mg |
| 41 | `DOSE_TAKEN_THU` | FLOAT |  | Dose taken Thursday in mg |
| 42 | `DOSE_TAKEN_FRI` | FLOAT |  | Dose taken Friday in mg |
| 43 | `DOSE_TAKEN_SAT` | FLOAT |  | Dose taken Saturday in mg |
| 44 | `PILL_SZ_SUN_ADL` | VARCHAR |  | Sunday pill size of additional pills |
| 45 | `PILL_SZ_MON_ADL` | VARCHAR |  | Monday pill size of additional pills |
| 46 | `PILL_SZ_TUE_ADL` | VARCHAR |  | Tuesday pill size of additional pills |
| 47 | `PILL_SZ_WED_ADL` | VARCHAR |  | Wednesday pill size of additional pills |
| 48 | `PILL_SZ_THU_ADL` | VARCHAR |  | Thursday pill size of additional pills |
| 49 | `PILL_SZ_FRI_ADL` | VARCHAR |  | Friday pill size of additional pills |
| 50 | `PILL_SZ_SAT_ADL` | VARCHAR |  | Saturday pill size of additional pills |
| 51 | `PILLS_SUN_ADL` | NUMERIC |  | Number of additional pills for Sunday |
| 52 | `PILLS_MON_ADL` | NUMERIC |  | Number of additional pills for Monday |
| 53 | `PILLS_TUE_ADL` | NUMERIC |  | Number of additional pills for Tuesday |
| 54 | `PILLS_WED_ADL` | NUMERIC |  | Number of additional pills for Wednesday |
| 55 | `PILLS_THU_ADL` | NUMERIC |  | Number of additional pills for Thursday |
| 56 | `PILLS_FRI_ADL` | NUMERIC |  | Number of additional pills for Friday |
| 57 | `PILLS_SAT_ADL` | NUMERIC |  | Number of additional pills for Saturday |
| 58 | `WEEKLY_DOSE_ALT` | NUMERIC |  | If an alternate week schedule is used, this column contains the total dose for the second (alternate) week |
| 59 | `DOSE_SUN_ALT` | NUMERIC |  | Sunday alternate week dose in mg |
| 60 | `DOSE_MON_ALT` | NUMERIC |  | Monday alternate week dose in mg |
| 61 | `DOSE_TUE_ALT` | NUMERIC |  | Tuesday alternate week dose in mg |
| 62 | `DOSE_WED_ALT` | NUMERIC |  | Wednesday alternate week dose in mg |
| 63 | `DOSE_THU_ALT` | NUMERIC |  | Thursday alternate week dose in mg |
| 64 | `DOSE_FRI_ALT` | NUMERIC |  | Friday alternate week dose in mg |
| 65 | `DOSE_SAT_ALT` | NUMERIC |  | Saturday alternate week dose in mg |
| 66 | `PILL_SZ_SUN_ALT` | VARCHAR |  | Sunday alternate week pill size |
| 67 | `PILL_SZ_MON_ALT` | VARCHAR |  | Monday alternate week pill size |
| 68 | `PILL_SZ_TUE_ALT` | VARCHAR |  | Tuesday alternate week pill size |
| 69 | `PILL_SZ_WED_ALT` | VARCHAR |  | Wednesday alternate week pill size |
| 70 | `PILL_SZ_THU_ALT` | VARCHAR |  | Thursday alternate week pill size |
| 71 | `PILL_SZ_FRI_ALT` | VARCHAR |  | Friday alternate week pill size |
| 72 | `PILL_SZ_SAT_ALT` | VARCHAR |  | Saturday alternate week pill size |
| 73 | `PILLS_SUN_ALT` | NUMERIC |  | Sunday alternate week number of pills |
| 74 | `PILLS_MON_ALT` | NUMERIC |  | Monday alternate week number of pills |
| 75 | `PILLS_TUE_ALT` | NUMERIC |  | Tuesday alternate week number of pills |
| 76 | `PILLS_WED_ALT` | NUMERIC |  | Wednesday alternate week number of pills |
| 77 | `PILLS_THU_ALT` | NUMERIC |  | Thursday alternate week number of pills |
| 78 | `PILLS_FRI_ALT` | NUMERIC |  | Friday alternate week number of pills |
| 79 | `PILLS_SAT_ALT` | NUMERIC |  | Saturday alternate week number of pills |
| 80 | `WKLY_DOSE_TKN_ALT` | FLOAT |  | The total actual dose taken by patient during the alternate week |
| 81 | `DOSE_TKN_SUN_ALT` | FLOAT |  | The actual dose taken by patient during the alternate week on Sunday |
| 82 | `DOSE_TKN_MON_ALT` | FLOAT |  | The actual dose taken by patient during the alternate week on Monday |
| 83 | `DOSE_TKN_TUE_ALT` | FLOAT |  | The actual dose taken by patient during the alternate week on Tuesday |
| 84 | `DOSE_TKN_WED_ALT` | FLOAT |  | The actual dose taken by patient during the alternate week on Wednesday |
| 85 | `DOSE_TKN_THU_ALT` | FLOAT |  | The actual dose taken by patient during the alternate week on Thursday |
| 86 | `DOSE_TKN_FRI_ALT` | FLOAT |  | The actual dose taken by patient during the alternate week on Friday |
| 87 | `DOSE_TKN_SAT_ALT` | FLOAT |  | The actual dose taken by patient during the alternate week on Saturday |
| 88 | `ANTICOAG_DX` | VARCHAR |  | Anticoagulation diagnoses at time of visit in a comma delimited list. The most recent list is maintained at the episode level in the table EPI_PROBLEM_LIST. |
| 89 | `INDEFINITE_TREAT_YN` | VARCHAR |  | The value of the anticoagulation indefinite treatment episode item at the time of the visit. |
| 90 | `ANTICOAG_TREND_C_NAME` | VARCHAR |  | Used to keep track of the trend of the dosing instructions (up, down, same) in the calendar based anticoagulation tracking section. |
| 91 | `AC_LAST_CHG_USER_ID` | VARCHAR |  | Keeps track of the last user to document dosing instructions (dosing plan, override/hold or no change) in the calendar based anticoagulation tracking section. |
| 92 | `AC_LAST_CHG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 93 | `ANTICOAG_NO_CHAN_YN` | VARCHAR |  | When a user documents that no change was made to dosing instructions, then this is set to "Yes". This is an option in the calendar based anticoagulation tracking section. |
| 94 | `MANAGEMENT_TYPE_C_NAME` | VARCHAR | org | Anticoagulation management type/priority (such as high, critical, routine). This appears in the calendar based tracking section and suggests to the user an appropriate return date. |
| 95 | `LAST_INR_ORDER_ID` | NUMERIC |  | The unique ID of the order record associated with the INR result selected for this encounter |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

