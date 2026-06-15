# OR_IMP_ACCESSORIES

> This table stores information about implant accessories.

**Primary key:** `IMPLANT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMPLANT_ID` | VARCHAR | PK shared | The unique identifier for the implant record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMP_ACCESSORY_EXPIRATION_DATE` | DATETIME |  | This column stores the expiration date for the implant accessory item. |
| 4 | `IMP_ACCESSORY_TRACKING_NUMBER` | VARCHAR |  | This column stores the tracking number for the implant accessory item. |
| 5 | `IMP_ACCESSORY_LOT_NUMBER` | VARCHAR |  | This item stores the lot number for the implant accessory item that is being documented. |
| 6 | `IMP_ACCESSORY_SERIAL_NUMBER` | VARCHAR |  | This item stores the serial number for the implant accessory item that is being documented. |
| 7 | `IMP_ACCESSORY_RECEIVED_DATE` | DATETIME |  | This item stores the date that the implant accessory item has been received by the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

