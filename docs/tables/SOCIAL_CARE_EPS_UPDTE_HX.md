# SOCIAL_CARE_EPS_UPDTE_HX

> Update history for Social Care specific episode data.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SC_UPDATE_INSTANT_DTTM` | DATETIME (UTC) |  | The instant the episode was updated. |
| 4 | `SC_UPDATE_USER_ID` | VARCHAR |  | The unique ID of the user who updated the episode |
| 5 | `SC_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `SC_UPDATE_RESP_ID` | VARCHAR |  | The unique ID of the responsible user when this line was updated. |
| 7 | `SC_UPDATE_RESP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

