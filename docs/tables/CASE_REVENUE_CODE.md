# CASE_REVENUE_CODE

> The CASE_REVENUE_CODE table allows you to report on the revenue code(s) associated with your case records.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | NUMERIC | PK shared | The unique identifier for the case record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REVENUE_CODE_ID` | NUMERIC |  | Stores the revenue code(s) associated with your case records. Networked to UB revenue codes (UBC). |
| 4 | `REVENUE_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

