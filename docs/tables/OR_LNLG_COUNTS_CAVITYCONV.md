# OR_LNLG_COUNTS_CAVITYCONV

> This table contains information about the types of providers who participated in the conversation about all potential cavities that could harbor a retained item being searched.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COUNT_CAVITY_SEARCH_CONV_C_NAME` | VARCHAR | org | The category value for the types of providers who participated in the conversation that all potential cavities that could harbor a retained item were searched. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

