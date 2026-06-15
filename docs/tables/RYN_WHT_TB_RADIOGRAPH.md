# RYN_WHT_TB_RADIOGRAPH

> Data for Ryan White TB Chest Radiograph screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_TB_RADIOGRAPH_DT` | DATETIME |  | The date of the Ryan White TB Chest Radiograph screening. |
| 4 | `RW_TB_RG_RSLT_C_NAME` | VARCHAR |  | The result of the Ryan White TB Chest Radiograph screening. |
| 5 | `RW_TB_RG_SCORE` | NUMERIC |  | The numerical score for the Ryan White TB Chest Radiograph screening. |
| 6 | `RW_TB_RG_COMMENTS` | VARCHAR |  | The comments for the Ryan White TB Chest Radiograph screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

