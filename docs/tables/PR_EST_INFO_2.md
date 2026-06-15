# PR_EST_INFO_2

> General information about the price estimate. Split from PR_EST_INFO.

**Overflow of:** [PR_EST_INFO](PR_EST_INFO.md)  
**Primary key:** `ESTIMATE_ID`  
**Columns:** 27  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the patient estimate record. |
| 2 | `MATCHING_TREATMENT_ESTIMATE_ID` | NUMERIC |  | This items stores the treatment estimate matched to the associated visit grouper estimate. It is only populated for dental estimates. |
| 3 | `PREPAY_UPDATE_SOURCE_C_NAME` | VARCHAR |  | The source of prepay amount for the estimate. |
| 4 | `PREPAY_UPDATE_USER_ID` | VARCHAR |  | The user that last updated the prepay amount. |
| 5 | `PREPAY_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `PREPAY_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant at which the prepay amount was last updated. |
| 7 | `VAP_PROPOSED_AMT` | NUMERIC |  | The proposed consent amount for visit auto pay that should be applied to the encounter. |
| 8 | `VAP_SOURCE_C_NAME` | VARCHAR |  | The source of the visit auto pay proposed amount value. If the source is set to 1 - System Calculated - Visit, the visit auto pay amount is calculated based on configuration when the estimate is finalized. A user may override the visit auto pay amount at that point as well. If the source is set to 2 - User Override, a user specified an amount to use as the visit auto pay consent amount for the estimate's encounter. |
| 9 | `VAP_PROPOSAL_USER_ID` | VARCHAR |  | The last user who updated the visit auto pay proposal on the estimate. |
| 10 | `VAP_PROPOSAL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 11 | `VAP_PROPOSAL_DTTM` | DATETIME (Attached) |  | The last instant the visit auto pay proposal associated with the estimate was updated, formatted with time zone attached. |
| 12 | `GROUP_NUMBER` | VARCHAR |  | The group number for the coverage associated with this estimate. |
| 13 | `PAT_SEX_C_NAME` | VARCHAR | org | The patient's legal sex. |
| 14 | `PAT_BIRTH_DATE` | DATETIME |  | Date of birth of the patient. |
| 15 | `HB_SP_DSCNT_AMT` | NUMERIC |  | The total of all hospital billing self-pay discount amounts on an estimate. |
| 16 | `PB_SP_DSCNT_AMT` | NUMERIC |  | The total of all professional billing self-pay discount amounts on an estimate. |
| 17 | `TOT_SP_DSCNT_AMT` | NUMERIC |  | The total of all self-pay discount amounts on an estimate. |
| 18 | `HB_FIN_ASST_AMT` | NUMERIC |  | The total of all hospital billing financial assistance discount amounts on an estimate. |
| 19 | `PB_FIN_ASST_AMT` | NUMERIC |  | The total of all professional billing financial assistance discount amounts on an estimate. |
| 20 | `TOT_FIN_ASST_AMT` | NUMERIC |  | The total of all financial assistance discount amounts on an estimate. |
| 21 | `MYCHART_REQ_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 22 | `MYCHART_REQ_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 23 | `NOTIF_CONTENT_C_NAME` | VARCHAR |  | Stores what notification content was available when they are sent after an estimate was finalized. |
| 24 | `IS_EXTERNAL_ADJUDICATION_YN` | VARCHAR |  | Whether the estimate was adjudicated by an external payer or not. |
| 25 | `PRIMARY_CVG_ORGANIZATION_ID` | NUMERIC |  | Stores the organization record associated with the primary coverage on the estimate. |
| 26 | `PRIMARY_CVG_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 27 | `VARIANCE_WO_SKIP_RSN_C_NAME` | VARCHAR |  | The reason that an estimate is not eligible for an automatic variance write-off. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

