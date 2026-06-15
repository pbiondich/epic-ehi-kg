# HH_EPSD_SURG_PROC

> This table contains user-entered surgical procedures information for Home Health episodes. This information is part of the Intake encounter for the Home Health episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SURG_PROC_ID` | VARCHAR |  | ID for the surgical procedure for the episode. Links to table CL_ICD_PX. |
| 4 | `SURG_PROC_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 5 | `SURG_PROC_CMT` | VARCHAR |  | Comment text for the procedure. |
| 6 | `SURG_PROC_DATE` | DATETIME |  | Surgical procedure approximate date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

