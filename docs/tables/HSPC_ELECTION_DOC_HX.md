# HSPC_ELECTION_DOC_HX

> Table to store the audit trail of changes made to Election Addendum discussion that someone at the agency is supposed to have with a patient when they are electing for Hospice care.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHANGED_BY_USER_ID` | VARCHAR |  | User who is changing the documentation for election addendum discussion. |
| 4 | `CHANGED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CHANGE_INST_UTC_DTTM` | DATETIME (UTC) |  | Instant when change to election addendum discussion was recorded in the system (UTC). |
| 6 | `DISCUS_WITH_PAT_YN` | VARCHAR |  | Used to determine if the user changed the response to whether or not hospice coverage was discussed during hospice election. |
| 7 | `PAT_REQUESTED_YN` | VARCHAR |  | Used to determine if the user changed the response to whether or not patient requested coverage information during hospice election. |
| 8 | `DISCUS_WITH_USER_ID` | VARCHAR |  | Used to determine if the user changed who it was that discussed the Election Addendum with the patient during Hospice Election. |
| 9 | `DISCUS_WITH_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `DISCUSSION_DATE` | DATETIME |  | Used to determine if the user changed the response to when the Election Addendum was discussed with the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

