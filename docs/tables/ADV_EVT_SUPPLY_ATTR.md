# ADV_EVT_SUPPLY_ATTR

> This table stores supply attribution information about an adverse event.

**Primary key:** `ADVERSE_EVENT_ID`, `LINE`  
**Columns:** 5  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ADVERSE_EVENT_ID` | NUMERIC | PK FK→ | The unique identifier for the adverse event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ITEM_ID` | VARCHAR |  | The unique identifier of the supply record that is related to the adverse event. |
| 4 | `ITEM_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 5 | `ITEM_ATTRIBUTION_C_NAME` | VARCHAR | org | The attribution level category ID for the corresponding supply to the adverse event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ADVERSE_EVENT_ID` | [ADVERSE_EVENT_INFO](ADVERSE_EVENT_INFO.md) | sole_pk | high |

