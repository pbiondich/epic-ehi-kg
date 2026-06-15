# LIT_ALLOWED_TREAT_CLASS

> Table for Allowed Treatment Classes for Treatment Template type intervention types.

**Primary key:** `INTRVNTN_TYPE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTRVNTN_TYPE_ID_INTRVNTN_TYPE_NAME` | VARCHAR |  | The name of the intervention type. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `ALLOWED_TREATMENT_CLASS_ID` | NUMERIC |  | Treatment classes this treatment exercise can be added to |
| 5 | `ALLOWED_TREATMENT_CLASS_ID_DISPLAY_NAME` | VARCHAR |  | The name of the treatment class that is displayed to end users. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

