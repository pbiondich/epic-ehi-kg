# CHG_REVIEW_CVGS

> Stores all the coverages on the guarantor for this procedure. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the subject record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the charge in the charge session. Multiple charges can be associated with this charge session. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple coverages associated with the temporary transaction. |
| 4 | `OVRD_AUTH_CVG_ID` | NUMERIC |  | Lists the coverages on patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

