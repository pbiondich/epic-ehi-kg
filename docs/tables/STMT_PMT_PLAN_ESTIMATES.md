# STMT_PMT_PLAN_ESTIMATES

> Contains the pre-service estimates on payment plan that were included in the statement.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the statement or detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ESTIMATE_ID` | NUMERIC | shared | The unique ID of the pre-service estimate on the payment plan that generated this statement. |
| 4 | `INITIAL_ESTIMATED_BAL` | NUMERIC |  | The initial balance of the pre-service estimate on the payment plan. |
| 5 | `TOT_PAT_PMT_AMT` | NUMERIC |  | The total patient payments towards the pre-service estimate on the payment plan. |
| 6 | `TOT_PAT_ADJ_AMT` | NUMERIC |  | The total patient adjustments towards the pre-service estimate on the payment plan. |
| 7 | `REMAINING_ESTIMATED_BAL` | NUMERIC |  | The remaining balance of the pre-service estimate on the payment plan. |
| 8 | `PREVIOUS_ESTIMATED_BAL` | NUMERIC |  | The remaining balance from the previous statement for the pre-service estimate on the payment plan. |
| 9 | `NEW_PAT_PMT_AMT` | NUMERIC |  | The new patient payments towards the pre-service estimate on the payment plan. |
| 10 | `NEW_PAT_ADJ_AMT` | NUMERIC |  | The new patient adjustments towards the pre-service estimate on the payment plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

