# QUESR_LST_ANS_INFO

> This table stores information about the most recent patient questionnaire submission. This table stores when the questionnaire was last answered and the contact serial number for the encounter.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `QUESR_ANS_FORM_ID` | VARCHAR |  | This column stores recently answered questionnaire IDs. Use the QUESR_ANS_CSN_ID and QUESR_ANS_DDATETIME columns to determine the encounter and last submission instant for each questionnaire. |
| 4 | `QUESR_ANS_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `QUESR_ANS_CSN_ID` | NUMERIC |  | This column stores the encounter contact serial number (CSN) for the most recent questionnaire submissions. Use the QUESR_ANS_FORM_ID and QUESR_ANS_CSN_ID columns to determine the form ID and encounter contact serial number for each questionnaire. |
| 6 | `QUESR_ANS_DATETIME` | DATETIME (Attached) |  | This column stores the last instant of submission for questionnaires. Use the QUESR_ANS_FORM_ID and QUESR_ANS_CSN_ID columns to determine the form ID and encounter contact serial number for each questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

