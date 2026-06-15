# TRANSPLANT_LST_OTH

> This table includes a list of other transplant facilities where the patient has been waitlisted.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LISTED_ELSEWHERE_C_NAME` | VARCHAR | org | List of other facilities where the patient has been waitlisted. |
| 4 | `LISTED_ELSEWHERE_DT` | DATETIME |  | Dual listing date at other transplant facility. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

