# PROB_CONTACT

> This table contains contact specific information on care integrator problems associated with a patient.

**Primary key:** `PROBLEM_ID`, `CONTACT_DATE_REAL`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_ID` | VARCHAR | PK FK→ | The unique ID for the care integrator problem. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date for the problem in internal format. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user who added the problem. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `LAST_EDIT_TIME` | DATETIME (Local) |  | The instant that this problem was last edited. |
| 7 | `RESOLVED_YN` | VARCHAR |  | Indicates if this problem has been resolved. |
| 8 | `CP_PRIORITY_C_NAME` | VARCHAR | org | The priority level assigned to a given problem. |
| 9 | `START_DATE` | DATETIME |  | The start date assigned to begin work on a problem. |
| 10 | `RESOLVED_DATE` | DATETIME |  | The date a problem is considered resolved. |
| 11 | `PAT_CSN` | NUMERIC | FK→ | Patient contact serial number (CSN) associated with a particular care plan problem contact. |
| 12 | `READING_UTC_DTTM` | DATETIME (UTC) |  | Documents when the original reading contact was documented. Used to order active documentation readings in the order they clinically happened. |
| 13 | `CONTACT_NUMBER` | VARCHAR |  | The serial number of the contact on the care plan problem record. |
| 14 | `CAREPLAN_CSN_ID` | NUMERIC |  | The unique contact serial number of the care plan problem contact that is associated with the care plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PROBLEM_ID` | [PROBLEM](PROBLEM.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

