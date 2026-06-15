# IP_HANDOFF_INFO

> This table contains contact related information.

**Primary key:** `HANDOFF_ID`, `CONTACT_DATE_REAL`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HANDOFF_ID` | NUMERIC | PK FK→ | The unique identifier for the handoff data record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 5 | `LAST_UPDATE_USER_ID` | VARCHAR |  | This item specifies the most recent user to update the handoff field. |
| 6 | `LAST_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `LAST_UPDATE_DTTM_DTTM` | DATETIME (UTC) |  | This item specifies the most recent instant that the handoff field was updated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HANDOFF_ID` | [IP_HANDOFF](IP_HANDOFF.md) | sole_pk | high |

