# SERVICE_PLAN_VERSION

> The SERVICE_PLAN_VERSION table contains overtime information about service plans, which describe plans for recurring visits to address the care required for a patient.

**Primary key:** `SERVICE_PLAN_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SERVICE_PLAN_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the service plan record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact. |
| 4 | `SERVICE_PLAN_CSN_ID` | NUMERIC |  | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | The contact number |
| 6 | `PLAN_STATUS_PLN_C_NAME` | VARCHAR |  | The status of this version of the service plan. |
| 7 | `START_DATE` | DATETIME |  | The start date of this version of the service plan. |
| 8 | `END_DATE` | DATETIME |  | The end date of this version of the service plan. |
| 9 | `COMMENT_NOTE_CSN_ID` | NUMERIC |  | The CSN of the version of the note record that contains the comment for this version of the service plan. |
| 10 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Local) |  | Stores the instant of entry when a record is edited |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SERVICE_PLAN_ID` | [SERVICE_PLAN](SERVICE_PLAN.md) | sole_pk | high |

