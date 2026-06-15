# CL_QQUEST_OVTM

> The CL_QQUEST_OVTM table contains each contact for questionnaire questions.

**Primary key:** `QUEST_ID`, `CONTACT_DATE_REAL`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUEST_ID` | VARCHAR | PK FK→ | The unique ID of the question record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | The contact date in decimal format. |
| 3 | `QUESTION` | VARCHAR |  | The question that the user sees. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QUEST_ID` | [CL_QQUEST](CL_QQUEST.md) | sole_pk | high |

