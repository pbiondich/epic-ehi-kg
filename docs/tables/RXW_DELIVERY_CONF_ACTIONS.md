# RXW_DELIVERY_CONF_ACTIONS

> This contains the history of delivery confirmation actions on a work request.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DLV_DTLS_CNF_UTC_DTTM` | DATETIME (UTC) |  | This item stores the UTC instant the delivery details were marked as confirmed. |
| 4 | `DLVDTLCONFRSN_C_NAME` | VARCHAR |  | This item stores the reason the delivery details were marked as confirmed. |
| 5 | `DLVDTLCNFUSER_ID` | VARCHAR |  | This item stores the user that marked the delivery details as confirmed. |
| 6 | `DLVDTLCNFUSER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

