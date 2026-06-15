# CRITERIA_REV_CNCT

> Table contains the overtime information in the Criteria Review records.

**Primary key:** `CRITERIA_REVIEW_ID`, `CONTACT_DATE_REAL`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CRITERIA_REVIEW_ID` | NUMERIC | PK FK→ | The unique identifier for the review record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `INST_OF_ENTRY_DTTM` | DATETIME (Local) |  | Instant of an entry. |
| 5 | `CONTACT_STATUS_C_NAME` | VARCHAR |  | The status of the utilization review for this contact of the review. |
| 6 | `REV_ENTRY_USER_ID` | VARCHAR |  | The user who created or edited the review (for this contact of the review). |
| 7 | `REV_ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `NOTE_ENTRY_ID` | VARCHAR |  | The unique ID of the note associated with the criteria review for a given contact. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CRITERIA_REVIEW_ID` | [CRITERIA_REVIEW](CRITERIA_REVIEW.md) | sole_pk | high |

