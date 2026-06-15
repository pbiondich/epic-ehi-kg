# PAT_MCARE_ELIGIBILITY_RSN

> This table stores a member's Medicare eligibility reason information.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MCARE_ELIG_RSN_C_NAME` | VARCHAR | org | The Medicare eligibility reason category ID for the member. |
| 4 | `START_DATE` | DATETIME |  | The start date corresponding to the Medicare eligibility reason. |
| 5 | `END_DATE` | DATETIME |  | The end date corresponding to the Medicare eligibility reason. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

