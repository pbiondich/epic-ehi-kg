# MYC_MESG_SEX_QTNS

> This table contains patient answers to sexual activity questions submitted in a history questionnaire.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEX_QUESN_ID` | VARCHAR |  | The ID of the sexual activity history question answered by the patient. |
| 4 | `SEX_QUESN_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 5 | `SEX_QUESN_RESP_C_NAME` | VARCHAR |  | The patient's response to the sexual history question. |
| 6 | `SEX_QUESN_CMT` | VARCHAR |  | The comment entered by the patient for the sexual history question. |
| 7 | `SEX_QUESN_FILED_YN` | VARCHAR |  | The filed status of the sexual activity question--has the provider filed it to the patient's record. |
| 8 | `SEX_QUESN_FILED_USER_ID` | VARCHAR |  | Stores the ID of the user who reconciled this sexual actiovity history data. |
| 9 | `SEX_QUESN_FILED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `SEX_QUESN_FILED_LOCAL_DTTM` | DATETIME (Local) |  | Stores the instant (in local time) this sexual activity history data was filed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

