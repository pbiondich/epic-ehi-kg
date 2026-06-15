# DENTAL_PROC_HX_ADDL_TOOTH

> This table contains the history of the list of additional teeth associated with a dental procedure.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the procedure record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of one of the history lines in the procedure record. Together with FINDING_ID, this forms the foreign key to the DENTAL_PROCEDURE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple additional teeth associated with the procedure and the history line from the DENTAL_PROCEDURE_HX table. |
| 4 | `DENTAL_HX_ADDL_TOOTH_ID` | NUMERIC |  | The audit trail of the additional teeth documented for a procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

