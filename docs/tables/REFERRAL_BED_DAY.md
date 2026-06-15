# REFERRAL_BED_DAY

> The REFERRAL_BED_DAY table contains information on bed days on referrals.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 35  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The unique ID of the referral in database. |
| 2 | `LINE` | INTEGER | PK | A line number that is used to identify a group of bed day information |
| 3 | `START_DATE` | DATETIME |  | The date on which the member is scheduled to start treatment associated with each bed day type |
| 4 | `END_DATE` | DATETIME |  | The date on which the member is scheduled to or actually does complete treatment associated with each bed day type. |
| 5 | `BED_DAY_TYPE_ID` | NUMERIC | FK→ | The bed day type or classification used to categorize the scheduled days of treatment. |
| 6 | `BED_DAY_TYPE_ID_BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |
| 7 | `ESTIMATED_DAYS` | NUMERIC |  | The estimated number of days the member spends in treatment associated with each bed day type. |
| 8 | `CONVERTED_DAYS` | NUMERIC |  | A manual conversion of the calculated number of Raw days for each bed day type, the raw days are calculated from the start and end date. Partial days are allowed |
| 9 | `RAW_DAYS` | NUMERIC |  | Displays the actual number of days the member spends in treatment associated with each bed day type, calculated from the start and end date. Partial days are allowed. |
| 10 | `OVERRIDE_DAYS` | NUMERIC |  | A manual override of the calculated number of days for each bed day type. Partial days are allowed. |
| 11 | `AVOID_BED_DAY_RSN_C_NAME` | VARCHAR | org | Track the avoidable bed day reason for the current row in the bed days table. |
| 12 | `BED_DAYS_COMMENTS` | VARCHAR |  | Track the comments for the current row in the bed days table. If the comment is more than 256 characters, it will be truncated to 256. |
| 13 | `DEN_BED_DAY_RSN_C_NAME` | VARCHAR | org | Track the denied reason for the current row in the bed days table. |
| 14 | `BED_DAY_STATUS_C_NAME` | VARCHAR |  | Track the Approved/Denied status for the current row in the bed days table. |
| 15 | `APPR_BED_DAY_RSN_C_NAME` | VARCHAR | org | Track the approved reason for the current row in the bed days table. |
| 16 | `REQUESTED_ON_UTC_DTTM` | DATETIME (UTC) |  | Track the date and time the bed day was requested for the current row in the table. |
| 17 | `DECIDED_ON_UTC_DTTM` | DATETIME (UTC) |  | Track the date and time a decision was made on the bed day status for the current row in the table. |
| 18 | `BED_DAY_PRIORITY_C_NAME` | VARCHAR | org | The bed days request priority category ID for the bed day line on the referral record. |
| 19 | `PEND_BED_DAY_RSN_C_NAME` | VARCHAR | org | Track the pending review reason for the current row in the bed days table. |
| 20 | `CLOSED_BED_DAY_RSN_C_NAME` | VARCHAR | org | Track the closed reason for the current row in the bed days table. |
| 21 | `BED_DAY_AUTH_REQUEST_TYPE_C_NAME` | VARCHAR |  | The request type of the bed day line. |
| 22 | `ELECTRONIC_REQUEST_YN` | VARCHAR |  | Tracks whether the request for the current row in the bed days table was made electronically. If set to electronic, the bed day period will also be evaluated for turnaround times for e-submissions. |
| 23 | `ADDL_INFO_REQ_OVR_UTC_DTTM` | DATETIME (UTC) |  | The user-override value of the additional information request instant for a bed day line. |
| 24 | `ADDL_INFO_REQ_OVR_LOCAL_DTTM` | DATETIME (Local) |  | The user-override value of the additional information request instant for a bed day line. This is a virtual copy of RFL 2411 that contains the system local time. |
| 25 | `ADDL_INFO_RCPT_OVR_UTC_DTTM` | DATETIME (UTC) |  | The user-override value of the additional information receipt instant for a bed day line. |
| 26 | `ADDL_INFO_RCPT_OVR_LOCAL_DTTM` | DATETIME (Local) |  | The user-override value of the additional information receipt instant for a bed day line. This is a virtual copy of RFL 2413 that contains the system local time. |
| 27 | `ADDL_INFO_EXTENSION_TAKEN_YN` | VARCHAR |  | Whether an additional information request extension was taken for the bed day line. |
| 28 | `MANUAL_EXTENSION_DAYS` | INTEGER |  | The number of manual extension days taken for the bed day. |
| 29 | `WITHDRAWN_BED_DAY_RSN_C_NAME` | VARCHAR | org | Track the withdrawn reason for the current row in the bed days table. |
| 30 | `DISMISSED_BED_DAY_RSN_C_NAME` | VARCHAR | org | Track the dismissed reason for the current row in the bed days table. |
| 31 | `NO_AUTH_RQ_BED_DAY_RSN_C_NAME` | VARCHAR | org | Track the no authorization required reason for the current row in the bed days table. |
| 32 | `APPEAL_STATUS_C_NAME` | VARCHAR |  | Indicates the status of the last bed day line in the series representing appeals to this bed day line. This item is empty if this bed day line is not appealed or is an appeal. |
| 33 | `APPEALED_UNIQ_IDENT` | VARCHAR |  | The appealed bed day unique key that this line is the effectuation of. |
| 34 | `RPT_ADDL_INFO_EXT_TAKEN_YN` | VARCHAR |  | Whether an additional information request TAT extension was taken for the bed day line through the Request For Information workflow or documenting the additional information request datetime on the bed day or referral while taking the review category of the bed day into account. |
| 35 | `RPT_MANUAL_EXTENSION_DAYS` | INTEGER |  | The number of TAT manual extension days taken for the bed day line while taking the review category of the bed day, bed day line level manual extension (I RFL 2416), and referral level manual extension (I RFL 18618) into account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BED_DAY_TYPE_ID` | [CLARITY_BED_DAY](CLARITY_BED_DAY.md) | sole_pk | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

