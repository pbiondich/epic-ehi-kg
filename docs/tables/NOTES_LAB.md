# NOTES_LAB

> Contains lab-specific information about notes. Only notes associated with labs, which are notes (HNOs) with a Note Type (I HNO 50) value of 81-Lab, are included.

**Primary key:** `NOTE_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique ID of the note record. |
| 2 | `LAB_NOTE_SUB_TYPE_C_NAME` | VARCHAR |  | The Lab type for this note. Only Lab notes have a value populated for this item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

