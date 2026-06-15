# AGENDA_HX_REM_EMP_TOPICS

> History of edits to removed clinician topics.

**Primary key:** `AGENDA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AGENDA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit agenda record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EMP_IDENT` | INTEGER |  | Indicates the user involved with the given edit to the removed clinician topics on the agenda. |
| 4 | `AGENDA_CODEASSIST_C_NAME` | NUMERIC |  | Indicates the code/workflow involved with the given edit to the removed clinician topics on the agenda. |
| 5 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | Time as a UTC instant for the given edit to the removed clinician topics on the agenda. |
| 6 | `VAT_IDENT` | VARCHAR |  | State of the removed clinician topics on the agenda before the given edit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AGENDA_ID` | [AGENDA_INFO](AGENDA_INFO.md) | sole_pk | high |

