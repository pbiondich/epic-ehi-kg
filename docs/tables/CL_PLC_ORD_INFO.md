# CL_PLC_ORD_INFO

> This table extracts the Patient Location (PLC) update event information that corresponds to Orders (ORD) events into Clarity.

**Primary key:** `LOCATION_EVNT_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOCATION_EVNT_ID` | NUMERIC | PK FK→ | The unique ID of the location event. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_ID` | NUMERIC | shared | Order ID if location event came from an order |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LOCATION_EVNT_ID` | [CL_PLC](CL_PLC.md) | sole_pk | high |

