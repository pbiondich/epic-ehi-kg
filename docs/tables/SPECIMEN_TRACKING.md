# SPECIMEN_TRACKING

> Contains the post resulted tracking information about specimens.

**Primary key:** `SPECIMEN_RECORD_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_RECORD_ID` | NUMERIC | PK | The unique identifier for the finding record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TRACKING_STATUS_C_NAME` | VARCHAR | org | Contains the current status for tracking a specimen after it's been resulted. |
| 4 | `TRACKING_COMP_C_NAME` | VARCHAR |  | Stores whether this specimen is considered complete with respect to tracking after the specimen is resulted. |
| 5 | `POST_RESULT_DX_C_NAME` | VARCHAR | org | Contains the diagnosis used for tracking purposes after the specimen has been resulted. Not to be used as a clinical diagnosis. |
| 6 | `TRACKING_DESC_ID` | VARCHAR |  | Contains the a summary/comment about the specimen tracking done after the specimen has been resulted. |
| 7 | `TRACK_ORD_ID` | NUMERIC |  | The order that the tracking data relates to. This is a virtual item linked to other rows containing the same information. Future: This column should be deprecated after the conversion from DLG 2154560 is complete. |
| 8 | `TRACKING_ORDER_ID` | NUMERIC |  | The order that the tracking data relates to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

