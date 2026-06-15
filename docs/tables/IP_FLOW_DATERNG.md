# IP_FLOW_DATERNG

> Tracks the dates during which a flowsheet template was used on a given patient stay.

**Primary key:** `INPATIENT_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INPATIENT_DATA_ID` | VARCHAR | PK shared | The unique ID of the inpatient data store record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FLOWSHEET_DATE_ID` | VARCHAR |  | Stores the flowsheet template (FLT) ID related to the first and last instants documented. |
| 4 | `FLOWSHEET_DATE_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

