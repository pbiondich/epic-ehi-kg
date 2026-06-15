# NOTE_EDIT_TRAIL

> This table displays edit trail information for notes (HNO).

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IP_ACTION_DTTM` | DATETIME (Local) |  | Instant associated with a particular action taken on a note in local format. |
| 4 | `ACT_TAKEN_INST_DTTM` | DATETIME (UTC) |  | UTC formatted instant associated with a particular action taken on a note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

