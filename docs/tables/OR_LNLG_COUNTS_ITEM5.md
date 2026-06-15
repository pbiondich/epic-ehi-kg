# OR_LNLG_COUNTS_ITEM5

> Stores counts details for the fifth item counted.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique identifier for the line record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COUNTS_ITEM5_COUNT` | INTEGER |  | Used to document an individual count for the item being counted. |
| 4 | `COUNTS_ITEM5_RUNNING_TOTAL` | INTEGER |  | The running total of this type of item for the current line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

