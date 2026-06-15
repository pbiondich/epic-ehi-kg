# POC_VERSION_INFO

> Overtime plan of care information.

**Primary key:** `POC_ID`, `CONTACT_DATE_REAL`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `POC_ID` | NUMERIC | PK | The unique identifier for the plan of care record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | NUMERIC |  | Stores contact number |
| 6 | `CONTACT_COMMENT` | VARCHAR |  | Describes the reason for creating the new contact |
| 7 | `INSTANT_OF_ENTRY_DTTM` | DATETIME (Local) |  | Stores the instant of entry when a record is edited |
| 8 | `SPOC_EFF_FROM_DATE` | DATETIME |  | The date when the plan of care is effective from. |
| 9 | `SPOC_EFF_TO_DATE` | DATETIME |  | The date when the plan of care is effective until. |
| 10 | `END_AGE_MAJORITY_YN` | VARCHAR |  | Indicates whether the effective to date for this plan is set to the patient's birthday when they achieve the age of majority. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

