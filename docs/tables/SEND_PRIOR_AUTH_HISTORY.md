# SEND_PRIOR_AUTH_HISTORY

> This table tracks the history of values for the the send medication prior authorization request flag, ORD 22101.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SEND_PA_REQ_HX_YN` | VARCHAR |  | This item is used to track the history of different values for ORD 22101-Send Med Prior Authorization Request. This item holds the value that ORD 22101 was set to. |
| 4 | `PA_HX_CHANGE_SRC_C_NAME` | VARCHAR |  | This item is used to track the history of different values for ORD 22101-Send Med Prior Authorization Request. This item holds what caused the value of ORD 22101 to change. |
| 5 | `PA_HX_CHANGE_UTC_DTTM` | DATETIME (UTC) |  | This item is used to track the history of different values for ORD 22101-Send Med Prior Authorization Request. This item holds when the value of ORD 22101 changed. |
| 6 | `PA_HX_CHNG_USER_ID` | VARCHAR |  | This item is used to track the history of different values for ORD 22101-Send Med Prior Authorization Request. This item holds which user changed the value of ORD 22101. |
| 7 | `PA_HX_CHNG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `PA_PRIORITY_HX_C_NAME` | VARCHAR |  | The prior authorization priority category ID for the value history of priority of medication prior authorization request before the order is signed. |
| 9 | `PA_PRIORITY_HX_CHANGE_SRC_C_NAME` | VARCHAR |  | The prior authorization priority change source category ID for the change source history of priority of medication prior authorization request before the order is signed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

