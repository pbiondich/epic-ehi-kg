# DOCS_RCVD

> High level information about received documents.

**Primary key:** `DOCUMENT_ID`  
**Columns:** 46  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `TYPE_C_NAME` | VARCHAR | org | Specifies the document type. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient for this received document. |
| 4 | `DOC_SOURCE_ORG_ID` | NUMERIC |  | Source organization record for this document |
| 5 | `DOC_SOURCE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 6 | `DOC_SET` | VARCHAR |  | Specifies the Set ID for these documents. |
| 7 | `ENC_EVENT_IDENT` | VARCHAR |  | The event identifier for the event contained in this document. Applies only to Encounter Summary records. |
| 8 | `AUTHOR_INST_ID` | NUMERIC |  | Specifies the Author Institution that created the document. |
| 9 | `AUTHOR_INST_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 10 | `REPOSITORY_ID` | VARCHAR |  | The unique ID of the repository holding the received document. |
| 11 | `INVLD_INSTANT_TM` | DATETIME (Local) |  | This item stores the instant this received document was invalidated. |
| 12 | `DOCUMENT_FILE_NAME` | VARCHAR |  | Stores the file name for the document on the BLOB server |
| 13 | `SENDER_REFERRALID` | VARCHAR |  | This item stores the referral ID for Care Everywhere Referral-type external document records as received from the outside organization. The format is OID^ID, where the ID is usually a record ID at the outside organization. |
| 14 | `PHR_ID` | NUMERIC |  | The unique ID of the pharmacy that sent this received document. |
| 15 | `PHR_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 16 | `DOC_CONTENT_TYPE_C_NAME` | VARCHAR | org | Specifies the content type of the document. |
| 17 | `EXTERNAL_EPT_CSN` | NUMERIC |  | For received documents from external systems that Epic rehosts, this stores the patient encounter Contact Serial Number (CSN). |
| 18 | `ATTACHED_DOC_ID` | VARCHAR |  | This item stores the ID of the document record, which contains the attached document that was received. |
| 19 | `EPISODE_UUID` | VARCHAR |  | Stores a UUID identifying an episode of care |
| 20 | `RECORD_STATE_C_NAME` | VARCHAR |  | The record state category ID for this received document. |
| 21 | `DOC_EPSD_IDENT` | VARCHAR |  | The episode identifier of the episode contained in this document. |
| 22 | `INVLD_USER_ID` | VARCHAR |  | The unique ID of the user that invalidated this received document. |
| 23 | `INVLD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `DOC_CONTENT_TYPE` | VARCHAR |  | This is the type of document stored in the record. For Care Everywhere Encounter Summaries, this is the type of encounter stored in this record. |
| 25 | `CAN_HAVE_RESTRICTED_ENC_YN` | VARCHAR |  | Indicates if this Event List row could have restricted encounters |
| 26 | `EXT_MED_PBM_IDENT` | VARCHAR |  | This item stores the PBM ID for the patient. |
| 27 | `RECEIVED_CLINICAL_NOTE_ID` | VARCHAR |  | The ID of the note record automatically created in the local chart from the received clinical note information. |
| 28 | `RX_DOCUMENT_STATUS_C_NAME` | VARCHAR |  | This item tracks the status of a prescription document as it is being processed. |
| 29 | `COVERAGE_ID` | NUMERIC | FK→ | This item stores the CVG ID for which document is being requested. |
| 30 | `RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 31 | `DATA_ORIG_SRC_ORGANIZATION_ID` | NUMERIC |  | This item is set for documents that contain data that was forwarded from an organization external to the source organization in I DXR 70. This is used by Cosmos and Payor Platform to identify the source of unreconciled data. |
| 32 | `DATA_ORIG_SRC_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 33 | `RX_TRANSFER_STATUS_C_NAME` | VARCHAR | org | This item is used during electronic prescription transfers between two pharmacies. This is the current status of the electronic prescription transfer. |
| 34 | `RX_TRANSFER_TO_PHARMACY_ID` | NUMERIC |  | This item is used during electronic prescription transfers between two pharmacies. This is the pharmacy the prescription was transferred to. |
| 35 | `RX_TRANSFER_TO_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 36 | `RX_TRANSFER_FROM_PHARMACY_ID` | NUMERIC |  | This item is used during electronic prescription transfers between two pharmacies. This is the pharmacy the prescription was transferred from. |
| 37 | `RX_TRANSFER_FROM_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 38 | `RX_TRANSFER_TO_USER_ID` | VARCHAR |  | This item is used during electronic prescription transfers between two pharmacies. This is the user for the transfer to pharmacy that authorized the transfer. |
| 39 | `RX_TRANSFER_TO_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 40 | `RX_TRANSFER_FROM_USER_NAME` | VARCHAR |  | This item is used during electronic prescription transfers between two pharmacies. This is the user for the transfer from pharmacy that authorized the transfer. |
| 41 | `RX_TRANSFER_COMMENTS` | VARCHAR |  | This item is used during electronic prescription transfers between two pharmacies. This contains the comments associated with the transfer. |
| 42 | `RX_TRANSFER_REQ_DOCUMENT_ID` | NUMERIC |  | The electronic prescription transfer request document associated with this electrionc prescription transfer response. |
| 43 | `EXT_DEMOG_ID` | NUMERIC |  | Holds a pointer to the REQ record that holds the identifier and demographics that this external document was loaded with, linking this external document data record to an ID bundle. |
| 44 | `AMBNT_PIPE_WKFL_C_NAME` | VARCHAR |  | Stores the workflow that created this ambient session. |
| 45 | `AMBNT_PROCESS_REQ_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant at which the user last requested processing of this session's audio data. Once this is set, the user will not be able to create additional recordings or request processing again. |
| 46 | `RX_TRANSFER_TO_USER_NAME` | VARCHAR |  | This item is used during electronic prescription transfers between two pharmacies. This is the user for the transfer to pharmacy that authorized the transfer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

