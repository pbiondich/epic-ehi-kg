# GUAR_WRITTEN_LANG

> Stores information about the Guarantor's Written Language.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID for the guarantor account. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `GUAR_WRITTEN_LANG_C_NAME` | VARCHAR | org | Category number for the guarantor's written language. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

