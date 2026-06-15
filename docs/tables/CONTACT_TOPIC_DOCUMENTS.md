# CONTACT_TOPIC_DOCUMENTS

> This table contains Clinical References linked to patient education topics.

**Primary key:** `EDUCATION_RECORD_ID`, `CONTACT_DATE_REAL`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EDUCATION_RECORD_ID` | NUMERIC | PK | The unique identifier (.1 item) for the education record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `GROUP_LINE` | INTEGER | PK | The line number of the associated topic in the patient's education record. Together with EDUCATION_RECORD_ID and CONTACT_DATE_REAL, this forms the foreign key to the CL_PATEDU_CT_TOPIC table. |
| 4 | `VALUE_LINE` | INTEGER | PK | The line number of one of the Clinical References associated with a topic in the patient's education record. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `CONTACT_TOPIC_DCS_ID` | VARCHAR |  | The unique ID of the Document Information record for a Clinical Reference document that is associated with the education topic in CL_PATEDU_CT_TOPIC with a LINE number that matches this row's GROUP_LINE number. This column is frequently used to link to Document Information tables like DOC_INFORMATION and DOC_INFORMATION_2. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

