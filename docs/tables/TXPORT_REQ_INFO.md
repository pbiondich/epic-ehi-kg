# TXPORT_REQ_INFO

> This table contains information about transport requests.

**Primary key:** `TRANSPORT_ID`  
**Columns:** 40  
**Org-specific columns:** 3  
**Joined by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TRANSPORT_ID` | NUMERIC | PK | The unique ID of the transport request record. |
| 2 | `TRANSPORT_NAME` | VARCHAR |  | The name of the transport request record. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient to be transported. |
| 4 | `TXPORT_PAT_CSN` | NUMERIC | FK→ | The unique contact serial number of the patient associated with this transport request. This is optional as there may not be a particular patient contact that the transport request is linked to. |
| 5 | `TXPORT_TYPE_C_NAME` | VARCHAR |  | The transport type category number for the transport request. |
| 6 | `TXPORT_DATE` | DATETIME |  | The date on which the transport request needs to be completed. |
| 7 | `TXPORT_TIME` | DATETIME (Local) |  | The time at which the transport request needs to be completed. |
| 8 | `TXPORT_FROM_PLF_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 9 | `TXPORT_TO_PLF_ID_RECORD_NAME` | VARCHAR |  | The name of the PLF record. |
| 10 | `ROUND_TRIP_YN` | VARCHAR |  | Flag to indicate if this is a round trip request. |
| 11 | `TXPORT_MODE_C_NAME` | VARCHAR | org | The transport mode category number for the transport request. |
| 12 | `REQUEST_SOURCE_C_NAME` | VARCHAR | org | The source of the transport request. |
| 13 | `REQ_USER_ID` | VARCHAR |  | The unique ID of the user who created the transport request. |
| 14 | `REQ_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 16 | `CANCEL_USER_ID` | VARCHAR |  | The unique ID of the user who canceled the transport request. |
| 17 | `CANCEL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 18 | `CANCEL_EVENT_DTTM` | DATETIME (UTC) |  | The date and time when a transport request was canceled. |
| 19 | `PRIORITY_C_NAME` | VARCHAR |  | The priority of the transport request. |
| 20 | `RECORD_CREATION_DT` | DATETIME |  | The date on which the transport request was created. |
| 21 | `RND_TRIP_RETURN_ID` | NUMERIC |  | This item contains the linked return transport request for a round trip request. |
| 22 | `RND_TRIP_ORIG_ID` | NUMERIC |  | This item contains the linked original transport request for a round trip request. |
| 23 | `TXPORT_FROM_TYPE_C_NAME` | VARCHAR |  | Indicates if the patient is to be picked up at their current location or an override location specified. |
| 24 | `TXPORT_TO_TYPE_C_NAME` | VARCHAR |  | Indicates if the patient is to be dropped off at their currently occupied bed or to a specific location. |
| 25 | `CURRENT_STATUS_C_NAME` | VARCHAR |  | This item indicates the current status of the request. |
| 26 | `TXPORT_ADMIT_CSN` | NUMERIC |  | This item contains the contact serial number (CSN) of the admission contact. This is optional as there may not be a current admission contact for the patient. |
| 27 | `PARENT_REQUEST_ID` | NUMERIC |  | This item contains the parent transporter request of a multiple transporter request. |
| 28 | `ASSOCIATED_BEV_ID` | NUMERIC |  | This item contains the linked bed clean request (if any). |
| 29 | `REGION_ID` | NUMERIC |  | The unique ID of the region record that the transport request is for. |
| 30 | `REGION_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |
| 31 | `TXPORT_PAT_OUT_CSN` | NUMERIC |  | This item contains the contact serial number (CSN) of the patient contact that is linked to this transport request if the request is an outgoing request from an appointment. This may not always be populated if the request is not linked to an appointment contact. |
| 32 | `SECTOR_ID` | NUMERIC |  | This item contains the sector that the transport request is in. |
| 33 | `SECTOR_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |
| 34 | `COMP_ACTION_RSLT_C_NAME` | VARCHAR |  | Holds the result of the attempt to transfer or discharge a patient. |
| 35 | `REQ_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 36 | `TXPORT_PHONE_NUM` | VARCHAR |  | This item contains the phone number associated with the transport request, stored as a short free-text string. |
| 37 | `TNP_CREATE_SRC_C_NAME` | VARCHAR |  | Specifies what made the request be created |
| 38 | `BED_TYPE_C_NAME` | VARCHAR | org | This item tracks the bed type associated with this transport request. |
| 39 | `TXPORT_HOUR_OF_DAY_C_NAME` | VARCHAR |  | The hour of day category value that the transport was last set to a pending status. Note this is a category value that is often joined to ZC_HOUR_OF_DAY. |
| 40 | `FOLLOW_UP_SOURCE_TRANSPORT_ID` | NUMERIC |  | Holds the transport request record that triggered the creation of this follow-up task. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `TXPORT_PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

## Joined in — referenced by (4)

| From | Column | Confidence |
|------|--------|------------|
| [ED_IEV_EVENT_INFO](ED_IEV_EVENT_INFO.md) | `TRANSPORT_ID` | high |
| [LINKED_MULT_ASGN](LINKED_MULT_ASGN.md) | `TRANSPORT_ID` | high |
| [PRIORITY_AUDIT_TRL](PRIORITY_AUDIT_TRL.md) | `TRANSPORT_ID` | high |
| [TXPORT_DATA_AUDIT](TXPORT_DATA_AUDIT.md) | `TRANSPORT_ID` | high |

