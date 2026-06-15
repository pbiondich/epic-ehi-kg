# NOTE_COPY_TRACKING

> Track the source note information that this note was copied from.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_COPY_INST_DTTM` | DATETIME (UTC) |  | The instant (UTC) when this note was copied. |
| 4 | `NOTE_COPY_LOC_DTTM` | DATETIME (Local) |  | The instant when this note was copied. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

