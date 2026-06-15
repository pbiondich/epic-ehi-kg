# COMM_TRACE_AUTH_DEM

> Table for tracking information related to demographics verification as part of an authentication attempt.

**Primary key:** `OUTREACH_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the outreach record record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `AUTH_DEM_FIELD_C_NAME` | NUMERIC |  | The demographic field category ID for an authentication attempt. |
| 5 | `AUTH_DEM_VALUE` | VARCHAR |  | The demographics value collected to verify user identity in an authentication attempt. |
| 6 | `AUTH_DEM_IS_MATCH_YN` | VARCHAR |  | Whether or not a demographic value collected matches the expected user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OUTREACH_ID` | [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | sole_pk | high |

