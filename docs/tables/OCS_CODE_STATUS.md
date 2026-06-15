# OCS_CODE_STATUS

> This table contains information about patient code statuses, which are mainly used for documenting compliance reasons and quality. This table replaces the older IP_CODE_STATUS table.

**Primary key:** `OCS_ID`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OCS_ID` | VARCHAR | PK | The unique ID for the code status record. |
| 2 | `OCS_NAME` | VARCHAR |  | The name of the code status record. |
| 3 | `OCS_STATUS_C_NAME` | VARCHAR |  | This stores the status of the record (hidden, soft deleted, etc.) |
| 4 | `CODE_STATUS_C_NAME` | VARCHAR | org | Code status category value. |
| 5 | `ACTIVATED_INST` | DATETIME (Local) |  | The instant at which the code status (full code, DNR, etc.) was created. |
| 6 | `USER_ID` | VARCHAR | FK→ | The unique identifier of the user that created the code status |
| 7 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `ORDER_ID` | NUMERIC | shared | The unique identifier for the code status order record. |
| 9 | `COMMENTS` | VARCHAR |  | The comment associated with the code status. |
| 10 | `INACTIVATED_INST` | DATETIME (Local) |  | The instant at which the code status was inactivated. |
| 11 | `CONTEXT_C_NAME` | VARCHAR |  | The context (inpatient/ambulatory/etc.) in which the status was recorded. |
| 12 | `PATIENT_ID` | VARCHAR |  | The patient for which this code status was recorded. |
| 13 | `PATIENT_CSN` | NUMERIC |  | The Contact Serial Number of the encounter in which the code status order was placed. |
| 14 | `ACTV_UTC_DTTM` | DATETIME (UTC) |  | Holds the instant the code status was activated in UTC time. |
| 15 | `INACTV_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the code status was inactivated in UTC time. |
| 16 | `VERBAL_ORDER_ID` | VARCHAR | FK→ | The unique identifier of the home care order that created this code status record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |
| `VERBAL_ORDER_ID` | [HH_VO_INFO](HH_VO_INFO.md) | sole_pk | high |

