# AWM_ORD_MEASUREMENTS

> Stores data pertaining to Automatic Wound Measurements usage in Orders.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this ORD record. Multiple pieces of information can be associated with this record. |
| 3 | `AWM_MEASUREMENT_ROW` | VARCHAR |  | Contains the FLO IDs of all the measurement rows that were documented with Automated Wound Measurements that are associated with the order. To determine if they are pre or post debridement check item 68511 |
| 4 | `MEASUREMENT_PRE_DEBRIDE_YN` | VARCHAR |  | Whether or not the measurement from the row in 68510 is a pre or post debridement measurement. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

