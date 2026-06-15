# REIMB_CALC_HX

> This table contains a line for each reimbursement calculation related to a transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | Unique ID of the transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AMOUNT` | NUMERIC |  | Dollar amount of the calculated reimbursement. This value is the amount we expect to be reimbursed and cannot exceed the charge amount. |
| 4 | `USER_ID` | VARCHAR | FK→ | User ID of the person who performed the reimbursement calculation. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CALC_MODULE_C_NAME` | VARCHAR |  | Module that triggered this reimbursement calculation. The possible values for this column are: 1) CLAIMS: Claims Processing 2) CHG ENTRY: Charge Entry 3) ACCT MAINT: Account Maintenance 4) PMT POST: Payment Posting 5) RECALC UTIL: Reimbursement Recalculation Utility |
| 7 | `CALC_DATE` | DATETIME |  | Date of the reimbursement calculation. |
| 8 | `CALC_TIME` | DATETIME (Local) |  | Date and time of the reimbursement calculation. |
| 9 | `CONTRACT_AMOUNT` | NUMERIC |  | Stores the allowed amount as calculated by the reimbursement contract. This amount can exceed the charge amount. |
| 10 | `REIMB_SOURCE_C_NAME` | VARCHAR |  | Stores how the reimbursement amount was calculated for the charge. |
| 11 | `COVERAGE_ID` | NUMERIC | FK→ | This column stores the coverage used to compute reimbursement. |
| 12 | `REIMB_COVERAGE_ID` | NUMERIC |  | This item is part of the reimbursement history group. It stores the coverage used to compute reimbursement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

