# SSC_PAT_EDUCATION

> This table contains information about patient-level SmartSet Information records with a data row type of Patient Education.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID of the patient-level SmartSet Information record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `PAT_EDU_ITEM_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 5 | `PAT_EDU_TITLE_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |
| 6 | `PAT_EDU_TOPIC_ID_TTP_NAME` | VARCHAR |  | The name of the Title/Topic/Point. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

