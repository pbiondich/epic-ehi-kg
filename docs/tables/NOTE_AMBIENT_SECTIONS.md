# NOTE_AMBIENT_SECTIONS

> Stores ambient note section information.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AMBIENT_SESSION_SECTION_IDENT` | VARCHAR |  | Stores the Ambient Note Section ID that was updated by the user. Points to I DXR 41500. |
| 4 | `AMBIENT_SESSION_IDENT` | VARCHAR |  | Stores the Ambient Session ID that this HNO pulled in note section data from. Points to DXR. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

