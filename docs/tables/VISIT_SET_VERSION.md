# VISIT_SET_VERSION

> The VISIT_SET_VERSION table contains overtime information about a single visit set, which are templates for recurring visits to address the care required for a patient.

**Primary key:** `VISIT_SET_ID`, `CONTACT_DATE_REAL`  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VISIT_SET_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the visit set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact. |
| 4 | `VISIT_SET_CSN_ID` | NUMERIC |  | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | The contact number |
| 6 | `VISIT_TYPE_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 7 | `START_DATE` | DATETIME |  | The start date of the visit set. |
| 8 | `END_DATE` | DATETIME |  | The end date of the visit set. |
| 9 | `DURATION_MINUTES` | INTEGER |  | The duration, in minutes, of the visit defined by this version of the visit set. |
| 10 | `ORDER_COMMENT_NOTE_CSN_ID` | NUMERIC |  | The CSN of the version of the note record that contains the order comment for this version of the visit set. The order comment is reviewed and approved by a physician. |
| 11 | `SCHED_INSTRUCTIONS_NOTE_CSN_ID` | NUMERIC |  | The CSN of the version of the note record that contains the scheduling instructions for this version of the visit set. Scheduling instructions serve to provide additional context to schedulers and are neither reviewed nor approved by a physician. |
| 12 | `FREQUENCY_FREQ_ID` | VARCHAR |  | The frequency record (EFQ) that defines the recurrence of visits for this version of the visit set. Only specified frequencies of type 'same time days of week' and 'relative' are supported. |
| 13 | `FREQUENCY_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 14 | `VISIT_RECUR_PATTERN_TYPE_C_NAME` | VARCHAR |  | The type of the visit pattern. |
| 15 | `VISIT_PATTERN_RECURRENCE` | INTEGER |  | How often visits defined by this version of the visit set should recur. |
| 16 | `TIME_WINDOW_BEGIN_TM` | DATETIME (Local) |  | The beginning of the time window during which it is acceptable to schedule visits defined by this version of the visit set. If both start and end times are specified, visits must begin within those times. If only a start time is specified, visits must begin at that time. At least a start time is required. |
| 17 | `TIME_WINDOW_END_TM` | DATETIME (Local) |  | The end of the time window during which it is acceptable to schedule visits defined by this version of the visit set. If both start and end times are specified, visits must begin within those times. If only a start time is specified, visits must begin at that time. At least a start time is required. |
| 18 | `TOLERANCE_BEFORE_DAYS` | INTEGER |  | The number of days before the specified date that it is acceptable to schedule visits defined by this version of the visit set. |
| 19 | `TOLERANCE_AFTER_DAYS` | INTEGER |  | The number of days after the specified date that it is acceptable to schedule visits defined by this version of the visit set. |
| 20 | `AUTO_GENERATED_YN` | VARCHAR |  | Whether or not this version of the visit set was automatically generated. This is always populated with either Yes or No. |
| 21 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Local) |  | Stores the instant of entry when a record is edited |
| 22 | `VISIT_PATTERN_MIN_VISITS` | INTEGER |  | The minimum number of visits that must occur per interval. |
| 23 | `VISIT_PATTERN_MAX_VISITS` | INTEGER |  | The maximum number of visits that must occur per interval. |
| 24 | `DISCONTINUE_DATE` | DATETIME |  | The discontinue date of the visit set. |
| 25 | `IS_DELETED_YN` | VARCHAR |  | Whether this version of the visit set has been deleted. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VISIT_SET_ID` | [VISIT_SET](VISIT_SET.md) | sole_pk | high |

