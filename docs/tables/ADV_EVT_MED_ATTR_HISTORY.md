# ADV_EVT_MED_ATTR_HISTORY

> This table contains the history of this adverse event's attribution to the associated medication. Together with ADV_EVT_MED_HISTORY, these tables contain the history of an adverse event's medication attributions.

**Primary key:** `ADVERSE_EVENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ADVERSE_EVENT_ID` | NUMERIC | PK FK→ | The unique identifier for the adverse event record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the adverse event history in the adverse event record. Together with ADVERSE_EVENT_ID, this forms the foreign key to the ADVERSE_EVENT_HISTORY table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple attribution levels for the corresponding medication record that is related to the adverse event at the time the adverse event was documented. |
| 4 | `HX_MEDICATION_ATTRIBUTION_C_NAME` | VARCHAR | org | The attribution level category ID for the corresponding medication to the adverse event at the time the adverse event was documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ADVERSE_EVENT_ID` | [ADVERSE_EVENT_INFO](ADVERSE_EVENT_INFO.md) | sole_pk | high |

