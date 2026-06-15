# ORDER_REACTIVATION_HX

> Order reactivation details. Includes information regarding the discontinue (e.g. discontinue user, discontinue reason, etc).

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 17  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REACT_USER_ID` | VARCHAR |  | The unique identifier of the user that reactivated the order. |
| 4 | `REACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `REACT_DTTM` | DATETIME (UTC) |  | The instant the order was reactivated. |
| 6 | `REACT_REASON_C_NAME` | VARCHAR | org | The reactivation reason category ID for the order. |
| 7 | `REACT_DC_USER_ID` | VARCHAR |  | The unique identifier for the user that discontinued the order. |
| 8 | `REACT_DC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `REACT_DC_DTTM` | DATETIME (UTC) |  | The instant the order was discontinued. |
| 10 | `REACT_DC_REASON_C_NAME` | VARCHAR | org | The discontinue reason category ID for the order. |
| 11 | `REACT_DC_ENC` | NUMERIC |  | The patient encounter the order was discontinued in. |
| 12 | `REACT_COMMENTS` | VARCHAR |  | Comments entered when the order was reactivated. |
| 13 | `REACT_DC_END_DATE` | DATETIME |  | The end date specified when the order was discontinued. |
| 14 | `REACT_DC_END_TIME` | DATETIME (Local) |  | The end time specified when the order was discontinued. |
| 15 | `REACT_DC_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the discontinue encounter. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 16 | `REACT_PHARMACY_ID` | NUMERIC |  | The unique identifier for the owning pharmacy of the order when it was reactivated. |
| 17 | `REACT_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

