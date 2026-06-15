# CL_RMT_CLM_NOTES

> This table stores the special Notes (NTE) segments from the remittance image.

**Primary key:** `IMAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | Unique identifier for the remittance image record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NOTE_REF_CODE` | VARCHAR |  | This item stores the note reference code |
| 4 | `NOTE_DESCRIPTION` | VARCHAR |  | This is a free text description of the note |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

