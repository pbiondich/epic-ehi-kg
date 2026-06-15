# GUAR_EMPR_ADDRESS

> The GUAR_EMPR_ADDRESS table contains information about the address of the guarantor's employer.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of the guarantor account for this row. This column is frequently used to link to the ACCOUNT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GUAR_EMPR_ADDRESS` | VARCHAR |  | The address of the guarantor's employer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

