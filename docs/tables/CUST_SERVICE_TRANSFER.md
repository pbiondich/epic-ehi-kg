# CUST_SERVICE_TRANSFER

> The CUST_SERVICE_TRANSFER table contains information about patient transfer requests that have been documented in a customer service communication record. This can be used to report on communication documented by staff who facilitate calls between referring providers and admitting providers for potential transfer patients.

**Primary key:** `COMM_ID`  
**Columns:** 63  
**Org-specific columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique ID of the customer service communication record. |
| 2 | `TRANS_PAT_SSN` | VARCHAR |  | The social security number of the patient for whom the transfer is requested. |
| 3 | `TRANS_REF_PROV` | VARCHAR |  | The name of the referring provider who is requesting the patient be transferred. |
| 4 | `TRANS_PAT_NAME` | VARCHAR |  | The name of the patient for whom the transfer is requested. |
| 5 | `TRANS_PAT_AGE` | INTEGER |  | The age of the patient for whom the transfer is requested. |
| 6 | `TRANS_PAT_SEX_C_NAME` | VARCHAR | org | The category ID for the sex of the patient for whom the transfer is requested. |
| 7 | `TRANS_PAT_POINT_OF_ORIGIN_C_NAME` | VARCHAR | org | The point of origin category ID for the source location from which the requested patient will be physically transferred. |
| 8 | `TRANS_REASON_C_NAME` | VARCHAR | org | The transfer reason category ID for the patient transfer request. |
| 9 | `TRANS_LVL_OF_CARE_C_NAME` | VARCHAR | org | The level of care category ID for the patient transfer request. |
| 10 | `TRANS_PAT_CLASS_C_NAME` | VARCHAR | org | The patient class category ID for the patient transfer request. |
| 11 | `TRANS_ACCOMMODATION_CODE_C_NAME` | VARCHAR | org | The accommodation code category ID for the patient transfer request. |
| 12 | `TRANS_ACCOMMODATION_REASON_C_NAME` | VARCHAR | org | The accommodation code reason category ID for the patient transfer request. |
| 13 | `TRANS_HOSPITAL_SERVICE_C_NAME` | VARCHAR | org | The hospital service category ID for the patient transfer request. |
| 14 | `TRANS_NEEDED_BY_DT` | DATETIME |  | The date the patient transfer is needed by. |
| 15 | `TRANS_CLIN_ACCEPTED_YN` | VARCHAR |  | Indicates whether the patient transfer is clinically accepted or not. |
| 16 | `TRANS_CLIN_DECISION_USER_ID` | VARCHAR |  | The unique ID of the user who recorded the clinical decision for the transfer request. |
| 17 | `TRANS_CLIN_DECISION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 18 | `TRANS_FIN_ACCEPTED_YN` | VARCHAR |  | Indicates whether the patient transfer is financially accepted or not. |
| 19 | `TRANS_FIN_DECISION_USER_ID` | VARCHAR |  | The unique ID of the user who recorded the financial decision for the transfer request. |
| 20 | `TRANS_FIN_DECISION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 21 | `TRANS_DECISION_REASON_C_NAME` | VARCHAR | org | The decision reason category ID for the patient transfer, entered when the request is either accepted or denied. |
| 22 | `TRANS_REF_ORG_C_NAME` | VARCHAR | org | The transfer referral organization category ID for the patient transfer request. |
| 23 | `TRANS_PAT_DOB_DT` | DATETIME |  | The date of birth of the patient for whom the transfer is requested. |
| 24 | `TRANS_CLIN_DECISION_DATETIME` | DATETIME (UTC) |  | The date and time when the clinical decision regarding the patient transfer request was recorded. |
| 25 | `TRANS_FIN_DECISION_DATETIME` | DATETIME (UTC) |  | The date and time when the financial decision regarding the patient transfer request was recorded. |
| 26 | `REQUEST_STATUS_C_NAME` | VARCHAR |  | This item stores the current status of the Transfer Center request. |
| 27 | `DEST_DECLINE_RSN_C_NAME` | VARCHAR | org | This item stores why a considered destination was marked as declined for the request. |
| 28 | `CANCEL_STATUS_RSN_C_NAME` | VARCHAR | org | This item stores the reason why a Transfer Center request was canceled. |
| 29 | `REFERRING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 30 | `REFERRING_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 31 | `TRANSFER_TYPE_C_NAME` | VARCHAR | org | This item stores the type of transfer being requested. |
| 32 | `REFERRING_LOC_IS_OTHER_YN` | VARCHAR |  | This column stores whether the referring location of this Transfer Center request is stored as a discrete record or as free text. |
| 33 | `FREETEXT_REFERRING_LOC_NAME` | VARCHAR |  | The referring location of a Transfer Center request, stored as free text. |
| 34 | `REQUEST_IS_EMTALA_YN` | VARCHAR |  | This item stores whether a patient transfer falls under EMTALA (Emergency Medical Treatment and Labor Act) legislation in the United States. |
| 35 | `TRANSFER_REGION_ID` | NUMERIC |  | Region associated with the Transfer Center request. |
| 36 | `TRANSFER_REGION_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |
| 37 | `DEST_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 38 | `MODE_OF_TXPORT_C_NAME` | VARCHAR | org | Describes by what method a Transfer Center patient is being transported to the destination location. |
| 39 | `TXPORT_SERVICE_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 40 | `TXPORT_SERVICE_IS_OTHER_YN` | VARCHAR |  | Indicates whether the transportation service provider has been stored as free text. If yes, then column FREETEXT_TXPORT_SERVICE_NAME will contain the free-text name. |
| 41 | `TXPORT_CONTACT_NUM` | VARCHAR |  | The contact number for the transportation service provider moving the patient to the destination location. |
| 42 | `EXPECTED_ARRIVAL_DTTM` | DATETIME (Local) |  | The date and time the patient is expected to arrive at the destination location. |
| 43 | `TXPORT_DISPATCH_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the transportation service provider was dispatched to pick up the patient being transferred. |
| 44 | `TXPORT_PICK_UP_UTC_DTTM` | DATETIME (UTC) |  | The date and time that the patient was picked up from the referring location. |
| 45 | `PAT_ARRIVAL_UTC_DTTM` | DATETIME (UTC) |  | What time the patient arrived at the destination location. |
| 46 | `FREETEXT_TXPORT_SERVICE_NAME` | VARCHAR |  | This item stores the free-text name of the transportation service provider associated with a Transfer Center request. |
| 47 | `SOURCE_ADMISSION_DTTM` | DATETIME (Local) |  | The date and time of a request's source encounter. For manually entered encounters. For linked hospital encounters, use PAT_ENC_HSP__INP_ADM_DATE, for the inpatient admission date/time, and/or PAT_ENC_HSP__HOSP_ADMSN_TIME, for the date and time that the patient was first admitted to the facility, bedded in the ED, or confirmed for an HOV for this contact, regardless of patient's base patient class. For appointment encounters, use PAT_ENC_APPT__CONTACT_DATE for the date and PAT_ENC_APPT__PROV_START_TIME for the time. |
| 48 | `SOURCE_ADMSN_LVL_OF_CARE_C_NAME` | VARCHAR |  | The level of care of a request's source encounter. For manually entered encounters. For linked hospital encounters, use PAT_ENC_HSP__LEVEL_OF_CARE_C instead. |
| 49 | `TRANS_BACK_TO_REFERRING_LOC_YN` | VARCHAR |  | Indicates whether a source encounter location is willing to accept a transfer back. 'Y' indicates that they are. 'N' or NULL indicates that they are not. |
| 50 | `PAT_IS_IN_STATE_RESIDENT_YN` | VARCHAR |  | Indicates whether or not the patient of a Transfer Center request is an in-state resident of the state of the target destination. |
| 51 | `TRANS_REFER_ZONE_C_NAME` | VARCHAR | org | The geographical zone of the referring facility. |
| 52 | `TRANS_REQ_ZONE_C_NAME` | VARCHAR |  | The geographical zone the referring facility asked to send the patient to. |
| 53 | `TRANS_DEST_ZONE_C_NAME` | VARCHAR |  | The geographical zone of the selected destination. |
| 54 | `REQUESTED_DEST_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 55 | `TC_PRIORITY_C_NAME` | VARCHAR |  | The priority of a Transfer Center request. |
| 56 | `PRIN_ACC_PROV_CONTACT_IDENT` | INTEGER |  | This stores the line number of the Contact Log entry that is the principal accepting provider for the Transfer Center request. |
| 57 | `REFERRING_PROV_ADDR_ID` | VARCHAR |  | This provides a link to the address of the referring provider. To obtain the address information, join to the table CLARITY_SER_ADDR on the ADDR_UNIQUE_ID column. If you use IntraConnect, you also need to join the REFERRING_PROV_ID column to CLARITY_SER_ADDR.PROV_ID. |
| 58 | `SOURCE_ENC_DEPT` | VARCHAR |  | The department where a source encounter on a request occurred. For manually entered encounters. For linked hospital encounters, use PAT_ENC_HSP__DEPARTMENT_ID. For linked appointment encounters, use PAT_ENC_APPT__DEPARTMENT_ID. |
| 59 | `SOURCE_ENC_ROOM_AND_BED` | VARCHAR |  | The bed (and room, if applicable) that a patient was assigned to in a manually entered source encounter. For linked hospital encounters, use PAT_ENC_HSP__ROOM_ID and PAT_ENC_HSP__BED_ID instead. |
| 60 | `TC_FUTURE_RSN_C_NAME` | VARCHAR | org | This item stores the reason why a Transfer Center request is being futured. |
| 61 | `TRANS_REVERT_STATUS_DATE` | DATETIME |  | Stores the date for when this request will move from the future request status back to pending. |
| 62 | `TRANS_FUTURE_COMMENT` | VARCHAR |  | Stores a comment related to the reason for putting this request into the Future tab. |
| 63 | `TC_REQUEST_STATUS_MOD_C_NAME` | VARCHAR | org | Modifier to the main Request Status item (I NCS 11110). When a NCS record has a value in this item, that category value becomes the request status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

