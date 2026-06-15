# ADV_EVT_MED_HISTORY

> This table contains the history of this adverse event's related medications. Together with ADV_EVT_MED_ATTR_HISTORY, these tables contain the history of an adverse event's medication attributions.

**Primary key:** `ADVERSE_EVENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ADVERSE_EVENT_ID` | NUMERIC | PK FK→ | The unique identifier for the adverse event record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the adverse event history in the adverse event record. Together with ADVERSE_EVENT_ID, this forms the foreign key to the ADVERSE_EVENT_HISTORY table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple medication records that is related to the adverse event at the time the adverse event was documented. |
| 4 | `HX_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ADVERSE_EVENT_ID` | [ADVERSE_EVENT_INFO](ADVERSE_EVENT_INFO.md) | sole_pk | high |

