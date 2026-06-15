# OR_LNLG_COUNTS_NUM_SPONGE

> The OR_LNLG_COUNTS_NUM_SPONGE table contains information about whether the number of sponges was confirmed.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COUNT_NUM_SPONGES_USED_C_NAME` | VARCHAR | org | The category value for whether the numbers of sponges were confirmed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

