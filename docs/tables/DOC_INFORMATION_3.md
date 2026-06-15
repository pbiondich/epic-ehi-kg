# DOC_INFORMATION_3

> The DOC_INFORMATION table contains information about documents, including scanned and electronically signed documents.

**Overflow of:** [DOC_INFORMATION](DOC_INFORMATION.md)  
**Primary key:** `DOCUMENT_ID`  
**Columns:** 14  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `CREATED_BY_SYSTEM_C_NAME` | VARCHAR | org | The system that this document originated from. This is set on a document in a document batch that was created from directory sweep. The source system comes from the directory sweep extension. |
| 3 | `STAFF_COUNTERSIGNED_BY` | VARCHAR |  | The name of the person who countersigned the document. |
| 4 | `DOC_DEMOG_ID` | NUMERIC |  | The demographic set (REQ) record associated with the document. This is only populated for documents created by importing files from a legacy archive system. If a patient (EPT) record's demographics matched the data from the legacy system, the document is also linked to the patient record in I DCS 270. |
| 5 | `COMM_ORIG_DOCUMENT_ID` | VARCHAR |  | This item stores the original Document (DCS) ID when a document is converted to a PDF. |
| 6 | `DOC_DISCLOSED_YN` | VARCHAR |  | This item is set to Yes when this document is disclosed through Release of Information workflows. |
| 7 | `RQSTD_BIN_OBJECTS_C_NAME` | VARCHAR |  | Stores the requested binary object (I ROI 2486) fulfilled by this document. |
| 8 | `DOC_PROXY_MYPT_ID` | VARCHAR |  | Stores WPR ID for the proxy that the document is associated with. This version of the document will be displayed to the proxy instead of the document linked in I DCS 950. Used by Tapestry. |
| 9 | `SENT_BY_FAX_NUM` | VARCHAR |  | The fax number that sent the fax that created the batch this document came from. |
| 10 | `SENT_BY_CALLER_NAME` | VARCHAR |  | The name associated with the sender of the fax that created the batch this document came from. |
| 11 | `RECEIVED_FAX_SENT_DATE` | DATETIME |  | The date the fax vendor says the fax that created the batch this document came from was sent. |
| 12 | `RECD_FAX_SENT_TM` | DATETIME (Local) |  | The time the fax vendor says the fax that created the batch this document came from was sent. |
| 13 | `PROXY_ORIG_DCS_ID` | VARCHAR |  | Stores DCS ID for the original document that this proxy document was generated for. Used by Tapestry. |
| 14 | `FAM_DOC_ID` | NUMERIC | FK→ | The family document this record links to. This is set on records where Document Attachment Level (I DCS 116) is set to Family Document [23]. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FAM_DOC_ID` | [FAM_DOC](FAM_DOC.md) | sole_pk | high |

## Joined in

Inbound joins are tracked on the logical base [DOC_INFORMATION](DOC_INFORMATION.md).

