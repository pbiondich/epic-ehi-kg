# COMMUNITY_RESOURCE

> This table stores details about the recommendation of a community resource for a patient. This table can be joined with the COMMUNITY_RESOURCE_CNCT table on COMMUNITY_RESOURCE__LAST_UPDATE_RECOM_CSN_ID and COMMUNITY_RESOURCE_CNCT__RECOMMENDATION_CSN_ID in order to form a resulting table that includes all current information about the community resource recommendation.

**Primary key:** `RECOMMENDATION_ID`  
**Columns:** 14  
**Org-specific columns:** 1  
**Joined by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECOMMENDATION_ID` | NUMERIC | PK | The unique identifier (.1 item) for the recommendation record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, or both) |
| 3 | `RECORD_TYPE_CRC_C_NAME` | VARCHAR |  | The type of this community resource recommendation record, used to differentiate various implementations of the CRC masterfile. |
| 4 | `PAT_ID` | VARCHAR | FK→ | The patient this community resource recommendation is for. |
| 5 | `CREATING_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The patient encounter in which this community resource recommendation was created. |
| 6 | `RESOURCE_FACILITY_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 7 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created |
| 8 | `RESOURCE_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `RESOURCE_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `RESOURCE_PROV_ADDRESS_ID` | VARCHAR |  | The unique address ID associated with the provider record to which the patient was recommended or referred. |
| 11 | `DP_COORD_TYPE_C_NAME` | VARCHAR | org | The coordination type. |
| 12 | `CREATING_SOURCE_C_NAME` | VARCHAR |  | This column contains the source of creation for a community resource recommendation row represented as a number indicating the category value of the creation source. |
| 13 | `RESOURCE_SVC_LN_ID` | NUMERIC |  | The service line or program ID to which the patient was recommended or referred to receive services. |
| 14 | `RESOURCE_SVC_LN_ID_SVC_LN_NAME` | VARCHAR |  | The name (.2 item) of the service line record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CREATING_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (6)

| From | Column | Confidence |
|------|--------|------------|
| [COMMUNITY_RESOURCE_CNCT](COMMUNITY_RESOURCE_CNCT.md) | `RECOMMENDATION_ID` | high |
| [COMMUNITY_RESOURCE_SDOH](COMMUNITY_RESOURCE_SDOH.md) | `RECOMMENDATION_ID` | high |
| [COMMUNITY_RESOURCE_SRVC](COMMUNITY_RESOURCE_SRVC.md) | `RECOMMENDATION_ID` | high |
| [COMMUNITY_RESRC_PRIM_SVC](COMMUNITY_RESRC_PRIM_SVC.md) | `RECOMMENDATION_ID` | high |
| [COMMUNITY_RESRC_SEC_SVC](COMMUNITY_RESRC_SEC_SVC.md) | `RECOMMENDATION_ID` | high |
| [DP_FACILITY](DP_FACILITY.md) | `RECOMMENDATION_ID` | high |

