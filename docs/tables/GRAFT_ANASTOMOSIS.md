# GRAFT_ANASTOMOSIS

> The anastomosis vessels and segments for a graft.

**Primary key:** `FINDING_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ANAS_VESSEL_ID` | NUMERIC |  | Stores the major vessels that the graft branch is attached to. |
| 4 | `ANAS_VESSEL_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 5 | `ANAS_SEGMENT_ID` | NUMERIC |  | Stores the vessel segments that the graft branch is attached to. |
| 6 | `ANAS_SEGMENT_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

