# VISIT_SET_SLOT_HX_RVSN

> The VISIT_SET_SLOT_HX_RVSN table contains the slot index and period that was modified and the instant at which it was modified. Information about specific items modified during the revision can be found in VISIT_SET_SLOT_HX_CHANGE.

**Primary key:** `VISIT_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact. |
| 5 | `AUDIT_SLOT_INSTANT_DTTM` | DATETIME (UTC) |  | The instant a slot change was made |
| 6 | `AUDIT_SLOT_ACTION_C_NAME` | VARCHAR |  | The type of change being made to this slot |
| 7 | `AUDIT_SLOT_PERIOD` | INTEGER |  | The period of the slot changed |
| 8 | `AUDIT_SLOT_INDEX` | INTEGER |  | The index of the slot changed |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

