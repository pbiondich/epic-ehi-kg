# DOC_INFORMATION_2

> The DOC_INFORMATION table contains information about documents, including scanned and electronically signed documents.

**Overflow of:** [DOC_INFORMATION](DOC_INFORMATION.md)  
**Primary key:** `DOCUMENT_ID`  
**Columns:** 57  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `DOC_RDI_ID` | NUMERIC |  | Stores the linked form (RDI) that contains key-value pairs. |
| 3 | `COMM_ORIG_RDI_ID` | NUMERIC |  | This item stores the original form (RDI) ID when a form is converted to a PDF. |
| 4 | `RSH_LAST_UPDATE_USER_ID` | VARCHAR |  | The last user who updated the research data capture form. |
| 5 | `RSH_LAST_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `RSH_LAST_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The last instant this data capture form was updated. |
| 7 | `RSH_FORM_STAT_C_NAME` | VARCHAR |  | Used to indicate whether or not all of the required fields on an esignature document's smartform have been completed. |
| 8 | `DOC_SPEC_TYPE_C_NAME` | VARCHAR | org | The document specialty for a document (DCS) record. |
| 9 | `DOC_SUBSPECIALTY_C_NAME` | VARCHAR | org | This item stores the document subspecialty for a document (DCS) record |
| 10 | `TMPLT_SF_FORM_ID` | VARCHAR |  | The unique ID of the SmartForm used to collect information for this document. Should be used in conjunction with DOC_INFORMATION.TMPLT_SF_CNTCT to identify the SmartForm Record. |
| 11 | `TMPLT_SF_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 12 | `RSH_FORM_NAME` | VARCHAR |  | The instance name for the research data capture form. |
| 13 | `DOCUMENT_USAGE_C_NAME` | VARCHAR |  | The document usage category ID for the document record. |
| 14 | `BLOB_CATEGORY_C_NAME` | VARCHAR | org | The blob category for the document. |
| 15 | `RX_CUST_ID_OWNER_NAM_RECORD_ID` | VARCHAR |  | This item contains a pointer to the name record of the owner of the customer ID used to pick up the prescriptions for the patient from outpatient pharmacies. |
| 16 | `ESIG_ACCESSIBLE_PDF_FILE` | VARCHAR |  | Stores the file name for the accessible PDF of this document on the BLOB. |
| 17 | `SERIES_SEQ_NUM` | INTEGER |  | The sequence number of the series in a DICOM study (attribute 0020,0011). |
| 18 | `PS_SERIES_UID` | VARCHAR |  | The instance UID of the series that has the presentation state for the image. |
| 19 | `PS_UID` | VARCHAR |  | The presentation state instance UID for the image. |
| 20 | `IMAGE_SEQUENCE_NUM` | INTEGER |  | The image sequence number within the series (attribute 0020,0013). |
| 21 | `IMG_SLCT_TYPE_C_NAME` | VARCHAR |  | The category ID indicating how the DICOM image associated with the record was selected, including if it was computer selected or marked as a key image. |
| 22 | `FILE_CREATION_TIME` | VARCHAR |  | Stores the timestamp in HL7 format of when the file was created on the blob or DMS server. |
| 23 | `FILE_LAST_UPD_TIME` | VARCHAR |  | Timestamp in HL7 format of when the image was last updated. |
| 24 | `FILE_TYPE` | VARCHAR |  | Mime type of the image/document. |
| 25 | `CLN_DOC_SRC_APT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The appointment that a Document Information (DCS) record was attached to before it was moved to a Clinical Documentation Only encounter. |
| 26 | `ENROLL_ID` | NUMERIC | FK→ | The unique ID of the research study association that has been linked to this document. |
| 27 | `FILE_CREATION_DTTM` | DATETIME (UTC) |  | Stores the file creation time of the document on the Web Blob Server (WBS) |
| 28 | `DEFERRED_GEN_STATUS_C_NAME` | VARCHAR |  | The deferred generation status category ID for the document. This field is only used for deferred generation documents. |
| 29 | `DOC_TX_ID` | NUMERIC |  | Stores ETR ID for the service-line on a claim that the document is associated with, used by Tapestry |
| 30 | `START_DOC_PERIOD_DATE` | DATETIME |  | Start date of document period. |
| 31 | `END_DOC_PERIOD_DATE` | DATETIME |  | End date of document period. |
| 32 | `CLM_ATTACH_CTL_NUM` | VARCHAR |  | Attachment control number for electronic attachments. This is used to identify electronic attachments for a claim in an ANSI X12 275. |
| 33 | `CLM_PROV_ACCT_NUM` | VARCHAR |  | Provider submitted account number for electronic attachments. This is used to identify electronic attachments for a claim in an ANSI X12 275. |
| 34 | `CLAIM_VENDOR_NPI` | NUMERIC |  | NPI of the vendor sent in ANSI X12 275. This is used to identify electronic attachments for a claim in an ANSI X12 275. |
| 35 | `COPIED_FROM_DOCUMENT_ID` | VARCHAR |  | This item links to the original DCS record that this record was copied from. |
| 36 | `DOCUMENT_IDENT_SOURCE_C_NAME` | VARCHAR |  | Indicates whether the identifier for this document, which is stored in item 350, is a native Epic identifier, or an identifier assigned by external system. When this item is set to 1-Native, the identifier refers to binary data that was uploaded through the Blob service. If the identifier was generated by an external system, this item is set to 2-External. If this item is set to 0-Unknown or not set, then other items must be used to determine if item 350 is a Blob or external identifier. |
| 37 | `EOB_MEMBER_SHARE_AMOUNT` | NUMERIC |  | Total amount a member is responsible for, for all the claims included in an Explanation of Benefits document. |
| 38 | `DOC_SOURCE_ROI_ID` | VARCHAR |  | Stores the ROI ID used to generate a composite document (DCS). A composite document represents one or more contexts which is included in the ROI. |
| 39 | `RX_CUST_ID_BIRTH_DATE` | DATETIME |  | The date of birth of the customer ID holder. |
| 40 | `RX_CUST_ID_CITY` | VARCHAR |  | The city component of the address from the customer ID. |
| 41 | `RX_CUST_ID_STATE_C_NAME` | VARCHAR | org | The state component of the address from the customer ID. |
| 42 | `RX_CUST_ID_ZIP` | VARCHAR |  | The postal code component of the address from the customer ID. |
| 43 | `RX_CUST_ID_COUNTY_C_NAME` | VARCHAR | org | The county component of the address from the customer ID. |
| 44 | `RX_CUST_ID_COUNTRY_C_NAME` | VARCHAR | org | The country component of the address from the customer ID. |
| 45 | `RX_CUST_ID_DISTRCT_C_NAME` | VARCHAR | org | The district component of the address from the customer ID. |
| 46 | `RX_CUST_ID_HOUSE_NUM` | VARCHAR |  | The house number component of the address from the customer ID. |
| 47 | `CREATED_BY_USER_ID` | VARCHAR |  | The user who created the document. |
| 48 | `CREATED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 49 | `CREATED_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time the document was created. |
| 50 | `INDEXED_BY_USER_ID` | VARCHAR |  | The user who indexed the document. |
| 51 | `INDEXED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 52 | `INDEXED_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time the document was indexed. |
| 53 | `DOC_APPEAL_GRV_ID` | NUMERIC |  | Stores the TAG ID for the appeal or grievance that the document is associated with. |
| 54 | `DEPTH_CAPT_STATUS_C_NAME` | VARCHAR |  | Whether depth information was captured on an image, or why depth was unable to be obtained. Only applies to images. |
| 55 | `LINK_DEPTH_DCS_ID` | VARCHAR |  | Stores the ID for the DCS record of the depth map taken with the image. |
| 56 | `DEPTH_ACCURACY_C_NAME` | VARCHAR |  | Depth map accuracy measured on mobile when taking a wound image. |
| 57 | `DEPTH_QUALITY_C_NAME` | VARCHAR |  | Depth map quality measured on mobile when taking a wound image. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLN_DOC_SRC_APT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

## Joined in

Inbound joins are tracked on the logical base [DOC_INFORMATION](DOC_INFORMATION.md).

