# TPL_LAST_VERIFY_HX

> The verification history of a treatment plan.

**Primary key:** `TREATMENT_PLAN_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TREATMENT_PLAN_ID` | NUMERIC | PK shared | The treatment plan ID. |
| 2 | `LINE` | INTEGER | PK | The line number that corresponds to each verification of the treatment plan in this row. |
| 3 | `PLAN_VER_DT_HX_TM` | DATETIME (Local) |  | The date/time in external format of a verification of the treatment plan in this row. |
| 4 | `PLAN_VERUSER_HX_ID` | VARCHAR |  | The user ID of the person who performed a verification of the treatment plan in this row. |
| 5 | `PLAN_VERUSER_HX_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

