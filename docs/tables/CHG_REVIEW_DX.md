# CHG_REVIEW_DX

> This table contains one row for each diagnosis entered on a temporary accounts receivable (TAR) record that is or has been in a charge review workqueue. This is not the diagnosis associated with individual procedures (I TAR 200), but rather the diagnosis entered on the TAR record as a whole as the Charge Diagnosis (I TAR 130). This table contains basic information about the diagnosis (Dx_ID and ICD9 Code). Note: TAR records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique ID of a TAR record. This represents an individual charge session. |
| 2 | `LINE` | INTEGER | PK | The line count for the item. This represents a single diagnosis on the temporary transaction record. |
| 3 | `DX_QUAL_C_NAME` | VARCHAR | org | The diagnosis qualifier category ID for the temporary transaction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

