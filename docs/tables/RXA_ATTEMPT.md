# RXA_ATTEMPT

> Contains information about adjudication records, including the user and workstation that initiated the adjudication, the National Council for Prescription Drug Programs (NCPDP) transaction type, and the date the record was created. Adjudication records are used during prescription copay adjudication.

**Primary key:** `RECORD_ID`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category ID of the adjudication message (hidden, soft-deleted, etc...) |
| 3 | `ADJ_WORKSTATION_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |
| 4 | `USER_ID` | VARCHAR | FK→ | The user who initiated the adjudication. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RECORD_CREATION_DT` | DATETIME |  | Stores the date the record was created |
| 7 | `UPDATE_DATETIME` | DATETIME (Local) |  | Stores the instant the record was last locked/unlocked |
| 8 | `ADJ_INTENT_C_NAME` | VARCHAR |  | The overall intent category ID of the adjudication message (for example, reversal or billing). |
| 9 | `MESSAGE_SOURCE_C_NAME` | VARCHAR |  | The source category ID of the adjudication message. |
| 10 | `ADJ_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 11 | `TEST_CLAIM_YN` | VARCHAR |  | Indicates if the adjudication attempt is a test claim. 'N' or NULL indicate that the attempt is not a test claim. 'Y' indicates that the attempt is a test claim. |
| 12 | `PAT_ID` | VARCHAR | FK→ | The patient record to which this RXA record is associated. For Eligibility checking, this identifies the patient for whom the check is being performed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

