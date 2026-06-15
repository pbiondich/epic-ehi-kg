# DOCS_RCVD_DETAILS_2

> This record provides details about received documents including audit request information.

**Overflow of:** [DOCS_RCVD_DETAILS](DOCS_RCVD_DETAILS.md)  
**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`  
**Columns:** 41  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) for the document received record |
| 4 | `HISTORICAL_DOCUMENT_INFO_ID` | VARCHAR |  | Historical document information (DCS) records for the object. |
| 5 | `PAT_GEN_IDN_C_NAME` | VARCHAR | org | Patient gender identity for the patient associated with the incoming document. |
| 6 | `PAT_SAAB_C_NAME` | VARCHAR | org | Patient sex assigned at birth for the patient associated with the incoming document. |
| 7 | `SOURCE_RFL_ID` | NUMERIC |  | When receiving a referral complete message for an encounter in another organization, this item links the encounter document to the initiating referral record. |
| 8 | `HAS_INSURANCE_INFO_YN` | VARCHAR |  | Indicates whether or not this contact has insurance updates. |
| 9 | `AUTHOR_NATL_PROV_IDENT` | VARCHAR |  | The National Provider ID of the author. |
| 10 | `ERX_PATIENT_LANGUAGE_C_NAME` | VARCHAR | org | This item represents the patient's preferred language for the external prescription. |
| 11 | `ERX_PREVENT_RENEWAL_YN` | VARCHAR |  | This item represents whether refill requests should not be sent to the authorizing provider for this external prescription. |
| 12 | `AUDIT_SOURCE_RFL_ID` | NUMERIC |  | Stores history of Source Referral ID. |
| 13 | `UPDATE_NOTIF_TYPE_C_NAME` | VARCHAR |  | If the received message was an Update Notification, this column describes the event that triggered the Update Notification. |
| 14 | `PEHX_SRC_MYPT_ID` | VARCHAR |  | The MyChart user who answered the history question for the contact. |
| 15 | `PEHX_SRC_USER_ID` | VARCHAR |  | The user who answered the history question in non-captive mode for the contact. |
| 16 | `PEHX_SRC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `HAS_MED_HX_INFO_YN` | VARCHAR |  | This column indicates whether the contact stores discrete medical history information. |
| 18 | `ERX_MIXTURE_FORM_C_NAME` | VARCHAR | org | This column stores the mixture form of a mixture-based medication. |
| 19 | `EVENT_CE_NOTIFICATN_TYP_C_NAME` | VARCHAR |  | This item describes the type of event which the message represents and is used for displaying the event type in In Basket messages. This item is only set for Event Notifications. |
| 20 | `PUSH_MESSAGE_TYPE_C_NAME` | VARCHAR |  | The incoming message type category ID for the Received Direct messages. |
| 21 | `PEHX_SRC_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the contact serial number (CSN) of the encounter a history question submission is associated with. |
| 22 | `HAS_ICU_STAY_UPD_YN` | VARCHAR |  | Indicates whether the external document record contact has updated ICU stay data. |
| 23 | `FHIR_BINARY_URL` | VARCHAR |  | Contains the URL at which the attachment content can be retrieved |
| 24 | `IMR_REPLY_RCVD_INST_UTC_DTTM` | DATETIME (UTC) |  | Instant the most recent reply was received from the remote organization |
| 25 | `RELATES_TO` | VARCHAR |  | Stores the content of the RelatesTo header from a direct message. |
| 26 | `REPLYTO_ADDRESS_EXT_ADDR_ID` | NUMERIC |  | The unique ID of the External Address record to which replies to this message should go. This item is only populated for messages sent through Direct SMTP. |
| 27 | `REPLYTO_ADDRESS_EXT_ADDR_ID_MIXED_DIRECT_ADDR` | VARCHAR |  | Formatted like an email address, this is how Direct messaging knows where to send a message. This item is stored in mixed case to use in display in addressing. |
| 28 | `MATCH_UPDATE_ON_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the patient record match is updated for a Received Document. |
| 29 | `PAT_NAME_PREFIX` | VARCHAR |  | This column contains the title associated with the patient's name. |
| 30 | `EXT_MED_COVERAGE_IDENT` | VARCHAR |  | This item stores the coverage ID of the patient under each PBM. |
| 31 | `PAT_COUNTY_C_NAME` | VARCHAR | org | The county of the patient's address from the received document. NOTE: Not all DXR use cases discretely parse this item. |
| 32 | `PAT_LIVING_STAT_C_NAME` | VARCHAR |  | Holds status information about whether the patient is deceased. NOTE: Not all DXR use cases discretely parse this item. |
| 33 | `PAT_DEATH_DATE` | DATETIME |  | Holds information about when the patient died if known in the received document. NOTE: Not all DXR use cases discretely parse this item. |
| 34 | `PAT_MARITAL_STAT_C_NAME` | VARCHAR |  | Holds discrete marital status information from the received document. |
| 35 | `PAT_MARITAL_STAT_TEXT` | VARCHAR |  | Holds the display name of the received document for remapping purposes. |
| 36 | `HAS_NOTE_SECTION_YN` | VARCHAR |  | This item indicates whether the contact stores note section data. |
| 37 | `HAS_TREAT_RESTR_UPD_YN` | VARCHAR |  | Indicates whether the contact stores treatment restrictions |
| 38 | `CLINICAL_NOTE_CSN_ID` | NUMERIC |  | The unique contact serial number of the Clinical Note contact containing the text retrieved as a part of this received document's contact. |
| 39 | `DOCUMENT_TITLE` | VARCHAR |  | Free text title of a received document |
| 40 | `EXTERNAL_ORDER_NET_IDENT` | VARCHAR |  | The external order ID. This is used to link the document (DXR) to an order in the local organization by matching the value stored in this field to an order with the same unique external order ID (I ORD 30600). |
| 41 | `INT_FAILURE_REASON_C_NAME` | VARCHAR |  | Reason for document failure |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PEHX_SRC_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

