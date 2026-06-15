# HH_CPLN_ELEMENT

> This table no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). This table contains information about Home Health care plan problems (elements) entered on the Remote Client in the Care Plan task.

**Primary key:** `CAREPLAN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the CARE_INTG_ID column in the CARE_INTG_ELEM table to report on this item instead. Unique identifier for the care plan. |
| 2 | `LINE` | INTEGER | PK | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the LINE column in the CARE_INTG_ELEM table to report on this item instead. The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CP_ELEMNT_ID` | VARCHAR |  | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Use the PROBLEM_ID column in the CARE_INTG_ELEM table to report on this item instead. The unique identifier for the care plan problem. Links to table PROBLEM. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

