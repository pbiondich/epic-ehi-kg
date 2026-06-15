# PAT_ENC_COMM_MGT

> The patient encounter communication management table stores communication details for a patient. It contains recipient, sender, and communication information for communications created and sent using the communication management module.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 67  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `COMM_SENT_HOUSE_NO` | VARCHAR |  | Communication recipient house number |
| 6 | `COMM_SENT_DISTRCT_C_NAME` | VARCHAR | org | The category number for the district in the communication recipient's address. |
| 7 | `COMM_SENT_COUNTY_C_NAME` | VARCHAR | org | The category number for the county in the communication recipient's address. |
| 8 | `COMM_SENT_UID_ID` | VARCHAR |  | The unique ID of the user who sent the communication. |
| 9 | `COMM_SENT_UID_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `COMM_SENT_INST` | DATETIME (Local) |  | The instant when the communication was sent. |
| 11 | `COMM_SENT_INI` | VARCHAR |  | The record type of the communication's recipient, for example SER for provider, DEP for department, etc. |
| 12 | `COMM_SENT_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 13 | `COMM_SENT_TO_NAME` | VARCHAR |  | Communication recipient name |
| 14 | `COMM_SENT_FAX` | VARCHAR |  | Communication recipient fax number |
| 15 | `COMM_SENT_PHONE` | VARCHAR |  | Communication recipient phone number |
| 16 | `COMM_SENT_ADDR` | VARCHAR |  | The street address of the communication recipient. |
| 17 | `COMM_SENT_CITY` | VARCHAR |  | Communication recipient city |
| 18 | `COMM_SENT_STATE` | VARCHAR |  | Communication recipient state. |
| 19 | `COMM_SENT_ZIP` | VARCHAR |  | Communication recipient zip code. |
| 20 | `COMM_SENT_COUNTRY` | VARCHAR |  | Communication recipient country |
| 21 | `COMM_SENT_METHOD_C_NAME` | VARCHAR | org | The category value for the method used to send the communication. |
| 22 | `COMM_SENT_LTR_NUM` | VARCHAR |  | Letter number of the communication sent |
| 23 | `COMM_SENT_RPT_ID` | VARCHAR |  | The unique ID of the report sent with the communication. |
| 24 | `COMM_SENT_RPT_ID_REPORT_NAME` | VARCHAR |  | The name of the report |
| 25 | `COMM_SENT_OTH_BLBID` | VARCHAR |  | Blob ID of the communication sent |
| 26 | `COMM_SENT_LTR_BLOB` | VARCHAR |  | Letter blob of the communication sent. Only applies to communications sent via fax. |
| 27 | `COMM_SENT_RPT_BLOB` | VARCHAR |  | Report blob of the communication sent. Only applies to communications sent via fax. |
| 28 | `COMM_SENT_STAT_C_NAME` | VARCHAR |  | Communication sent status category number for the communication. |
| 29 | `COMM_SENT_JOB_ID` | VARCHAR |  | The unique ID of the communication job. |
| 30 | `COMM_SENT_BY_USR_ID` | VARCHAR |  | The unique ID of the user (EMP) who actually sent the communication from the communication management module. |
| 31 | `COMM_SENT_BY_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `COMM_SENT_SER_ADDR` | VARCHAR |  | Stores the selected address ID if the recipient is a provider |
| 33 | `COMM_ROUTING_MESSG` | VARCHAR |  | The routing message included when the communication is routed to support staff. |
| 34 | `OR_LOG_ID` | VARCHAR |  | The unique ID of the surgical log (ORL) record associated with the communication note. |
| 35 | `COMM_SENT_HNO_ID` | VARCHAR |  | The unique ID of the note (HNO) record associated with the communication note. |
| 36 | `COMM_SENT_EMP_ID` | VARCHAR |  | The unique ID of the user (EMP) record for the communication recipient. |
| 37 | `COMM_SENT_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 38 | `COMM_IS_OVERDUE_YN` | VARCHAR |  | Indicates whether the communication has been waiting for either transcriptions, results, or both, and is now overdue. A Y indicates that it is overdue. N indicates that the communication is not overdue. |
| 39 | `COMM_PREV_LETTER_YN` | VARCHAR |  | Indicates whether the communication is using a previously sent letter. A Y indicates that the communication is using a previously sent letter. N indicates that the communication is not using a previously sent letter. |
| 40 | `COMM_WAIT_FOR_TX_C_NAME` | VARCHAR |  | Indicates whether the communication is waiting for transcriptions. Yes indicates that the communication is waiting for transcriptions, No indicates that the communication is not waiting for transcriptions, and Resulted indicates that the communication was waiting for a transcription that has since been completed. |
| 41 | `COMM_WAIT_FOR_RES_C_NAME` | VARCHAR |  | Indicates whether the communication is waiting for results. Yes indicates that the communication is waiting for results, No indicates that the communication is not waiting for results, and Resulted indicates the communication was waiting for results that have since been resulted. |
| 42 | `COMM_SENT_DIR_ADDR` | VARCHAR |  | This is the Direct address to which a communication is sent. |
| 43 | `COMM_CREATED_MTH_C_NAME` | VARCHAR | org | This item stores the communication's creation method. "Automatic on Close Encounter" means the communication was created from an automatic communication when the encounter was closed and has not been sent yet. "ED Discharge" is for automatic communications created upon discharge from the emergency department. "IP Discharge" is for automatic communications created upon discharge from an inpatient admission. "Order Transmittal" is for automatic communications created based on order transmittal rules when an order is signed. "Referral Transmittal" is for automatic communications created with referral workqueue functionality. Otherwise, communications created with the Communication Management navigator section or activity will have the "Standard" value. |
| 44 | `COMM_CE_SUB_MTHD_C_NAME` | VARCHAR |  | This is the sub routing method when the routing method "Outside provider messaging" is used in a communication. |
| 45 | `COMM_SENT_EMAIL` | VARCHAR |  | Communication recipient email |
| 46 | `COMM_PRIORITY_C_NAME` | VARCHAR | org | Communication priority |
| 47 | `COMM_SOURCE_RFL_ID` | NUMERIC |  | Stores a referral ID associated with a transition of care communication. |
| 48 | `COMM_SENT_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Communication sent instant in UTC format |
| 49 | `COMM_UPDATE_INST_UTC_DTTM` | DATETIME (UTC) |  | The instant (in UTC) at which the associated communication was last updated. |
| 50 | `COMM_VOID_REASON_C_NAME` | VARCHAR | org | Selected reason for voiding this communication |
| 51 | `COMM_VOID_USER_ID` | VARCHAR |  | User (EMP) ID of user who voided this communication |
| 52 | `COMM_VOID_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 53 | `COMM_VOID_INSTANT_DTTM` | DATETIME (UTC) |  | The instant (in UTC) at which this communication was voided |
| 54 | `CONSENT_DOC_INFO_ID` | VARCHAR |  | The unique ID of the document (DCS) record which grants patient consent for sending the message. |
| 55 | `COMM_SENT_EAF_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 56 | `COMM_SENT_HIP_ID` | NUMERIC |  | The unique ID of the registry (HIP) record for the communication recipient. |
| 57 | `COMM_SENT_HIP_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 58 | `COMM_SENT_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 59 | `COMM_SENT_AGY_ID` | VARCHAR |  | The unique ID of the agency (AGY) record for the communication recipient. |
| 60 | `COMM_SENT_AGY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 61 | `COMM_SENT_DXO_ID` | NUMERIC |  | The unique ID of the data exchange organization (DXO) record for the communication recipient. |
| 62 | `COMM_SENT_DXO_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 63 | `COMM_RES_CMT` | VARCHAR |  | Indicates what was done to resolve the negative or missing acknowledgment |
| 64 | `COMM_VOID_COMMENT` | VARCHAR |  | Comment for communication retraction reason. |
| 65 | `COMM_PRINT_STATUS_C_NAME` | VARCHAR |  | Stores status of print job attached to communication |
| 66 | `COMM_SENT_ORG_ID` | NUMERIC |  | The DXO ID of the organization associated with the recipient's address at the time the communication is sent. |
| 67 | `COMM_SENT_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

