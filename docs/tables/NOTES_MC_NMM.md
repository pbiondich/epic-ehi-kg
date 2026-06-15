# NOTES_MC_NMM

> This table contains the information about notes (HNO) records attached to case (NMM) records.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique internal id of the case record. |
| 2 | `LINE` | INTEGER | PK | The line number of the note attached to the case. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique ID of the note record attached to the case. |
| 4 | `NOTE_DATE` | DATETIME |  | The date when the note was created. |
| 5 | `NOTE_TIME` | DATETIME (Local) |  | The time the note was created. |
| 6 | `NOTE_USER_ID` | VARCHAR |  | The unique ID of the user who created the note. |
| 7 | `NOTE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

