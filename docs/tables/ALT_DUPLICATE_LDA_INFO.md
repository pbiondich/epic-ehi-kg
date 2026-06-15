# ALT_DUPLICATE_LDA_INFO

> It contains specific information for duplicate LDA warnings. Link it to ALT_HISTORY table to get general history information. Link it to ALERT table to get patient and vendor information. Link it to ALT_DUPLICATE_LDA_CONTENT to get information for each potentially duplicate LDA that appeared inside the warning.

**Primary key:** `ALERT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALERT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the alert record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `ALT_CSN_ID` | NUMERIC | FK→ | A unique serial number for this contact. This number is unique across all warnings in the system. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_CSN_ID` | [ALT_HISTORY](ALT_HISTORY.md) | sole_pk | high |

