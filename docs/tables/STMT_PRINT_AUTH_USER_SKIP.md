# STMT_PRINT_AUTH_USER_SKIP

> Contains information about the reasons why the authorized user statement copy was not generated for a MyChart user account, despite the request for a physical copy by an authorized user.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the stmt/det bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `AUTH_BILL_USER_MYPT_ID` | VARCHAR |  | Stores the authorized users who were not sent a statement copy. |
| 4 | `AUTH_USER_STMT_ERROR_C_NAME` | VARCHAR | org | Stores the reason why the authorized user copy was not sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

