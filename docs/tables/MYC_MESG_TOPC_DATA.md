# MYC_MESG_TOPC_DATA

> This table contains information about the topics answered by the patient in a history questionnaire submission.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TOPIC_TYP_C_NAME` | VARCHAR |  | The topic type of the history questionnaire topic answered by the patient. |
| 4 | `TOPIC_ID` | VARCHAR |  | The ID of the history questionnaire topic answered by the patient. |
| 5 | `TOPIC_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 6 | `NUM_QUESN` | INTEGER |  | The number of questions in the history questionnaire topic answered by the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

