# DP_FACILITY

> This table contains information regarding Continued Care and Services Coordination, where each row represents a service considered for the patient's care. All services populated in a Continued Care and Services Coordination navigator section will be included in the table. The services can be provider (SER), facility (EAF), or department (DEP) records.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 36  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `PROV_ADDR_ID` | VARCHAR |  | Unique Address ID for the address in the provider/resource (SER) record that has been selected in a Continued Care and Services Coordination navigator section. A provider/resource (SER) record can have more than one address, and each address can be selected in a Continued Care and Services Coordination navigator section. |
| 7 | `DP_FAC_STATUS_C_NAME` | VARCHAR | org | The category ID of the request status for this service for this patient. |
| 8 | `STATUS_DTTM` | DATETIME (UTC) |  | Instant when the Continued Care and Services Coordination request status for this service was last updated for the specific patient. |
| 9 | `DEST_BOOL` | INTEGER |  | This indicates whether a service has been selected as a caregiver for the patient. A service is defined as a caregiver service if it's included in the list on the Case Management - Caregiver Services screen in System Definitions. |
| 10 | `DEST_DTTM` | DATETIME (UTC) |  | The instant the patient's selected caregiver flag for this service was last updated. |
| 11 | `LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 12 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 13 | `NOTE_ID` | VARCHAR | shared | This item is the note ID of a note record containing user comments about the related service in a Continued Care and Services Coordination navigator section for the given patient encounter. |
| 14 | `COORD_TYPE_C_NAME` | VARCHAR | org | The coordination type for Continued Care and Services Coordination. |
| 15 | `SELECTED_SERVICE_BOOL` | INTEGER |  | Set to 1 if this service is marked as a patient's selected service, 0 otherwise. |
| 16 | `ARCHIVE_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant a request or selected service for Continued Care and Services Coordination is archived. |
| 17 | `ARCHIVE_USER_ID` | VARCHAR |  | Stores the user who archives the request or selected service for Continued Care and Services Coordination. |
| 18 | `ARCHIVE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 19 | `ENC_LOC_HAS_FIN_INTEREST_YN` | VARCHAR |  | Records whether the patient's encounter location had a disclosable financial interest in this service provider at the time this service provider was first added to Continued Care and Services Coordination navigator section. Financial interest is determined by settings items I EAF 34017, I EAF 34018, I EAF 34019, and I EAF 34020. |
| 20 | `DECISION_UTC_DTTM` | DATETIME (UTC) |  | Stores the latest instant when the service provider decided whether they would accept the patient. This value will be cleared if the status is changed to pending. |
| 21 | `SELECTION_UTC_DTTM` | DATETIME (UTC) |  | Stores the latest instant when the service provider was selected. This value will be cleared if the service provider is unselected. |
| 22 | `ACCEPTED_DTTM` | DATETIME (Local) |  | Stores the instant when the patient's request for this service was accepted. |
| 23 | `ARCHIVE_DTTM` | DATETIME (Local) |  | Stores the instant when the patient's request for this service was archived. |
| 24 | `DECLINED_DTTM` | DATETIME (Local) |  | Stores by instant when the patient's request for this service was declined. |
| 25 | `SELECTION_DTTM` | DATETIME (Local) |  | Stores the instant when a service was selected from the patient's request for the service. |
| 26 | `ENC_SPECIFIC_FAX_NUMBER` | VARCHAR |  | This item holds a temporary fax number for a corresponding post-acute facility or agency during this encounter. This fax number can come from selecting a contact point for the post-acute facility/agency or from free text entry. A contact point contains a name, purposes, phone and fax and can be selected on the Contact Points popup in CCSC. |
| 27 | `RECOMMENDATION_ID` | NUMERIC | FK→ | The community resource recommendation record associated with this request. |
| 28 | `ACCEPTED_SELECTED_BUS_DAYS` | INTEGER |  | The number of business days between the accepted and selected dates. Business days exclude weekends and holidays. |
| 29 | `SELECTED_ENDED_BUS_DAYS` | INTEGER |  | The number of business days between the selected and end dates. Business days exclude weekends and holidays. |
| 30 | `ACCEPTED_ENDED_BUS_DAYS` | INTEGER |  | The number of business days between the accepted and end dates. Business days exclude weekends and holidays. |
| 31 | `COMP_BY_THIRD_PARTY_YN` | VARCHAR |  | A flag that is set when a third party marks a CCSC request as complete in a context that doesn't support archiving requests. This is not used for recommendation type requests or requests sent in a Compass Rose episode. |
| 32 | `SVC_LN_ID` | NUMERIC | FK→ | The ID of the service line associated with a service request for post-acute care documented in the Continued Care and Services Coordination (CCSC) activity. |
| 33 | `SVC_LN_ID_SVC_LN_NAME` | VARCHAR |  | The name (.2 item) of the service line record. |
| 34 | `ENC_SPEC_CNCT_NAME` | VARCHAR |  | The name of an encounter-specific contact point associated with a post-acute facility or agency. A contact point contains a name, purposes, phone and fax and can be selected on the Contact Points popup in CCSC. |
| 35 | `ENC_SPEC_CNCT_PHONE_NUM` | VARCHAR |  | The phone number of an encounter-specific contact point associated with a post-acute facility or agency. A contact point contains a name, purposes, phone and fax and can be selected on the Contact Points popup in CCSC. |
| 36 | `DP_FAC_PREF_PARTNER_TIER_C_NAME` | VARCHAR | org | The preferred partner type that this service request is a part of at the time of adding it to Continued Care and Services Coordination. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `RECOMMENDATION_ID` | [COMMUNITY_RESOURCE](COMMUNITY_RESOURCE.md) | sole_pk | high |
| `SVC_LN_ID` | [CARE_SVC_LN](CARE_SVC_LN.md) | sole_pk | high |

