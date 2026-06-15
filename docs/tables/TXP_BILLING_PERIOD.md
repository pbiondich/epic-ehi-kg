# TXP_BILLING_PERIOD

> Transplant billing period information. This is also used to represent Tapestry billing phase information.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | This column stores the unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_BILLING_C_NAME` | VARCHAR | org | Transplant billing period. |
| 4 | `TX_BILLING_START_DT` | DATETIME |  | Transplant billing period start date. |
| 5 | `TX_BILLING_END_DT` | DATETIME |  | Transplant billing period end date. |
| 6 | `PHASE_TAP_PAID_AMT` | NUMERIC |  | The total amount paid by your organization so far for this phase. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

