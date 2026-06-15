# REACTIVATED_EXP_ORDERS

> This table lists medication orders that had expired before the patient was admitted, but became active again after their drugs were marked as long-term. These medications are shown in discharge order reconciliation, alongside the medications that were active at admission, as needing reconciliation.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 2 | `REACTIVATED_ORDER_ID` | NUMERIC |  | The unique ID of the medication order that was reactivated. |
| 3 | `REACTIVATED_DTTM` | DATETIME (Local) |  | The date and time at which this medication order was reactivated. |
| 4 | `EVENT_ID` | VARCHAR | PK FK→ | The unique ID for the event record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

