# DENTAL_PROC_ALTS

> This table contains dental alternate procedure choices for a procedure.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DENT_ALT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `DENT_ALT_DFLT_EST_YN` | VARCHAR |  | Indicates that a given procedure alternative should be included on an estimate by default |
| 5 | `DENT_ALT_EST_TYPE_C_NAME` | VARCHAR |  | Indicates that a given procedure alternative should be included as a particular type for estimates, such as Basic Covered Benefit. These categories are also used by the Estimates activity for non-Substatus values. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

