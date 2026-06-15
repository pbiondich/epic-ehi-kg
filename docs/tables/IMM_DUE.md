# IMM_DUE

> The IMM_DUE table contains information about when an immunization is due. The rows included in this table are items from DXR (Document) masterfile which include information on type of immunization, due date, earliest date and next dose number for the due immunization.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `IMM_DUE_TYPE_ID` | NUMERIC |  | The type ID of immunization that is due. This column is frequently used to link to the table CLARITY_IMMUNZATN. |
| 6 | `IMM_DUE_TYPE_ID_NAME` | VARCHAR |  | The name of the immunization. |
| 7 | `IMM_DUE_TYPE_FT` | VARCHAR |  | The free text description of the type of immunization that is due. |
| 8 | `IMM_DUE_DUE_DATE` | DATETIME |  | The due date for immunization that is due. |
| 9 | `IMM_DUE_EARLIEST_DT` | DATETIME |  | The earliest date of immunization that is due. |
| 10 | `IMM_DUE_NEXT_DOSE` | VARCHAR |  | The next dose number of immunization that is due. |
| 11 | `IMM_DUE_SCHED_ID_FT` | VARCHAR |  | Immunization schedule ID used for the recommended vaccination. |
| 12 | `IMM_DUE_SCHED_NM_FT` | VARCHAR |  | Immunization schedule name used for the recommended vaccination. |
| 13 | `IMM_DUE_SCHED_CD_FT` | VARCHAR |  | Immunization schedule coding system used for the recommended vaccination. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

