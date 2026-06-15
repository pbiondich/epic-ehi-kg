# ORDER_EQUIPMENT_INFO

> Information related to equipment orders.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `FILL_DISP_QTY` | NUMERIC |  | The dispense quantity for item. |
| 4 | `FILL_SOURCE_C_NAME` | VARCHAR |  | Where the prescription fill was requested from. |
| 5 | `CHARGING_CSN` | NUMERIC |  | Contains the unique contact serial number for the patient's pharmacy visit contact to use for charge and payment posting. |
| 6 | `FILL_EPISODE_ID` | NUMERIC |  | This item is a link from the order fill to the therapy episode under which the medication is being given. |
| 7 | `FILL_DELIVERY_TYPE_C_NAME` | VARCHAR | org | The delivery type for this order's fill. Delivery type in this context refers to the type of delivery mechanism that infuses the medication from the bag to the patient, not a commercial shipping carrier. |
| 8 | `EQUIPMENT_DVT_CSN` | NUMERIC |  | The unique contact serial number for the device tracking record. |
| 9 | `DISPENSE_PHR_ID` | NUMERIC |  | The dispensing pharmacy for the order. |
| 10 | `DISPENSE_PHR_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

