# NOTE_ATTACHED_IMG

> Stores the document IDs of images attached to the note from Canto.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the attached image associated with this note. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_IMG_DOC_ID` | VARCHAR |  | Stores the storage ID of images attached to the note from Canto. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

