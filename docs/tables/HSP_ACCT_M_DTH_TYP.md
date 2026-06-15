# HSP_ACCT_M_DTH_TYP

> This table contains death type abstracting information from the hospital account. It is possible for multiple death types to be abstracted on a single account.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital account with associated death-type information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Because multiple death types can apply to a patient and be stored in one hospital account, each abstracted death type will have a unique line number. |
| 3 | `DEATH_TYPE_C_NAME` | VARCHAR | org | This abstracting item indicates the death type that is associated with a particular account and line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

