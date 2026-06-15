# RXHI_SHIPMENT_STATUS

> Current and previous shipment status information for a home infusion shipment.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RXHI_SHIP_STATUS_C_NAME` | VARCHAR | org | This item stores the current and past statuses for a home infusion shipment. The current status is stored on the last (highest numbered) line |
| 4 | `RXHI_STS_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant of update for each change to the home infusion shipment status (I RXW 10091). The most recent update is stored in the last (highest numbered) line |
| 5 | `RXHI_STATUS_COMMENT` | VARCHAR |  | User entered or system generated comment for a home infusion status event. |
| 6 | `RXHI_CHNG_RSN_C_NAME` | VARCHAR | org | The reason why the medications or supplies in an order have been modified after the shipment has left the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

