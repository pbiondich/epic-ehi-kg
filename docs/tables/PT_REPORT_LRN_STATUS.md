# PT_REPORT_LRN_STATUS

> This table tracks the patient-reported extent to which the patient understood the educational material in question.

**Primary key:** `EDUCATION_RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EDUCATION_RECORD_ID` | NUMERIC | PK | This column stores the unique identifier for the education record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `USER_STATUS_KEY` | VARCHAR |  | Caret-delimited list of title/topic/point whose user-entered status was updated. |
| 6 | `USER_STATUS_DAT_KEY` | VARCHAR |  | Caret-delimited contact date (DAT) key related to the title/topic/point whose user-entered status was updated (item 96011) |
| 7 | `USER_STATUS_C_NAME` | VARCHAR |  | Status entered by the patient or patient representative relating to their viewing of this patient education. If not set, the education is assumed to be unread. |
| 8 | `USER_ENTER_AT_DTTM_DTTM` | DATETIME (UTC) |  | The instant at which the status was specified by the patient or patient representative relating to their viewing of this patient education. |
| 9 | `STATUS_WEB_USER_ID` | VARCHAR |  | This item holds the ID of the MyChart user who updated the status of this education |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

