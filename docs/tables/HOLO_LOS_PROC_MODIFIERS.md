# HOLO_LOS_PROC_MODIFIERS

> This table contains level of service component procedure modifiers.

**Primary key:** `HOLOGRAM_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HOLOGRAM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hologram record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `LEVEL_OF_SERV_PROC_MODIFIER_ID` | VARCHAR |  | The unique identifier (.1 item) for the modifier for the level of service component in this hologram record. |
| 5 | `LEVEL_OF_SERV_PROC_MODIFIER_ID_MODIFIER_NAME` | VARCHAR |  | The name of the modifier record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HOLOGRAM_ID` | [HOLOGRAM_DETAILS](HOLOGRAM_DETAILS.md) | sole_pk | high |

