# PERSON_PREFERENCES

> This table contains items related to Person Preferences. Unlike COMM_PREF_ADDL_ITEMS which stores communication preferences, this table stores data that is relevant to a person's preferences.

**Primary key:** `PERSON_PREFERENCE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PERSON_PREFERENCE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the subject name record. |
| 2 | `TZ_DIFF_ALERT_YN` | VARCHAR |  | Indicates whether a user chooses to see an alert popup for time zone difference between the notification time zone and local time zone. "Y" indicates that the user chooses to see the popup. "N" or NULL indicates that the user does not want to see the popup. |
| 3 | `HIDE_WOUND_IMAGE_SPOILER_YN` | VARCHAR |  | This item stores whether wound images for all wounds should be shown without a spoiler in MyChart. This preference is chosen by the user. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

