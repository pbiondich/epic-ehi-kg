# HH_OASIS_SUBM_RESP

> Contains information on Outcome and Assessment Information Set (OASIS) data set responses as obtained from the Centers for Medicare and Medicaid Services (CMS) through validation files.

**Primary key:** `OASIS_SET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK FK→ | The unique identifier for the data set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `OAS_RESP_STATUS_C_NAME` | VARCHAR |  | The response status of an individual OASIS submission. This could be "Accepted" or "Rejected". |
| 6 | `OAS_VALD_MRK_DTTM` | DATETIME (UTC) |  | The instant when an OASIS submission response status is changed either by the validation batch process or manually from Home Health Intake or actions taken in Reporting Workbench reports. |
| 7 | `OAS_RES_MRK_USER_ID` | VARCHAR |  | The ID of the user who manually updates the status of an OASIS submission. If the batch process updates the submission status, this user ID is stored as ". |
| 8 | `OAS_RES_MRK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `OAS_RESP_HNO_ID` | VARCHAR |  | The ID of the note corresponding to an individual OASIS submission. The note stores the reason why a submission was marked as Accepted or Rejected. Errors and warnings received from CMS are stored in this note. |
| 10 | `OAS_RESP_EXP_LN` | INTEGER |  | The OASIS export file that generated this response. This number corresponds to a line in Home Health OASIS Data Sets (I LHO 320), which stores all of the exports for a given OASIS data set. |
| 11 | `OAS_VALD_CMS_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the dataset was marked as accepted by CMS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OASIS_SET_ID` | [HH_OASIS_INFO](HH_OASIS_INFO.md) | sole_pk | high |

