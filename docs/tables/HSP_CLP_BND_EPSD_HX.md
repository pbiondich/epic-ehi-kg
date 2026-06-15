# HSP_CLP_BND_EPSD_HX

> Holds a history of bundled episodes linked to or unlinked from the claim; also includes line-level link information.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | This column stores the unique identifier for the claim print record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BND_EPSD_INST_UTC_DTTM` | DATETIME (UTC) |  | Instant that this episode was linked/unlinked. |
| 4 | `BND_EPSD_EPISODE_ID` | NUMERIC |  | Bundled episode record associated with this history line. |
| 5 | `BND_EPSD_ACTION_C_NAME` | VARCHAR |  | The action performed on the corresponding episode (link/unlink). |
| 6 | `BND_EPSD_SRC_C_NAME` | VARCHAR |  | The source of the action performed on this claim to the related bundled episode (user/system/automation). |
| 7 | `BND_EPSD_USER_ID` | VARCHAR |  | This column stores the unique identifier for the user who performed the corresponding action on the related episode. |
| 8 | `BND_EPSD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `BND_EPSD_LINKED_INCL_CLM_LNS` | VARCHAR |  | Holds a comma-delimited string of claim lines linked to the related episode if only part of the claim should be linked and if the number of lines to link is <= 50% of the claim line count. |
| 10 | `BND_EPSD_LINKED_EXCL_CLM_LNS` | VARCHAR |  | Holds a comma-delimited string of claim lines excluded from the related episode if only part of the claim should be linked and if the number of lines to link is > 50% of the claim line count. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

