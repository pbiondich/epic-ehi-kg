# CUST_SRVC_FAX_HX

> This table extracts the fax history for the Customer Relationship Management record.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the communication record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `FAX_COMM_BY_USER_ID` | VARCHAR |  | This item stores the user who sent the fax. |
| 4 | `FAX_COMM_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `FAX_COMM_DTTM` | DATETIME (Local) |  | This item stores the instant of communication for the fax. |
| 6 | `FAX_COMM_INI` | VARCHAR |  | This item stores the master file initials of the fax recipient if the fax recipient is an existing master file record. |
| 7 | `FAX_COMM_NAME` | VARCHAR |  | This item stores the name of the fax recipient. |
| 8 | `FAX_COMM_FAX_NUM` | VARCHAR |  | This item stores the fax number of the fax recipient. |
| 9 | `FAX_COMM_PHONE_NUM` | VARCHAR |  | This item stores the phone number of the fax recipient. |
| 10 | `FAX_COMM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `FAX_COMM_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 12 | `FAX_COMM_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 13 | `FAX_COMM_PHRM_ID` | NUMERIC |  | The unique ID of the pharmacy which received the fax. |
| 14 | `FAX_COMM_PHRM_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

