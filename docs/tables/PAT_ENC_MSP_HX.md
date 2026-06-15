# PAT_ENC_MSP_HX

> History of who touched or changed the Medicare as a Secondary Payer Questionnaire (MSPQ) for a contact. Includes the MSPQ status, time of change, and reason incomplete as well.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `LINE` | INTEGER | PK | The line number, representing a line of 1 or more history data |
| 3 | `MSP_USER_HISTORY` | VARCHAR |  | History of users who have touched the MSPQ for this contact |
| 4 | `MSP_USER_HISTORY_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `MSP_STATUS_HISTORY` | VARCHAR |  | History of MSPQ statuses for this contact |
| 6 | `MSP_HISTORY_TM` | DATETIME (Local) |  | History of instant of changes/touches of MSPQ for this contact |
| 7 | `CONTACT_DATE` | DATETIME |  | Date for this MSPQ History |
| 8 | `MSP_COMPLETION_ST_C_NAME` | VARCHAR | org | History of the MSPQ completion status for this contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

