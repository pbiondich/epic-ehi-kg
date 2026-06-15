# PR_EST_EVENT_HX

> Price Estimate event history information.

**Primary key:** `ESTIMATE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the estimate record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_EVENT_TYPE_C_NAME` | VARCHAR |  | The event type category ID for the patient estimate. |
| 4 | `HX_USER_ID` | VARCHAR |  | The user associated with the event for this line in the event history table. |
| 5 | `HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `HX_INSTANT_DTTM` | DATETIME (UTC) |  | The instant of the event for this line in the event history table. |
| 7 | `HX_MYPT_ID` | VARCHAR |  | Stores the MyChart user for this line in the event history table. |
| 8 | `HX_INSTANT_LOC_DTTM` | DATETIME (Local) |  | The local instant of the event for this line in the event history table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

