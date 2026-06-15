# RYN_WHT_RECTAL_PAP_SMEAR

> Data for Ryan White Rectal Pap Smear screenings.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RW_REC_PAP_DATE` | DATETIME |  | The date of the Ryan White Rectal Pap Smear screening. |
| 4 | `RW_REC_PAP_RSLT_C_NAME` | VARCHAR |  | The result of the Ryan White Rectal Pap Smear screening. |
| 5 | `RW_REC_PAP_SCORE` | NUMERIC |  | The numerical score of the Ryan White Rectal Pap Smear screening. |
| 6 | `RW_REC_PAP_CMTS` | VARCHAR |  | The comments for the Ryan White Rectal Pap Smear screening. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

