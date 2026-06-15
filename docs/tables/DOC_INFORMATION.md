# DOC_INFORMATION

> The DOC_INFORMATION table contains information about documents, including scanned and electronically signed documents.

**Overflow family:** [DOC_INFORMATION_2](DOC_INFORMATION_2.md), [DOC_INFORMATION_3](DOC_INFORMATION_3.md)  
**Primary key:** `DOC_INFO_ID`  
**Columns:** 79  
**Org-specific columns:** 9  
**Joined by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOC_INFO_ID` | VARCHAR | PK | The unique ID of the document information record. |
| 2 | `DOC_INFO_TYPE_C_NAME` | VARCHAR | org | The type of document described by this document information. |
| 3 | `DOC_STAT_C_NAME` | VARCHAR | org | The current status of the document described by this document information. |
| 4 | `DOC_DESCR` | VARCHAR |  | A short free text description of the document described by this document information. |
| 5 | `DOC_RECV_TIME` | DATETIME (Local) |  | The date and time the document described by this document information was received. |
| 6 | `RECV_BY_USER_ID` | VARCHAR |  | The employee who received the document described by this document information. This ID may be encrypted. |
| 7 | `RECV_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `PAT_REP` | VARCHAR |  | The free text name of the person who legally represents the patient described by this document information. |
| 9 | `DT_ON_DOC` | DATETIME |  | The date which appears on the document described by this document information. |
| 10 | `DOC_EXPIR_TIME` | DATETIME (Local) |  | The date and time the document described by this document information expires. |
| 11 | `DOC_LOC` | VARCHAR |  | A short free text description of the location of the paper copy of the document described by this document information. |
| 12 | `IS_SCANNED_YN` | VARCHAR |  | Specifies whether there is a scanned image version of the document described by this document information. |
| 13 | `SCAN_TIME` | DATETIME (Local) |  | The date and time the document described by this document information was scanned. |
| 14 | `SCAN_BY_USER_ID` | VARCHAR |  | The employee who scanned the document described by this document information. This ID may be encrypted. |
| 15 | `SCAN_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 16 | `SCAN_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 17 | `SCAN_FILE` | VARCHAR |  | The file name of the scanned image version of the document described by this document information. |
| 18 | `IS_ESIGNED_YN` | VARCHAR |  | Specifies whether the document described by this document information has been electronically signed. |
| 19 | `ESIGN_TIME` | DATETIME (Local) |  | The date and time the document described by this document information was electronically signed. |
| 20 | `WITNESS_BY_USER_ID` | VARCHAR |  | The employee who witnessed the electronic signing of the document described by this document information. This ID may be encrypted. |
| 21 | `WITNESS_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 22 | `ESIGN_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 23 | `ESIGN_HTML_FILE` | VARCHAR |  | The file name of either the template HTML file of the document to be electronically signed prior to it being electronically signed or the unique file name of the HTML file of the electronically signed document described by this document information. |
| 24 | `DOC_REQ_DT` | DATETIME |  | The date when a copy of the type of document described by this document information was requested. |
| 25 | `IS_REQ_YN` | VARCHAR |  | Specifies whether the type of document described by this document information was requested. |
| 26 | `DOC_EFF_TIME` | DATETIME (Local) |  | The date and time the document described by this document information becomes effective. |
| 27 | `IS_EFF_YN` | VARCHAR |  | Specifies whether the document is in effect. |
| 28 | `DOC_DISCL_DT` | DATETIME |  | The date when a copy of the document described by this document information was last disclosed. |
| 29 | `DOC_REVOK_DT` | DATETIME |  | The date when the type of document described by this document information was revoked. |
| 30 | `IS_REVOK_YN` | VARCHAR |  | Specifies whether the document was revoked. |
| 31 | `DOC_LOCATION_C` | VARCHAR | org | The category entry for the location of the document. |
| 32 | `DOC_PT_ID` | VARCHAR |  | The unique ID of the patient associated with the document record. |
| 33 | `DOC_CSN` | NUMERIC |  | This stores the contact serial number of the encounter that this record is attached to, if applicable. |
| 34 | `DOC_MEM_ID` | VARCHAR |  | Stores EPT id for the member that the document is associated with, used by Tapestry |
| 35 | `DOC_CLM_ID` | NUMERIC |  | Stores Claim (CLM) ID for the claim that the document is associated with, used by Tapestry. |
| 36 | `DOC_CVG_ID` | NUMERIC |  | Stores Coverage (CVG) ID for the coverage that the document is associated with, used by Tapestry. |
| 37 | `DOC_NCS_ID` | NUMERIC |  | Stores customer service (NCS) ID for the customer relationship management (CRM) that the document is associated with, used by Tapestry. |
| 38 | `DOC_NMM_ID` | NUMERIC |  | Stores the case master (NMM) ID for the case that the document is associated with, used by Tapestry. |
| 39 | `DOC_PBA_ID` | VARCHAR |  | Stores PBA id for the PB Account that the document is associated with, used by Tapestry |
| 40 | `DOC_RFL_ID` | NUMERIC |  | Stores Referral (RFL) ID for the Referral that the document is associated with, used by Tapestry. |
| 41 | `DOC_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 42 | `RECORD_STATE_C_NAME` | VARCHAR |  | The record state category number for the document record. |
| 43 | `SOURCE_ETX_ID` | VARCHAR |  | Stores the SmartText (ETX) ID that this document (DCS) record was created from. |
| 44 | `SOURCE_ETX_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 45 | `DOC_HNO_ID` | VARCHAR |  | The unique ID of the note record associated with this document. |
| 46 | `SCAN_LWS_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |
| 47 | `ESIG_SIGNED_BY` | VARCHAR |  | eSignature of person document was signed by. |
| 48 | `ESIGNED_REL_C_NAME` | VARCHAR | org | The relationship between the patient and the person who signed the form (self, parent, spouse, etc.). |
| 49 | `DOC_SRVC_DTTM` | DATETIME (Local) |  | The service date and time of the document. |
| 50 | `SCAN_INST_DTTM` | DATETIME (Local) |  | This item stores the most clinically relevant date for the document. From top to bottom, it looks to the service date/time (I DCS 246/247), the order prioritized instant (I ORD 24), the encounter date, and the import date/time (I DCS 310/315). |
| 51 | `DOC_STORAGE_LVL_C_NAME` | VARCHAR |  | The level at which the document is attached to the patient's record. For example, the document could be stored at the patient, encounter, or hospital account level. |
| 52 | `SOURCE_DOC` | VARCHAR |  | The identifier for the document (DCS) record's source document. This column is only populated for DCS records of type Discharge Attachments. If the document was created from a SmartText (ETX) record, this column contains the ID of that ETX record. If the document was created from an HTML document in the References Activity, this column contains the unique identifier from the CRS.mdb file. |
| 53 | `DOC_CREAT_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 54 | `PT_ENT_DRAW_STAT_C_NAME` | VARCHAR |  | Holds the status of the documents (DCS) record - Is it ready to show? |
| 55 | `PT_ENT_DRAWING_CMT` | VARCHAR |  | Holds any associated comments from a patient-entered drawing question. Only present for documents (DCS) records of type 32010 used by MyChart and Welcome. |
| 56 | `PHOTO_APPROVED_C_NAME` | VARCHAR | org | Whether or not this document (DCS) record is in the history of the patient's photos. If not, includes the reason the photo was rejected. |
| 57 | `PHOTO_APRV_APPL_C_NAME` | VARCHAR |  | The application that processed the approval/denial of the photo. |
| 58 | `WEB_USER_ID` | VARCHAR |  | This item holds the ID of the MyChart user who created this document record, for patient-generated document records. |
| 59 | `NEED_ENC_YN` | VARCHAR |  | This item is used to denote whether a document needs to be attached to an encounter or not. For Patient level documents this would always be No. For encounter level documents, depending on whether it is attached or detached from an encounter, this would say No or Yes respectively. |
| 60 | `PERFORMING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 61 | `ESIG_TMPLT_USED` | NUMERIC |  | Stores a link to the template used to sign the document |
| 62 | `TMPLT_SF_CNTCT` | NUMERIC |  | Contact of the SmartForm used to collect information for this document. |
| 63 | `RESEARCH_STUDY_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 64 | `FT_CONSENT_PROCS` | VARCHAR |  | Stores free text procedures for consent documents |
| 65 | `ORIGINAL_DOC_ID` | VARCHAR |  | Stores the link to the original (unannotated) document. |
| 66 | `DOC_SPECIALTY_C_NAME` | VARCHAR | org | This item can be extended to hold possible values for the specialty that a document can be associated with. |
| 67 | `DOC_SRVR_NAME_C_NAME` | VARCHAR | org | This item stores the desktop integration (FDI) record that was used for scanning the document. |
| 68 | `DOC_SOURCE_INFO_C_NAME` | VARCHAR |  | Determines the source of the document rather than the document's type. |
| 69 | `RX_CUST_ID_TYPE_C_NAME` | VARCHAR | org | This item contains the categories for the types of customer ID documents used to pick up prescriptions from outpatient pharmacies. |
| 70 | `RX_CUST_ID_NUM` | VARCHAR |  | This item contains the customer ID number. |
| 71 | `CE_SERVICE_START_DATE` | DATETIME |  | Service start date for a received Care Everywhere external authorization |
| 72 | `CE_SERVICE_END_DATE` | DATETIME |  | Service end date for a received Care Everywhere external authorization |
| 73 | `DOC_PND_APRV_STAT_C_NAME` | VARCHAR |  | Holds status of document undergoing review |
| 74 | `DOC_REJ_RSN_C_NAME` | VARCHAR | org | Denial reason |
| 75 | `DOC_REJ_RSN_TEXT` | VARCHAR |  | Rejection reason freetext |
| 76 | `COMM_ORIG_LRP_ID` | VARCHAR |  | This item stores the original report (LRP) ID when a report is converted to a PDF. |
| 77 | `COMM_ORIG_LRP_ID_REPORT_NAME` | VARCHAR |  | The name of the report |
| 78 | `CREATED_STUDY_AMENDMENT` | INTEGER |  | The ID of the research study amendment considered to be the consent version signed for Research Consent type document (DCS) records. Use the RESEARCH_STUDY_ID column to link to RESEARCH_VERSION_INFO table which has the user-entered version number (STUDY_VERSION) as well as other information. |
| 79 | `EFF_STUDY_AMENDMENT` | INTEGER |  | The ID of the research study amendment considered to be the current effective version for Research Consent type document (DCS) records. Use the RESEARCH_STUDY_ID column to link to RESEARCH_VERSION_INFO table which has the user-entered version number (STUDY_VERSION) as well as other information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (10)

| From | Column | Confidence |
|------|--------|------------|
| [BDC_INFO](BDC_INFO.md) | `DOC_INFO_ID` | high |
| [CHART_REVIEW_BOOKMARKS](CHART_REVIEW_BOOKMARKS.md) | `DOC_INFO_ID` | high |
| [CL_QANSWER_QA](CL_QANSWER_QA.md) | `DOC_INFO_ID` | high |
| [DATA_CAPTURE_FORMS](DATA_CAPTURE_FORMS.md) | `DOC_INFO_ID` | high |
| [DOC_INFO_NOTES](DOC_INFO_NOTES.md) | `DOC_INFO_ID` | high |
| [DOC_LINKED_ORDERS](DOC_LINKED_ORDERS.md) | `DOC_INFO_ID` | high |
| [FLOWSHEET_IMG_LINK](FLOWSHEET_IMG_LINK.md) | `DOC_INFO_ID` | high |
| [PATIENT_DOCS](PATIENT_DOCS.md) | `DOC_INFO_ID` | high |
| [PAT_ENC_DOCS](PAT_ENC_DOCS.md) | `DOC_INFO_ID` | high |
| [V_EHI_AUDIT_DCS](V_EHI_AUDIT_DCS.md) | `DOC_INFO_ID` | high |

