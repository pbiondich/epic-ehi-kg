# DOCS_RCVD_COM_RESRC_USAGE

> Contains information about a member/patient's community resource usages, as received from an outside organization over Care Everywhere or Payer Platform.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `COMM_RESRC_USAGE_REF_IDENT` | VARCHAR |  | This column stores the unique reference ID of a discrete community resource usage. |
| 6 | `COMM_RESRC_USAGE_STATUS_C_NAME` | VARCHAR |  | Stores the status of if a member/patient is currently using this community resource. |
| 7 | `COMM_RESRC_REQ_STATUS_C_NAME` | VARCHAR | org | This column stores the request status. The request status answers the question of "was the request to use this community resource sent to that community resource and did they receive it, did it get canceled, etc.?" |
| 8 | `COMM_RESRC_STREET_ADDR` | VARCHAR |  | This column stores the street address of the community resource being used. |
| 9 | `COMM_RESRC_COUNTY_C_NAME` | VARCHAR | org | This column stores the county for the community resource being used. |
| 10 | `COMM_RESRC_CITY` | VARCHAR |  | This column stores the city of the community resource being used. |
| 11 | `COMM_RESRC_ADDR_STATE_C_NAME` | VARCHAR | org | This column stores the state of the community resource being used. |
| 12 | `COMM_RESRC_POSTAL_CODE` | VARCHAR |  | This column stores the postal code of the community resource being used. |
| 13 | `COMM_RESRC_COUNTRY_C_NAME` | VARCHAR | org | This column stores the country of the community resource being used. |
| 14 | `COMM_RESRC_REFERRED_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant that the community resource was first documented or referred to the member or patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

