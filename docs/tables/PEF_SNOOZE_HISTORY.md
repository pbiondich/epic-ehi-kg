# PEF_SNOOZE_HISTORY

> This table contains extracts of audit information for alert snooze.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SNOOZE_SPR_HX_YN` | VARCHAR |  | Audit item for history of this flag |
| 4 | `SNOOZE_HX_SRC_C_NAME` | VARCHAR |  | This item stores the audit information for source of change in the snooze setting. |
| 5 | `SNOOZE_HX_USER_ID` | VARCHAR |  | This item stores the audit information about which user changed the snooze setting. |
| 6 | `SNOOZE_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `SNOOZE_HX_UTC_DTTM` | DATETIME (UTC) |  | This item stores audit information about the instant when the snooze setting was changed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

