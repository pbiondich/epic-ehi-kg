# OR_CASE_QUEST_AN_P

> The OR_CASE_QUEST_AN_P table contains OR management system case procedure questionnaire answers.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The line number of the procedure answer. |
| 3 | `PROC_ID` | VARCHAR | FK→ | The unique ID of the procedure record for which there is an answer. |
| 4 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |
| `PROC_ID` | [CLARITY_EAP](CLARITY_EAP.md) | sole_pk | high |

