# ED_IEV_EVENT_INFO

> This table contains information about the current event records.

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 88  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique ID of the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this event. Multiple pieces of information can be associated with this record. |
| 3 | `EVENT_DISPLAY_NAME` | VARCHAR |  | The display name of the event. |
| 4 | `EVENT_TIME` | DATETIME (Local) |  | The instant when the event occurred. |
| 5 | `EVENT_RECORD_TIME` | DATETIME (Local) |  | The instant when the event was recorded. |
| 6 | `EVENT_USER_ID` | VARCHAR |  | The unique ID of the user who initiated the event. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `EVENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `EVENT_CMT` | VARCHAR |  | The comments entered for the event. |
| 9 | `EVENT_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `ADT_EVENT_ID` | NUMERIC |  | The unique ID of the Admission, Transfer, Discharge, or Leave of Absence (ADT) event record link that is associated with this event. The following ED events have linked ADT evens: ED Roomed (A) ED Transfer (T) ED Admit to Hospital (T) |
| 11 | `STAFFED_BEDS` | NUMERIC |  | The number of staffed beds for a department at the time of the event. This item is populated only if you are using the Staffed Beds activity. |
| 12 | `EVENT_KEY` | VARCHAR |  | A unique key associated with this event. The key is stored in other master files in order to reference this event. |
| 13 | `EVENT_NOTE_ID` | VARCHAR |  | The unique ID of the note that is associated with this event. |
| 14 | `EVENT_FINDING_ID` | NUMERIC |  | The unique ID of the result that is associated with this event. This column is frequently used to link to the ORDER_RES table. |
| 15 | `EVENT_IMPLANT_ID` | VARCHAR |  | The unique ID of the implant that is associated with this event. This column is frequently used to link to the OR_IMP table. |
| 16 | `EVENT_LINE_DATA_ID` | VARCHAR |  | The line number of the associated data stored for this event in OpTime's Log Entry activity. This column can be used to link to the OR_LNLG_GENERAL table. |
| 17 | `EVENT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `LOCATION_ID` | NUMERIC |  | The unique ID of the patient location record that is associated with this event. This link is available only for emergency department contacts and for any location definition in the patient location facility master file that is associated with an event template master file. This column can be used to link to the CL_PLC table. |
| 19 | `EVENT_STATUS_C_NAME` | VARCHAR |  | The category number for the event's status. |
| 20 | `REC_VERB_ORD_TYPE_C_NAME` | VARCHAR | org | The Inpatient reconciliation verbal order type flag category number for the event. |
| 21 | `REC_VRB_ORD_COMM_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `REC_VRB_SIGNER_ID` | VARCHAR |  | The unique ID of the provider who is the Inpatient reconciliation verbal order signer for this event. This column is frequently used to link to the CLARITY_SER table. |
| 23 | `REC_VRB_SIGNER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 24 | `REC_VRB_ORD_MODE_C_NAME` | VARCHAR | org | The Inpatient reconciliation verbal order mode category number for the event. |
| 25 | `REC_ORD_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 26 | `REC_PROC_AUTH_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 27 | `REC_MED_AUTH_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 28 | `REC_PROC_MSG_RCP_ID` | VARCHAR |  | The unique ID of the provider who is the Inpatient reconciliation procedure cosign message recipient for this event. This column is frequently used to link to the CLARITY_SER table. |
| 29 | `REC_PROC_MSG_RCP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `REC_MED_MSG_RCP_ID` | VARCHAR |  | The unique ID of the provider who is the Inpatient reconciliation medication cosign message recipient for this event. This column is frequently used to link to the CLARITY_SER table. |
| 31 | `REC_MED_MSG_RCP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 32 | `REC_IS_PROC_HOSP_YN` | VARCHAR |  | Indicates whether the Inpatient reconciliation procedure hospitalist flag is set for this event. |
| 33 | `REC_IS_MED_HOSP_YN` | VARCHAR |  | Indicates whether the Inpatient reconciliation medication hospitalist flag is set for this event. |
| 34 | `REC_VERB_ORD_CMT` | VARCHAR |  | The comments entered by the user who placed the Inpatient reconciliation verbal order associated with the event. |
| 35 | `REC_ADMIT_STATUS_C_NAME` | VARCHAR | org | The category number for the status of the Inpatient order reconciliation associated with this event. |
| 36 | `IP_REC_NOTE_ID` | VARCHAR |  | The unique ID of the order reconciliation (process of reviewing a orders when the patient moves to another level or area of care) note that is the associated with this event. |
| 37 | `EVENT_LOG_ID` | VARCHAR |  | The unique ID of the surgical log that is associated with this event. This column is frequently used to link to the OR_LOG table. |
| 38 | `EVENT_SUPPLY_ID` | VARCHAR |  | The unique ID of the supply that is associated with "supply used" events generated in Cupid "add supply" workflows. This column should be used to link to the OR_SPLY table. |
| 39 | `EVENT_SUPPLY_ID_SUPPLY_NAME` | VARCHAR |  | The name of the inventory item. |
| 40 | `EVENT_INI_RECORD_ID` | VARCHAR |  | The master file and ID of the source of a duplicate procedure alert event. For example, this item usually holds LDG-ID (the ID of the procedure duplicate group used) or EAP-ID (the ID of the procedure used). |
| 41 | `EVENT_CONTEXT` | VARCHAR |  | For some events, this column holds the context of the event. Lab Ordered events might store the order ID here. Duplicate procedure alert events might store information on specific user actions in response to the alert. |
| 42 | `SOURCE_PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 43 | `SOURCE_PX_INFO` | VARCHAR |  | Detailed information about the duplicate procedure checked in SOURCE_PX_ID. |
| 44 | `MATCH_PX_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 45 | `MATCH_PX_INFO` | VARCHAR |  | Detailed information about the duplicate procedure checked in MATCH_PX_ID. |
| 46 | `EVENT_SIGN_OFF_ID` | NUMERIC |  | The record that contains all the sign off information for this event. |
| 47 | `DEPT_SCORE` | NUMERIC |  | Stores the numeric department score for department-specific events records. When a department scoring system is coordinated with a department event, the score calculated is saved in this item. It groups the score to the specific event instant, type, etc. from which the score was calculated. |
| 48 | `STAFF_ROLE_C_NAME` | VARCHAR | org | For a staff sign-in or sign-out event, this item holds what their role was when they signed in. |
| 49 | `STAFF_IS_ATTN_YN` | VARCHAR |  | For a staff sign-in or sign-out event, this item holds whether or not the user signed in as an attending provider. |
| 50 | `LINKED_IEV_REC_ID` | VARCHAR |  | When linking two events, this item holds the record ID of the linked event. Use this in combination with the line number. |
| 51 | `LINKED_IEV_LINE` | INTEGER |  | When linking two events, this item holds the line number of the linked event within its respective record. Use this in combination with the record ID. |
| 52 | `EVENT_TYPE_VERSION` | NUMERIC |  | If the data model for a particular event type changes, this item can be used to say which version of the data model is being used. Assume that blank is version 1. The version number only has meaning in relation to EVENT_TYPE. |
| 53 | `EVENT_OWNER_ID` | VARCHAR |  | Stores the owner of the event. |
| 54 | `EVENT_OWNER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 55 | `PEND_ACTIVE_C_NAME` | VARCHAR |  | This column shows the current pend (group of pended orders) status. Each pend type has a separate active status. A pend can also have a status of cleanup needed. A null status is used for pends that are no longer in use. |
| 56 | `PEND_STATUS_C_NAME` | VARCHAR |  | The status of the pended orders. |
| 57 | `PEND_RESTORED_BY_ID` | VARCHAR |  | Unique ID of the user who restored the pended orders. |
| 58 | `PEND_RESTORED_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 59 | `PEND_RESTORED_DTTM` | DATETIME (UTC) |  | Instant the pended orders were restored. |
| 60 | `PEND_DELETED_BY_ID` | VARCHAR |  | Unique ID of the user who deleted pended orders. |
| 61 | `PEND_DELETED_BY_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 62 | `PEND_DELETED_I_DTTM` | DATETIME (UTC) |  | The instant pended orders were deleted. |
| 63 | `PEND_COMMENT` | VARCHAR |  | User or autogenerated comment about the pended orders. |
| 64 | `PEND_CHANGE_COUNT` | INTEGER |  | Count of number of changes from a user perspective (some actions will not count as changes) |
| 65 | `PEND_INSTANT_DTTM` | DATETIME (UTC) |  | Instant that the pended orders were created. |
| 66 | `PEND_CREATE_TYPE_C_NAME` | VARCHAR |  | Category indicating how these orders were pended such as automatically on timeout. |
| 67 | `EVENT_OVRIDE_RSN_C_NAME` | VARCHAR | org | Stores override reason for not scanning patient to verify the event. |
| 68 | `EVENT_LABEL` | VARCHAR |  | The label for the value associated with an event. |
| 69 | `EVENT_VALUE` | VARCHAR |  | The value associated with an event. |
| 70 | `NOTIFY_STATUS_C_NAME` | VARCHAR |  | Store the current status for a bed planning notification |
| 71 | `NOTIFY_PND_STATUS_C_NAME` | VARCHAR |  | Store the status of why a bed request is being escalated |
| 72 | `AN_LINKED_EVENT_ID` | VARCHAR |  | Stores the record ID of an event that is linked to another Anesthesia event. |
| 73 | `AN_LINKED_EVENT_LINE` | INTEGER |  | When linking an Anesthesia event to another event, this item holds the line number of the linked event within its respective record. |
| 74 | `ED_C_CLIENT_SRC_C_NAME` | VARCHAR |  | This tracks from what client the user filed an ED Course event. |
| 75 | `CT_EVENT_FILED_BY_C_NAME` | VARCHAR | org | If an event was filed automatically by a Case Tracking Event, this item holds the category ID of the case tracking event that did it |
| 76 | `TRANSPORT_ID` | NUMERIC | FK→ | This item stores the ID of the transport request that triggered the event, if applicable. |
| 77 | `TXPORT_HLR_ID` | NUMERIC |  | The unique ID of the logistics patient transport request (HLR) that triggered the event. |
| 78 | `EVENT_ORIGIN_C_NAME` | VARCHAR |  | This indicates whether the event came from an internal or external source. If blank, the event came from an internal source. |
| 79 | `RX_REQUEST_TYPE_C_NAME` | VARCHAR |  | If this event represents orders created from an incoming Rx request, this indicates the type of the request (New Rx, Renewal, etc.). |
| 80 | `RX_REQUEST_PHARMACY_ID` | NUMERIC |  | If this event represents orders created from an incoming Rx request, this indicates the pharmacy that requested the medications. |
| 81 | `RX_REQUEST_PHARMACY_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 82 | `RX_REQUEST_VIEWED_YN` | VARCHAR |  | If this event represents orders created from an incoming Rx request, this indicates whether any user has viewed the requested medications. Once the request has been viewed, no more orders can be added to it. |
| 83 | `TRANSFER_DEST_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 84 | `REC_ROLE_ADMIT_USERROL_C_NAME` | VARCHAR |  | Specifies the role of the user who revewed the current med list. |
| 85 | `REC_ROLE_ADMIT_STATUS_C_NAME` | VARCHAR | org | Specifies the role-based status of the current admission. This may be set in home meds and the admission navigator. |
| 86 | `INTERFACE_EVENT_SUB_IDN` | VARCHAR |  | A unique event identifier filed through incoming orders interfaces. |
| 87 | `AN_PROBLEM_LIST_ID` | NUMERIC |  | Networks to the LPL record that the corresponds to the problem documented during Anesthesia problem list integration with the pre-evaluation note. |
| 88 | `AN_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |
| `TRANSPORT_ID` | [TXPORT_REQ_INFO](TXPORT_REQ_INFO.md) | sole_pk | high |

