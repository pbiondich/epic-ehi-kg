# VISIT_SET_SLOT

> The VISIT_SET_SLOT table contains slots for visit set versions. A slot is a target for an individual visit to occur, containing an appointment request generated to achieve the visit and other information surrounding its fulfillment.

**Primary key:** `VISIT_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact. |
| 5 | `SLOT_PERIOD` | INTEGER |  | The period within the visit set in which the slot falls. A period is the smallest repeatable date window of a visit set, or the unit of its repeating pattern. For example, if a visit set is set to be every week on Monday, Wednesday, and Friday, each period would represent a week. Period 1 is week 1, period 2 is week 2, and so on. To determine this unit, link to VISIT_SET_VERSION and look to VISIT_PATTERN_TYPE_C or FREQUENCY_FREQ_ID (one or the other is populated, not both). |
| 6 | `SLOT_INDEX` | INTEGER |  | The index of the slot in its period. With N being the slot index, this means the Nth slot in the period. For example, if a visit set is set to be every week on Monday, Wednesday, and Friday, index 1 identifies a slot that falls on Monday, index 2 identifies a slot that falls on Wednesday, and index 3 identifies a slot that falls on Friday. Link to VISIT_SET_VISIT_PATTERN and look to VISIT_SET_WHICH_DAYS_C to find the days of the week of a visit set. A LINE of VISIT_SET_VISIT_PATTERN contains the same day of the week on which the SLOT_INDEX of the same value identifies. |
| 7 | `SLOT_STATUS_C_NAME` | VARCHAR |  | The status of the slot |
| 8 | `SLOT_APPT_REQUEST_ID` | NUMERIC |  | The appointment request created to fill this slot |
| 9 | `SLOT_DATE` | DATETIME |  | The date for the slot calculated based on the visit set recurrence, period, and index. In addition to corresponding to the requested date on the ORD appointment request, it is used to match slots during evaluation and to determine whether a slot is skipped due to episode pauses. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

