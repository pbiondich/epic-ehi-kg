# OR_LNLG_SPEC_CMTS

> This table contains the Specimens comments for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the Line (ORM) record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPECIMEN_COMMENTS` | VARCHAR |  | Anesthesia complication comments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

