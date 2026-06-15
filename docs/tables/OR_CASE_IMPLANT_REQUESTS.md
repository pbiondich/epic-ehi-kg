# OR_CASE_IMPLANT_REQUESTS

> Implant requests specific to this patient's case.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMPLANT_REQ_INVENTORY_ITEM_ID` | VARCHAR |  | Enter the inventory item for each implant request. |
| 4 | `IMPLANT_REQ_INVENTORY_ITEM_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 5 | `IMPLANT_REQ_COMMENT` | VARCHAR |  | Enter the comment for each implant request. |
| 6 | `IMPLANT_REQ_QUANTITY` | INTEGER |  | Enter the requested quantity for each implant request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

