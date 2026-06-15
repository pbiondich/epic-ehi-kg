# CLARITY_DEP_4

> This table extends CLARITY_DEP, which contains high-level information about departments from the Department master file.

**Overflow of:** [CLARITY_DEP](CLARITY_DEP.md)  
**Primary key:** `DEPARTMENT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 2 | `MED_REC_STYLE_C_NAME` | VARCHAR |  | The medication reconciliation style category ID for the department. |
| 3 | `DEP_TYPE_C_NAME` | VARCHAR |  | The type of the department. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

