# ORD_EXPECTED_PERFORM_DATE

> This table contains the list of expected perform dates in chronological order for a Recurring outpatient procedure order.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `STANDING_EXPECTED_PERFORM_DATE` | DATETIME |  | Stores the list of dates on which the orders in corresponding lines of ORD 663 are expected to be performed. Used for outpatient Recurring only. |
| 4 | `STAND_EXPECT_PERFORM_ORDER_ID` | NUMERIC |  | Stores the list of orders corresponding to the dates on which orders are expected to be performed. Typically these will be individual occurrences (child orders) of a main order (parent order), but if the order is released in an inpatient/Hospital-Outpatient-Visit(HOV) setting the intermediate parent will be stored instead. Used for outpatient Recurring only. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

