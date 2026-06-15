# SPOC_NOTES

> Specialty plan of care notes information.

**Primary key:** `POC_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier for the plan of care record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SPOC_NOTE_ID` | VARCHAR |  | The unique ID of the note for the plan of care. |
| 6 | `SPOC_NOTE_CSN` | NUMERIC |  | This item contains a link to a note contact. The note contact can be used to determine what the note contained in a particular version. |
| 7 | `SPOC_NOTE_PURPOSE_C_NAME` | VARCHAR | org | The purpose category ID for the plan of care. The purpose is used to classify the note and match it to the section which contains its definitions. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

