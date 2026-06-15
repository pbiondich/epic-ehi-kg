# DOCS_RCVD_WADO_REQUESTS

> This table holds an audit of outgoing WADO-RS requests.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `REQUEST_TOKEN` | VARCHAR |  | An Imaging Study retrieval is made up of one or more WADO-RS requests. Each line in this related group represents an individual request. This item holds the request ID of the WADO-RS request. |
| 6 | `SERIES_IDENT` | VARCHAR |  | An Imaging Study retrieval is made up of one or more WADO-RS requests. Each line in this related group represents an individual request. This item holds the series UID listed in the WADO-RS query string. It corresponds to the DICOM series instance UID (I DCM 2000) in the corresponding DCM record. |
| 7 | `REQ_STATUS_RCVD_C_NAME` | VARCHAR |  | An Imaging Study retrieval is made up of one or more WADO-RS requests. Each line in this related group represents an individual request. This item holds the status of the WADO-RS request. By comparison, the contact-level current status (I DXR 180) represents the overall status of the Imaging Study retrieval across all WADO-RS requests. For example, if one WADO-RS request is 3-Document Received and another is 5-Request Failed, the contact-level current status will be 22-Mixed. |
| 8 | `SENT_INST_UTC_DTTM` | DATETIME (UTC) |  | An Imaging Study retrieval is made up of one or more WADO-RS requests. Each line in this related group represents an individual request. This item holds the instant the WADO-RS request was put on the outgoing Interconnect queue. |
| 9 | `RCVD_INST_UTC_DTTM` | DATETIME (UTC) |  | An Imaging Study retrieval is made up of one or more WADO-RS requests. Each line in this related group represents an individual request. This item holds the instant at which we audited the response to the WADO-RS request. This will often not be the actual instant we received the WADO-RS response but rather the instant we received acknowledgment that the requested instances were stored to the local PACS/VNA. In the event an error occurs which prevents the requested instances from being returned, we will not be able to store anything; thus, this will represent the instant we received the error response. |
| 10 | `REQ_STA_RSN_CD_C_NAME` | VARCHAR |  | An Imaging Study retrieval is made up of one or more WADO-RS requests. Each line in this related group represents an individual request. This item holds the discrete error code returned in the WADO-RS response (if one exists). |
| 11 | `ERROR_COMMENT` | VARCHAR |  | An Imaging Study retrieval is made up of one or more WADO-RS requests. Each line in this related group represents an individual request. This item holds the error comment returned in the WADO-RS response (if one exists). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

