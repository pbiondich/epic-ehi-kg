# AP_CLAIM_PX_BND_EPSD_INFO

> Stores the bundled episodes linked to AP claim service lines. AP claim service lines are also referred to as transactions.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_EPSD_EPISODE_ID` | NUMERIC |  | Stores the unique identifier of a bundled episode linked to the service line. |
| 4 | `BND_EPSD_HX_LINE` | INTEGER |  | Stores the line in the service line's bundled payment history (see Clarity table AP_CLAIM_PX_BNDL_EPSD_HX) that this bundled episode corresponds to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

