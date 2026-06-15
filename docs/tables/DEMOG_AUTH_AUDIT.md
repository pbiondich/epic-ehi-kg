# DEMOG_AUTH_AUDIT

> Audit trail for events related to demographic authentication tokens.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EVENT_UTC_DTTM` | DATETIME (UTC) |  | The instant an action was taken on a token. |
| 4 | `TOKEN` | VARCHAR |  | The token this action happened in relation to. |
| 5 | `USER_ID` | VARCHAR | FK→ | If applicable, this stores the Hyperspace user ID associated with this action. |
| 6 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `MYPT_ID` | VARCHAR | shared | If applicable, this stores the MyChart user ID that performed an action taken on a token. |
| 8 | `MYC_DEMOG_AUTH_ACTION_C_NAME` | VARCHAR |  | Stores the type of action taken on a token. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

