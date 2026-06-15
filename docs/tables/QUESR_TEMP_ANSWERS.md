# QUESR_TEMP_ANSWERS

> The QUESR_TEMP_ANSWERS table stores information about patient questionnaire answers which have not been submitted. The records included in this table are partial submissions which may be modified by the patient before being moved to the permanent storage location.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QUESR_TMP_ANSWER_ID` | VARCHAR |  | The unique ID of the answer set for this row. |
| 4 | `QUESR_TMP_MYPT_ID` | VARCHAR |  | The unique ID of the patient account for this row. |
| 5 | `QUESR_TMP_ROOT_ID` | VARCHAR |  | Stores the root questionnaire (LQF) record ID for each questionnaire that has not yet been submitted. |
| 6 | `QUESR_TMP_ROOT_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 7 | `HX_QUESR_TMP_ID` | VARCHAR |  | Stores the web-based chart system message records of partially completed history questionnaires that have not been submitted by the patient. |
| 8 | `CTX_PAT_ENC_CSN_ID` | NUMERIC | FK→ | If the TEMP_QUESR_SRC_WRKFLW_C is a value of 1, this stores the contact serial number of the patient contact that serves as the appointment context for this temporary questionnaire answer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CTX_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

