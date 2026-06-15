# DEMOG_AUTH_INFO

> Demographic authentication tokens associated with specific patients. Active tokens allow users to login to MyChart without a normal account through unique URLs.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TOKEN` | VARCHAR |  | The unique token associating a demographic authentication URL with a patient. |
| 4 | `GENERATION_DATE` | DATETIME |  | The date a specific token was created. |
| 5 | `EXPIRATION_UTC_DTTM` | DATETIME (UTC) |  | The instant a specific token will expire. |
| 6 | `ASSOCIATED_MYPT_ID` | VARCHAR |  | Stores the MyChart account ID intended to log in with a specific token. |
| 7 | `FAILED_LOGIN_CNT` | INTEGER |  | Stores the count of failed consecutive logins for a specific token. If this exceeds the max allowed failed logins, the token will no longer be valid. |
| 8 | `DEMOG_AUTH_WKFLW_C_NAME` | VARCHAR |  | Stores the type of workflow a specific token was created for. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

