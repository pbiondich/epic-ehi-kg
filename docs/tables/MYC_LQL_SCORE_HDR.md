# MYC_LQL_SCORE_HDR

> Stores the HTML header that is displayed to the patient when they complete the questionnaire (for scoring questions).

**Primary key:** `QUESTION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUESTION_ID` | VARCHAR | PK | The unique ID of the question record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `SCORE_HEADER` | VARCHAR |  | RTF header for use in score reports when showing to patient |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

