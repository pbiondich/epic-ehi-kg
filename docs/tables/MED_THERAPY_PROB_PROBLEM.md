# MED_THERAPY_PROB_PROBLEM

> This table contains information about medication therapy problems.

**Primary key:** `PROBLEM_ID`, `CONTACT_DATE_REAL`  
**Columns:** 18  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the medication therapy problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `MED_THERAPY_PROBLEM_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the medication therapy problem contact. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 4 | `CONTACT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient encounter where this edit happened. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `DOCUMENTING_USER_ID` | VARCHAR |  | The unique ID of the user who documented changes made on this contact. |
| 6 | `DOCUMENTING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `INSTANT_OF_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant this contact was saved. This is stored in UTC time. |
| 8 | `MTP_STATUS_C_NAME` | VARCHAR |  | The status category ID of the medication therapy problem. |
| 9 | `CONTACT_RESPONSIBLE_USER_ID` | VARCHAR |  | The unique ID of the responsible user at the time of the contact for this medication therapy problem. |
| 10 | `CONTACT_RESPONSIBLE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `MTP_PRIORITY_LEVEL_C_NAME` | VARCHAR |  | The relative priority category ID of the medication therapy problem. |
| 12 | `START_DATE` | DATETIME |  | The date the medication therapy problem was identified. |
| 13 | `END_DATE` | DATETIME |  | The date the medication therapy problem was resolved or changed to an inactive status. |
| 14 | `DUE_DATE` | DATETIME |  | The date that the next action is due for a medication therapy problem. |
| 15 | `MTP_RATIONALE_C_NAME` | VARCHAR | org | The rationale category ID for this medication therapy problem. |
| 16 | `MTP_PROBLEM_C_NAME` | VARCHAR | org | The problem type category ID for this medication therapy problem. |
| 17 | `MED_RELATED_NEED_MTP_TOPIC_C_NAME` | VARCHAR | org | The medication related need category ID for this medication therapy problem. |
| 18 | `REVERT_TO_PROBLEM_CSN_ID` | NUMERIC |  | Stores the MTP CSN of a contact that this contact can be reverted to, and is equivalent to, using the utility to revert MTP Cleanup Batch Job runs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CONTACT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |

