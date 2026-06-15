# RYN_WHT_PELVIC_EXAM

> Data for Ryan White Pelvic Exam screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_PELVIC_EXAM_DATE` | DATETIME |  | The date of the Ryan White Pelvic Exam screening. |
| 4 | `RW_PELV_EXAM_RSLT_C_NAME` | VARCHAR |  | The result of the Ryan White Pelvic Exam screening. |
| 5 | `RW_PELV_EXAM_SCORE` | NUMERIC |  | The numerical score of the Ryan White Pelvic Exam screening. |
| 6 | `RW_PELVIC_EXAM_CMTS` | VARCHAR |  | The comments for the Ryan White Pelvic Exam screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

