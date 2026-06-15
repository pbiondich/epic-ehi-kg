# DENT_PROC_HX_ALT_EST_DFLT

> This table returns history data regarding whether or not a procedure's alternate choices would be defaulted onto an estimate.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the procedure record. Together with FINDING_ID, this forms the foreign key to the DENTAL_PROC_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple Yes/No values, representing whether procedure alternatives default on an estimate, associated with the procedure record and the historical instant from the DENTAL_PROC_HX table. |
| 4 | `DENT_ALT_DFLT_HX_YN` | VARCHAR |  | History of values that indicate whether or not a given procedure alternative should be included on an estimate by default |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

