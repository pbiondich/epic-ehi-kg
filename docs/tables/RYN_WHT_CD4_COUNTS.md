# RYN_WHT_CD4_COUNTS

> This table contains the CD4 counts for the Ryan White patients.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RYN_WHT_CD4_TEST_CNT` | INTEGER |  | All CD4 test counts for the patient during the reporting period. |
| 4 | `RYN_WHT_CD4_SVC_DATE` | DATETIME |  | All CD4 test dates for the patient during the reporting period. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

