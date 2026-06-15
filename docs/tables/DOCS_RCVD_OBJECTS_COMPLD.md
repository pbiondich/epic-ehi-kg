# DOCS_RCVD_OBJECTS_COMPLD

> This table contains the most recently received metadata for each object the external organization has indicated we could retrieve.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `OBJECT_VERSION_IDENT` | VARCHAR |  | The Universal Unique Identifier (UUID) for the binary object. |
| 4 | `OBJECT_SET_IDENT` | VARCHAR |  | The document set ID that represents a common identifier across all document revisions. |
| 5 | `OBJECT_EXTERNAL_TYPE` | VARCHAR |  | The type assigned to the object at the sending organization. |
| 6 | `DOCUMENT_TYPE_GROUP_C_NAME` | VARCHAR |  | The object's document type group (I ECT 55330 value). |
| 7 | `OBJECT_MIME_TYPE_C_NAME` | VARCHAR |  | The format used to store the object. |
| 8 | `OBJECT_DIMENSIONS` | VARCHAR |  | The width and height of the object in pixels. |
| 9 | `OBJECT_SPECIALTY` | VARCHAR |  | The name of the specialty this object is associated with. The specialty listed is the department specialty from the received object. |
| 10 | `OBJECT_PROV` | VARCHAR |  | Provider or user associated with this image. |
| 11 | `DICOM_STUDY_UID` | VARCHAR |  | The Digital Imaging and Communications in Medicine (DICOM) Study Instance Unique Identifier (UID) as recorded by the image archive. |
| 12 | `DICOM_SERIES_UID` | VARCHAR |  | The Digital Imaging and Communications in Medicine (DICOM) Series Instance Unique Identifier (UID) for the imaging series. |
| 13 | `DICOM_SERIES_SEQ_NUM` | INTEGER |  | The order a series occurs in a Digital Imaging and Communications in Medicine (DICOM) Study Instance |
| 14 | `DICOM_IMAGE_SEQ_NUM` | VARCHAR |  | The order an image occurs in a Digital Imaging and Communications in Medicine (DICOM) Series Instance. |
| 15 | `DICOM_MODALITY` | VARCHAR |  | The Digital Imaging and Communications in Medicine (DICOM) modality type as determined by a DICOM image header |
| 16 | `OBJECT_DESC` | VARCHAR |  | The description for the object. |
| 17 | `OBJECT_CREATION_UTC_DTTM` | DATETIME (UTC) |  | The instant the received object was created at the sending organization. |
| 18 | `OBJECT_RECEIVED_UTC_DTTM` | DATETIME (UTC) |  | The last instant the object was received on a query response. |
| 19 | `OBJECT_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The last instant the binary data was changed for the object at the sending organization. |
| 20 | `CLINICALLY_RELEVANT_UTC_DTTM` | DATETIME (UTC) |  | The most clinically relevant instant for the object at the sending organization. |
| 21 | `LINKED_EVENT_IDENT` | VARCHAR |  | The event identifier for the encounter document at the sending organization to which the object is related. |
| 22 | `OBJECT_LOCATION_NAME` | VARCHAR |  | The Care Everywhere location name for the object. |
| 23 | `OBJECT_LOCATION_IDENT` | VARCHAR |  | The Care Everywhere location ID for the object. |
| 24 | `OBJECT_HOME_COMMUNITY_IDENT` | VARCHAR |  | Stores the Home Community ID for the object. This item stores the Home Community ID where this object lives. This is used for IHE XDS.b and XCA profiles. |
| 25 | `OBJECT_BLOB_TYPE_C_NAME` | VARCHAR | org | Stores the object's blob type (I DCS 250) if it was received in a query response. |
| 26 | `OBJECT_TYPE_CODE` | VARCHAR |  | The type code of the object |
| 27 | `OBJECT_TYPE_SCHEME` | VARCHAR |  | The type code scheme of the object |
| 28 | `IMG_SLCT_TYPE_CMP_C_NAME` | VARCHAR |  | This item stores how this Digital Imaging and Communications in Medicine (DICOM) image was selected by image exchange. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

