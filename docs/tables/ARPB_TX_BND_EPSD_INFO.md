# ARPB_TX_BND_EPSD_INFO

> A table of currently linked episodes for the A/R Transactions (ETR). It also contains a line key for where in the history group this link came from.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_EPSD_EPISODE_ID` | NUMERIC |  | The current linked bundled episode ID for the transaction record. |
| 4 | `BND_EPSD_HX_LINE` | INTEGER |  | The line in the history related group corresponding to this link |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

