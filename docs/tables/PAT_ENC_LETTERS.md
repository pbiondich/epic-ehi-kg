# PAT_ENC_LETTERS

> The patient encounter letters table contains information about letters associated with encounters.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line count used to identify different letters associated with an encounter. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `LTR_STATUS_C_NAME` | VARCHAR |  | The category value associated with the status of each letter, such as 1- Open, 2- Deleted, 3- Sent, 4- Voided, 5-Sent by batch. |
| 5 | `LETTER_CREAT_DT` | DATETIME |  | The date that the letter was created. |
| 6 | `LETTER_HNO_ID` | VARCHAR |  | The note (HNO) record that hold the letter text. |
| 7 | `LETTER_FROM_ID` | VARCHAR |  | The user ID of the user entered as the "from" user in the letter activity. |
| 8 | `LETTER_FROM_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `LETTER_ROUT_CMT_ID` | VARCHAR |  | The note (HNO) ID that holds the letter routing comments. |
| 10 | `LETTER_REASON_C_NAME` | VARCHAR | org | The category value associated with the reason for the letter. |
| 11 | `LETTER_REASON_CMT` | VARCHAR |  | The comment for the letter reason. |
| 12 | `LTR_STATUS_CHG_TM` | DATETIME (Attached) |  | The instant (date and time) the status of the letter was created or changed. |
| 13 | `LTR_STAT_CH_USR_ID` | VARCHAR |  | The user that changed or created the letter status. |
| 14 | `LTR_STAT_CH_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `LETTER_DELVRY_ADDR` | VARCHAR |  | The address the letter was sent to. |
| 16 | `LETTER_RETURN_ADDR` | VARCHAR |  | The return address for the letter |
| 17 | `LETTER_WORKINGDAYS` | INTEGER |  | The number of work days (excluding weekends and holidays) from the date of the letter's encounter to the date the letter was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

