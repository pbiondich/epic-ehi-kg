# NOTES_TRANS_AUTH

> This table contains transcription authorization info.

**Primary key:** `NOTE_CSN_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `AUTH_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `AUTH_DTTM` | DATETIME (Local) |  | Date and time the transcription was authenticated |
| 5 | `AUTH_USER_ID` | VARCHAR |  | Id of the user who authenticated the transcription |
| 6 | `AUTH_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `DICTATION_TIME` | DATETIME (Local) |  | This is the dictation date and time in datetime format. Please note that this only contains information for authorized transcriptions. |
| 8 | `TRANSCRIPTION_TIME` | DATETIME (Local) |  | This is the transcription date and time in datetime format. Please note that this only contains information for authorized transcriptions. |
| 9 | `ACTIVITY_DTTM` | DATETIME (Local) |  | This is the activity date and time in datetime format. |
| 10 | `ORIGINATOR_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `EDIT_DTTM` | DATETIME (Local) |  | This is the transcription edit date and time in datetime format. |
| 12 | `CHR_CNT_DTTM` | DATETIME (Local) |  | The date and time in which the transcription character count was recorded. |
| 13 | `CHR_CNT_MET` | FLOAT |  | The character count of the transcription. |
| 14 | `DICT_PRIORITY_C_NAME` | VARCHAR |  | The dictation priority category number for the transcription. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

