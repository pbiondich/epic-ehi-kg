# AUTH_REQUEST

> This table contains information about an individual authorization request.

**Primary key:** `AUTH_REQUEST_ID`  
**Columns:** 46  
**Org-specific columns:** 1  
**Joined by:** 22 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_REQUEST_ID` | NUMERIC | PK | The unique identifier for the authorization request. |
| 2 | `RECORD_STATUS_2_C_NAME` | VARCHAR |  | The Chronicles record status category ID for the authorization request. |
| 3 | `EXTERNAL_IDENTIFIER` | VARCHAR |  | The external identifier of the authorization request. |
| 4 | `LAST_EDIT_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) of the latest published (non-draft) contact of the authorization request. |
| 5 | `REQUEST_CONTEXT_C_NAME` | VARCHAR |  | The request context category ID for the authorization request. |
| 6 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient/member that this authorization request is for. This column is frequently used to link to the PATIENT table. |
| 7 | `REFERRAL_ID` | NUMERIC | FK→ | The unique ID of the referral record that this authorization request is associated with. |
| 8 | `COVERAGE_ID` | NUMERIC | FK→ | The unique ID of the coverage record that applies to this authorization request. |
| 9 | `REQUEST_CREATION_UTC_DTTM` | DATETIME (UTC) |  | The date and time (UTC) that this authorization request was initiated. |
| 10 | `LOB_ID` | VARCHAR | FK→ | The unique ID of the line of business associated with the coverage when the authorization request was processed. |
| 11 | `LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 12 | `PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 13 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 14 | `ORDER_ENTRY_ORDER_ID` | NUMERIC |  | When an authorization request is received, if any of the requested services were created during order entry, this column will be populated as a pointer back to the order. |
| 15 | `DECISION_USER_ID` | VARCHAR |  | The unique ID of the user responsible for the decision of the authorization request. In the case of medical director review, this is the person who conducted the medical director review rather than the user who changed the status in the system. This column is frequently used to link to the CLARITY_EMP table. |
| 16 | `DECISION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `UM_DECISION_USER_ROLE_C_NAME` | VARCHAR |  | The decision user role category ID for the user making the decision on the authorization request. |
| 18 | `RESP_PARTY_AGENCY_ID` | VARCHAR |  | The unique ID of the responsibility class of the party responsible for rendering a decision for the authorization request. |
| 19 | `RESP_PARTY_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 20 | `EXT_TRACKED_RSN_C_NAME` | VARCHAR |  | Keeps track of the reason why this auth request's turnaround time is tracked externally. |
| 21 | `APPEALED_AUTH_REQUEST_ID` | NUMERIC |  | The Authorization Request that was adversely determined and is being appealed by this Request. |
| 22 | `REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 23 | `MEDICAL_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 24 | `CREATED_BY_PENDING_CVG_YN` | VARCHAR |  | This item will be set to Yes if the authorization request was originally created using a non-verified coverage. |
| 25 | `PREVIOUS_COVERAGE_ID` | NUMERIC |  | When an Authorization Request is created with a non-verified coverage, the Authorization Request is eligible for a one-time coverage change. If the coverage is changed, this item will provide a link to the previous coverage. |
| 26 | `CVG_CHANGE_SOURCE_C_NAME` | VARCHAR |  | When an Authorization Request is created with a pending coverage, the Authorization Request is eligible for a one-time coverage change. If the coverage is changed, this item indicates if the change was initiated manually by a user or done automatically by the system. |
| 27 | `CVG_CHANGE_USER_ID` | VARCHAR |  | When an Authorization Request is created with a pending coverage, the Authorization Request is eligible for a one-time coverage change. If the coverage is changed, this item provides a link to the user that initiated the change. |
| 28 | `CVG_CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 29 | `CVG_CHANGE_UTC_DTTM` | DATETIME (UTC) |  | When an Authorization Request is created with a pending coverage, the Authorization Request is eligible for a one-time coverage change. If the coverage is changed, this item stores the instant in which the change was made. |
| 30 | `REQUESTING_ORGANIZATION_ID` | NUMERIC |  | The unique ID of the organization that initiated this auth request. |
| 31 | `REQUESTING_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 32 | `GUIDE_REVIEW_VENDOR_C_NAME` | VARCHAR | org | The guideline review vendor that is used for the guideline review process for the authorization request. |
| 33 | `GUIDE_REV_INIT_MTHD_C_NAME` | VARCHAR |  | The method used to initiate the guideline review process for the authorization request. |
| 34 | `GUIDE_REV_REQ_DTTM` | DATETIME (Local) |  | The instant the guideline review request was sent to the guideline review vendor. If the guideline review was manually initiated, this item is left blank. |
| 35 | `GUIDE_REV_REQ_UTC_DTTM` | DATETIME (UTC) |  | The instant the guideline review request was sent to the guideline review vendor. If the guideline review was manually initiated, this item is left blank. |
| 36 | `EXT_EVENT_MSG` | VARCHAR |  | Event-level MSG data received by Payer Platform from an external system. |
| 37 | `EXT_EVT_REF_NUM` | VARCHAR |  | the administrative reference number received by Payer Platform from an external system for this event |
| 38 | `EXT_EVT_AUTH_NUM` | VARCHAR |  | the authorization number received by Payer Platform from an external system for this event |
| 39 | `OVERTURNED_ON_APPEAL_YN` | VARCHAR |  | Indicates whether all denied services on this authorization request were later overturned on appeal. |
| 40 | `SPLIT_FROM_AUTH_REQUEST_ID` | NUMERIC |  | The AUG ID that this authorization request is split from. |
| 41 | `AUTH_BENEFIT_TYPE_C_NAME` | VARCHAR |  | The benefit type category ID of the authorization request indicating whether the authorization request applies to medical benefits or pharmacy benefits. |
| 42 | `SOURCE_AUTH_REQUEST_ID` | NUMERIC |  | Tracks the source authorization request that this request was created from. |
| 43 | `DERIVATION_TYPE_C_NAME` | VARCHAR |  | Indicates how the child authorization request was created from the parent request. |
| 44 | `PUBLISHED_START_DATE` | DATETIME |  | The authorization start date (I AUG 2600) from the published contact. |
| 45 | `OVERALL_APPEAL_DECISION_C_NAME` | VARCHAR |  | The overall decision of all appeals on this authorization request. This column is NULL if no appealed authorization requests are linked to this authorization request or if all appealed authorization requests are pending or closed. |
| 46 | `APPEALED_ORIG_AUTH_REQUEST_ID` | NUMERIC |  | The original authorization request's ID of this appeal authorization request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `LOB_ID` | [CLARITY_LOB](CLARITY_LOB.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

## Joined in — referenced by (22)

| From | Column | Confidence |
|------|--------|------------|
| [AUTH_REQUEST_EXT_TRN](AUTH_REQUEST_EXT_TRN.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX](AUTH_REQUEST_HX.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX_2](AUTH_REQUEST_HX_2.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX_COMMS](AUTH_REQUEST_HX_COMMS.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX_DXS](AUTH_REQUEST_HX_DXS.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX_ENT_INFO](AUTH_REQUEST_HX_ENT_INFO.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX_NOTES](AUTH_REQUEST_HX_NOTES.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX_OWNER](AUTH_REQUEST_HX_OWNER.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX_REASONS](AUTH_REQUEST_HX_REASONS.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_HX_UNS_NOTE](AUTH_REQUEST_HX_UNS_NOTE.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQUEST_REC_STAT_HX](AUTH_REQUEST_REC_STAT_HX.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQ_GUIDELINE_VENDOR](AUTH_REQ_GUIDELINE_VENDOR.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQ_HX_DECISION_REQT](AUTH_REQ_HX_DECISION_REQT.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQ_HX_NOTIF_IGN_TAT](AUTH_REQ_HX_NOTIF_IGN_TAT.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQ_HX_NOTIF_METHOD](AUTH_REQ_HX_NOTIF_METHOD.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQ_HX_NOTIF_OVRIDE](AUTH_REQ_HX_NOTIF_OVRIDE.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQ_HX_NOTIF_REQT](AUTH_REQ_HX_NOTIF_REQT.md) | `AUTH_REQUEST_ID` | high |
| [AUTH_REQ_HX_TIMELINESS](AUTH_REQ_HX_TIMELINESS.md) | `AUTH_REQUEST_ID` | high |
| [CRITERIA_REVIEW](CRITERIA_REVIEW.md) | `AUTH_REQUEST_ID` | high |
| [MYC_CONVO_ABT_REFERRALS](MYC_CONVO_ABT_REFERRALS.md) | `AUTH_REQUEST_ID` | high |
| [MYC_MESG](MYC_MESG.md) | `AUTH_REQUEST_ID` | high |
| [PR_EST_INFO_3](PR_EST_INFO_3.md) | `AUTH_REQUEST_ID` | high |

