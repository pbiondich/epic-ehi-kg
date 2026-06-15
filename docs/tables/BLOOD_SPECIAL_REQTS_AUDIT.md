# BLOOD_SPECIAL_REQTS_AUDIT

> This table contains the change user, change instant, and encounter contact serial number (CSN) for the current and all previous values that were set for a patient's special requirements when ordering blood. Use with table BLD_REQS_VALS_AUDIT to view the complete audit trail for the patient's special requirements.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BLOOD_REQTS_CHANGE_UTC_DTTM` | DATETIME (UTC) |  | Stores all previous instants when a patient's special requirements for blood transfusions were edited. |
| 4 | `BLOOD_REQTS_CHANGE_USER_ID` | VARCHAR |  | The unique identifier of the user who documented the special requirements needed for a patient's blood transfusion. |
| 5 | `BLOOD_REQTS_CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `BLOOD_REQTS_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This column stores the contact serial number (CSN) of each visit in which the patient's blood special requirements were changed. |
| 7 | `TYPE_AND_SCREEN_AUDIT_YN` | VARCHAR |  | This column stores the history of when the patient was or was not eligible to receive a type and screen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BLOOD_REQTS_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

