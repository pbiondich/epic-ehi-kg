# ARPB_TX_BND_EPSD_HX

> This is a table for episode link history on PB A/R Transactions (ETRs).

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_EPSD_INST_UTC_DTTM` | DATETIME (UTC) |  | This column indicates when the episode was linked to or unlinked from this service line. |
| 4 | `BND_EPSD_EPISODE_ID` | NUMERIC |  | This column defines which episode is being linked or unlinked on this line. |
| 5 | `BND_EPSD_ACTION_C_NAME` | VARCHAR |  | This column defines whether this history line is linking or unlinking the related episode. |
| 6 | `BND_EPSD_SRC_C_NAME` | VARCHAR |  | This column indicates how the link or unlink of the related episode was performed, either by a user, by the system, or by configured automation. |
| 7 | `BND_EPSD_USER_ID` | VARCHAR |  | This column indicates the user who linked or unlinked the episode. |
| 8 | `BND_EPSD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

