# TREATMENT_PLAN_NOTES

> The TREATMENT_PLAN_NOTES table contains the note text from Treatment Plan Notes (I TPL 50) as written in the properties window of a Treatment Plan. The text from Treatment Plan Notes is first converted to plain text. The formatting information in RTF note text or HTML note text is removed. The plain text is then broken up into lines of 4000 characters or fewer.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The record ID for the treatment plan. |
| 2 | `LINE` | INTEGER | PK | The line number for the note text associated with this treatment plan. The note text is first converted to plain text, then broken into lines of 4000 characters or fewer. Words and line breaks are not split across different lines. This column ("LINE") indicates the line number of the processed text. |
| 3 | `NOTES_TEXT` | VARCHAR |  | The text of the treatment plan note. The note text is first converted to plain text, then broken into lines of 4000 characters or fewer. Words and line breaks are not split across different lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

