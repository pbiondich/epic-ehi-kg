# DENTAL_PROC_ALTS_HX

> The history of procedure alternatives for a dental procedure.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated procedure alternative edit history in the dental procedure record. Together with FINDING_ID, this forms the foreign key to the DENTAL_PROCEDURE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the historical edits to procedure alternatives associated with the dental procedure from the DENTAL_PROCEDURE_HX table. |
| 4 | `DENT_ALT_HX_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

