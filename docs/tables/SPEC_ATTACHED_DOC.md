# SPEC_ATTACHED_DOC

> A table to store information relating to documents attached to a specimen.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPEC_ATTCHD_DCS_ID` | VARCHAR |  | This item links to document records which are attached to the specimen. |
| 4 | `SPEC_ATTACHED_CMTS` | VARCHAR |  | This item stores comments associated with document records attached to the specimen. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

