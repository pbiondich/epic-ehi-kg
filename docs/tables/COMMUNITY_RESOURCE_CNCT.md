# COMMUNITY_RESOURCE_CNCT

> This table stores updates made to community resource recommendations for a patient. Each update to a CRC record is represented by a new row in this table with a new contact date.

**Primary key:** `RECOMMENDATION_ID`, `CONTACT_DATE_REAL`  
**Columns:** 18  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECOMMENDATION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the recommendation record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `DOCUMENTING_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant at which this contact was created. |
| 4 | `DOCUMENTING_SOURCE_C_NAME` | VARCHAR |  | The source of creation of this contact. |
| 5 | `DOCUMENTING_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The patient encounter from which this contact was created. |
| 6 | `DOCUMENTING_USER_ID` | VARCHAR |  | The user who was responsible for the creation of this contact. |
| 7 | `DOCUMENTING_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `USAGE_CRC_C_NAME` | VARCHAR |  | The usage of this community resource recommendation. |
| 9 | `NOT_USED_REASON_C_NAME` | VARCHAR | org | The reason that this community resource was not utilized by the patient. |
| 10 | `COMPLETED_OUTCOME_C_NAME` | VARCHAR | org | The outcome of this completed community resource recommendation. |
| 11 | `COMMENT_NOTE_CSN_ID` | NUMERIC |  | The HNO CSN of the comment associated with this community resource recommendation. |
| 12 | `HISTORIC_YN` | VARCHAR |  | Whether the community resource is historic (Y) or current (N). |
| 13 | `HIST_LINE_OV_IDENT` | INTEGER |  | The historical line for information associated with the community resource's contact (stored in related group EPT 34000). Use this column, in conjunction with column CREATING_PAT_ENC_CSN_ID in table COMMUNITY_RESOURCE, to join to DP_FACILITY, which contains more information on the community resource's contact. |
| 14 | `DOCUMENTING_MYPT_ID` | VARCHAR |  | The unique ID of the MyChart user who created this contact. |
| 15 | `IS_SENSITIVITY_OVERRIDDEN_YN` | VARCHAR |  | Whether the user manually updated the sensitivity of the community resource/service request. |
| 16 | `ASSOC_ORDER_ID` | NUMERIC |  | Stores the order ID of the post-discharge referral order that is associated with this service request. Orders are automatically associated with service requests upon selection if the service request's primary service (MAG) matches the primary service on the order's procedure (EAP) record. |
| 17 | `SVC_REQ_DESELECT_RSN_C_NAME` | VARCHAR | org | This column is used to document the reason a service request was deselected in CCM CCSC workflows for auditing purposes. Currently, this deselection reason is only documented when deselecting service requests that have an associated referral order, since deselecting a service provider and/or selecting another service provider will affect where the associated referral record is routed to. |
| 18 | `DESELECT_REASON_COMMENT` | VARCHAR |  | The comment for a deselection reason of 99999 - Other (Comment). Other deselection reasons should not have a comment specified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DOCUMENTING_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `RECOMMENDATION_ID` | [COMMUNITY_RESOURCE](COMMUNITY_RESOURCE.md) | sole_pk | high |

