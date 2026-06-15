# AUTH_REQUEST_HX

> This table contains a snapshot of information about an individual authorization request as of a point in time.

**Overflow family:** [AUTH_REQUEST_HX_2](AUTH_REQUEST_HX_2.md)  
**Primary key:** `AUTH_REQUEST_ID`, `CONTACT_DATE_REAL`  
**Columns:** 66  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier for the authorization request. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `AUTH_REQUEST_CNCT_TYPE_C_NAME` | VARCHAR |  | The contact type category ID for the authorization request. |
| 4 | `UM_STATUS_C_NAME` | VARCHAR |  | The status category ID for the authorization request. |
| 5 | `CONTACT_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the authorization request contact. If this contact is a draft, this column holds the date and time that this draft contact was created. If this contact is published, this column holds the date and time that it was published. |
| 6 | `HISTORY_USER_ID` | VARCHAR |  | The unique ID of the user record of the user who created this contact. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `HISTORY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `AUTH_REQUEST_TYPE_C_NAME` | VARCHAR |  | The request type category ID for the authorization request. |
| 9 | `INSTANT_OF_ENTRY_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of when the authorization request contact was edited. |
| 10 | `FINALIZED_STATUS_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) the finalized status was made on the authorizations in this request. |
| 11 | `SUBMISSION_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the user-override value for the authorization request submission. |
| 12 | `SUBMISSION_RPT_UTC_DTTM` | DATETIME (UTC) |  | The reported submission date and time (UTC) of the authorization request. If an override value is set, the override value is shown. Otherwise, this is the system-calculated value. |
| 13 | `DECISION_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the user-override value for the authorization request decision. |
| 14 | `DECISION_RPT_UTC_DTTM` | DATETIME (UTC) |  | The reported decision date and time (UTC) of the authorization request. If an override value is set, the override value is shown. Otherwise, this is the system-calculated value. |
| 15 | `ADDL_INFO_REQ_SYS_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the system-calculated value of the additional information request. |
| 16 | `ADDL_INFO_REQ_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the user-override value of the additional information request. |
| 17 | `ADDL_INFO_RCPT_SYS_UTC_DTTM` | DATETIME (UTC) |  | The system-calculated date and time (UTC) of the additional information receipt. |
| 18 | `ADDL_INFO_RCPT_OVRIDE_UTC_DTTM` | DATETIME (UTC) |  | The user-override date and time (UTC) of the additional information receipt instant. |
| 19 | `PEER_TO_PEER_OFFER_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) that the peer-to-peer review was offered. |
| 20 | `PEER_TO_PEER_COMPLETE_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) that the peer-to-peer review was completed. |
| 21 | `PRIORITY_C_NAME` | VARCHAR | org | The unique ID of the priority of the authorization request. |
| 22 | `RFL_TYPE_C_NAME` | VARCHAR | org | The service type of the authorization request. This is used for authorization requests opened in Authorization Review. |
| 23 | `SERVICE_REQUESTER_C_NAME` | VARCHAR |  | The unique ID of the requester of the authorization request. |
| 24 | `MEM_RESP_GUID` | VARCHAR |  | A unique key representing the authorized representative associated with the authorization request. This can be used to join to table MEMBER_RESP_PERSON on MEM_RESP_GUID to report on demographic information associated with the authorized representative. |
| 25 | `REF_BY_IS_CONTRACTED_SYS_YN` | VARCHAR |  | The system-calculated value of whether the referred by entity is contracted or not. |
| 26 | `REF_BY_IS_CONTRACTED_OVRIDE_YN` | VARCHAR |  | The user-override value of whether the referred by entity is contracted or not. |
| 27 | `REF_TO_IS_CONTRACTED_SYS_YN` | VARCHAR |  | The system-calculated value of whether the referred to entity is contracted or not. |
| 28 | `REF_TO_IS_CONTRACTED_OVRIDE_YN` | VARCHAR |  | The user-override value of whether the referred to entity is contracted or not. |
| 29 | `MED_DIRECTOR_REVIEW_YN` | VARCHAR |  | Indicates whether medical director review was performed on this authorization request. |
| 30 | `MED_DIRECTOR_REVIEW_USER_ID` | VARCHAR |  | The unique ID of the user who performed medical director review. |
| 31 | `MED_DIRECTOR_REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `DENIED_FOR_LACK_OF_MED_NEC_YN` | VARCHAR |  | Whether the authorization request was denied for lack of medical necessity. |
| 33 | `PEER_TO_PEER_STATUS_C_NAME` | VARCHAR |  | The unique ID of the status of the peer-to-peer review offer. |
| 34 | `ADDL_INFO_EXTENSION_TAKEN_YN` | VARCHAR |  | Whether an additional information request extension was taken for the authorization request. |
| 35 | `MANUAL_EXTENSION_DAYS` | INTEGER |  | The number of manual extension days taken for the authorization request. |
| 36 | `SUBMISSION_SYS_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the system-calculated value for the authorization request submission instant, based on associated communications with a purpose of Request for Authorization. |
| 37 | `DECISN_UM_STATUS_CHANGE_SRC_C_NAME` | VARCHAR |  | The change source category ID that resulted in the decision status being set for the authorization request. |
| 38 | `HISTORY_EDIT_SOURCE_C_NAME` | VARCHAR |  | Where the contact (authorization request edit) was created from. |
| 39 | `ADDL_INFO_REQ_EXT_TKN_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of when additional information request extension was taken for the authorization request. |
| 40 | `ADDL_INFO_REQ_USER_ID` | VARCHAR |  | The unique ID of the user who made the additional info request. |
| 41 | `ADDL_INFO_REQ_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 42 | `MED_DIRECTOR_REVIEW_NOTE_ID` | VARCHAR |  | The unique ID associated with the medical director review note. |
| 43 | `MAN_EXT_DAYS_TKN_DTTM` | DATETIME (Local) |  | The date and time (local) of when manual extension days were taken. |
| 44 | `MAN_EXT_DAYS_TKN_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of when manual extension days were taken. |
| 45 | `MAN_EXT_DAYS_USER_ID` | VARCHAR |  | The unique ID of the user who has taken the manual extension days. |
| 46 | `MAN_EXT_DAYS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 47 | `EXPEDITED_STATUS_C_NAME` | VARCHAR |  | The expedite status of the authorization request. |
| 48 | `RQST_TO_EXPEDITE_DTTM` | DATETIME (Local) |  | The instant of the request to expedite communication in local time zone. |
| 49 | `RQST_TO_EXPEDITE_UTC_DTTM` | DATETIME (UTC) |  | The instant of the request to expedite communication in UTC time zone. |
| 50 | `RQST_TO_EXPEDITE_COMM_ID` | VARCHAR |  | The unique ID of the communication record that represents the request to expedite. |
| 51 | `PRIORITY_UPGRADE_DTTM` | DATETIME (Local) |  | The instant the priority of a standard authorized request changed to a priority that is part of the expedited/urgent priorities list in the system setting in local time zone. |
| 52 | `PRIORITY_UPGRADE_UTC_DTTM` | DATETIME (UTC) |  | The instant the priority of a standard authorized request changed to a priority that is part of the expedited/urgent priorities list in the system setting in UTC time zone. |
| 53 | `PRIORITY_UPGRADE_USER_ID` | VARCHAR |  | The unique ID of the user who changed the priority of a standard authorization request to a priority part of the expedited/urgent priorities list in the system settting. |
| 54 | `PRIORITY_UPGRADE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 55 | `PRIORITY_DOWNGRADE_DTTM` | DATETIME (Local) |  | The instant the priority of an expedited authorization request changed to a priority not part of the expedited/urgent priorities list in the system setting in local time zone. |
| 56 | `PRIORITY_DOWNGRADE_UTC_DTTM` | DATETIME (UTC) |  | The instant the priority of an expedited authorization request changed to a priority not part of the expedited/urgent priorities list in the system setting in UTC time zone. |
| 57 | `PRIORITY_DOWNGRADE_USER_ID` | VARCHAR |  | The unique ID of the user who changed the priority of an expedited authorization request to a priority not part of the expedited/urgent priorities list in the system settting. |
| 58 | `PRIORITY_DOWNGRADE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 59 | `CLM_NET_OVRIDE_STAT_C_NAME` | VARCHAR |  | The network status to override to when adjudicating the linked claim. |
| 60 | `CLM_NET_OVRIDE_LVL_C_NAME` | VARCHAR | org | The network level to override to when adjudicating the linked claim. |
| 61 | `CLM_NET_OVRIDE_RSN_C_NAME` | VARCHAR | org | The reason for override a linked claim's adjudication network. |
| 62 | `OVERTURNED_ON_APPEAL_OVRIDE_YN` | VARCHAR |  | Indicates whether any denied service on this authorization request was later overturned on appeal. Intended to be imported as an override value to the calculated value in AUTH_REQUEST.OVERTURNED_ON_APPEAL_YN. |
| 63 | `ELECTRONIC_SUBMIT_OVERRIDE_YN` | VARCHAR |  | The user-override value for whether the authorization was electronically submitted. |
| 64 | `ELECTRONIC_SUBMIT_REPORT_YN` | VARCHAR |  | The reported value of whether the authorization was electronically submitted. If an override value is set, the override value is shown. Otherwise, this is the system-calculated value. |
| 65 | `FILL_PHARMACY_ID` | NUMERIC |  | Represents the fill pharmacy for the Auth Requests Medication |
| 66 | `FILL_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUTH_REQUEST_ID` | [AUTH_REQUEST](AUTH_REQUEST.md) | sole_pk | high |

