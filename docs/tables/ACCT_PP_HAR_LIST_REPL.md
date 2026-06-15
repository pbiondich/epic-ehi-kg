# ACCT_PP_HAR_LIST_REPL

> The hospital account ID lists that are associated with payment plans attached to guarantor accounts.

**Primary key:** `ACCT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the guarantor record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated payment plan in this guarantor account's record. Together with ACCT_ID, this forms the foreign key to the HSP_GUAR_PMT_PLAN table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple hospital account IDs that are associated with the guarantor account and the payment plan from the HSP_GUAR_PMT_PLAN table. |
| 4 | `HB_PP_HAR` | NUMERIC |  | This column stores the unique identifier for the hospital account that is associated with this guarantor account and payment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

