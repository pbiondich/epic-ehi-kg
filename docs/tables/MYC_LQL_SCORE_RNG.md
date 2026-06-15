# MYC_LQL_SCORE_RNG

> Stores information about scoring questions related to specific score ranges and what is displayed to patients and providers.

**Primary key:** `QUESTION_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUESTION_ID` | VARCHAR | PK | The unique ID of the question record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `SCOREDISP_LOW_RNG` | NUMERIC |  | lower bound for this score range |
| 5 | `SCOREDISP_UPR_RNG` | NUMERIC |  | upper bound for this score range |
| 6 | `SCOREDISP_PAT_TEXT` | VARCHAR |  | HTML to display to patient for given score range |
| 7 | `SCOREDISP_RNG_DESC` | VARCHAR |  | a short description of what this score range means |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

