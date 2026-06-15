# SYN_FORMS

> The SYN_FORMS table contains information about the form and contact used to populate the synoptic data.

**Primary key:** `SYNOPTIC_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SYNOPTIC_ID` | NUMERIC | PK FK→ | The unique identifier for the synoptic result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FORM_ID` | VARCHAR | FK→ | The unique ID of the form used for documenting synoptic results. |
| 4 | `FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `CONTACT_DATE_REAL` | NUMERIC |  | A unique contact date in decimal format for the SmartForm. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FORM_ID` | [CL_QFORM1](CL_QFORM1.md) | sole_pk | high |
| `SYNOPTIC_ID` | [SYNOPTIC_RESULT_MAIN](SYNOPTIC_RESULT_MAIN.md) | sole_pk | high |

