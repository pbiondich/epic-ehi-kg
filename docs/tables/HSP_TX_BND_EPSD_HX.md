# HSP_TX_BND_EPSD_HX

> This table holds the history of bundled episodes linked to and unlinked from this transaction.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the hospital billing transaction. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_EPSD_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant that an episode was linked or unlinked to this transaction. |
| 4 | `BND_EPSD_EPISODE_ID` | NUMERIC |  | The episode that this transaction was linked or unlinked to. |
| 5 | `BND_EPSD_ACTION_C_NAME` | VARCHAR |  | The action that occurred with this episode on this transaction. |
| 6 | `BND_EPSD_SRC_C_NAME` | VARCHAR |  | The source of the episode link or unlink. |
| 7 | `BND_EPSD_USER_ID` | VARCHAR |  | The user who linked or unlinked the episode from the transaction. |
| 8 | `BND_EPSD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

