# RES_REPEAT_COMP_SNOMED

> This table contains the SNOMED codes for component repeats as reported by the external resulting agency.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the specific repeat of a component on the result from the RES_REPEAT_COMP table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple SNOMED codes for this specific repeat of the component on the result. |
| 4 | `SNOMED_CODE` | VARCHAR |  | The SNOMED code associated with the value for the specific repeat of the component on this result as reported by the external resulting agency. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

