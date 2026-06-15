# ACCT_PP_BSP_LIST_REPL

> The scheduled payment records associated with a payment plan history line on the guarantor record. The payment plan scheduled payment information in this table only applies to Hospital Billing and Single Billing Office payment plans. To find information about the payment plan, including the terms, users, and source, use the HSP_GUAR_PMT_PLAN table. This houses the history and information about all of the guarantor's HB/SBO payment plans.

**Primary key:** `ACCT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the guarantor record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `HB_PP_SCHED_PMT_ID` | NUMERIC |  | Payment plan payment schedule list. This list of scheduled payments only applies to Hospital Billing and Single Billing Office payment plans. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

