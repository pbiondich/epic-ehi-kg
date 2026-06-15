# RES_MICRO_STAIN

> The RES_MICRO_STAIN table contains data for microbiology stain results.

**Primary key:** `RESULT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique ID of the result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MIC_STAIN_QTY_C_NAME` | VARCHAR | org | The stain quantity category number for the microbiology stain. |
| 4 | `MIC_STAIN_DSCR_C_NAME` | VARCHAR | org | The stain description category number for the microbiology stain. |
| 5 | `STAIN_ABNORMAL_C_NAME` | VARCHAR | org | The category value of the abnormal level assigned to this stain. |
| 6 | `STAIN_RES_VAL_STATUS_C_NAME` | VARCHAR |  | The stain verification status category ID for each stain on the result that has been reported. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

