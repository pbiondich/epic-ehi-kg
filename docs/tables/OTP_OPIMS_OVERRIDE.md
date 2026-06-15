# OTP_OPIMS_OVERRIDE

> This table stores information about the override that a clinician entered when they chose to not use the products chosen by outpatient Intelligent Medication Selection (IMS).

**Primary key:** `OTP_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant of the override of the Intelligent Medication Selection (IMS) suggest products. |
| 4 | `USER_ID` | VARCHAR | FK→ | Stores the user who overrode the Intelligent Medication Selection (IMS) suggestion. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `REASON_C_NAME` | VARCHAR | org | Stores the reason for the override of the Intelligent Medication Selection (IMS) suggested products. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

