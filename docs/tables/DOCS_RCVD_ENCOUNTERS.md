# DOCS_RCVD_ENCOUNTERS

> Encounters received from external documents.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 72  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EVENT_START_DTTM` | DATETIME (Local) |  | Start instant (date and time) for the encounter. |
| 6 | `EVENT_END_DTTM` | DATETIME (Local) |  | End instant (date and time) for the encounter. |
| 7 | `EVENT_IDENTIFIER` | VARCHAR |  | Unique identifier for the encounter in which the document was edited on the remote system. This is either a contact serial number (CSN) or, if using IntraConnect, a Unique Contact Identifier (UCI). |
| 8 | `EVENT_ENC_MOOD` | VARCHAR |  | Mood code of the remote encounter. |
| 9 | `EVENT_ENC_TYPE_NAME` | VARCHAR |  | Free text name of the remote encounter type. |
| 10 | `EVENT_ENC_TYPE_C_NAME` | VARCHAR | org | Encounter type of the contact at the remote organization. |
| 11 | `EVENT_POS_CODE_C_NAME` | VARCHAR | org | The place of service code category ID for the location where the patient's encounter on the remote system occurred. Category values can be found in ZC_POS_TYPE. |
| 12 | `EVENT_KEY` | INTEGER |  | Key for use by other related event groups. |
| 13 | `EVENT_SPECIALTY_NAME` | VARCHAR |  | Free text name for the department specialty associated with the event. |
| 14 | `EVENT_SPECIALTY_C_NAME` | VARCHAR | org | Department specialty category ID associated with the event. |
| 15 | `EVENT_DEPT_NAME` | VARCHAR |  | Free text department name for the encounter. |
| 16 | `EVENT_DEPT_IDENT` | VARCHAR |  | This item stores the department ID for the encounter. |
| 17 | `EVENT_DESC` | VARCHAR |  | Free text description for this event. |
| 18 | `EVENT_DOC` | VARCHAR |  | The unique ID for the encounter document. |
| 19 | `EVENT_DOC_TYPE_C_NAME` | VARCHAR | org | The CDA type category ID for the document. |
| 20 | `EVENT_LOC_NAME` | VARCHAR |  | Free text of the location name associated with the patient's encounter on the remote system. |
| 21 | `EVENT_LOC_IDENT` | VARCHAR |  | The unique ID of the location on the remote system where the patient's encounter occurred. |
| 22 | `EVENT_MED_REV_YN` | VARCHAR |  | Indicates whether the medication associated with the event was reviewed or not. |
| 23 | `EVENT_SRC_DXR_CSN` | NUMERIC |  | This item stores the source external document CSN (Contact Serial Number) that contains the external event information. |
| 24 | `EVENT_HL7_TYPE_C_NAME` | VARCHAR | org | HL7 encounter type of the contact at the remote organization. |
| 25 | `EVENT_CE_ENC_TYPE_C_NAME` | VARCHAR |  | Care Everywhere encounter type of the contact at the remote organization. |
| 26 | `EVENT_ED_TO_INP_YN` | VARCHAR |  | Indicates whether this encounter was upgraded from ED to Inpatient. Y indicates that the encounter was upgraded from ED to Inpatient. N indicates an inpatient encounter that was not upgraded from ED. Null indicates either a non-inpatient encounter or an encounter for which this information is not available. |
| 27 | `EVENT_LOS_CPT` | VARCHAR |  | This item stores the level of service CPT (Current Procedure Terminology) code for where the encounter took place. |
| 28 | `EVENT_RCVD_INSTANT_DTTM` | DATETIME (Local) |  | This item stores the last received instant. |
| 29 | `EVENT_SET_ID` | VARCHAR |  | Document set ID that represents a common identifier across all document revisions. |
| 30 | `EVENT_DUP_EPT_CSN` | NUMERIC |  | The internal patient contact serial number (CSN) that is a duplicate of this external encounter. |
| 31 | `EVENT_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the event in UTC. |
| 32 | `EVENT_NOTE_ID` | VARCHAR |  | The note (HNO) ID related to this encounter. |
| 33 | `EVENT_ADDR_STREET` | VARCHAR |  | Street address of the place where the event occurred. |
| 34 | `EVENT_ADDR_CITY` | VARCHAR |  | The city where the event occurred. |
| 35 | `EVENT_ADDR_STATE_C_NAME` | VARCHAR | org | The state where the event occurred. |
| 36 | `EVENT_ADDR_COUNTY_C_NAME` | VARCHAR | org | The county where the event occurred. |
| 37 | `EVENT_TZ_OFFSET` | NUMERIC |  | Contains the time zone offset of this encounter in hours |
| 38 | `EVENT_REL_DOC` | VARCHAR |  | Stores ID of the document that contains a given encounter (event) in its encounter section. |
| 39 | `RCVD_EVENT_ID` | VARCHAR |  | Stores the encounter reference ID received in an external document when reference IDs are not trusted. |
| 40 | `EVENT_DATA_SRC_C_NAME` | VARCHAR |  | Indicates whether the data comes from the encompassingEncounter section or an encounter section of a CDA document, or from the event list. By default (i.e. when this value is blank) the data is assumed to come from the encounter section. |
| 41 | `REL_DOC_RCVD_INSTANT_DTTM` | DATETIME (Local) |  | Stores the last received instant of the related document. |
| 42 | `EVENT_ENC_STAT_C_NAME` | VARCHAR |  | This item holds the status of the encounter, if cancelled |
| 43 | `EVENT_HOSP_ADMSN_YN` | VARCHAR |  | Indicates whether the encounter is a hospital admission. Y indicates that the encounter is a hospital admission. N indicates that the encounter is not a hospital admission. NULL indicates an encounter for which this information is not available. |
| 44 | `EVENT_HOV_YN` | VARCHAR |  | Indicates whether the encounter is a hospital outpatient visit. Y indicates that the encounter is a hospital outpatient visit. N indicates that the encounter is not a hospital outpatient visit. NULL indicates an encounter for which this information is not available. |
| 45 | `EVENT_OUTPAT_F2F_YN` | VARCHAR |  | Indicates whether the encounter is an outpatient face-to-face visit. Y indicates that the encounter is an outpatient face-to-face visit. N indicates that the encounter is not an outpatient face-to-face visit. NULL indicates an encounter for which this information is not available. |
| 46 | `EVENT_ACUITY_LEVEL_C_NAME` | VARCHAR | org | Stores the received acuity level for an encounter. |
| 47 | `EVENT_FILTER_RSN_C_NAME` | VARCHAR |  | Stores the reason why an external encounter should be filtered from the composite record |
| 48 | `EVENT_ADMISSION_RSN` | VARCHAR |  | The reason for the admission based on HL7v2 tables |
| 49 | `EVENT_FAC_NPI` | VARCHAR |  | Stores the facility NPI where the event occurred. |
| 50 | `EVENT_FAC_TIN` | VARCHAR |  | Stores the facility TIN where the event occurred. |
| 51 | `DOC_CREATE_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | Holds the creation instant of the document as returned by the query response header. This is distinct from I DXR 172, which is the creation instant as returned by metadata within the received document. |
| 52 | `EVENT_ENC_IDENT` | VARCHAR |  | The unique identifier for this encounter as received on the remote system. This is only populated for documents received from non-Epic organizations. |
| 53 | `EVENT_AUTH_NUM` | VARCHAR |  | Authorization Number of the encounter |
| 54 | `EVENT_PRE_CERT_NUM` | VARCHAR |  | Pre-admit Certification Number of the encounter |
| 55 | `EVENT_ADMSN_TYPE_C_NAME` | VARCHAR |  | Admission type of the encounter. |
| 56 | `EVENT_ADMIT_SRC_C_NAME` | VARCHAR |  | Admit source of the encounter. |
| 57 | `EVENT_TITLE` | VARCHAR |  | Title of a document associated with an event. |
| 58 | `EXPECT_LEN_OF_STAY` | INTEGER |  | The expected length of the stay in days. |
| 59 | `EXPECT_DISCH_DATE` | DATETIME |  | Expected discharge date for the encounter |
| 60 | `EXPECT_DISCH_TM` | DATETIME (Local) |  | Expected discharge time for the encounter |
| 61 | `EVENT_LINK_RSH_PROTOCOL_VISIT` | VARCHAR |  | The linked protocol visit for a Research Study linked encounter. |
| 62 | `EVENT_STUDY_CODE` | VARCHAR |  | Stores the study code of the research study associated with this event. |
| 63 | `EVENT_EXTERNAL_TO_SEND_ORG_YN` | VARCHAR |  | This item tracks whether the event occurred at the organization that sent the received document, or if it occurred elsewhere. If it occurred elsewhere, this item will be set to 1. Otherwise, this item will be null. |
| 64 | `EVENT_PAT_CLASS_C_NAME` | VARCHAR |  | Patient Class of the encounter. |
| 65 | `EVENT_UPGRADED_HOV_YN` | VARCHAR |  | Indicates whether the encounter is an admission upgraded from an HOV Y indicates that the encounter is an admission upgraded from HOV. N indicates that the encounter is not an admission upgraded from HOV. NULL indicates an encounter for which this information is not available. |
| 66 | `EVENT_BULK_STAT_C_NAME` | VARCHAR |  | The status of this data element within DINE. |
| 67 | `EVENT_HL7_TYPE_MAPPED_YN` | VARCHAR |  | Whether this encoutner's Event HL7 Type was mapped based on the free text Event Encounter Type Name |
| 68 | `EVENT_START_UTC_DTTM` | DATETIME (UTC) |  | Start instant for each event in the event list in UTC. |
| 69 | `EVENT_END_UTC_DTTM` | DATETIME (UTC) |  | End instant for each event in the event list in UTC. |
| 70 | `EVENT_BULK_INCL_DATE` | DATETIME |  | The date to compare to the change tracking window when loading flat files in bulk via DINE. If the date is within the window, but the data element is missing from the load, then the data element is invalidated. |
| 71 | `ENC_SOURCE_CSN` | VARCHAR |  | A source org CSN for an encounter that can be exchanged between organizations. Can help identify an encounter that has been exchanged between organizations. |
| 72 | `EVENT_SENDING_FAC_NAMESPACE` | VARCHAR |  | Stores the raw value of the namespace ID of the event sending facility |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

