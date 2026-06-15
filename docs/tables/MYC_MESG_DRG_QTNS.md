# MYC_MESG_DRG_QTNS

> This table contains patient answers to drug use questions submitted in a history questionnaire.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DRG_QUESN_ID` | VARCHAR |  | The ID of the drug use history question answered by the patient. |
| 4 | `DRG_QUESN_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 5 | `DRG_QUESN_RESP_C_NAME` | VARCHAR |  | The patient's response to the question about drug use. |
| 6 | `DRG_QUESN_FREQ` | VARCHAR |  | The patient's response to the drug use frequency question. |
| 7 | `DRG_QUESN_CMT` | VARCHAR |  | The comment added by the patient when answering the drug use question. |
| 8 | `DRG_QUESN_FILED_YN` | VARCHAR |  | The filed status of the drug use question--has the provider filed it to the patient's record. |
| 9 | `DRG_QUESN_FILED_USER_ID` | VARCHAR |  | Stores the ID of the user who reconciled this drug use history data. |
| 10 | `DRG_QUESN_FILED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `DRG_QUESN_FILED_LOCAL_DTTM` | DATETIME (Local) |  | Stores the instant (in local time) this drug use history data was filed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

