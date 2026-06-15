# SNAPSHOT_ORDER_DATA

> This table has the identifiers for individual data elements that were stored at the time of discharge or when the patient's After Visit Summary was printed. The actual snapshot data is in the SNAPSHOT_ORD_INFO_VALUE table.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the discharge reconciliation event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SNAPSHOT_ORDERS_LINE` | INTEGER |  | The line number of the associated snapshot information for this order. Together with EVENT_ID, this forms the foreign key to the SNAPSHOT_ORDERS table. |
| 4 | `SNAPSHOT_ORD_KEY_C_NAME` | VARCHAR |  | The category ID for the orders' individual data element that was stored. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

