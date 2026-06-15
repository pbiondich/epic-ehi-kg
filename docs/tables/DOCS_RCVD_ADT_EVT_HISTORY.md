# DOCS_RCVD_ADT_EVT_HISTORY

> This table contains event history information from external ADT encounters.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EVT_HX_REF_IDENT` | VARCHAR |  | Unique identifier for the ADT event history data. |
| 6 | `EVT_HX_ENC_IDENT` | VARCHAR |  | Reference ID of the associated encounter. |
| 7 | `EVT_HX_EVENT_TYPE_C_NAME` | VARCHAR | org | The event type category ID for the ADT event. |
| 8 | `EVT_HX_EVENT_PAT_CLASS_C_NAME` | VARCHAR |  | The patient class category ID for the ADT event. |
| 9 | `EVT_HX_FAC_NAME` | VARCHAR |  | Facility name of the ADT event. |
| 10 | `EVT_HX_DEPT_NAME` | VARCHAR |  | Department name of the ADT event. |
| 11 | `EVT_HX_EVT_INST_UTC_DTTM` | DATETIME (UTC) |  | Start instant for the ADT event in UTC. |
| 12 | `EVT_HX_SPECIALTY_DEP_C_NAME` | VARCHAR | org | The specialty category ID for the ADT event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

