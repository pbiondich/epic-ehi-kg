# CL_QANSWER_GEN_CMT

> This stores general comments associated with question answers.

**Primary key:** `ANSWER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique identifier for the answer record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GENERAL_COMMENT` | VARCHAR |  | A general comment for the entire questionnaire. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

