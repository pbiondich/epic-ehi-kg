# HM_ENC_DATE

> This table contains data related to when the patient was contacted for upcoming or overdue health maintenance topics.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HM_LET_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The HM_LET_PAT_ENC_CSN_ID column stores the CSN for a Health Maintenance letter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HM_LET_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

