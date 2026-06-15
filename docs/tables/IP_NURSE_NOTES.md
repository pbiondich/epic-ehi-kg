# IP_NURSE_NOTES

> This table displays information for nurse notes.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique identifier for the inpatient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NURSE_NOTE_TYPE_C_NAME` | VARCHAR |  | The type of the nurse note. |
| 4 | `NURSE_NOTE_STATUS_C_NAME` | VARCHAR |  | The status of the nurse note. |
| 5 | `NURSE_AUTHOR_ID` | VARCHAR |  | The ID of the nurse who authored the note. |
| 6 | `NURSE_AUTHOR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `NURSE_NOTE_INST_TM` | DATETIME (Local) |  | The time that the nurse note was saved. |
| 8 | `NURSE_NOTE_TEXT` | VARCHAR |  | The text of the nurse note. |
| 9 | `NURSE_NOTE_COPIED` | VARCHAR |  | Stores the nurse note copied to chart. |
| 10 | `SR_PRIORITY_C_NAME` | VARCHAR | org | The priority of the nurse note. |
| 11 | `NURSE_NOTE_RICH_TEXT` | VARCHAR |  | Stores the rich text of a nurse note created from the Sign Out Report or ED Comments activity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

