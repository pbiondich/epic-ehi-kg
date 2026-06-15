# OR_LNLG_POST_SKCMT

> This table holds the value of the Post-op skin comments (I ORM 890) item. It is used to hold additional comments about the patient's post-op skin condition.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `POSTOP_SKIN_CMTS` | VARCHAR |  | The post-operative (post-op) skin condition comments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

