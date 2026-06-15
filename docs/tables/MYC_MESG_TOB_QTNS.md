# MYC_MESG_TOB_QTNS

> This table contains patient answers to tobacco use questions submitted in a history questionnaire.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique identifier for the message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TOB_QUESN_ID` | VARCHAR |  | The ID of the tobacco use question answered by the patient. |
| 4 | `TOB_QUESN_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 5 | `TOB_QUESN_RESP_C_NAME` | VARCHAR |  | The patient's response to the tobacco use question. |
| 6 | `TOB_QUESN_PPD` | VARCHAR |  | The number of packs smoked per day entered by the patient. |
| 7 | `TOB_QUESN_YRS` | VARCHAR |  | The number of years of tobacco use entered by the patient. |
| 8 | `TOB_QUESN_QUIT_DT` | DATETIME |  | The date quit smoking entered by the patient. |
| 9 | `TOB_QUESN_CMT` | VARCHAR |  | The comment entered by the patient for the tobacco use question. |
| 10 | `TOB_QUESN_FILED_YN` | VARCHAR |  | The filed status of the tobacco use question--has the provider filed it to the patient's record. |
| 11 | `SMOKELESS_TOB_USE_C_NAME` | VARCHAR |  | The patient's response to the smokeless tobacco use question. |
| 12 | `SMOKELESS_QUIT_DATE` | DATETIME |  | The date quit smokeless tobacco entered by the patient. |
| 13 | `SMOKING_TOB_USE_C_NAME` | VARCHAR |  | The patient's response to the smoking tobacco use question. |
| 14 | `SMOKING_QUIT_DATE` | DATETIME |  | The date quit smoking entered by the patient. |
| 15 | `TOBACCO_READY_QT_C_NAME` | VARCHAR |  | The patient's response to the ready to quit question. |
| 16 | `SMOKING_START_DATE` | DATETIME |  | The start smoking date entered by the patient. |
| 17 | `CURRENT_PACKS_PER_DAY` | VARCHAR |  | The number of packs currently smoked per day entered by the patient. |
| 18 | `CURRENT_YEARS` | VARCHAR |  | The current number of years of tobacco use entered by the patient. |
| 19 | `HAS_CUR_CIG_PER_DAY_QUESN_YN` | VARCHAR |  | Used to know if we are asking a current cigarettes per day question. Stores 1 if we are 0 if it's a current packs per day question. |
| 20 | `HAS_AVG_CIG_PER_DAY_QUESN_YN` | VARCHAR |  | Used to know if we are asking a average cigarettes per day question. Stores 1 if we are 0 if it's a average packs per day question. |
| 21 | `TOB_QUESN_FILED_USER_ID` | VARCHAR |  | Stores the ID of the user who reconciled the tobacco data on this submission. |
| 22 | `TOB_QUESN_FILED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 23 | `TOB_QUESN_FILED_LOCAL_DTTM` | DATETIME (Local) |  | Stores the instant (in local time) this tobacco history data was filed. |
| 24 | `PASSIVE_SMOKE_EXPOSURE_C_NAME` | NUMERIC |  | The patient's response to the passive smoke exposure question. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

