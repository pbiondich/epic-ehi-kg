# DOC_EVENT_LIST_INFO

> Information about changes to a document (DXR) record.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 34  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EVENT_START_DTTM` | DATETIME (Local) |  | Start instant for the event corresponding to this row. |
| 4 | `EVENT_END_DTTM` | DATETIME (Local) |  | End instant for the event corresponding to this row. |
| 5 | `EVENT_IDENTIFIER` | VARCHAR |  | Unique identifier for the encounter in which the document was edited on the remote system. This is either a contact serial number or, if using IntraConnect, a Unique Contact Identifier. |
| 6 | `EVENT_ENC_TYPE_NAME` | VARCHAR |  | Free text name of the type of encounter in which the document was edited on the remote system. |
| 7 | `EVENT_ENC_TYPE_C_NAME` | VARCHAR | org | The encounter type category ID for the patient's encounter in which the document was edited on the remote system. Category values can be found in ZC_ORDER_TYPE. |
| 8 | `EVENT_POS_CODE_C_NAME` | VARCHAR | org | The place of service code for the location where the patient's encounter on the remote system occurred. Category values can be found in ZC_POS_TYPE. |
| 9 | `EVENT_SPECIALTY_NAME` | VARCHAR |  | Free text name of the specialty of the department on the remote system where the patient's encounter took place. |
| 10 | `EVENT_SPECIALTY_ID_C_NAME` | VARCHAR | org | The department specialty category ID for the patient's encounter on the remote system. Category values can be found in ZC_SPECIALTY_DEP. |
| 11 | `EVENT_DEPT_NAME` | VARCHAR |  | Free text name of the department on the remote system where the patient's encounter took place. |
| 12 | `EVENT_DEPT_ID` | VARCHAR |  | The unique ID of the department on the remote system where the patient's encounter occurred. |
| 13 | `EVENT_DESC` | VARCHAR |  | Free text description of the patient's encounter on the remote system. |
| 14 | `EVENT_DOC_ID` | VARCHAR |  | Universally unique identifier for the encounter document linked to this event. |
| 15 | `EVENT_DOC_TYPE_C_NAME` | VARCHAR | org | The CDA type category ID for the document. Category values can be found in ZC_DOC_CONTENT_TYPE. |
| 16 | `EVENT_LOCATION_NAME` | VARCHAR |  | Free text of the location name associated with the patient's encounter on the remote system. |
| 17 | `EVENT_LOCATION_ID` | VARCHAR |  | The unique ID of the location on the remote system where the patient's encounter occurred. |
| 18 | `EVENT_HOME_COMM_ID` | VARCHAR |  | The unique ID of the home community where the patient's encounter occurred. |
| 19 | `EVENT_HL7_ENC_TYPE_CMP_C_NAME` | VARCHAR | org | HL7 encounter type of the contact at the remote organization. |
| 20 | `EVENT_CE_ENC_TYPE_CMP_C_NAME` | VARCHAR |  | The Care Everywhere encounter type category ID for the received event. |
| 21 | `EVENT_ENC_MOOD_CMP` | VARCHAR |  | This item stores the value from the moodCode node for an encounter in a received CDA document. |
| 22 | `EVENT_ED_TO_INP_CMP_YN` | VARCHAR |  | Indicates whether this encounter was upgraded from ED to Inpatient. Y indicates that the encounter was upgraded from ED to Inpatient. N indicates an inpatient encounter that was not upgraded from ED. Null indicates either a non-inpatient encounter or an encounter for which this information is not available. |
| 23 | `EVENT_KEY_CMP` | VARCHAR |  | Key for use by other related event groups. |
| 24 | `EVENT_MED_REV_CMP_YN` | VARCHAR |  | Indicates whether the medication associated with the event was reviewed or not. |
| 25 | `EVENT_LOS_CPT_CMP` | VARCHAR |  | This item stores the level of service CPT (Current Procedure Terminology) code for where the encounter took place. |
| 26 | `EVENT_SET_ID_CMP` | VARCHAR |  | Document set ID that represents a common identifier across all document revisions. |
| 27 | `EVNT_SERVICE_EVENT` | VARCHAR |  | Stores the service event ID from an incoming CDA document. |
| 28 | `CREATE_INSTANT_COMPLD_DTTM` | DATETIME (UTC) |  | Holds the creation instant of the document as returned by the query response header. This is distinct from I DXR 172, which is the creation instant as returned by metadata within the received document. |
| 29 | `EVENT_ENC_IDENT` | VARCHAR |  | Compiled encounter identifier received from the remote system. This is only populated for documents received from non-Epic organizations. |
| 30 | `EVENT_TITLE` | VARCHAR |  | Title of a document associated with an event. |
| 31 | `EVENT_STUDY_CODE_CMP` | VARCHAR |  | Stores the study code of the research study associated with this event. |
| 32 | `COMP_ENC_SOURCE_CSN` | VARCHAR |  | A source org CSN for an encounter that can be exchanged between organizations. Can help identify an encounter that has been exchanged between organizations. |
| 33 | `EVENT_CMP_APPT_STATUS_C_NAME` | VARCHAR | org | The encounter status as translated to an Epic appointment status (EPT 7020) |
| 34 | `EVENT_UPDT_INST_CMP_UTC_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the event in UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

