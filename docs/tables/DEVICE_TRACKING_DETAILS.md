# DEVICE_TRACKING_DETAILS

> Contains overtime info related to equipment tracking.

**Primary key:** `TRACKING_ID`, `CONTACT_DATE_REAL`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRACKING_ID` | NUMERIC | PK | The unique identifier (.1 item) for the event record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `PAT_ID` | VARCHAR | FK→ | Patient (EPT) ID |
| 4 | `ORDER_ID` | NUMERIC | shared | Order (ORD) ID |
| 5 | `EPISODE_ID` | NUMERIC | FK→ | The associated episode (HSB) ID |
| 6 | `RXW_RECORD_ID` | NUMERIC |  | The shipment (RXW) ID |
| 7 | `COMMENTS` | VARCHAR |  | Comments relating to the device |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

