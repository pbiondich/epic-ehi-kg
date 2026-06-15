# PAT_ENC_FOLLOW_UPS

> This table contains the data for the follow up appointments requested by a provider at each encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `DISPOSITION` | VARCHAR |  | This the sentence form of the follow-up disposition. |
| 5 | `NUM_OF_UNITS` | INTEGER |  | This item contains the number of the given units (days/months/etc) into the future to schedule the follow-up. |
| 6 | `UNIT_TYPE_C_NAME` | VARCHAR |  | This is the unit of measure used to determine how far into the future to schedule a follow-up appointment |
| 7 | `FREE_TEXT` | VARCHAR |  | This is the note that is sent along with the follow-up request to the scheduler. |
| 8 | `PRN_USED_YN_NAME` | VARCHAR |  | Indicates whether PRN is used on a follow-up appointment. |
| 9 | `APPROX_USED_YN_NAME` | VARCHAR |  | Indicates if the date of a follow-up was approximate. |
| 10 | `PRN_TEXT` | VARCHAR |  | This is the text that indicates why the follow-up is PRN. |
| 11 | `DISP_DATE` | DATETIME |  | This is the date the follow-up should be scheduled for. |
| 12 | `DISP_ID` | INTEGER |  | This is a unique identifier for each follow-up. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

