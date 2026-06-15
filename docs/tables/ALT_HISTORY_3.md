# ALT_HISTORY_3

> This table contains general history information for each type of medication warning or advisory. Since each warning could be triggered in different activities at different times, it contains general warning information for each time the warning was triggered. This table is an extension of ALT_HISTORY table.

**Overflow of:** [ALT_HISTORY](ALT_HISTORY.md)  
**Primary key:** `ALT_CSN_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALT_ID` | NUMERIC | FK→ | The unique identifier for the med alert record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `ALT_CSN_ID` | NUMERIC | PK | A unique serial number for this contact. This number is unique across all alerts in the system. |
| 5 | `VIGILANCE_SEVERITY_C_NAME` | VARCHAR |  | This column contains the severity level provided by Vigilance Santé. |
| 6 | `VIGILANCE_WARNING_TYPE_C_NAME` | VARCHAR |  | This column contains the specific type of warning provided by Vigilance Santé. |
| 7 | `AVOIDANCE_LEVEL_C_NAME` | VARCHAR |  | The avoidance level assigned to warning, such as contraindicated or should be avoided. |
| 8 | `INFORMATIONAL_YN` | VARCHAR |  | This stores whether a medication warning is informational. |
| 9 | `SVV_STATUS_C_NAME` | VARCHAR |  | Stores the status of the user's latest interaction with this Sign Visit Validation message. |
| 10 | `MAR_CUMULATIVE_DOSE_TEXT` | VARCHAR |  | Stores the MAR short-term cumulative dose warning text the user saw. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_ID` | [ALERT](ALERT.md) | sole_pk | high |

## Joined in

Inbound joins are tracked on the logical base [ALT_HISTORY](ALT_HISTORY.md).

