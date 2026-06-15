# MYC_MESG_SURG_QTNS

> This table contains patient answers to sexual activity questions submitted in a history questionnaire.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SURG_QUESN_ID` | VARCHAR |  | The ID of the surgical history question answered by the patient. |
| 4 | `SURG_QUESN_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 5 | `SURG_QUESN_RESP_C_NAME` | VARCHAR |  | The patient's response to the surgical history question. |
| 6 | `SURG_QUESN_DT` | VARCHAR |  | The date entered by the patient for the surgical history question. |
| 7 | `SURG_QUESN_CMT` | VARCHAR |  | The comment entered by the patient for the surgical history question. |
| 8 | `SURG_QUESN_FILED_YN` | VARCHAR |  | The filed status of the surgical history question--has the provider filed it to the patient's record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

