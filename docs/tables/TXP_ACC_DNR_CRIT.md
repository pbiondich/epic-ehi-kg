# TXP_ACC_DNR_CRIT

> Table containing acceptable donor criteria information for the transplant episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACC_DNR_CRIT_C_NAME` | VARCHAR | org | List of acceptable donor criteria. |
| 4 | `ACC_CRIT_CMT` | VARCHAR |  | Comments related to an acceptable donor criterion. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

