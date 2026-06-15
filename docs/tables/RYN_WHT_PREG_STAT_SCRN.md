# RYN_WHT_PREG_STAT_SCRN

> Stores data for Ryan White CAREWare Pregnancy Status screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_PREG_STATUS_DATE` | DATETIME |  | The date on which the Pregnancy Status screening took place. |
| 4 | `RW_PREG_STAT_RSLT_C_NAME` | VARCHAR |  | The result of the Pregnancy Status screening. |
| 5 | `RW_PREG_STAT_SCORE` | NUMERIC |  | The numerical score for the Pregnancy Status screening. |
| 6 | `RW_PREG_STAT_CMTS` | VARCHAR |  | The comments for the Pregnancy Status screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

