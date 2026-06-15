# FAILED_ACCESS

> This table contains information on failed MyChart activation attempts.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FAILED_DTTM_DTTM` | DATETIME (Local) |  | This item stores the instant a correct MyChart activation code was used with incorrect validation data. |
| 4 | `FAILED_IP` | VARCHAR |  | This item stores the remote IP address from where a correct MyChart activation code was used with incorrect validation info. |
| 5 | `FAILED_REASON_C_NAME` | VARCHAR | org | This item stores the validation field that failed when a correct MyChart activation code is used with incorrect validation info. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

