# DENT_PROC_HIST_ALT_BCB

> History for the alternate override type.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the procedure record. Together with FINDING_ID, this forms the foreign key to the DENTAL_PROC_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple procedure alternative types (like Basic Covered Benefit) associated with the procedure record and the historical instant from the DENTAL_PROC_HX table. |
| 4 | `DENT_ALT_EST_T_HX_C_NAME` | VARCHAR |  | History of values that indicate that a given procedure alternative should be included as a particular type for estimates, such as Basic Covered Benefit |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

