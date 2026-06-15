# LOW_INCOME_SUBSIDY_HX

> Historical Medicare Part D Low Income Subsidy (LIS) eligibility information.

**Primary key:** `REGISTRY_DATA_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `HX_IS_DEEMED_LIS_YN` | VARCHAR |  | Historical value for whether the patient was deemed Low Income Subsidy (LIS). Patients who qualify for LIS receive financial support for Medicare Part D related expenses, such as reduced medication copays. |
| 5 | `HX_LIS_COPAY_LEVEL_C_NAME` | VARCHAR | org | Historical Copayment Level for Part D Low Income Subsidy (LIS). Determines how much patients in Medicare Part D plans pay for their medication copays. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

