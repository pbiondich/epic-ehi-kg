# ACCT_EB_STMT_RSN

> Table for Enterprise Statement Processing Hold Reasons.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of the guarantor account record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EB_STMT_ERROR_C_NAME` | VARCHAR | org | Stores the current list of enterprise statement processing hold reasons at the guarantor level. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

