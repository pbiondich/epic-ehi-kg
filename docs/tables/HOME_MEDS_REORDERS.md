# HOME_MEDS_REORDERS

> This table contains lists of home medication orders that were replaced on the home medications list by reordering them during an inpatient encounter.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SOURCE_ORDER_ID` | NUMERIC |  | If a home med is reordered and the new order gets added to the home meds list (e.g., because of setup in I LSD 36785/86) the source order is recorded here so that it can be efficiently hidden. |
| 4 | `REORDER_ID` | NUMERIC |  | If a home med is reordered and the new order gets added to the home meds list (e.g., because of setup in I LSD 36785/86) the new order is recorded here. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

