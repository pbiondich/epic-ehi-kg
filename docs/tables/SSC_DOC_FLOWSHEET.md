# SSC_DOC_FLOWSHEET

> This table contains information about patient-level SmartSet Information records with a data row type of Documentation Flowsheet. This table is populated only for patient-level SmartSet Information records with a data row type of Documentation Flowsheet.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique ID of the patient-level SmartSet Information record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `DOC_FLOWSHEET_ID` | VARCHAR |  | The unique IDs of the Doc Flowsheet Rows or Groups that are associated with this SmartSet Information record and have been added to the patient's chart. |
| 5 | `DOC_FLOWSHEET_ID_DISP_NAME` | VARCHAR |  | The display name given to the flowsheet group/row. |
| 6 | `DOC_FLOWSHEET_DAT` | VARCHAR |  | The DAT of the Doc Flowsheet Row or Group that is associated with this SmartSet Information record and has been added to the patient's chart. |
| 7 | `FLOWSHEET_TEMPLT_ID` | VARCHAR |  | The unique ID of the Flowsheet Template to which the Doc Flowsheet Row or Group from DOC_FLOWSHEET_ID has been added. |
| 8 | `FLOWSHEET_TEMPLT_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

