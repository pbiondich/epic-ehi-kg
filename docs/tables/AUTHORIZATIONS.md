# AUTHORIZATIONS

> This table contains information about authorization records. This includes links to the patient, referral, and coverage/payer.

**Overflow family:** [AUTHORIZATIONS_2](AUTHORIZATIONS_2.md)  
**Primary key:** `AUTH_ID`  
**Columns:** 97  
**Org-specific columns:** 11  
**Joined by:** 23 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK | The authorization ID for the authorization record. |
| 2 | `AUTH_FROM_DT` | DATETIME |  | Authorization start date |
| 3 | `AUTH_TO_DT` | DATETIME |  | Authorization end date |
| 4 | `PAT_ID` | VARCHAR | FK→ | The patient for whom the authorization record was created. This column is frequently used to link to the PATIENT table. |
| 5 | `REFERRAL_ID` | NUMERIC | FK→ | Referral associated with this authorization. If this is a UM owned service-level authorization, this column is not populated and, instead, column UM_REFERRAL_ID will be populated. This column is frequently used to link to the REFERRAL table. |
| 6 | `AUTH_TYPE_C_NAME` | VARCHAR |  | Authorization type category value |
| 7 | `NUM_SVCS_APPROVED` | INTEGER |  | Number of services, units or visits approved. |
| 8 | `NUM_SVCS_REQUESTED` | INTEGER |  | Number of services, units, or visits requested. |
| 9 | `CVG_ID` | NUMERIC | FK→ | Linked coverage record. This column is frequently used to link to the COVERAGE table. |
| 10 | `AUTH_NUM` | VARCHAR |  | Authorization number |
| 11 | `AUTH_COMMENTS` | VARCHAR |  | Free text authorization comment. |
| 12 | `RECORD_CREATION_DT` | DATETIME |  | Record creation date. |
| 13 | `CHARGE_COUNTS` | INTEGER |  | Keeps track of number of counts used by charges. |
| 14 | `AUTH_REF_NUMBER` | VARCHAR |  | The reference number given to us by the payer for this service-level authorization (AUT). |
| 15 | `AP_CLAIM_COUNT` | INTEGER |  | Number of services, units, or visits used for AP Claims. |
| 16 | `INTER_NUM_SVCS_APRV` | INTEGER |  | The number of services approved for each interval. |
| 17 | `INTER_NUM_SVCS_REQ` | INTEGER |  | The number of services requested for each interval. |
| 18 | `INTER_APRV_FREQ_ID` | VARCHAR |  | The ID of the associated Frequency Record for the approved recurring authorization. |
| 19 | `INTER_APRV_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 20 | `INTER_REQ_FREQ_ID` | VARCHAR |  | The ID of the associated Frequency Record for the requested recurring authorization. |
| 21 | `INTER_REQ_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 22 | `INTER_NUM_APRV` | INTEGER |  | The number of times the interval has been approved to repeat. |
| 23 | `INTER_NUM_REQ` | INTEGER |  | The number of times the interval has been requested to repeat. |
| 24 | `PARENT_AUTH_ID` | NUMERIC |  | The Parent Authorization that this authorization (AUT) inherits from. |
| 25 | `AP_CLAIM_COUNT_METHOD_C_NAME` | VARCHAR |  | The counting method for the AP Claim counts. |
| 26 | `UM_STATUS_C_NAME` | VARCHAR |  | The utilization management authorization decision status for the requested service. |
| 27 | `UM_APPROVED_RSN_C_NAME` | VARCHAR | org | The reason the authorized status was assigned to this service. |
| 28 | `UM_PART_APRV_RSN_C_NAME` | VARCHAR | org | The reason the partial authorization status was assigned to this service. |
| 29 | `UM_DENIED_RSN_C_NAME` | VARCHAR | org | The reason the denied status was assigned to this service. |
| 30 | `UM_DISMISSED_RSN_C_NAME` | VARCHAR | org | The reason the dismissed status was assigned to this service. |
| 31 | `UM_NOT_REQUIRED_RSN_C_NAME` | VARCHAR | org | The reason the no auth required status was assigned to this service. |
| 32 | `UM_PENDING_RSN_C_NAME` | VARCHAR | org | The reason the pending status was assigned to this service. |
| 33 | `UM_CANCELED_RSN_C_NAME` | VARCHAR | org | The reason the canceled/withdrawn status was assigned to this service. |
| 34 | `UM_DECISION_DTTM` | DATETIME (Local) |  | The date and time the authorization decision was set on the service level authorization. Note that if a service's status changes from a finalized status to another after the entire authorization request has been finalized, this column does not update with the new instant and will instead reflect the original decision instant. |
| 35 | `NON_UM_AUTH_ID` | NUMERIC |  | Service authorizations that are created as part of UM workflows will only appear in UM workflows. If the authorization details are needed outside the UM department, then corresponding non-UM service-level authorizations are created. This separation is required to ensure non-UM staff cannot alter authorization decisions rendered by UM staff. This column provides a link between the UM service authorizations and non-UM service-level authorizations. There is a 1-to-1 link between UM and non-UM service-level authorizations. |
| 36 | `UM_AUTH_REQUEST_ID` | NUMERIC |  | If this is a UM-owned service authorization, this column serves as the pointer to the authorization request record. UM-owned service authorizations do not have direct pointers to referral and coverage. They must be accessed through the authorization request. |
| 37 | `NON_UM_ORDER_ID` | NUMERIC |  | This is a link between a UM service authorization and an order on the referral. |
| 38 | `ORDER_ENTRY_ORDER_ID` | NUMERIC |  | When the service is created as part of order entry, this column will be populated as a pointer back to the order. |
| 39 | `UM_CLOSED_RSN_C_NAME` | VARCHAR | org | The reason the closed status was assigned to this service. |
| 40 | `UM_FINALIZE_USER_ID` | VARCHAR |  | The unique ID associated with the user record that finalized this authorization. This column is frequently used to link to the CLARITY_EMP table. |
| 41 | `UM_FINALIZE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 42 | `FINAL_UM_STATUS_CHANGE_SRC_C_NAME` | VARCHAR |  | The change source category ID that resulted in the finalized status of the service. |
| 43 | `AUTH_STATUS_C_NAME` | VARCHAR |  | The provider-side authorization status category ID for the service. |
| 44 | `UM_MED_DIR_REV_USER_ID` | VARCHAR |  | The user who set the pending review status reason for a medical director review. |
| 45 | `UM_MED_DIR_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 46 | `UM_PEND_MED_DIRECTOR_DTTM` | DATETIME (Local) |  | The local date and time of when the authorization pended for review with a reason of medical director review. |
| 47 | `UM_PEND_MED_DIRECTOR_UTC_DTTM` | DATETIME (UTC) |  | The date and time in UTC of when the authorization pended for review with a reason of medical director review. |
| 48 | `FIRST_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Ths CSN of the encounter linked to the service level authorization with the earliest encounter instant. If the service level authorization doesn't have any encounters linked directly, it will search the linked referral or auth/cert. |
| 49 | `LAST_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The CSN of the encounter linked to the service level authorization with the latest encounter instant. If the service level authorization doesn't have any encounters linked directly, it will search the linked referral or auth/cert. |
| 50 | `APPEALED_SERVICE_AUTH_ID` | NUMERIC |  | The ID of the service that this service was created to appeal. |
| 51 | `LAST_CVG_GUIDANCE_C_NAME` | VARCHAR |  | When we receive a Coverage Requirements Discovery response message pertaining to this authorization, this item will store the coverage guidance value from that message. |
| 52 | `UM_CVG_GUIDANCE_SOURCE_C_NAME` | VARCHAR |  | The coverage guidance source category ID for the coverage guidance request. |
| 53 | `UM_CVG_GDNC_REALTIME_TX_CSN_ID` | NUMERIC |  | The unique contact serial number of the real-time transaction that originated the Coverage Requirements Discovery request. |
| 54 | `UM_CVG_GUIDANCE_PA_SVC_LN_IDNT` | INTEGER |  | The line number of the service from the real-time transaction that originated the Coverage Requirements Discovery service request. |
| 55 | `UM_CVG_GUIDANCE_C_NAME` | VARCHAR |  | The coverage guidance determination category ID for the requested service. |
| 56 | `UM_CVG_GUIDANCE_FROM_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 57 | `UM_CVG_GUIDANCE_REQ_DATE` | DATETIME |  | The date of the requested service for which guidance is being requested. If no date was provided with the request, the date of the request creation is used. |
| 58 | `UM_CVG_GUIDANCE_REQ_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 59 | `UM_CVG_GUIDANCE_REQ_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 60 | `UM_CVG_GUIDANCE_REQ_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 61 | `UM_CVG_GUIDANCE_REQUEST_NOTE` | VARCHAR |  | The free-text note text associated with the coverage guidance request. |
| 62 | `UM_CVG_GUIDANCE_LOB_ID` | VARCHAR |  | The unique ID of the line of business associated with the requested coverage guidance. |
| 63 | `UM_CVG_GUIDANCE_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 64 | `UM_CVG_GUIDANCE_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 65 | `UM_CVG_GUIDANCE_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 66 | `UM_CVG_GUIDANCE_CREATE_USER_ID` | VARCHAR |  | The unique ID of the user who created the coverage guidance request, if known. |
| 67 | `UM_CVG_GUIDANCE_CREATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 68 | `DENIAL_REASON_C_NAME` | VARCHAR |  | If this authorization's status is Denied, then this item will contain the rationale given for that denial. |
| 69 | `AUTH_BED_DAY_TYPE_ID` | NUMERIC |  | The type of day (TOD record) approved by the payer. |
| 70 | `AUTH_BED_DAY_TYPE_ID_BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |
| 71 | `NUM_DAYS_APPROVED` | INTEGER |  | The number of days approved by the payer for a bed day type. This is calculated as End Date - Start Date + 1. |
| 72 | `NUM_NIGHTS_APPROVED` | INTEGER |  | The number of nights approved by the payer for a bed day type. This is calculated as : End Date - Start Date. |
| 73 | `EXT_SVC_MSG` | VARCHAR |  | Service-level MSG data received by Payer Platform from an external system. |
| 74 | `EXT_SVC_REF_NUM` | VARCHAR |  | the administrative reference number received by Payer Platform from an external system for this service |
| 75 | `EXT_SVC_AUTH_NUM` | VARCHAR |  | the authorization number received by Payer Platform from an external system for this service |
| 76 | `UM_CVG_GUIDANCE_RESP_AGENCY_ID` | VARCHAR |  | The unique ID of the responsible entity for determining coverage guidance for the requested service. |
| 77 | `UM_CVG_GUIDANCE_RESP_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 78 | `AUTH_BED_DAY_TX_STATUS_C_NAME` | VARCHAR |  | Indicates the current transaction status for this bed day |
| 79 | `UM_REQ_RX_QTY` | NUMERIC |  | The requested quantity limit for the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 80 | `UM_REQ_RX_DISP_QTYUNIT_C_NAME` | VARCHAR | org | The requested quantity limit unit for the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 81 | `UM_REQ_RX_DAYS` | NUMERIC |  | The requested quantity limit number for days of the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 82 | `REQ_UM_MED_TIER_C_NAME` | VARCHAR | org | The requested tier for the current medication item. |
| 83 | `UM_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 84 | `UM_NDC_ID` | VARCHAR |  | The NDC of the current medication item. |
| 85 | `UM_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 86 | `UM_APRV_RX_QTY` | NUMERIC |  | The approved quantity limit for the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 87 | `UM_APRV_RX_DISP_QTYUNIT_C_NAME` | VARCHAR |  | The approved quantity limit unit for the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 88 | `UM_APRV_RX_DAYS` | NUMERIC |  | The approved quantity limit number for days of the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 89 | `APRV_UM_MED_TIER_C_NAME` | VARCHAR |  | The approved tier for the current medication item. |
| 90 | `UM_CVG_GUIDANCE_POS_TYPE_C_NAME` | VARCHAR | org | The place of service type category ID for the coverage guidance request. |
| 91 | `UM_FORMULARY_QL_QUANTITY` | NUMERIC |  | The formulary quantity limit for the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 92 | `UM_FORMULARY_QL_DISP_QTYUNIT_C_NAME` | VARCHAR |  | The formulary quantity limit unit for the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 93 | `UM_FORMULARY_QL_DAYS` | NUMERIC |  | The formulary quantity limit number for days of the current medication item. Quantity limit refers to the maximum amount of medication that can be dispensed to a patient within a specific timeframe. |
| 94 | `UM_FORMULARY_UM_MED_TIER_C_NAME` | VARCHAR |  | The formulary tier for the current medication item. |
| 95 | `UM_FINAL_STS_CHANGE_LOCAL_DTTM` | DATETIME (Local) |  | The local date and time the current authorization finalized status was set on the authorization. Note that unlike column UM_DECISION_DTTM, if a service's status changes from a finalized status to another after the entire authorization request has been finalized, this column will update with the new instant. |
| 96 | `UM_FINAL_STS_CHANGE_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time the current authorization finalized status was set on the authorization. Note that unlike column UM_DECISION_UTC_DTTM, if a service's status changes from a finalized status to another after the entire authorization request has been finalized, this column will update with the new instant. |
| 97 | `UM_CVG_GDNC_CVRD_MEM_BENEFIT_C_NAME` | VARCHAR |  | The benefit check result from the requested coverage guidance. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `FIRST_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `LAST_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

## Joined in — referenced by (23)

| From | Column | Confidence |
|------|--------|------------|
| [APPT_CSN_COUNTS](APPT_CSN_COUNTS.md) | `AUTH_ID` | medium |
| [AP_CLAIM_AUTH_ASGN_AUTHS](AP_CLAIM_AUTH_ASGN_AUTHS.md) | `AUTH_ID` | medium |
| [AP_CLAIM_PX_AUTH_INFO](AP_CLAIM_PX_AUTH_INFO.md) | `AUTH_ID` | medium |
| [ARPB_AUTH_INFO](ARPB_AUTH_INFO.md) | `AUTH_ID` | medium |
| [AUTHORIZATIONS_EXT_TRN](AUTHORIZATIONS_EXT_TRN.md) | `AUTH_ID` | medium |
| [AUTH_GUIDANCE_MOD](AUTH_GUIDANCE_MOD.md) | `AUTH_ID` | medium |
| [AUTH_PURPOSE](AUTH_PURPOSE.md) | `AUTH_ID` | medium |
| [AUTH_RESTRICTIONS](AUTH_RESTRICTIONS.md) | `AUTH_ID` | medium |
| [AUTH_UM_CVG_GUIDANCE_DX](AUTH_UM_CVG_GUIDANCE_DX.md) | `AUTH_ID` | medium |
| [AUTH_UM_CVG_GUIDANCE_INFO](AUTH_UM_CVG_GUIDANCE_INFO.md) | `AUTH_ID` | medium |
| [AUTH_UM_HX_RESTR](AUTH_UM_HX_RESTR.md) | `AUTH_ID` | medium |
| [AUTH_UM_HX_RESTR_DECISION](AUTH_UM_HX_RESTR_DECISION.md) | `AUTH_ID` | medium |
| [AUTH_UM_STATUS_HX](AUTH_UM_STATUS_HX.md) | `AUTH_ID` | medium |
| [AUT_ONC_EXP_REQCOUNT](AUT_ONC_EXP_REQCOUNT.md) | `AUTH_ID` | medium |
| [AUT_PROC_DETAILS](AUT_PROC_DETAILS.md) | `AUTH_ID` | medium |
| [AUT_PROC_MODS](AUT_PROC_MODS.md) | `AUTH_ID` | medium |
| [AUT_PROC_MODS_HX](AUT_PROC_MODS_HX.md) | `AUTH_ID` | medium |
| [CHARGE_COUNT_IGNORED_MODS](CHARGE_COUNT_IGNORED_MODS.md) | `AUTH_ID` | medium |
| [CRITERIA_REVIEW_SVC_AUTHS](CRITERIA_REVIEW_SVC_AUTHS.md) | `AUTH_ID` | medium |
| [HSP_PRE_AR_AUTH_ID](HSP_PRE_AR_AUTH_ID.md) | `AUTH_ID` | medium |
| [HSP_TX_AUTH_INFO](HSP_TX_AUTH_INFO.md) | `AUTH_ID` | medium |
| [PRE_AR_AUTH_RECORD](PRE_AR_AUTH_RECORD.md) | `AUTH_ID` | medium |
| [SMRTDTA_ELEM_AUTH](SMRTDTA_ELEM_AUTH.md) | `AUTH_ID` | medium |

