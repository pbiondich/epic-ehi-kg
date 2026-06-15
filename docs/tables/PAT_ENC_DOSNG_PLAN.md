# PAT_ENC_DOSNG_PLAN

> The PAT_ENC_DOSNG_PLAN table contains the dosing plans for anticoagulation patients when using the calendar based tracking section. This table contains the recurring instructions to the patient.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `DOSING_PLAN_C_NAME` | VARCHAR |  | The anticoagulation dosing plan type of pattern (every day, weekly, alternating). |
| 7 | `PLAN_REPEAT_DAYS` | INTEGER |  | The number of days after which the anticoagulation dosing plan will repeat for an alternating pattern. |
| 8 | `ALT_PLAN_RESTART_YN` | VARCHAR |  | Yes or no value of whether or not the user or the system checked the "Start on the first day of the cycle" check box in the anticoagulation calendar based plan editor. |
| 9 | `ALT_PLAN_START_DAY` | INTEGER |  | A numeric item to keep track of the start day in the cycle for an alternating anticoagulation plan. |
| 10 | `PLAN_START_DATE` | DATETIME |  | The date that the new anticoagulation dosing plan will start. |
| 11 | `PLAN_CHANGE_DATE` | DATETIME |  | The date the anticoagulation dosing plan was changed. |
| 12 | `DOSING_PLAN_TEXT` | VARCHAR |  | A textual description of the anticoagulation dosing plan. |
| 13 | `DOSE_INST_FULL_TEXT` | VARCHAR |  | A textual description of the anticoagulation full dosing instructions, includes holds, overrides and dosing plan. |
| 14 | `DAILY_DOSE_DAY1` | NUMERIC |  | Daily dose for day 1 of an anticoagulation dosing plan. |
| 15 | `DAILY_DOSE_DAY2` | NUMERIC |  | Daily dose for day 2 of an anticoagulation dosing plan. |
| 16 | `DAILY_DOSE_DAY3` | NUMERIC |  | Daily dose for day 3 of an anticoagulation dosing plan. |
| 17 | `DAILY_DOSE_DAY4` | NUMERIC |  | Daily dose for day 4 of an anticoagulation dosing plan. |
| 18 | `DAILY_DOSE_DAY5` | NUMERIC |  | Daily dose for day 5 of an anticoagulation dosing plan. |
| 19 | `DAILY_DOSE_DAY6` | NUMERIC |  | Daily dose for day 6 of an anticoagulation dosing plan. |
| 20 | `DAILY_DOSE_DAY7` | NUMERIC |  | Daily dose for day 7 of an anticoagulation dosing plan. |
| 21 | `PILL_SIZE_DAY1` | VARCHAR |  | Pill size for day 1 of an anticoagulation dosing plan. |
| 22 | `PILL_SIZE_DAY2` | VARCHAR |  | Pill size for day 2 of an anticoagulation dosing plan. |
| 23 | `PILL_SIZE_DAY3` | VARCHAR |  | Pill size for day 3 of an anticoagulation dosing plan. |
| 24 | `PILL_SIZE_DAY4` | VARCHAR |  | Pill size for day 4 of an anticoagulation dosing plan. |
| 25 | `PILL_SIZE_DAY5` | VARCHAR |  | Pill size for day 5 of an anticoagulation dosing plan. |
| 26 | `PILL_SIZE_DAY6` | VARCHAR |  | Pill size for day 6 of an anticoagulation dosing plan. |
| 27 | `PILL_SIZE_DAY7` | VARCHAR |  | Pill size for day 7 of an anticoagulation dosing plan. |
| 28 | `NUMBER_PILLS_DAY1` | NUMERIC |  | Number of pills for day 1 of an anticoagulation dosing plan. |
| 29 | `NUMBER_PILLS_DAY2` | NUMERIC |  | Number of pills for day 2 of an anticoagulation dosing plan. |
| 30 | `NUMBER_PILLS_DAY3` | NUMERIC |  | Number of pills for day 3 of an anticoagulation dosing plan. |
| 31 | `NUMBER_PILLS_DAY4` | NUMERIC |  | Number of pills for day 4 of an anticoagulation dosing plan. |
| 32 | `NUMBER_PILLS_DAY5` | NUMERIC |  | Number of pills for day 5 of an anticoagulation dosing plan. |
| 33 | `NUMBER_PILLS_DAY6` | NUMERIC |  | Number of pills for day 6 of an anticoagulation dosing plan. |
| 34 | `NUMBER_PILLS_DAY7` | NUMERIC |  | Number of pills for day 7 of an anticoagulation dosing plan. |
| 35 | `WEEKLY_TOTAL` | VARCHAR |  | The total weekly dose or average weekly dose the patient was instructed to take for an anticoagulation dosing plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

