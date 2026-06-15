# RADIOTHERAPY_CONTACT_INFO

> This table contains general contact specific information for external radiation therapy treatment records.

**Primary key:** `RT_SUMMARY_ID`, `CONTACT_DATE_REAL`  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RT_SUMMARY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the radiotherapy summary record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `ERT_SUMMARY_CSN_ID` | NUMERIC |  | The contact serial number (CSN) of the contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | Stores contact number |
| 6 | `NAME_HX` | VARCHAR |  | Stores the history of the record name |
| 7 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 8 | `RADIOTHERAPY_MODE_C_NAME` | VARCHAR |  | Contains the mode of the contact, indicating if the contact represents the prescription, plan, or treatment summary. |
| 9 | `PARENT_RT_SUMMARY_ID` | NUMERIC |  | Contains the parent record for the summary. For a phase, the parent ID will be a course. For a plan, the parent ID will be a phase. |
| 10 | `PARENT_RT_SUMMARY_DAT` | NUMERIC |  | Contains the DAT of the parent ID at the time this record was created. |
| 11 | `ANTECEDENT_RT_SUMMARY_DAT` | NUMERIC |  | Contains the DAT of the antecedent ID at the time this record was created. |
| 12 | `RADIOTHERAPY_STATUS_C_NAME` | VARCHAR |  | Stores the status of the contact of the record. |
| 13 | `REQUESTER_USER_ID` | VARCHAR |  | Contains the EMP record of the requester of the plan or prescription. |
| 14 | `REQUESTER_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `REQUESTER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 16 | `REQUESTER_ROLE_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 17 | `REQUESTER_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 18 | `REQUESTER_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 19 | `REQUESTER_LAB_ID` | NUMERIC |  | Contains the LLB record of the requester of the plan or prescription. |
| 20 | `REQUESTER_LAB_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 21 | `REQUESTER_REGISTRY_ID` | NUMERIC |  | Contains the HIP record of the requester of the plan or prescription. |
| 22 | `REQUESTER_REGISTRY_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 23 | `REQUESTER_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 24 | `START_DTTM` | DATETIME (Attached) |  | Contains the expected start or actual start instant for a radiotherapy course, phase, or plan. |
| 25 | `END_DTTM` | DATETIME (Attached) |  | Contains the expected end or actual end instant for a radiotherapy course, phase, or plan. |
| 26 | `CONTACT_LAST_UPD_VERSION_NUM` | INTEGER |  | Stores the FHIR version ID of the most recent version of the contact. |
| 27 | `INVOLVES_REIRRADIATION_YN` | VARCHAR |  | Flag indicating if the course involves reirradiation of targets or organs at risk that were already irradiated in previous courses. |
| 28 | `NUMBER_OF_FRACTIONS` | INTEGER |  | Stores the number of planned or delivered fractions in a phase or plan. |
| 29 | `NUMBER_OF_SESSIONS` | INTEGER |  | Stores the number of sessions in a course. |
| 30 | `ANTECEDENT_RT_SUMMARY_ID` | NUMERIC |  | Contains the plan or prescription the summary is based on. For a treatment summary, this will reference a plan. For a planned treatment, this will reference a prescription. |
| 31 | `CONTACT_VERSION_INST_UTC_DTTM` | DATETIME (UTC) |  | This item stores the last update instant of the contact, which is the instant the version in ERT 260 was created. |
| 32 | `TREATMENT_INTENT_TEXT` | VARCHAR |  | This item stores the text element for the treatment intent that is to be used when the treatment intent code (I ERT 215) does not contain a coded concept. |
| 33 | `RT_STATUS_REASON_TEXT` | VARCHAR |  | Stores a free text representation of the status reason when no coded value is stored in ERT item 210. |
| 34 | `CHANGE_REASON_TEXT` | VARCHAR |  | Stores a free text representation of the reason for revision or adaptation when no coded value is stored in ERT item 225. |
| 35 | `AUTHOREDON_DTTM` | DATETIME (Attached) |  | Stores the date that the prescription/plan request was authorized (signed). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

