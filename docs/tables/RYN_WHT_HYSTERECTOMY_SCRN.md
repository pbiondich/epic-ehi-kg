# RYN_WHT_HYSTERECTOMY_SCRN

> Stores data for Ryan White CAREWare Hysterectomy screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_HYSTER_DATE` | DATETIME |  | Date of the Hysterectomy (non-dysplasia/non-malignant indic.) screening. |
| 4 | `RW_HYST_RSLT_YN` | VARCHAR |  | Result of the Hysterectomy screening. |
| 5 | `RW_HYST_SCORE` | NUMERIC |  | The numerical score of the Hysterectomy screening. |
| 6 | `RW_HYSTERECTOMY_CMT` | VARCHAR |  | The comments for the Hysterectomy screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

