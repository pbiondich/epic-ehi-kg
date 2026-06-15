# NOTES_HISTORY_LOG

> This table contains the Edit History Information for all Notes (HNO records). Shows information about the type of edit, when the note was edited, and the user who made the edit.

**Primary key:** `NOTE_CSN_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK FK→ | A unique serial number identifier for this note contact. |
| 2 | `LINE` | INTEGER | PK | The line number of data, within the note contact. |
| 3 | `NOTE_ID` | VARCHAR | shared | The Note ID, or General Use Notes (HNO) record number. |
| 4 | `CONTACT_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date (calendar format) on which the encounter took place. |
| 6 | `EDIT_HX_INSTANT` | DATETIME (Local) |  | The instant at which the History Edit Action was performed. |
| 7 | `EDIT_HX_ACTION_C_NAME` | VARCHAR |  | The edit action that was performed on the note. Examples include Activate, Inactivate, and Edit. |
| 8 | `EDIT_HX_INFO` | VARCHAR |  | This item can contain additional general edit information about the edit. |
| 9 | `EDIT_HX_EXP_DATE` | DATETIME |  | This item stores the FYI expiration date at the time that this record was modified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

