# EPSD_PROB_HX_EVENTS

> This table contains the problem history events associated with the episode.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier for the episode of care record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROBLEM_HX_CONTACT_SERIAL_NUM` | NUMERIC |  | This column contains the contact serial number (CSN) of the problem history record where an event associated with the episode is documented. |
| 4 | `PROB_HX_EVENT_LINE` | INTEGER |  | This column contains the line number of the associated problem history event in the Problem Event State (I LPL 8100). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

