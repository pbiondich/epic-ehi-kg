# DOCS_FOR_HOSP_ACCT

> This table links the hospital account to the document (DCS) records relevant to the encounters associated with the hospital account.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of the hospital account (HAR) record for this row. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINKED_DCS_ID` | VARCHAR |  | Document (DCS) record ID of the document(s) attached to the hospital account. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

