# CL_QANSWER_OVTM

> The CL_QANSWER_OVTM table contains contact-specific information for questionnaire answers.

**Primary key:** `ANSWER_ID`, `CONTACT_DATE_REAL`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ANSWER_ID` | VARCHAR | PK FK→ | The unique ID of the answer record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The contact date in datetime format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | Store the contact owner for the record. |
| 5 | `INSTANT_OF_ENTRY` | DATETIME (Attached) |  | The instant an interval begins. |
| 6 | `END_INSTANT` | DATETIME (Attached) |  | The instant an interval ends. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ANSWER_ID` | [CL_QANSWER](CL_QANSWER.md) | sole_pk | high |

