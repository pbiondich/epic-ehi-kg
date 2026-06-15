# PAT_RESERVATION

> The PAT_RESERVATION table contains reservation-related information for a patient. The table will contain one row per patient encounter.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 16  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `RES_CALLER_NAME` | VARCHAR |  | The person who called to make a reservation for the patient. |
| 6 | `RES_CALLER_PHONE` | VARCHAR |  | The phone number of the person who called to make a reservation for the patient. |
| 7 | `RES_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `RES_CALLED_DTTM` | DATETIME (Local) |  | The date and time when the reservation request was received. |
| 9 | `RES_USER_ID` | VARCHAR |  | The unique ID of the user who received the reservation request. |
| 10 | `RES_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `RES_ADM_APRV_YN` | VARCHAR |  | Indicates whether the admission for the patient was approved. |
| 12 | `RES_DENIAL_RSN_C_NAME` | VARCHAR | org | The category number for the admission denial reason. |
| 13 | `RES_TRANS_RSN_C_NAME` | VARCHAR | org | The category number for the reason behind the transfer request. |
| 14 | `RES_EXP_PAT_CLS_C_NAME` | VARCHAR | org | The category number for the patient's expected patient class. |
| 15 | `RES_EXP_LOC_C_NAME` | VARCHAR | org | The category number for the patient's expected level of care. |
| 16 | `RES_DECISION_DTTM` | DATETIME (Local) |  | The date and time when the decision on whether to accept the reservation was made. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

