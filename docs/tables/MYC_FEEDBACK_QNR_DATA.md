# MYC_FEEDBACK_QNR_DATA

> This table stores data about feedback questionnaires attached to appointments.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `MYC_FEEDBACK_QNR_ID` | VARCHAR |  | This item defines a patient feedback questionnaire to be asked for this appointment. |
| 7 | `MYC_FEEDBACK_QNR_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 8 | `MYC_FDBCK_QNR_SRC_C_NAME` | VARCHAR |  | This item stores how the related feedback questionnaire was assigned to the appointment. |
| 9 | `MYC_FDBK_QNR_STAT_C_NAME` | VARCHAR |  | The status of the related patient-entered feedback appointment questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

