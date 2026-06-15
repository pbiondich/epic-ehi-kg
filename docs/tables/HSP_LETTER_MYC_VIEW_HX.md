# HSP_LETTER_MYC_VIEW_HX

> This table stores the history of when billing letters were viewed in MyChart.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `VIEW_DTTM` | DATETIME (UTC) |  | Stores the date and time the letter was viewed in MyChart. |
| 4 | `MYPT_ID` | VARCHAR | shared | Stores the MyChart account ID that viewed the letter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

