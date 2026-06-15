# SHIPMENT_TRACKING_NUMBERS

> This table has tracking numbers associated with this shipment.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the work request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SHIP_CARRIER_C_NAME` | VARCHAR | org | Contains the carrier who is delivering this shipment, such as UPS, USPS, or FedEx. |
| 4 | `SHIP_TRACK_NUM` | VARCHAR |  | The tracking numbers associated with the prescriptions being shipped. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

