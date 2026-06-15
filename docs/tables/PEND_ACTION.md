# PEND_ACTION

> The PEND_ACTION table lists pending admission, transfer, and discharge actions to be taken.

**Primary key:** `PEND_ID`  
**Columns:** 86  
**Org-specific columns:** 21  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PEND_ID` | VARCHAR | PK | The unique identifier for the pending action record. |
| 2 | `PEND_EVENT_TYPE_C_NAME` | VARCHAR |  | The event type for the pending action. |
| 3 | `PEND_RECRD_TYPE_C_NAME` | VARCHAR | org | The record type for the pending action. |
| 4 | `IS_DELETED_YN` | VARCHAR |  | Indicates whether the pending action record is inactive or deleted. |
| 5 | `DELETE_TIME` | DATETIME (Local) |  | The date and time the pending action record was deleted. |
| 6 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 7 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | A unique serial number for the patient contact of the pending action record. This number is unique across all patient contacts in the system. |
| 8 | `REQ_GROUPER` | NUMERIC |  | The numeric index used to group pending action records. |
| 9 | `START_TIME` | DATETIME (Local) |  | The date and time the pending action is to start. |
| 10 | `END_TIME` | DATETIME (Local) |  | The date and time the pending action is to end. |
| 11 | `PEND_PRIORITY_C_NAME` | VARCHAR |  | The priority of the pending action. |
| 12 | `PEND_REASON_C_NAME` | VARCHAR | org | The reason for the pending action. |
| 13 | `PEND_CMNT` | VARCHAR |  | The comments for the pending action. |
| 14 | `UNIT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 15 | `ROOM_ID_ROOM_NAME` | VARCHAR |  | The name of the Room record. |
| 16 | `BED_ID` | VARCHAR |  | The ID of the bed in which the pending action will occur. |
| 17 | `BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 18 | `PAT_SERVICE_C_NAME` | VARCHAR | org | The service of the patient for whom the pending action will occur. |
| 19 | `LOC_KEY` | VARCHAR |  | The unique key identifying the unit-room-bed of the pending action. |
| 20 | `PAT_CLASS_C_NAME` | VARCHAR | org | The patient type of the patient for whom the pending action will occur. |
| 21 | `PEND_ATND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `PEND_ATND_DT` | DATETIME |  | The effective date for the attending provider during the pending action. |
| 23 | `LVL_OF_CARE_C_NAME` | VARCHAR | org | The level of care for the patient for whom the pending action will occur. |
| 24 | `ACCOMMODATION_C_NAME` | VARCHAR | org | The accommodation code of the room for the pending action. |
| 25 | `ACCOM_REASON_C_NAME` | VARCHAR | org | The accommodation reason for the room for the pending action. |
| 26 | `INCOMING_OK_USR_ID` | VARCHAR |  | The authorizing user for the incoming patient of the pending transfer. This ID may be encrypted. |
| 27 | `INCOMING_OK_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 28 | `OUTGOING_OK_USR_ID` | VARCHAR |  | The authorizing user for the outgoing patient of the pending transfer. This ID may be encrypted. |
| 29 | `OUTGOING_OK_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 31 | `ADM_COND_C_NAME` | VARCHAR | org | The admission condition of the patient for whom the pending action will occur. |
| 32 | `RES_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 33 | `INTERN_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 34 | `EXPECT_LEN_OF_STAY` | INTEGER |  | The expected length of stay in days of the pending admission for this patient contact. |
| 35 | `EXPECT_DISCHRG_DT` | DATETIME |  | The expected discharge date for the pending discharge of this patient contact. |
| 36 | `PEND_DISP_C_NAME` | VARCHAR |  | The disposition for the pending action. |
| 37 | `ON_LIST_TIME` | DATETIME |  | The date and time the pending action is good until. |
| 38 | `SVC_PRIORITY_C_NAME` | VARCHAR | org | The bed service priority to use when the pending action is completed. |
| 39 | `ADT_TRANSFER_RSN` | VARCHAR |  | A single line freetext reason for the transfer pending action. |
| 40 | `PEND_TRANSFER_TIME` | DATETIME (Local) |  | The date and time of the transfer pending action. |
| 41 | `OLD_BED_PRIORITY_C_NAME` | VARCHAR |  | The priority to use for a pending action to the patient's old bed. |
| 42 | `PEND_REQ_STATUS_C_NAME` | VARCHAR |  | The pending bed assignment request status for a pending admission or transfer. I.e., 1-Requested, 2-Assigned, 3-Rejected, 4-Approved. |
| 43 | `REQUEST_TIME` | DATETIME (Local) |  | The date and time that the pending bed assignment was requested. |
| 44 | `REQ_BY_USR_ID` | VARCHAR |  | The ID of the user requesting the pending bed assignment. |
| 45 | `REQ_BY_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 46 | `ASSIGNED_TIME` | DATETIME (Local) |  | The date and time that the pending bed assignment was assigned. |
| 47 | `REJECTED_TIME` | DATETIME (Local) |  | The date and time that the pending bed assignment was rejected. |
| 48 | `APPROVED_TIME` | DATETIME (Local) |  | The date and time that the pending bed assignment was approved. |
| 49 | `REQ_STATUS_RSN_C_NAME` | VARCHAR | org | The pending bed assignment request status reason for a pending admission or transfer. |
| 50 | `TYPE_OF_ROOM_C_NAME` | VARCHAR |  | The type of room category number for the pend record. This is extracted as the category title. |
| 51 | `ROOM_REASON_C_NAME` | VARCHAR | org | The category number of the reason for the type of room requested for the pend record. This is extracted as the category title. |
| 52 | `TYPE_OF_BED_C_NAME` | VARCHAR | org | The type of bed category number for the pend record. This is extracted as the category title. |
| 53 | `BED_REASON_C_NAME` | VARCHAR | org | The category number of the reason for the type of bed requested for the pend record. This is extracted as the category title. |
| 54 | `CREATED_BY_USER_ID` | VARCHAR |  | The user who created this PND record. |
| 55 | `CREATED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 56 | `ADT_PND_ADMITNG_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 57 | `ACUITY_C_NAME` | VARCHAR | org | The category number of the acuity level that will be assigned upon confirmation of the pending event record. This is extracted as the category title. |
| 58 | `COMPLETED_YN` | VARCHAR |  | This item indicates whether the pending event was used to complete an action. |
| 59 | `LINKED_EVENT_ID` | NUMERIC |  | This item holds a link to the Admission, Discharge, Transfer, or Leave of Absence (ADT) event that caused the pending event to become deleted. |
| 60 | `DELETE_CAUSE_C_NAME` | VARCHAR |  | Indicates the reason that a pending event record is marked as deleted. |
| 61 | `EXPECT_DLVR_METH_C_NAME` | VARCHAR | org | This is the expected delivery method for a mother who is going to deliver. |
| 62 | `TRAN_LD_STAT_YN` | VARCHAR |  | Flag to denote if the encounter is for a mother who will deliver |
| 63 | `REQUEST_URGENCY_C_NAME` | VARCHAR |  | The urgency for the pending bed assignment. I.e., A-High, B-Medium, or C-Low. |
| 64 | `ADT_ORDER_ID` | NUMERIC |  | Networked to an order ID when the pending event record was created by an order |
| 65 | `HOSPITAL_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 66 | `LOA_REASON_C_NAME` | VARCHAR | org | The leave of absence reason category ID for the pending event. |
| 67 | `READ_DTTM` | DATETIME (Local) |  | Instant when the request was first marked as read. |
| 68 | `READY_TO_PLAN_DTTM` | DATETIME (Local) |  | Instant when the request status reached Ready to Plan. |
| 69 | `PREASSIGNED_DTTM` | DATETIME (Local) |  | Instant when the request status reached Pre-assigned. |
| 70 | `BED_READY_DTTM` | DATETIME (Local) |  | Instant when the request status reached Bed Ready. |
| 71 | `DELAY_UNTIL_DTTM` | DATETIME (Local) |  | Time when the current delay expires. At that time, this item is cleared. |
| 72 | `REQUEST_DIVISION_C_NAME` | VARCHAR | org | This item stores the division for which this request falls, if any. The request division is used to divide bed requests into different groups which can be worked and managed independently. |
| 73 | `BP_REQ_READY_MOVE_YN` | VARCHAR |  | Is the bed request currently marked ready to move? |
| 74 | `BP_REQ_R2M_MANUAL_YN` | VARCHAR |  | Was this bed request marked ready to move set manually? |
| 75 | `BP_R2M_DTTM` | DATETIME (Local) |  | Timestamp of the last time this bed request was marked Ready to Move. |
| 76 | `BP_R2M_SET_BY_ID` | VARCHAR |  | User who last marked this bed request Ready to Move. |
| 77 | `BP_R2M_SET_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 78 | `PROJ_R2M_DATE` | DATETIME |  | Date when we expect the patient to be ready to move. |
| 79 | `PROJ_R2M_TM` | DATETIME (Local) |  | Time when we expect the patient to be ready to move. |
| 80 | `EVENT_RECORD_ID` | VARCHAR |  | References the event record for use in bed planning notifications |
| 81 | `BED_TYPE_C_NAME` | VARCHAR | org | This item tracks the type of bed a patient will need when a transfer is completed. |
| 82 | `OFF_SERVICE_YN` | VARCHAR |  | This column tracks if the bed request was completed as off service or off level of care. |
| 83 | `CANCEL_REASON_C_NAME` | VARCHAR | org | This holds the reason the user indicated when cancelling a pending event record. |
| 84 | `REJ_REASON_C_NAME` | VARCHAR | org | Stores the reason the bed request was rejected. |
| 85 | `ORIGIN_GROUP_C_NAME` | VARCHAR | org | The current bed request origin group that the request falls into. |
| 86 | `DEFAULT_ORIGIN_GROUP_C_NAME` | VARCHAR |  | The current bed request origin group that the request would fall into if there were no custom groups defined. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [BED_PLAN_HX](BED_PLAN_HX.md) | `PEND_ID` | high |
| [EVENT_NOTIF_HX](EVENT_NOTIF_HX.md) | `PEND_ID` | high |
| [PEND_PRED_DEPT](PEND_PRED_DEPT.md) | `PEND_ID` | high |
| [PEND_PRED_LOC_GRP](PEND_PRED_LOC_GRP.md) | `PEND_ID` | high |
| [PEND_PRED_SVC_GRP](PEND_PRED_SVC_GRP.md) | `PEND_ID` | high |

