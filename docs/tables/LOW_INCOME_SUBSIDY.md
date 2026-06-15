# LOW_INCOME_SUBSIDY

> Medicare Part D Low Income Subsidy (LIS) eligibility information.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IS_DEEMED_LIS_YN` | VARCHAR |  | Whether the patient was deemed Low Income Subsidy (LIS). Patients who qualify for LIS receive financial support for Medicare Part D related expenses, such as reduced medication copays. |
| 4 | `LIS_COPAY_LEVEL_C_NAME` | VARCHAR | org | Copayment Level for Part D Low Income Subsidy (LIS). Determines how much patients in Medicare Part D plans pay for their medication copays. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

