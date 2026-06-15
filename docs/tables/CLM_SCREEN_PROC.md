# CLM_SCREEN_PROC

> Assessment outcome screen procedure.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique ID for the claim information record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SCREEN_PROCEDURE_C_NAME` | VARCHAR |  | The screening procedure for the assessment outcomes. |
| 4 | `SCR_ASSESSMENT_C_NAME` | VARCHAR |  | The assessment related to the screening procedure. |
| 5 | `SCR_NEW_PROBLEM_C_NAME` | VARCHAR |  | The follow-up code corresponding to the new problems related to the suspected screening procedure. |
| 6 | `SCR_KNOWN_PROB_C_NAME` | VARCHAR |  | The follow-up code corresponding to the known problems related to the suspected screening procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

