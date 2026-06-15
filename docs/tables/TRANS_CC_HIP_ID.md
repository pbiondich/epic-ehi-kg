# TRANS_CC_HIP_ID

> This table holds the list of Pool records that are CC'ed recipients on transcription messages for the associated note. The value is entered from the incoming interface or CC recipient field.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TRANS_CC_HIP_ID` | NUMERIC |  | This column holds the list of Pool records that are CC'ed recipients on transcription messages for the associated note. The value is entered from the incoming interface or CC recipient field. |
| 4 | `TRANS_CC_HIP_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

