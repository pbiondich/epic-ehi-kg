# UNCONFRM_PAT_INFO

> This table stores unconfirmed patient tracking information.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `UNCONFRM_PAT_STAT_C_NAME` | VARCHAR | org | The unconfirmed patient status category ID for the patient. |
| 4 | `UNCONFRM_PAT_SRC_C_NAME` | VARCHAR | org | The unconfirmed patient workflow source category ID for the patient. |
| 5 | `UNCONFRM_PAT_RSN_C_NAME` | VARCHAR | org | The unconfirmed patient status reason category ID for the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

