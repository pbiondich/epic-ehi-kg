# OR_CASE_PAT_RPT_ANTICOAG

> This table contains data about patient-reported anti-coagulants.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_RPTD_ANTICOAG_TYPE_C_NAME` | VARCHAR | org | This item stores patient-reported anti-coagulants. |
| 4 | `ANTICOAG_STATUS_C_NAME` | VARCHAR | org | Status of patient reported anti-coagulant. |
| 5 | `ANTICOAG_NUM_DAYS_BEF_TO_STOP` | NUMERIC |  | The number of days before surgery the patient should stop taking the anti-coagulant. |
| 6 | `ANTICOAG_CMT` | VARCHAR |  | This item stores comments about the patient-reported anti-coagulants. |
| 7 | `ANTICOAG_PLAN_C_NAME` | VARCHAR | org | This column stores the plan for each anti-coagulant before surgery. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

