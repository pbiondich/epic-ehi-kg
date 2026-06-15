# HL_REQ_INFO

> Hospital Logistics Requests Information.

**Primary key:** `HLR_ID`  
**Columns:** 44  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLR_ID` | NUMERIC | PK shared | The unique identifier for the request record. |
| 2 | `HLR_NAME` | VARCHAR |  | Record name |
| 3 | `HLR_TYPE_C_NAME` | VARCHAR |  | The Hospital Logistics Request type. |
| 4 | `REQ_TEMPLATE_TASK_ID` | NUMERIC |  | The Logistics Task Template this Request is linked to. This Task defines the meaning of this Request and provides configuration info for the Request. |
| 5 | `REQ_TEMPLATE_TASK_ID_TASK_NAME` | VARCHAR |  | The name of the task. |
| 6 | `REQ_START_UTC_DTTM` | DATETIME (UTC) |  | This Logistics Request's UTC start instant. |
| 7 | `REQ_PRIORITY_C_NAME` | VARCHAR |  | This Logistics Request's priority. |
| 8 | `REQ_START_PLF_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 9 | `REQ_DYNAMIC_START_TYPE_C_NAME` | VARCHAR |  | This Logistics Request's dynamic start location type. This indicates what changes (like updates to the patient's bed or current location) will update the Request's start location. |
| 10 | `REQ_END_PLF_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 11 | `REQ_DYNAMIC_END_TYPE_C_NAME` | VARCHAR |  | This Logistics Request's dynamic end location type. This indicates what changes (like updates to the patient's bed) will update the Request's end location. |
| 12 | `REQ_TECHS_NUM` | INTEGER |  | The number of Logistics Technicians required to work on this Logistics Request. |
| 13 | `REQ_MODE_C_NAME` | VARCHAR | org | This Logistics Request's mode. Technicians need to use this mode to complete this Request. |
| 14 | `REQ_STATUS_C_NAME` | VARCHAR |  | The current status of this Logistics Request. |
| 15 | `REQ_CANCEL_RSN_C_NAME` | VARCHAR | org | When this Logistics Request or Job's status (I HLR 160) is Canceled or Skipped, this item contains the cancel or skip reason. |
| 16 | `REQ_START_APPT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of the appointment that this Logistics Request is going to. |
| 17 | `REQ_END_APPT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of the appointment this Logistics Request is coming from. |
| 18 | `REQ_ADMISSION_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number (CSN) of the admission this Logistics Request is associated with. |
| 19 | `REQ_PEND_ID` | VARCHAR |  | The Pending Event linked to this Logistics Request. |
| 20 | `REQ_EVENT_ID` | NUMERIC |  | The event linked to this Logistics Request. |
| 21 | `REQ_FIRST_STAGE_HLR_ID` | NUMERIC |  | The Logistics Request that serves as the first stage of this Multi-Stage Request. |
| 22 | `REQ_NEXT_STAGE_HLR_ID` | NUMERIC |  | The Logistics Request that serves as the next stage of this Multi-Stage Request. |
| 23 | `REQ_STAGE_NUM` | INTEGER |  | The stage number for this Logistics Request. |
| 24 | `REQ_IS_CONCURRENT_STAGE_YN` | VARCHAR |  | Indicates if this Logistics Request can be worked on concurrently with the previous stage. |
| 25 | `REQ_REGION_SEC_ID` | NUMERIC |  | The Logistics Region that this Logistics Request belongs to. |
| 26 | `REQ_REGION_SEC_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |
| 27 | `REQ_SECTOR_SEC_ID` | NUMERIC |  | The Logistics Sector that this Logistics Request belongs to. |
| 28 | `REQ_SECTOR_SEC_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |
| 29 | `REQ_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 30 | `REQ_HOSP_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 31 | `REQ_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 32 | `REQ_CREATION_SOURCE_C_NAME` | VARCHAR |  | Indicates whether this Logistics Request was created manually or automatically, and if created automatically, which automatic process created the Request. |
| 33 | `REQ_PAT_ID` | VARCHAR | FK→ | The Patient (EPT) linked to this Logistics Request. |
| 34 | `REQ_BED_TYPE_C_NAME` | VARCHAR | org | This Logistics Request's associated bed type. This indicates that a bed of this type is being moved with this Request. When this Request is completed, the destination's bed type will be updated to this bed type. |
| 35 | `REQ_FUNC_COMP_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant that a Logistics Request can be considered functionally complete in UTC. |
| 36 | `REQ_ACTIVATION_UTC_DTTM` | DATETIME (UTC) |  | The instant that a Logistics Request is eligible to be assigned. |
| 37 | `REQ_FUNC_COMP_LOCAL_DTTM` | DATETIME (Local) |  | Stores the instant that a Logistics Request can be considered functionally complete in local time. |
| 38 | `JOB_ACT_LINK_LOCATION_EVNT_ID` | NUMERIC |  | The Patient Location Event record created by the Update Patient Location action on this Logistics Request. |
| 39 | `REQ_TASK_SUBTYPE_C_NAME` | VARCHAR |  | Subtype of the request, used to broadly classify the type of request this is. |
| 40 | `REQ_BED_ID` | VARCHAR |  | For Bed Clean and Maintenance Clean requests, this is the ID of the bed being cleaned. |
| 41 | `REQ_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 42 | `RECORD_STATUS_C_NAME` | VARCHAR |  | The record status category ID for the hospital logistics request. |
| 43 | `PRIMARY_LINKED_EVENT_C_NAME` | VARCHAR |  | Indicates the primary event linked to this Logistics request. |
| 44 | `REQ_PROC_HELD_NUM` | INTEGER |  | The number of minutes that the associated Logistics Task specified that this request should be held before being activated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REQ_ADMISSION_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `REQ_END_APPT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `REQ_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `REQ_START_APPT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

