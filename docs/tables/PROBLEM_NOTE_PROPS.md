# PROBLEM_NOTE_PROPS

> Contains all related properties to assessment & plan notes which are stored in the PROBLEM_NOTES clarity extract.

**Primary key:** `PROBLEM_LIST_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GENERATED_NOTE_ID` | VARCHAR |  | This item stores the note the assessment & plan note has been generated into. If null then the corresponding assessment & plan note has not been generated into a note. |
| 4 | `AP_NOTE_SERVICE_C_NAME` | VARCHAR | org | This item stores the service for which the assessment and plan note was written. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

