# HOME_CARE_FORMS

> The HOME_CARE_FORMS table contains information about visit and assessment documentation forms used on the Remote Client for home health and hospice patients.

**Primary key:** `FORM_ID`, `CONTACT_DATE_REAL`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 2 | `FORM_DESCRIPTION` | VARCHAR |  | Holds the form name that displays on the Remote Client for this form. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

