# BMT_DONOR_LINK_AUDIT

> This table stores audit of linking and unlinking of donor episodes from the recipient episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DONOR_EPISODE_ID` | NUMERIC |  | The donor episode that was linked to or unlinked from the recipient episode. |
| 4 | `BMT_DONOR_LINK_ACTION_C_NAME` | VARCHAR |  | Specifies whether the donor episode was linked to or unlinked from the recipient episode. |
| 5 | `ACTION_USER_ID` | VARCHAR |  | The user that performed the action. |
| 6 | `ACTION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ACTION_INSTANT_DTTM` | DATETIME (UTC) |  | The instant of the change associated with the action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

