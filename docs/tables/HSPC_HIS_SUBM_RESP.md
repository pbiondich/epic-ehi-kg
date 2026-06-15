# HSPC_HIS_SUBM_RESP

> This table extracts information about Hospice Item Set (HIS) data set responses as obtained from CMS through validation files.

**Primary key:** `DATASET_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DATASET_ID` | NUMERIC | PK shared | The unique identifier for the data set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `HIS_RESP_STATUS_C_NAME` | VARCHAR |  | The response status of an individual dataset submission. This could be "Accepted" or "Rejected". |
| 6 | `HIS_VALD_MRK_INST_DTTM` | DATETIME (UTC) |  | The instant when a dataset submission response status is changed. |
| 7 | `HIS_RES_MRK_USER_ID` | VARCHAR |  | The unique identifier of the user record associated with an update to the status of a dataset submission. If the batch process updated the submission status, this user ID is stored as ". |
| 8 | `HIS_RES_MRK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `HIS_RESP_HNO_ID` | VARCHAR |  | The unique identifier of a note associated with the data set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

