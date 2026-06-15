# OR_LNLG_PRE_SKCMTS

> This table stores the value of the Pre-op skin comments (I ORM 790) item. It is used to hold additional comments about the patient's pre-op skin condition.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PREOP_SKIN_CMTS` | VARCHAR |  | The comments for the pre-operative (pre-op) skin condition. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

