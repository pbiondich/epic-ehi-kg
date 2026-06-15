# HSC_RECRD_STAT_HX

> This table stores information related to the record status of specimens.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID of the Specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number of one of the record statuses that are associated with the specimens from the HSC master file. |
| 3 | `SDFL_EDIT_INSTANT` | DATETIME (Attached) |  | The instant the Specimen record status was changed. |
| 4 | `SDFL_EDIT_USER_ID` | VARCHAR |  | The unique User ID of the user who changed the specimen record status. |
| 5 | `SDFL_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SDFL_EDIT_ACTION_C_NAME` | VARCHAR |  | The category number for the action taken in a change of the Specimen record status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

