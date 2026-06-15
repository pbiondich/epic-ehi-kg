# RADIOTHERAPY_DICOM_INFO

> This table contains identifiers to DICOM files used in the radiotherapy plan.

**Primary key:** `RT_SUMMARY_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RT_SUMMARY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the radiotherapy summary record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `INSTANCE_UID` | VARCHAR |  | UID for a DICOM image. |
| 5 | `SOP_CLASS_SYSTEM` | VARCHAR |  | Stores the system for the associated SOP class. |
| 6 | `SOP_CLASS_SYSTEM_VERSION` | VARCHAR |  | Stores the version of the associated system. |
| 7 | `SOP_CLASS_CODE` | VARCHAR |  | Stores the SOP class code for the associated DICOM instance UID. |
| 8 | `SOP_CLASS_USER_SELECTED_YN` | VARCHAR |  | Stores whether the user manually selected the SOP class code was chosen directly by the user. |
| 9 | `SOP_CLASS_DISPLAY_NAME` | VARCHAR |  | Stores the display name for the associated SOP class code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

