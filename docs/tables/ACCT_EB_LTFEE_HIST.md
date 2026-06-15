# ACCT_EB_LTFEE_HIST

> This table holds the late fee history for a guarantor account.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LTF_HIST_APPLIED_D` | DATETIME |  | This item stores the date upon which the late fee was processed for this guarantor. Each line in the related group is one instance of late fees being applied. |
| 4 | `LTF_HIST_PB_AMT` | NUMERIC |  | Amount assessed for Professional Billing transactions for late fees |
| 5 | `LTF_HIST_HB_AMT` | NUMERIC |  | The amount assessed for all hospital accounts for this particular late fee processing run. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

