# MYC_MESG_ADL_QTNS

> This table contains patient answers to activities of daily living (ADL) questions submitted in a history questionnaire.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADL_QUESN_ID` | VARCHAR |  | The ID of the ADL history question answered by the patient. |
| 4 | `ADL_QUESN_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 5 | `ADL_QUESN_RESP_C_NAME` | VARCHAR |  | The patient's response to the ADL question. |
| 6 | `ADL_QUESN_CMT` | VARCHAR |  | The comment added by the patient when answering an ADL (Activities of Daily Living) question. |
| 7 | `ADL_QUESN_FILED_YN` | VARCHAR |  | Whether a provider has filed to the patient's chart the patient's response to the ADL question. |
| 8 | `ADL_QUESN_FILED_USER_ID` | VARCHAR |  | Stores the ID of the user who reconciled this ADL history data. |
| 9 | `ADL_QUESN_FILED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `ADL_QUESN_FILED_LOCAL_DTTM` | DATETIME (Local) |  | Stores the instant (in local time) this ADL history data was filed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

