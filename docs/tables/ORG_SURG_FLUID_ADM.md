# ORG_SURG_FLUID_ADM

> Fluid administered type and amount.

**Primary key:** `ORG_RECORD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORG_RECORD_ID` | NUMERIC | PK shared | The unique identifier for the organ record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FLUID_ADMIN_C_NAME` | VARCHAR | org | Indicates the types of fluids administered during the transplant. |
| 4 | `FLUID_ADMIN_NUM` | NUMERIC |  | Indicates the amount of the corresponding type of fluid administered during the transplant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

