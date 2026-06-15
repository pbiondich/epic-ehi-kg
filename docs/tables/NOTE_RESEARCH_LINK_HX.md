# NOTE_RESEARCH_LINK_HX

> This table contains information about how the research study linkage on a note has changed over time.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 4 | `HX_ENROLL_ID` | NUMERIC |  | History of the linked study association for the note. |
| 5 | `HX_STUDY_LINK_UTC_DTTM` | DATETIME (UTC) |  | History of when the research link of the note was modified. |
| 6 | `HX_STUDY_USER_ID` | VARCHAR |  | History of the user who modified the research link of a note. |
| 7 | `HX_STUDY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

