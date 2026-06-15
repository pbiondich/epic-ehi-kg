# PAT_MYC_ACSS_TRK

> This table keeps an audit trail of changes made to the status of a web based chart system account.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique identifier for the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of access data associated with an individual patient record. |
| 3 | `MYC_ACSS_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user record who performed some action regarding the patient's web based chart system account. |
| 4 | `MYC_ACSS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `MYC_ACSS_ACTION_C_NAME` | VARCHAR |  | The category value corresponding to the action that was performed on the patient's web based chart system account. |
| 6 | `ACSS_TIMESTAMP` | DATETIME (Local) |  | This is a timestamp indicating when the patient's web based chart system account was changed. |
| 7 | `ACSS_PROXY_CMT` | VARCHAR |  | The comment, if one was entered, when an account was activated for proxy use. |
| 8 | `MYC_ACSS_CODE` | VARCHAR |  | This stores the access code that was generated for an activation action performed on the patient's web based chart system account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

