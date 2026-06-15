# TXP_DNR_CRIT

> Donor criteria information for transplant episodes.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TXP_DNR_CRIT_KEY_C_NAME` | VARCHAR | org | Contains the custom donor criteria data key |
| 4 | `TXP_DNR_CRIT_VALUE_YN` | VARCHAR |  | Contains the custom donor criteria data |
| 5 | `TXP_DNR_CRIT_REASON` | VARCHAR |  | Contains the reason for the custom donor criteria data |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

