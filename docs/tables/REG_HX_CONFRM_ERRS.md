# REG_HX_CONFRM_ERRS

> This table contains information related to confirmation errors that have occurred during registration encounters.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The internal ID of the note (HNO) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONFRM_ERR_PPT_ID` | NUMERIC |  | Stores the programming point (LPP) ID that caused an error. |
| 4 | `CONFRM_ERR_PPT_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

