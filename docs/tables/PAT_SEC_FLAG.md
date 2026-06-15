# PAT_SEC_FLAG

> The PAT_SEC_FLAG table contains a list of patient security flags associated with patients.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient. |
| 2 | `LINE` | INTEGER | PK | The line number. |
| 3 | `SEC_FLAG_C_NAME` | VARCHAR | org | The security flag associated with the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

