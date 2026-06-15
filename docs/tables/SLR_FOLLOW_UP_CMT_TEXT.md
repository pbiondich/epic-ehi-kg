# SLR_FOLLOW_UP_CMT_TEXT

> This table stores the follow-up comment added by the user to a second-level review in the completed follow-ups window.

**Primary key:** `REVIEW_ID`, `CONTACT_DATE_REAL`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the second-level review record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `FOL_COMMENT_TEXT` | VARCHAR |  | The follow-up comment, detailing additional follow-ups or other notes, entered by the user who requested the review. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REVIEW_ID` | [SECOND_LEVEL_REVIEWS](SECOND_LEVEL_REVIEWS.md) | sole_pk | high |

