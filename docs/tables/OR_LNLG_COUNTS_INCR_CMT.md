# OR_LNLG_COUNTS_INCR_CMT

> This table contains the free-text comment for why the count is incorrect.

**Primary key:** `COUNT_RESOLUTION_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COUNT_RESOLUTION_ID` | VARCHAR | PK | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COUNTS_INCORRECT_CMT` | VARCHAR |  | The reason comments on why the count was incorrect during the count resolution process. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

