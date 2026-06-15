# CODING_CLA_NOTES_SUGG

> This table extracts the suggested diagnosis code and the text description of the diagnosis suggestion for a query.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SUGGESTION_PRIM_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `SUGGESTION_ALT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 5 | `SUGGESTION_NAME` | VARCHAR |  | The display name of the suggested diagnosis code of the query. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

