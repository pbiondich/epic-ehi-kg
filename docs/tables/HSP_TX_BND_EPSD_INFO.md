# HSP_TX_BND_EPSD_INFO

> This table contains bundled episodes that were linked to a transaction when the transaction was filed.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_EPSD_EPISODE_ID` | NUMERIC |  | The list of currently linked bundled episodes associated with this transaction. |
| 4 | `BND_EPSD_HX_LINE` | INTEGER |  | The history line that corresponds to the linked action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

