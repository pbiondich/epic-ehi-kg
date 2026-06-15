# DENTAL_PROC_MODIFIERS_HX

> This table extracts the history of changes to a dental procedure's modifiers.

**Primary key:** `FINDING_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the finding record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated procedure modifier edit history in the dental procedure record. Together with FINDING_ID, this forms the foreign key to the DENTAL_PROCEDURE_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the procedure modifier histories associated with the dental procedure from the DENTAL_PROCEDURE_HX table. |
| 4 | `DENTAL_PROC_HX_MODIFIER_ID` | VARCHAR |  | This item contains the history of procedure modifiers associated with a dental procedure. These procedure modifiers allow users to add additional details to their dental procedures. |
| 5 | `DENTAL_PROC_HX_MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

