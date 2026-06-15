# FINDING_LOCATION

> The major vessels and segments of a finding.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FINDING_VESSEL_ID` | NUMERIC |  | Stores the major vessels of the finding. |
| 4 | `FINDING_VESSEL_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 5 | `FINDING_SEGMENT_ID` | NUMERIC |  | Stores the vessel segments of the finding. |
| 6 | `FINDING_SEGMENT_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 7 | `VESSEL_GRAFT_ID` | VARCHAR |  | Stores the specific graft, branch, and sequence if the major vessel is on a graft. |
| 8 | `VESSEL_BRANCH_ID` | INTEGER |  | Stores the lesion branch that the major vessel belongs to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

