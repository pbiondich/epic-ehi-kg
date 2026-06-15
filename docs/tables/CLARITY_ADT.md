# CLARITY_ADT

> The CLARITY_ADT table is the master table for ADT event history information. This table contains several foreign keys for other ADT tables.

**Primary key:** `EVENT_ID`  
**Columns:** 70  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | NUMERIC | PK FK→ | The unique ID number of the ADT event record. |
| 2 | `EVENT_TYPE_C_NAME` | VARCHAR | org | The category value corresponding to the type of the event record. |
| 3 | `EVENT_SUBTYPE_C_NAME` | VARCHAR |  | The category value indicating whether the event record has been changed or deleted. |
| 4 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `ROOM_ID_ROOM_NAME` | VARCHAR |  | The name of the Room record. |
| 6 | `ROOM_CSN_ID` | NUMERIC | FK→ | The serial number for the room contact of the event record. This number is unique across all room contacts in the system. |
| 7 | `BED_ID` | VARCHAR |  | The ID number of the bed of the event record at the effective time. |
| 8 | `BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 9 | `BED_CSN_ID` | NUMERIC | FK→ | The serial number for the bed contact of the event record. This number is unique across all bed contacts in the system. |
| 10 | `BED_STATUS_C_NAME` | VARCHAR |  | The category value corresponding to the record state of the bed of the event record at the effective time. |
| 11 | `EFFECTIVE_TIME` | DATETIME (Local) |  | The instant when the event was supposed to have happened. |
| 12 | `PAT_ID` | VARCHAR | FK→ | The ID of the patient of the event record at the effective time. |
| 13 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 14 | `EVENT_TIME` | DATETIME (Local) |  | The instant when the event record was actually created. |
| 15 | `USER_ID` | VARCHAR | FK→ | The ID number of the user who created the event record. |
| 16 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `PAT_CLASS_C_NAME` | VARCHAR | org | The category value corresponding to the classification for the patient of the event record at the effective time. |
| 18 | `PAT_SERVICE_C_NAME` | VARCHAR | org | The category value corresponding to the hospital service for the patient of the event record at the effective time. |
| 19 | `PAT_LVL_OF_CARE_C_NAME` | VARCHAR | org | The category value corresponding to the level of care for the patient of the event record at the effective time. |
| 20 | `DELETE_TIME` | DATETIME (Local) |  | The instant when the event record was actually deleted. |
| 21 | `CANC_EVENT_ID` | NUMERIC |  | The ID number of the canceled event record that this event record replaces. |
| 22 | `XFER_EVENT_ID` | NUMERIC |  | The ID number of the 'transfer out' event type event record which with this 'transfer in' event type event record corresponds to a transfer action for the patient of the event records. |
| 23 | `COMMENTS` | VARCHAR |  | The free text comment associated with the event record. This is used to hold overridden confirmation warnings by the user for the event type event record action. |
| 24 | `REASON_C_NAME` | VARCHAR | org | The category value corresponding to the reason the event record was undone or corrected. |
| 25 | `ACCOMMODATION_C_NAME` | VARCHAR | org | The accommodation code of the event. This is extracted as the category title. |
| 26 | `ACCOM_REASON_C_NAME` | VARCHAR | org | The category value corresponding to the reason for the room accommodation for the patient of the event record at the effective time. |
| 27 | `ALT_EVENT_TYPE_C_NAME` | VARCHAR |  | The category value corresponding to an alternate type for the event record. |
| 28 | `ORIG_EVENT_TIME` | DATETIME (Local) |  | The instant when the original subtype record for this event was actually created. |
| 29 | `PREV_UPD_EVNT_TIME` | DATETIME (Local) |  | The instant when the last previous update subtype record for this event was actually created. |
| 30 | `ORIG_EFF_TIME` | DATETIME (Local) |  | The instant when the original subtype record for this event was supposed to have happened. |
| 31 | `PREV_UPD_EFF_TIME` | DATETIME (Local) |  | The instant when the last previous update subtype record for this event was supposed to have happened. |
| 32 | `XFER_IN_EVENT_ID` | NUMERIC |  | The ID number of the 'transfer in' type record which with this 'transfer out' type record corresponds to a transfer action for the patient CSN of these records. |
| 33 | `NEXT_OUT_EVENT_ID` | NUMERIC |  | The ID number of the next 'transfer out' or 'discharge' type record for this bed for the patient CSN of these records. |
| 34 | `LAST_IN_EVENT_ID` | NUMERIC |  | The ID number of the last 'transfer in' or 'admission' type record for this bed for the patient CSN of these records. |
| 35 | `STATUS_OF_BED_C_NAME` | VARCHAR | org | The category value corresponding to the status of the bed of the event record at the event timestamp. |
| 36 | `BASE_PAT_CLASS_C_NAME` | VARCHAR |  | The category value corresponding to the base classification for the patient of the event record at the effective time. |
| 37 | `OUT_EVENT_TYPE_C_NAME` | VARCHAR |  | This column contains the outgoing event type as it would currently be interpreted |
| 38 | `FROM_BASE_CLASS_C_NAME` | VARCHAR |  | This column contains the base patient class that the patient had prior to this event. |
| 39 | `TO_BASE_CLASS_C_NAME` | VARCHAR |  | This column contains the base patient class that the patient had after this event. |
| 40 | `LABOR_STATUS_C_NAME` | VARCHAR |  | This item holds the L&D status of the encounter at the time of the ADT event. |
| 41 | `FIRST_IP_IN_IP_YN` | VARCHAR |  | This column indicates whether this event represents the first time a patient was admitted with an inpatient base class in an inpatient-type unit. |
| 42 | `ORDER_ID` | NUMERIC | shared | This item is a link to the ORD record directly responsible for generating an ADT event. |
| 43 | `SOURCE_LOC_EVNT_ID` | NUMERIC |  | The unique ID of the Patient Location event that generated this Admission, Discharge, Transfer, or Leave of Absence (ADT) event. This signifies that this ADT event was created from a Patient Location update. |
| 44 | `EVNT_REVIEW_C_NAME` | VARCHAR |  | The review status category number for the event. If empty, then this event never needed review. |
| 45 | `REVIEW_DTTM` | DATETIME (UTC) |  | The date and time when this event was reviewed by the user. |
| 46 | `REVIEW_USER_ID` | VARCHAR |  | The unique ID of the user who reviewed this event. |
| 47 | `REVIEW_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 48 | `LOA_REASON_C_NAME` | VARCHAR | org | The leave of absence reason category ID for the event. |
| 49 | `ORIGINAL_EVENT_ID` | NUMERIC |  | The unique ID of the original event that this event record replaces. If this event record has not been canceled or updated, this column will be equal to the EVENT_ID column. This column is not necessarily equal to the CANC_EVENT_ID column. If the original event has been updated multiple times, then this column will show the ID of the original event, not the ID of the event that was most recently replaced by this record. |
| 50 | `ACTION_SOURCE_C_NAME` | VARCHAR |  | This item holds the reason behind an auto-generated event (e.g. when the service is automatically updated due to an attending provider change). |
| 51 | `SPLIT_ACCT_HSP_ACCOUNT_ID` | NUMERIC |  | The unique ID of the hospital account for the associated event. This column will only be set for admissions enabled for split accounts. |
| 52 | `SPLIT_ACCT_FINANCIAL_CLASS_C_NAME` | VARCHAR | org | The category ID of the financial classification that corresponds to the primary payer for the associated event. This column will only be set for admissions enabled for split accounts. |
| 53 | `SPLIT_ACCT_PRIMARY_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 54 | `SPLIT_ACCT_PRIMARY_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 55 | `SPLIT_ACCT_OUT_FIN_CL_EV_TYP_C_NAME` | VARCHAR | org | The event type category ID of the outgoing financial class for this event. |
| 56 | `SPLIT_ACCT_IN_FIN_CL_EV_TYP_C_NAME` | VARCHAR |  | The event type category ID of the incoming financial class for this event. |
| 57 | `SPLIT_ACCT_FROM_FIN_CLASS_C_NAME` | VARCHAR |  | The category ID of the financial class prior to this event. |
| 58 | `SPLIT_ACCT_TO_FIN_CLASS_C_NAME` | VARCHAR |  | The category ID of the financial class after this event. |
| 59 | `SPLIT_ACCT_OUT_PAYER_EV_TYP_C_NAME` | VARCHAR |  | The unique ID of the outgoing payer for this event. |
| 60 | `SPLIT_ACCT_IN_PAYER_EV_TYP_C_NAME` | VARCHAR |  | The unique ID of the incoming payer for this event. |
| 61 | `SPLIT_ACCT_FROM_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 62 | `SPLIT_ACCT_TO_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 63 | `SPLIT_ACCT_OUT_PLAN_EV_TYP_C_NAME` | VARCHAR |  | The unique ID of the outgoing payer for this event. |
| 64 | `SPLIT_ACCT_IN_PLAN_EV_TYP_C_NAME` | VARCHAR |  | The unique ID of the incoming payer for this event. |
| 65 | `SPLIT_ACCT_FROM_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 66 | `SPLIT_ACCT_TO_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 67 | `IS_LOA_UPDATE_YN` | VARCHAR |  | Indicates whether this event is part of a leave of absence update. 'Y' indicates that the event is part of a leave of absence update, 'N' or NULL indicates it is not. |
| 68 | `EVENT_CONVERTED_FLAG_C_NAME` | VARCHAR |  | Indicates that this event has been converted to another event type. |
| 69 | `EFFECTIVE_UTC_DTTM` | DATETIME (UTC) |  | The instant when the event was supposed to have happened in UTC. |
| 70 | `CONVERTED_TO_EVENT_ID` | NUMERIC |  | When an event converts from an LOA Out to a Discharge or from a Discharge to an LOA Out, as indicated in I ADT 95 (Event Conversion Flag), a new ADT event is created which is not linked to the canceled event via I ADT 92 (Event Pointer). This item points to that new ADT event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BED_CSN_ID` | [CLARITY_BED](CLARITY_BED.md) | sole_pk | high |
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `ROOM_CSN_ID` | [CLARITY_ROM](CLARITY_ROM.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

