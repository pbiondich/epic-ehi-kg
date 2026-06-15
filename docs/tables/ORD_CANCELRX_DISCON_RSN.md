# ORD_CANCELRX_DISCON_RSN

> Information about CancelRx reason codes and the discontinue reasons mapped to those codes.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CANCEL_REASON_CODE` | VARCHAR |  | Cancel reason codes received in a CancelRx message. |
| 4 | `RSN_FOR_DISCON_C_NAME` | VARCHAR | org | Discontinue reason mapped to a cancel reason code received in a CancelRx message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

