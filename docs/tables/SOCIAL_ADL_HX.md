# SOCIAL_ADL_HX

> This table contains data recorded in the activities of daily living section of social history contacts entered in the patient's chart during a clinical system encounter. Note: This table is designed to hold a patient's history over time; however, it is most typically implemented to only extract the latest patient history contact.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `HX_ADL_QUESTION_ID` | VARCHAR |  | Stores the link to the unique ID of the ADL question. |
| 4 | `HX_ADL_QUESTION_ID_RECORD_NAME` | VARCHAR |  | The name of the Visit Navigator (VN) History Template Definition (LQH) record. |
| 5 | `HX_ADL_RESPONSE_C_NAME` | VARCHAR |  | This column stores the category value (1, 2 or 3) of the response to ADL questions. |
| 6 | `HX_ADL_COMMENTS` | VARCHAR |  | Holds comments for Activities of Daily Living (ADL) questions. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

