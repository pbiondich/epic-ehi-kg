# OTHER_COMMUNCTN

> This table stores miscellaneous communication devices that can be used to reach the patient. Examples are mobile phone and pager.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique identifier for the patient record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OTHER_COMMUNIC_C_NAME` | VARCHAR | org | Other communication devices such as: 1) MOBILE: Mobile 2) PAGER: Pager 3) HOME FAX: Home Fax 4) OTH FAX: Other Fax 5) ASTNT: Assistant 6) TTY/TDP: TTY/TDP 7) HOME PH: Home Phone 8) WORK PH: Work Phone |
| 4 | `OTHER_COMMUNIC_NUM` | VARCHAR |  | Different kinds of communication numbers such as Home Phone, Work Phone, Fax, Pager, etc, that correspond to the type of device stored in OTHER_COMMUNIC_C. |
| 5 | `START_DAY_C_NAME` | VARCHAR |  | The beginning day for the date range that this phone number is valid. |
| 6 | `END_DAY_C_NAME` | VARCHAR |  | The end day for the date range that this phone number is valid. |
| 7 | `START_TIME` | DATETIME (Local) |  | The beginning time for the time range that this phone number is valid. |
| 8 | `END_TIME` | DATETIME (Local) |  | The end time for the time range that this phone number is valid. |
| 9 | `CONTACT_PRIORITY` | INTEGER |  | Priorities are numbers, and are used to set a calling preference for phone numbers. 1 is the highest priority. |
| 10 | `CONTACT_NOTES` | VARCHAR |  | Notes associated with this phone/contact number. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

