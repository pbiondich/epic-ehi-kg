# DIFFERENCE_PERIOD_EVENT

> Information about difference period events.

**Primary key:** `DIFF_PERIOD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DIFF_PERIOD_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the difference period record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `DIFF_PERIOD_STATUS_C_NAME` | VARCHAR |  | The status that this event moves the difference period to. |
| 4 | `DIFF_PERIOD_EVENT_C_NAME` | VARCHAR |  | The type of difference period event that has occurred. |
| 5 | `USER_ID` | VARCHAR | FK→ | The user associated with the difference period event. |
| 6 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ORGANIZATION_ID` | NUMERIC | FK→ | The organization associated with this difference period event. |
| 8 | `ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 9 | `EVENT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant the difference period event occurred. |
| 10 | `EVENT_LOCAL_DTTM` | DATETIME (Local) |  | The calculated local instant that the difference period event occurred. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DIFF_PERIOD_ID` | [DIFFERENCE_PERIOD](DIFFERENCE_PERIOD.md) | sole_pk | high |
| `ORGANIZATION_ID` | [ORG_DETAILS](ORG_DETAILS.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

