# PT_GOALS_UPDATES

> This table contains data for the Discrete Goals (IGO) masterfile that is over-time data.

**Primary key:** `GOAL_ID`, `CONTACT_DATE_REAL`  
**Columns:** 17  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique identifier for the goal record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `EDIT_USER_ID` | VARCHAR |  | The user (EMP) ID of the person who entered this data. |
| 5 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `PAT_CSN` | NUMERIC | FK→ | Patient CSN (contact serial number I.E. unique contact identifier) associated with a particular IGO (goal) contact. |
| 7 | `STATUS_C_NAME` | VARCHAR |  | Current status of the goal record |
| 8 | `INSTNT_OF_EDIT_DTTM` | DATETIME (Local) |  | Instant of edit for this contact. This column no longer populates data for new HH/HSPC care plans as of Epic May 2024. Use the EDIT_INST_DTTM column in PT_GOAL_UPDATES table to report on this item instead. |
| 9 | `DISPLAY_NAME_OT` | VARCHAR |  | Display name for the goal |
| 10 | `LOW_VALUE_OVERRIDE` | VARCHAR |  | Low value for the goal value range |
| 11 | `HIGH_VALUE_OVERRIDE` | VARCHAR |  | High value for goal value range |
| 12 | `COMPLIANCE_VALUE_NAME` | VARCHAR | org | Current outcome value for the goal. This column stores the manually tracked goal compliance value. |
| 13 | `MYC_EDIT_USER_ID` | VARCHAR |  | This item stores the proxy/patient (WPR) ID of the proxy/patient who added or edited a goal from MyChart. |
| 14 | `PT_STATED_YN` | VARCHAR |  | Indicates whether or not a goal is patient-stated. |
| 15 | `LONG_RANGE_YN` | VARCHAR |  | Indicates whether the goal is a long-range goal or a short-term goal. |
| 16 | `LINKED_LONG_RANGE_ID` | VARCHAR |  | The ID of the long-range goal that this short-term goal is linked to. |
| 17 | `OUTPAT_PRIORITY_C_NAME` | VARCHAR | org | Outpatient Priority |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

