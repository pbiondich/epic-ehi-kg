# PRE_AR_ORG_DX

> This table contains the original diagnosis information of the transaction. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the temporary transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORG_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `ORG_DX_QUAL_C_NAME` | VARCHAR | org | The qualifier category ID for the current diagnosis in a charge review session. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

