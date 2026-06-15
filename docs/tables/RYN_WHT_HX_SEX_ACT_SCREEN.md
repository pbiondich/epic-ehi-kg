# RYN_WHT_HX_SEX_ACT_SCREEN

> Stores data for Ryan White CAREWare History of Sexual Activity screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_SEX_ACT_DT` | DATETIME |  | The date of the History of Sexual Activity (Adolescent) screening. |
| 4 | `RW_SEX_ACT_RESULT_YN` | VARCHAR |  | The result of the History of Sexual Activity (Adolescent) screening. |
| 5 | `RW_SEX_ACT_SCORE` | NUMERIC |  | The numerical score of the History of Sexual Activity (Adolescent) screening. |
| 6 | `RW_SEX_ACT_COMMENTS` | VARCHAR |  | The comments for the History of Sexual Activity (Adolescent) screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

