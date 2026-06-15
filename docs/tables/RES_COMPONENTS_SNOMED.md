# RES_COMPONENTS_SNOMED

> This table stores the SNOMED code for the component value or antibiotic received from the external system.

**Primary key:** `RESULT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RESULT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the result record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the result component in the result. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple SNOMED codes associated with the result and result component from the RES_COMPONENTS table. |
| 4 | `SNOMED_CODE` | VARCHAR |  | The SNOMED code for the component value or antibiotic received from an external system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

