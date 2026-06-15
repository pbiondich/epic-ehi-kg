# LAB_REDRAW_INFO

> The LAB_REDRAW_INFO table contains information on specimen redraws for an order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LAB_REDRAW_REASON_C_NAME` | VARCHAR | org | The specimen redraw reason category number for a specimen attached to this order. This explains why a specimen needed to be redrawn. |
| 4 | `LAB_REDRAW_DTTM` | DATETIME (Local) |  | The date and time when the request for specimen redraw was placed. |
| 5 | `LAB_REDRAW_USER_ID` | VARCHAR |  | The unique identifier of the user who requested the specimen redraw. |
| 6 | `LAB_REDRAW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `LAB_REDRAW_PREV_SPE` | VARCHAR |  | The external identifier of the specimen on which the redraw was requested. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

