# PAT_REVIEW_DATA

> Table contains patient entered clinical data review from Welcome Kiosk and MyChart.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 15  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PAT_REVIEW_ELG_C_YN` | VARCHAR |  | Patient allergies reviewed by the patient. The response to the prompt, "do you have any additional allergies?" |
| 6 | `PAT_REVIEW_ORD_C_YN` | VARCHAR |  | Patient medications reviewed by the patient. The response to the prompt, "do you have any additional medications?" |
| 7 | `PAT_REVIEW_LPL_C_YN` | VARCHAR |  | Patient problems reviewed by the patient. The response to the prompt, "do you have any additional problems?" |
| 8 | `PAT_ALG_RVW_INFO_C_NAME` | VARCHAR | org | The patient's response to the "are these allergies correct?" question in Welcome. |
| 9 | `PAT_MED_RVW_INFO_C_NAME` | VARCHAR |  | The patient's response to the "are these medications correct?" question in Welcome. |
| 10 | `PAT_PROB_RVW_INFO_C_NAME` | VARCHAR |  | The patient's response to the "are these problems correct?" question in Welcome. |
| 11 | `ENC_PHR_VERIF_INST_UTC_DTTM` | DATETIME (UTC) |  | The last instant that a patient's encounter pharmacy was updated or verified. |
| 12 | `ENC_PHR_VERIF_AUDIT_CONTEXT_C_NAME` | VARCHAR |  | The context of the last update or verification of a patient's encounter pharmacy. |
| 13 | `ENC_PHR_VERIF_USER_ID` | VARCHAR |  | The user that last updated or verified the patient's encounter pharmacy. |
| 14 | `ENC_PHR_VERIF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `ENC_PHR_VERIF_MYPT_ID` | VARCHAR |  | The MyChart user that last updated or verified the patient's encounter pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

