# DOCS_RCVD_OBJECTS

> High level information and metadata about received binary objects.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 27  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `OBJECT_VERSION_IDENT` | VARCHAR |  | The Universal Unique Identifier (UUID) for the binary object. |
| 6 | `OBJECT_SET_IDENT` | VARCHAR |  | The document set ID that represents a common identifier across all document revisions. |
| 7 | `OBJECT_EXTERNAL_TYPE` | VARCHAR |  | The type assigned to the object at the sending organization. |
| 8 | `DOCUMENT_TYPE_GROUP_C_NAME` | VARCHAR |  | The object's type group (I ECT 55330 value) |
| 9 | `OBJECT_MIME_TYPE_C_NAME` | VARCHAR |  | The format used to store the object. |
| 10 | `OBJECT_PROV` | VARCHAR |  | The name of the provider associated with the object. |
| 11 | `DICOM_STUDY_UID` | VARCHAR |  | The Digital Imaging and Communications in Medicine (DICOM) Study Instance Unique Identifier (UID) as recorded by the image archive. |
| 12 | `DICOM_SERIES_UID` | VARCHAR |  | The Digital Imaging and Communications in Medicine (DICOM) Series Instance Unique Identifier (UID) for the imaging series. |
| 13 | `DICOM_SERIES_SEQ_NUM` | INTEGER |  | The order a series occurs in a Digital Imaging and Communications in Medicine (DICOM) Study Instance |
| 14 | `DICOM_IMAGE_SEQ_NUM` | VARCHAR |  | The order an image occurs in in a Digital Imaging and Communications in Medicine (DICOM) Series Instant |
| 15 | `DICOM_MODALITY` | VARCHAR |  | The Digital Imaging and Communications in Medicine (DICOM) modality type as determined by a DICOM image header. |
| 16 | `OBJECT_DESC` | VARCHAR |  | The description for the object. |
| 17 | `OBJECT_CREATION_UTC_DTTM` | DATETIME (UTC) |  | The instant the received object was created at the sending organization. |
| 18 | `OBJECT_RECEIVED_UTC_DTTM` | DATETIME (UTC) |  | The last instant the object was received on a query response. |
| 19 | `OBJECT_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The last instant the binary data was changed for the object at the sending organization. |
| 20 | `CLINICALLY_RELEVANT_UTC_DTTM` | DATETIME (UTC) |  | The most clinically relevant instant for the object at the sending organization. |
| 21 | `LINKED_EVENT_IDENT` | VARCHAR |  | The event identifier for the encounter document at the sending organization to which the object is related. |
| 22 | `OBJECT_LOCATION_NAME` | VARCHAR |  | The Care Everywhere location name for the object. |
| 23 | `OBJECT_LOCATION_IDENT` | VARCHAR |  | The Care Everywhere location ID for the object. |
| 24 | `OBJECT_HOME_COMMUNITY_IDENT` | VARCHAR |  | Stores the Home Community ID for the object. This item stores the Home Community ID where this object lives. This is used for IHE XDS.b and XCA profiles. |
| 25 | `OBJECT_SPECIALTY` | VARCHAR |  | The name of the specialty this object is associated with. The specialty listed is the department specialty from the received object. |
| 26 | `OBJECT_BLOB_TYPE_C_NAME` | VARCHAR | org | Stores the object's blob type (DCS 250) if it was received in a query response. |
| 27 | `IMG_SLCT_TYPE_C_NAME` | VARCHAR |  | This item stores how this Digital Imaging and Communications in Medicine (DICOM) image was selected by image exchange. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

