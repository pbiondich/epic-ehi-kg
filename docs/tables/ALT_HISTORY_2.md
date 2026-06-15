# ALT_HISTORY_2

> This table contains general history information for each type of medication warning or advisory. Since each warning could be triggered in different activities at different times, it contains general warning information for each time the warning was triggered. This table is an extension of ALT_HISTORY table.

**Overflow of:** [ALT_HISTORY](ALT_HISTORY.md)  
**Primary key:** `ALT_CSN_ID`  
**Columns:** 28  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALT_ID` | NUMERIC | FK→ | The unique identifier for the med alert record. |
| 2 | `ALT_CSN_ID` | NUMERIC | PK | A unique serial number for this contact. This number is unique across all alerts in the system. |
| 3 | `FILTEROUT_REASON_C_NAME` | VARCHAR |  | Save the reason that the medication warning is filtered. |
| 4 | `TPN_VOL_INFUSED` | NUMERIC |  | It is possible to calculate warnings for total parenteral nutrition (TPN) based on the total volume present in the bag or the volume based upon how much the patient will actually receive. If the volume to be infused to the patient is being calculated, then this item will store the volume to be infused at the time that a TPN alert fired. If the warning is based on the volume in the TPN bag, then this item will not be set. |
| 5 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 6 | `CRIT_DOSE_POPUP_YN` | VARCHAR |  | Indicates whether or not a dose warning was saved from the critical dose warning popup. |
| 7 | `HARD_STOP_YN` | VARCHAR |  | Indicates whether or not a warning is a hard stop. |
| 8 | `DRUGSTUDY_SEVERITY_C_NAME` | VARCHAR | org | Stores the severity of a drug-study warning that is shown in the medication warnings popup. |
| 9 | `NBA_ACTION_UTC_DTTM` | DATETIME (UTC) |  | The instant of an next best action event. |
| 10 | `NBA_USER_ID` | VARCHAR |  | The user correlated with this next best action event. |
| 11 | `NBA_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `NBA_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 13 | `NBA_RESULT_C_NAME` | VARCHAR |  | The result of this next best action event. |
| 14 | `NBA_DFR_REASON_C_NAME` | VARCHAR | org | The defer reason correlated with this next best action event. |
| 15 | `NBA_DFR_DAYS_NUM` | INTEGER |  | The defer days correlated with this next best action event. |
| 16 | `NBA_DEC_REASON_C_NAME` | VARCHAR | org | The decline reason correlated with this next best action event. |
| 17 | `NBA_COMM_ID` | VARCHAR |  | The contact correlated with this next best action event. |
| 18 | `NBA_BUSINESS_SEG_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 19 | `NBA_ACTION_DTTM` | DATETIME (Local) |  | The instant of a next best action event in local time. |
| 20 | `MYC_TICKLER_AUDIT_CSN_ID` | NUMERIC |  | The CSN of the RCH record containing the auditing data of the tickler sent for this alert. |
| 21 | `BPA_ADDL_FACTORS_TEXT` | VARCHAR |  | Snapshot of data relevant to the evaluation of the advisory, in the format of plain text. |
| 22 | `BPA_ADDL_FACTORS_UTC_DTTM` | DATETIME (UTC) |  | The instant that the additional contributing factors text (I ALT 2200) was created. |
| 23 | `ALRGY_FROM_OUTSIDE_SRC_YN` | VARCHAR |  | This column only applies to ALTs that represent drug-allergy warnings. For all other types of ALTs, this column will be blank. This column indicates whether or not an allergy comes from reconciled data. If the allergy does come from outside data, it will contain the value Yes. If the allergy does not come from outside data, it will contain the value No. Additionally, this column will be blank for any warnings that fired before the system was keeping track of this. |
| 24 | `LOG_HM_ACTION_C_NAME` | VARCHAR |  | This is the Health Maintenance action to be logged. |
| 25 | `LOG_HMT_PPN_RSN_C_NAME` | VARCHAR | org | This is the postpone reason for the logged Health Maintenance action. |
| 26 | `LOG_HM_TYPE_C_NAME` | VARCHAR | org | This is the manual completion reason for the logged Health Maintenance action. |
| 27 | `LOG_HM_EDIT_RSN_C_NAME` | VARCHAR | org | This is the edited topic reason for the logged stored Health Maintenance action. |
| 28 | `LOG_HM_COMP_TYPE_C_NAME` | VARCHAR |  | This is the completion type for the logged Health Maintenance action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_ID` | [ALERT](ALERT.md) | sole_pk | high |

## Joined in

Inbound joins are tracked on the logical base [ALT_HISTORY](ALT_HISTORY.md).

