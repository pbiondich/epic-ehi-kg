# STMT_PB_SKIP_TX_LIST

> This table stores the list of skipped Professional Billing transactions for a given statement.

**Primary key:** `PRINT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRINT_ID` | NUMERIC | PK shared | The unique identifier for the statement print or detail bill record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_ID` | NUMERIC | shared | The skipped Professional Billing transaction ID. |
| 4 | `STMT_HOLD_RSN_C_NAME` | VARCHAR | org | The reason why the account was held in Professional Billing statement processing. |
| 5 | `STMT_HOLD_RSN_TEXT` | VARCHAR |  | The free text information related to the reason why the transaction was held in statement processing. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

