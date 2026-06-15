# ERX_EVENT

> This table holds information about e-prescribing event and e-prescribing error resolution for Inpatient E-Prescribing. Starting in the May 23 version, it will also hold information about e-prescribing error resolution for Ambulatory E-Prescribing.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ERX_EVENT_C_NAME` | VARCHAR |  | This item stores the type of e-prescribing event. |
| 4 | `ERX_STATUS_C_NAME` | VARCHAR |  | This item stores the status of an e-prescribing event. |
| 5 | `ERX_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant of an e-prescribing event. |
| 6 | `ERX_USER_ID` | VARCHAR |  | This item stores the user who initiated an e-prescribing event. If no user is listed, then the event was initiated by a background job (interface, order transmittal, etc.). |
| 7 | `ERX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

