# GUAR_PAT_BILLING_ACSS

> Information about billing accessors (authorized users) to a guarantor.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the account record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BILLING_ACSS_MYPT_ID` | VARCHAR |  | Stores MyChart accounts with billing access to the guarantor account, but which are not the same person as the guarantor. |
| 4 | `BILL_ACSS_REC_STMT_YN` | VARCHAR |  | Stores whether the MyChart account with billing access to the guarantor account should receive paper copy of statements |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

