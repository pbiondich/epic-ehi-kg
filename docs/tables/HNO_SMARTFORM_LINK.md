# HNO_SMARTFORM_LINK

> This table contains a list of SmartBlocks and the SmartForms that are linked to those SmartBlocks in a particular note.

**Primary key:** `NOTE_CSN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |
| 2 | `LINE` | INTEGER | PK | The line number for the SmartForm (customizable form) link associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `NOTE_ID` | VARCHAR | shared | The unique identifier for the note record. |
| 4 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `SMARTFORM_ID` | VARCHAR |  | The ID of the SmartForm (customizable form) that is linked to a particular SmartBlock (form that can generate text for a note) being used in the note. |
| 7 | `SMARTFORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 8 | `SMARTFORM_DAT` | NUMERIC |  | Which version of a SmartForm (customizable form) is used in the note |
| 9 | `LINKED_ORDER_ID` | NUMERIC |  | The ID of the order (if any) associated with a SmartForm (customizable form) in this note. |
| 10 | `SMARTDATA_ID` | VARCHAR |  | The ID of the SmartData Element (SDE) that links this SmartForm with a particular SmartBlock (form that can generate text for a note). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `NOTE_CSN_ID` | [NOTE_ENC_INFO](NOTE_ENC_INFO.md) | overflow_master | medium |

