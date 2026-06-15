# HOLO_SMARTTEXT_NOTE_TXT

> This table contains note text temporarily stored in a hologram record.

**Primary key:** `HOLOGRAM_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HOLOGRAM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the hologram record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `SMARTTEXT_NOTE_TEXT` | VARCHAR |  | Potential note content in the Rich Text Format (RTF). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HOLOGRAM_ID` | [HOLOGRAM_DETAILS](HOLOGRAM_DETAILS.md) | sole_pk | high |

