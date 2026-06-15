# DENT_TOOTH

> This table contains tooth information for a single dental treatment plan procedure line. This data is coming from the Dental - Tooth Numbers - Teeth Number (I DTP 127) item.

**Primary key:** `TREATMENT_PLAN_ID`, `PROC_LINE`, `TOOTH_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | VARCHAR | PK shared | The unique identifier for the treatment plan record. |
| 2 | `PROC_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `TOOTH_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `TOOTH_NUM_C_NAME` | VARCHAR |  | The tooth number category ID for the dental billing plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

