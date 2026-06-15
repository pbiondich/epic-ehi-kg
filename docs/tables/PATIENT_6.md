# PATIENT_6

> This table supplements the PATIENT table. It contains basic information about patients.

**Overflow of:** [PATIENT](PATIENT.md)  
**Primary key:** `PAT_ID`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `IMAGING_WILL_CALL_YN` | VARCHAR |  | Holds a "Will Call" status for the patient. This is a status toggled by a Radiology user (eg. Technologist) to flag the availability of the patient for further processing. |
| 3 | `PAT_PRONOUN_FOR_USE_IN_TEXT_C_NAME` | VARCHAR | org | The pronoun category ID for the patient which is used by the system for text generation. |
| 4 | `PAT_PRONOUN_COMMENT` | VARCHAR |  | The pronoun comment or instructions entered by the user who documented a patient's pronouns. |
| 5 | `PAT_PRONOUN_OTHER_FREE_TEXT` | VARCHAR |  | The free-text pronouns entered for a patient whose pronouns were not available to be discretely collected as a category value. |
| 6 | `PAT_PRONOUN_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the patient's pronouns were last updated, in UTC. |
| 7 | `SEX_FOR_MELD_C_NAME` | VARCHAR |  | The patient's sex for adult Model for End-Stage Liver Disease (MELD) calculation. |
| 8 | `DEDUPLICATED_RCVD_DOCUMENT_ID` | NUMERIC |  | Deduplicated received document for this patient |
| 9 | `INTERSEX_STATUS_C_NAME` | VARCHAR |  | The intersex status category ID for the patient. (Intersex is an umbrella term for differences in sex traits or reproductive anatomy that a person is born with or which develop in childhood.) |
| 10 | `INSIGHT_AI_INTRCT_ID` | NUMERIC |  | The ID of the record containing AI-generated insights for the patient. |
| 11 | `MOBILE_PHONE` | VARCHAR |  | This is a virtual item that returns the patient's mobile phone number from the patient phone numbers table in related group 94. If multiple mobile numbers are on file, then the number with the highest priority is returned. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PATIENT](PATIENT.md).

