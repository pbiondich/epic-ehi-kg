# HH_MED_ORD_EVENTS

> This table will store Home Health medication order event details.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MED_ORDER_EVENT_TYPE_C_NAME` | VARCHAR |  | This item stores the event that happens for a medication order that has been added to or removed from the Home Health Plan of Care. |
| 4 | `MED_ORDER_EVENT_USER_ID` | VARCHAR |  | This item stores the user associated with the event that happens for a medication order that has been added to or removed from the Home Health Plan of Care. |
| 5 | `MED_ORDER_EVENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `MED_ORDER_EVENT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant when an event happens for a medication order that has been added to or removed from the Home Health Plan of Care. |
| 7 | `MED_ORDER_EVENT_CSN` | NUMERIC |  | This item stores the contact serial number (CSN) associated with the medication update encounter that results in an event for medication orders that have been added to or removed from the Home Health Plan of Care. |
| 8 | `MED_ORDER_COMMENT_NOTE_ID` | VARCHAR |  | This item stores the ID of the note that stores the comment associated with the event that happens for medication orders that have been added to or removed from the Home Health Plan of Care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

