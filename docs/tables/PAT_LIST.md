# PAT_LIST

> The PAT_LIST table contains patients and the corresponding patient lists that they are members of.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | Unique patient ID. |
| 2 | `LINE` | INTEGER | PK | The line number within a multiple response or over time item |
| 3 | `LIST_ID_LIST_DESCRIPTION` | VARCHAR |  | Description of the patient list. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

