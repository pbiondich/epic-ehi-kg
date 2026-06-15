# PROB_UPDATES

> This table includes over-time single-response items from the Problem List (LPL) master file, such as the contact serial number (CSN), contact time, and contact user.

**Primary key:** `PROBLEM_LIST_ID`, `CONTACT_DATE_REAL`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK FK→ | The unique identifier for the problem record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME (Local) |  | The date and time of this contact. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact, which is a unique contact identifier. |
| 5 | `EDIT_USER_ID` | VARCHAR |  | The user ID of the user who made the change. |
| 6 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `CONTACT_STATUS_C_NAME` | VARCHAR |  | Stores the status of this contact - used by records of type "Problem History". |
| 8 | `EPT_CSN` | NUMERIC |  | Holds the patient CSN (contact serial number I.E. unique contact identifier) corresponding to the patient encounter in which related information was added to or removed from this problem, if the edit was made during a patient encounter. |
| 9 | `RECONCILED_YN` | VARCHAR |  | This item contains information about whether a problem has been reconciled in a given encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PROBLEM_LIST_ID` | [PROBLEM_LIST](PROBLEM_LIST.md) | name_stem | high |

