# STMT_PRINT_HAR_SKIP

> Contains information about the reasons why the hospital account was skipped from the statement.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the stmt/det bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STMT_SKIP_HSP_ACCOUNT_ID` | NUMERIC |  | Stores the hospital account that was skipped from the statement sent to the guarantor. |
| 4 | `STMT_SKIP_RSN_C_NAME` | VARCHAR | org | Stores the reason why the hospital account was not sent on the statement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

