# MYC_MESG_ALC_QTNS

> This table contains patient answers to alcohol use questions submitted in a history questionnaire.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ALC_QUESN_ID` | VARCHAR |  | The ID of the alcohol history question answered by the patient. |
| 4 | `ALC_QUESN_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 5 | `ALC_QUESN_RESP_C_NAME` | VARCHAR |  | The patient's response to the question about alcohol use. |
| 6 | `ALC_QUESN_CMT` | VARCHAR |  | The comment added by the patient when answering the alcohol use question. |
| 7 | `ALC_QUESN_FILED_YN` | VARCHAR |  | The filed status of the alcohol question--has the provider filed it to the patient's record. |
| 8 | `ALC_QUESN_FILED_USER_ID` | VARCHAR |  | Stores the ID of the user who reconciled this alcohol history data. |
| 9 | `ALC_QUESN_FILED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `ALC_QUESN_FILED_LOCAL_DTTM` | DATETIME (Local) |  | Stores the instant (in local time) this alcohol history data was filed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

