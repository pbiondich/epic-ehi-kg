# DOCS_RCVD_MAMMO_HX

> This table contains information about a patient's mammography history.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MAM_HX_REF_IDENT` | VARCHAR |  | The reference identifier associated with the mammography history. |
| 6 | `MAM_HX_LST_UPD_UTC_DTTM` | DATETIME (UTC) |  | The last update instant of the mammography history in UTC. |
| 7 | `MAM_HX_BASELINE_YN` | VARCHAR |  | Whether or not this is a baseline breast imaging exam. |
| 8 | `MAM_HX_SRC_DOCUMENT_CSN_ID` | NUMERIC |  | The contact serial number of the DXR record that owns the instance of this mammography history. |
| 9 | `MAM_HX_EXT_YN` | VARCHAR |  | Whether the patient's most recent breast imaging exam was performed at an external facility. |
| 10 | `MAM_HX_LST_EXM_FAC` | VARCHAR |  | The name of the external facility where the patient's most recent breast imaging exam was performed. |
| 11 | `MAM_HX_FAC_CMT` | VARCHAR |  | Comment for the name of the facility where the patient's last breast imaging exam was performed. |
| 12 | `MAM_HX_L_EXM_PX_C_NAME` | VARCHAR | org | The type of procedure that was the patient's most recent breast imaging exam. |
| 13 | `MAM_HX_LST_EXM_PX_CMT` | VARCHAR |  | Comment for the patient's most recent breast imaging procedure. |
| 14 | `MAM_HX_LST_EXM_DATE` | DATETIME |  | The date of the patient's most recent breast imaging exam. |
| 15 | `MAM_HX_SELF_EXM_NO_YES_NA_C_NAME` | VARCHAR |  | Whether the patient performs breast self-exams. |
| 16 | `MAM_HX_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

