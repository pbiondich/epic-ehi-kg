# BMT_ANONYMOUS_DONOR

> This table contains information about BMT anonymous donors.

**Primary key:** `RECORD_ID`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the BMT anonymous donor. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | The record status. |
| 3 | `BIRTH_DATE` | DATETIME |  | The date of birth of the BMT donor. |
| 4 | `SEX_ASGN_AT_BIRTH_C_NAME` | VARCHAR | org | The BMT donor's sex assigned at birth. |
| 5 | `CORD_BLOOD_BANK_C_NAME` | VARCHAR | org | The donor cord blood bank. |
| 6 | `DNR_ABO_C_NAME` | VARCHAR |  | The blood type of the BMT donor. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

