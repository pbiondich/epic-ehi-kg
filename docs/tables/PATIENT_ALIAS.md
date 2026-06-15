# PATIENT_ALIAS

> The PATIENT_ALIAS table contains the aliases and soundex data for your patients. Each patient may have multiple aliases; therefore, a line number is used to uniquely identify each alias for a patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID number assigned to the patient record. |
| 2 | `LINE` | INTEGER | PK | The line number associated with the alias information associated with this row. Multiple pieces of information can be associated with this row. |
| 3 | `ALIAS` | VARCHAR |  | The alias on the patient record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

