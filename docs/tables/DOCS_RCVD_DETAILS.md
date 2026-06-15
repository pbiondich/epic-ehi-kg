# DOCS_RCVD_DETAILS

> Details about received documents, including request audit information.

**Overflow family:** [DOCS_RCVD_DETAILS_2](DOCS_RCVD_DETAILS_2.md), [DOCS_RCVD_DETAILS_3](DOCS_RCVD_DETAILS_3.md)  
**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 52  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The unique contact serial number (CSN) of the Received Document contact. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 5 | `DOCUMENT_EXT` | VARCHAR |  | UUID for this document |
| 6 | `DOCUMENT_ORIGIN_C_NAME` | VARCHAR |  | How the document was requested |
| 7 | `DOCUMENT_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 8 | `DOCUMENT_DESC` | VARCHAR |  | Free text description of the contents of the document |
| 9 | `CEID` | VARCHAR |  | The patient Care Everywhere ID used for this request |
| 10 | `STRUCT_TYPE_C_NAME` | VARCHAR |  | Data type of the document being stored |
| 11 | `RECV_INST` | DATETIME (Local) |  | Instant the document was received from the remote organization |
| 12 | `DOC_KIND_C_NAME` | VARCHAR |  | The kind of document being stored here |
| 13 | `REQUEST_REASON_C_NAME` | VARCHAR |  | Reason for initiating the document request |
| 14 | `REQUEST_EXPLNATION` | VARCHAR |  | Free text explanation for requesting the document |
| 15 | `REQUEST_VST_PRV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 16 | `RECORD_CREATE_INST` | DATETIME (Local) |  | Instant of creation |
| 17 | `REC_CREATE_USR_ID` | VARCHAR |  | User |
| 18 | `CONSENT_DOC_REC_ID` | VARCHAR |  | If authorization was required for this document request then the ID of the document information record (DCS) for the authorization will be stored here. |
| 19 | `LETTER_CSN` | NUMERIC |  | Stores the Contact Serial Number (CSN) of the patient contact where additional information in this received document record is stored. |
| 20 | `REFERRAL_ID` | NUMERIC | FK→ | This item stores the referral record identifier for the referral on the local organization associated with this received document record. |
| 21 | `LETTER_ID` | VARCHAR |  | This item stores the note record identifier of the letter associated with this received document record. |
| 22 | `LETTER_NUM` | INTEGER |  | Stores the letter number of the letter associated with this external document record. The letter number corresponds to a line number in EPT related group 20200 which stores patient letters. |
| 23 | `EOW_ID` | VARCHAR |  | The In Basket message (EOW) that triggered this request. |
| 24 | `PAT_NAME` | VARCHAR |  | Patient name column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient name that was received in the document's metadata. |
| 25 | `PAT_FAMILY_NAME` | VARCHAR |  | Patient family name column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient's family name that was received in the document's metadata. |
| 26 | `PAT_NAME_SUFFIX` | VARCHAR |  | Patient name suffix column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient's name's suffix that was received in the document's metadata. |
| 27 | `PAT_CITY` | VARCHAR |  | The patient city received as a part of a document from an external system. |
| 28 | `PAT_STATE_C_NAME` | VARCHAR | org | Patient state column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient's state that was received in the document's metadata. |
| 29 | `PAT_ZIP` | VARCHAR |  | The patient's postal code. When a document is received from an external system, it contains certain metadata supplied by the sending system regarding the document. This column contains the patient's postal code that was received in the document's metadata. |
| 30 | `PAT_COUNTRY_C_NAME` | VARCHAR | org | The patient country received as a part of a document from an external system. |
| 31 | `PAT_SEX_C_NAME` | VARCHAR | org | Patient sex column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient's sex that was received in the document's metadata. |
| 32 | `PAT_DOB_DT` | DATETIME |  | Patient date of birth column. When a document is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the patient's date of birth that was received in the document's metadata. |
| 33 | `SUBSET_TITLE` | VARCHAR |  | Stores the title of the submission set received in an incoming Provide and Register message. Its value is supplied by the sending system. |
| 34 | `SUBSET_CMT` | VARCHAR |  | Submission set comments column. This column stores the comments associated with a submission set received in an incoming Provide and Register message. Its value is supplied by the sending system. |
| 35 | `AUTHOR_ID` | VARCHAR |  | Author ID column. This column stores the author ID associated with a document or submission set received in an incoming Provide and Register message. Its value is supplied by the sending system. This may be an ID from any codeset, and the codeset is not included in the document submission. |
| 36 | `AUTHOR_NAME` | VARCHAR |  | Author name column. This column stores the author name associated with a document or submission set received in an incoming Provide and Register message. Its value is supplied by the sending system. |
| 37 | `PAT_DEST_ID` | VARCHAR |  | The patient destination identifier for this external document received from the sending organization. |
| 38 | `DEST_LOC_DXO_ID` | NUMERIC |  | The destination location organization record (DXO) ID to which the message is sent (set only if it is different from local organization record ID). |
| 39 | `DEST_LOC_DXO_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 40 | `CE_TOKEN` | VARCHAR |  | This column contains the patient Care Everywhere token from the source organization of the received document. |
| 41 | `CREAT_INST_DTTM` | DATETIME (Local) |  | Instant the received document was created in the sender organization |
| 42 | `PAT_SSN` | VARCHAR |  | Patient's Social Security Number (SSN) from an incoming message. |
| 43 | `PAT_HOME_PH` | VARCHAR |  | Patient's home phone number. |
| 44 | `PAT_WORK_PH` | VARCHAR |  | Patient's work phone number from an incoming message. |
| 45 | `PAT_CELL_PH` | VARCHAR |  | Patient's mobile phone number. |
| 46 | `SRC_LOC_DXO_ID` | NUMERIC |  | The document source location organization ID from which the message is sent. It is set only if it is different from the source organization ID (I DXR 70). |
| 47 | `SRC_LOC_DXO_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 48 | `ERX_CONTROLLED_YN` | VARCHAR |  | This column indicates whether the external e-prescription accepted through the incoming e-prescribing interface is for a controlled substance. |
| 49 | `INC_CONTEXT_C_NAME` | VARCHAR | org | The context of the submission set that contains the documents for a received Provide and Register message. |
| 50 | `AUTHOR_ADDRESS` | VARCHAR |  | This item stores the address of the document author. |
| 51 | `AUTHOR_PHONE` | VARCHAR |  | This item stores the phone number of the document author. |
| 52 | `PAT_HOUSENUMBER` | VARCHAR |  | Patient's house number from an incoming message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

