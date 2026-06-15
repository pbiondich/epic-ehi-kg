# RYN_WHT_SMOKE_STATUS_SCRN

> Stores data for Ryan White CAREWare Smoking Status screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_SMOK_STATUS_DT` | DATETIME |  | The date on which the Smoking Status screening happened. |
| 4 | `RW_SMOK_STAT_RSLT_C_NAME` | VARCHAR |  | The result of the Smoking Status screening. |
| 5 | `RW_SMOK_STATUS_SCOR` | NUMERIC |  | The numerical score of the Smoking Status screening. |
| 6 | `RW_SMOK_STATUS_CMTS` | VARCHAR |  | Comments for the Smoking Status screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

