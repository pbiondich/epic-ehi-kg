# DENTAL_PROC_HIST_FINDS

> This table extracts the procedure's addressed findings history.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the historical instant in the procedure record. Together with FINDING_ID, this forms the foreign key to the DENTAL_PROC_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple addressed findings associated with the procedure and the historical instant from the DENTAL_PROC_HX table |
| 4 | `DENT_FIND_HIST_ID` | NUMERIC |  | This column lists the history of dental findings that are addressed by this procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

