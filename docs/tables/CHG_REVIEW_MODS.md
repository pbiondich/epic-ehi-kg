# CHG_REVIEW_MODS

> This table contains multiple response information for modifiers associated with temporary accounts receivable (TAR) transaction procedure lines. This table contains one row for each modifier entered on a TAR line for each TAR that has been in a charge review workqueue. Note: TAR records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `LINE_COUNT`, `MOD_LINE_COUNT`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique ID of the temporary transaction record. This represents an individual charge session. |
| 2 | `LINE_COUNT` | INTEGER | PK | The line number of the charge in the charge session. Multiple charges can be associated with this charge session. |
| 3 | `MOD_LINE_COUNT` | INTEGER | PK | The line number of the modifier on the charge. Multiple modifiers can be associated with each charge in the charge session. |
| 4 | `EXT_MODIFIER` | VARCHAR |  | The external ID of the modifier record. |
| 5 | `INT_MODIFIER_ID` | VARCHAR |  | The unique ID of the modifier of the charge. This column is frequently used to link to the CLARITY_MOD table. |
| 6 | `INT_MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

