# ALT_ALLERGY_REACT

> This table contains allergy reaction for drug-allergy warning.

**Primary key:** `ALT_CSN_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALT_ID` | NUMERIC | FK→ | The unique identifier for the alert. |
| 2 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ALLERGY_REACTION_C_NAME` | VARCHAR | org | It stores the patient allergy reaction for the allergy as of when the drug-allergy warning is fired. |
| 6 | `ALT_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this contact. This number is unique across all alerts in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_CSN_ID` | [ALT_HISTORY](ALT_HISTORY.md) | sole_pk | high |
| `ALT_ID` | [ALERT](ALERT.md) | sole_pk | high |

