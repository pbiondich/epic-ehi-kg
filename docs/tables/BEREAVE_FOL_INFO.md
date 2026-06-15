# BEREAVE_FOL_INFO

> This table contains information about your bereaved's follow-up record. These include bereaved record link, follow-up type, and follow-up form. The records included in this table are Bereavement Follow-Up (LHC) records.

**Primary key:** `RECORD_ID`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the bereavement follow-up record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status, such as active or soft-deleted. |
| 3 | `BEREAVED_ID` | NUMERIC |  | The unique identifier for the bereaved record linked to this bereavement follow-up. |
| 4 | `PAT_CSN` | NUMERIC | FK→ | The contact serial number of the contact in a patient record in which the bereavement follow-up was documented. |
| 5 | `FORM_ID` | VARCHAR | FK→ | The unique identifier of the custom interface (SmartForm) record that is used to document the bereavement follow-up. |
| 6 | `FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 7 | `FORM_DAT` | VARCHAR |  | The contact date (DAT) of the custom interface (SmartForm) record that is used to document the bereavement follow-up. |
| 8 | `FOLLOW_UP_TYPE_C_NAME` | VARCHAR | org | Type of documentation in bereavement follow-up. |
| 9 | `RECORD_CREATION_DT` | DATETIME |  | The date the record was created |
| 10 | `INSTANT_OF_UPD_DTTM` | DATETIME (Local) |  | The instant the record was last locked/unlocked |
| 11 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient associated with the bereaved. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FORM_ID` | [CL_QFORM1](CL_QFORM1.md) | sole_pk | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

