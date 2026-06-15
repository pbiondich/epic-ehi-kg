# HSP_ACCT_ABSTS_HX

> Stores the history of changes to the abstract status.

**Primary key:** `HSP_ACCT_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HSP_ACCT_ID` | NUMERIC | PK | The hospital account ID with related abstracting status history information. |
| 2 | `LINE` | INTEGER | PK | The line number in the results of a query. Each coding history will have its own line number. |
| 3 | `ABSTS_HX_STS_C_NAME` | VARCHAR | org | The abstract status category ID. |
| 4 | `ABSTS_HX_UTC_DTTM` | DATETIME (UTC) |  | This column stores the abstracting status changed instant in Coordinated Universal Time (UTC). Data will not exist in this column for abstracting statuses created before UTC instant tracking was enabled for abstracting history. |
| 5 | `ABSTS_HX_ASGN_USER_ID` | VARCHAR |  | Item to store abstracting assigned user changes |
| 6 | `ABSTS_HX_ASGN_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

