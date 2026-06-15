# HH_CPLN_RFL_INSTRC

> This table no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). This table contains Home Health care plan referral instructions. This information comes from the initial physician orders.

**Primary key:** `CAREPLAN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CAREPLAN_ID` | VARCHAR | PK shared | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Unique identifier for the care plan. |
| 2 | `LINE` | INTEGER | PK | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RFL_INSTRUCTIONS` | VARCHAR |  | This column no longer populates data for new HH/HSPC care plans as of the Epic November 2022 release (10.3). Care plan referral instructions text. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

