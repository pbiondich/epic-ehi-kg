# DOC_EPSD_LIST_INFO

> Episodes received from external documents.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 35  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `EPSD_START_INST_DTTM` | DATETIME (Local) |  | Start instant for the received episode. |
| 6 | `EPSD_END_INST_DTTM` | DATETIME (Local) |  | End instant for the received episode. |
| 7 | `EPSD_IDENT` | VARCHAR |  | Unique identifier for the received episode. |
| 8 | `EPSD_SET_ID` | VARCHAR |  | Episode set ID that represents a common identifier across all document revisions. |
| 9 | `EPSD_TYP_ID_C_NAME` | VARCHAR | org | The episode type category ID for the received episode. |
| 10 | `EPSD_NAME` | VARCHAR |  | Name of the received episode. |
| 11 | `EPSD_STAT_INFO_C_NAME` | VARCHAR |  | Status of the received episode. |
| 12 | `EPSD_CMT` | VARCHAR |  | The free text comment for this row's received episode. |
| 13 | `EPSD_DOC_ID` | VARCHAR |  | Universally unique identifier (UUID) of the received episode DXR document. |
| 14 | `EPSD_DOC_TYP_C_NAME` | VARCHAR | org | Document type for the document that has the received episode. |
| 15 | `EPSD_ENROLL_INST_DTTM` | DATETIME (Local) |  | Enrollment instant for the received episode. |
| 16 | `EPSD_USES_ENROLL_DT_YN` | VARCHAR |  | Stores whether an episode considers the enrollment date to be the first effective date of the episode instead of the start date. |
| 17 | `EPSD_TYPE_NAME` | VARCHAR |  | Name of the episode type for the received episode. |
| 18 | `EPSD_CMGMT_STATUS_C_NAME` | VARCHAR |  | Status of the received care coordination episode. |
| 19 | `EPSD_CMGMT_STATUS_NAME` | VARCHAR |  | Free text display name for the status of the received care coordination episode. |
| 20 | `EPSD_DEPT_NAME` | VARCHAR |  | Free text episode department name. |
| 21 | `EPSD_SPECIALTY_DEP_NAME` | VARCHAR |  | Free text department specialty name for the received episode. |
| 22 | `EPSD_SPECIALTY_DEP_C_NAME` | VARCHAR | org | Department specialty ID for the received episode. |
| 23 | `EPSD_POOL` | VARCHAR |  | Free text name of the In Basket pool associated with the received episode. |
| 24 | `EPSD_PARENT_EPISODE` | VARCHAR |  | The episode identifier for the parent episode. |
| 25 | `ESPD_SRC_DOCUMENT_CSN_ID` | NUMERIC |  | This item stores the source DXR CSN that contains the external episode information. |
| 26 | `EPSD_RCVD_INSTANT_DTTM` | DATETIME (Local) |  | Stores the last received instant. |
| 27 | `EPSD_LST_UPD_INST_DTTM` | DATETIME (UTC) |  | Stores the last update instant of the episode in UTC. |
| 28 | `EPSD_CCM_EPISODE_TYPE_C_NAME` | VARCHAR | org | Indicates whether the Coordinated Care Management episode is for a program or for a service. If null, this is not a Coordinated Care Management episode type. |
| 29 | `EPSD_CMGMT_PROG_CAT_C_NAME` | VARCHAR |  | This item stores the program category value, which defines the type of program supported by a Compass Rose episode type. |
| 30 | `EPSD_PAUSE_START_LOCAL_DTTM` | DATETIME (Local) |  | Pause period start instant for the received Compass Rose episode. Dates may also be stored as instants set to midnight. |
| 31 | `EPSD_PAUSE_END_LOCAL_DTTM` | DATETIME (Local) |  | Pause period end instant for the received Compass Rose episode. Dates may also be stored as instants set to midnight. |
| 32 | `EPSD_CMGMT_PAUSE_REASON` | VARCHAR |  | This item stores the reason for a Compass Rose episode pause period. |
| 33 | `EPSD_CMGMT_CLOSED_REASON` | VARCHAR |  | Status reason for closed Compass Rose episodes. |
| 34 | `EPSD_CMGMT_DECLINE_REASON` | VARCHAR |  | Status reason for declined Compass Rose episodes. |
| 35 | `EPSD_CMGMT_ENROLLMENT_REASON` | VARCHAR |  | Status reason for enrolled Compass Rose episodes. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

