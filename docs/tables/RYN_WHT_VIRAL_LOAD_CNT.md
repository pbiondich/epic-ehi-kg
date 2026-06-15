# RYN_WHT_VIRAL_LOAD_CNT

> The viral load counts of the Ryan White patient.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RYN_WHT_VIRAL_LOAD_CNT` | INTEGER |  | All viral load counts for the patient during the reporting period. |
| 4 | `RYN_WHT_VIRAL_LOAD_DATE` | DATETIME |  | All viral load test dates for the patient during the reporting period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

