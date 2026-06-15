# RX_RXW_ORDER_INFO

> Each work request can have any number of fill requests attached signifying the dispenses that should be grouped together. This table includes the patient, order, and order DAT for each fill request attached to the work request. The primary key for this table is RECORD_ID and LINE. The RECORD_ID column can be linked to the RX_RXW table in order to include general work request information in the report.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | Record ID of the work request. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FILL_REQ_ORDER_ID` | NUMERIC |  | Each work request can be attached to a fill request contact on any number of orders. This column links this work request with a given order. It can be linked to any order related table to include order related information in the report. |
| 4 | `FILL_REQ_ORDER_DAT` | VARCHAR |  | A fill request is a contact on the order record documenting a dispense of that order to the patient. This field specifies which fill request (or contact) on the order is associated with this work request. Each fill request on an order will be linked to a separate work request documenting that set of dispenses to the patient. |
| 5 | `FILL_REQ_DXR_ID` | NUMERIC |  | Document record for this fill request |
| 6 | `FILL_REQ_DXR_DAT` | VARCHAR |  | Document DAT for this fill request |
| 7 | `ADV_PREP_ORD_ID` | NUMERIC |  | This is the order ID of a cross-encounter signed and held inpatient e-prescription that has been sent to the pharmacy for advance prep. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

