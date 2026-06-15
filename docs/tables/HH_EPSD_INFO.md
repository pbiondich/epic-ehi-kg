# HH_EPSD_INFO

> This table contains Home Health/Hospice episode information. It contains the noadd single items for the Episode. These items are entered by a user as part of the Intake encounter.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 60  
**Org-specific columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the episode. |
| 2 | `TEAM_ASSIGNMENT_C_NAME` | VARCHAR | org | Team assignment category list selection for the episode. Links to category table ZC_TEAM_ASSIGNMENT. |
| 3 | `DME_CO_ID` | NUMERIC |  | This column contains the durable medical equipment supplier for the patient's episode. The column links to table RX_PHR. |
| 4 | `DME_CO_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 5 | `LABORATORY_ID` | NUMERIC |  | The unique id of the laboratory. |
| 6 | `LABORATORY_ID_LLB_NAME` | VARCHAR |  | Interface laboratory name. |
| 7 | `HOME_INFUSN_CO_ID` | NUMERIC |  | ID for the home infusion company for the episode. Links to table RX_PHR. |
| 8 | `HOME_INFUSN_CO_ID_PHARMACY_NAME` | VARCHAR |  | The name of the pharmacy. |
| 9 | `HOME_CARE_CITY` | VARCHAR |  | City in the home care address for the episode. |
| 10 | `HOME_CARE_STATE_C_NAME` | VARCHAR | org | Category list selection for home care state for the episode. Links to category table ZC_STATE. |
| 11 | `HOME_CARE_ZIP` | VARCHAR |  | ZIP code for the home care address for the episode. |
| 12 | `HOME_CARE_PHONE` | VARCHAR |  | Phone number for the home care address for the episode. |
| 13 | `PAT_WEIGHT` | NUMERIC |  | Patient weight entered for the episode. |
| 14 | `PAT_HEIGHT` | VARCHAR |  | Patient height entered for the episode. |
| 15 | `CARE_PLAN_ID` | VARCHAR |  | This item stores the careplan ID. |
| 16 | `EPISODE_DELETED_C_NAME` | VARCHAR | org | Depending on whether the episode is deleted, this item stores the category list selection for the episode. Links to category table ZC_EPISODE_DELETED. |
| 17 | `OUTPAT_ADMSN_C_NAME` | VARCHAR |  | Is this an outpatient admission? Links to category table ZC_OUTPAT_ADMSN. |
| 18 | `INTERPRETER_NEED_C_NAME` | VARCHAR |  | Is an interpreter needed for the episode? Links to category table ZC_OUTPAT_ADMSN. |
| 19 | `TRIAGE_CODE_C_NAME` | VARCHAR | org | Triage code category list selection for the episode. Links to category table ZC_TRIAGE_CODE. |
| 20 | `REFERRAL_RECVD_TIM` | DATETIME (Local) |  | Time the referral for this episode was received. |
| 21 | `REFERRAL_AUTHOR` | VARCHAR |  | Author of the referral for this episode. |
| 22 | `RFL_AUTHOR_PHONE` | VARCHAR |  | Referral author phone number. |
| 23 | `REASON_DISCH_C_NAME` | VARCHAR | org | Reason for discharge category list selection for the episode. Links to category table ZC_REASON_DISCH. |
| 24 | `HH_EPISODE_TYPE_C_NAME` | VARCHAR | org | Home Health episode type category list selection for the episode. Links to category table ZC_HH_EPS_TYPE. |
| 25 | `HC_ADM_STAT_C_NAME` | VARCHAR |  | This item tracks the status of the Home Care episode admission. |
| 26 | `HOSPICE_ELEC_DT` | DATETIME |  | Hospice Election Date |
| 27 | `HOSPICE_REV_DT` | DATETIME |  | Holds the Hospice Revocation Date |
| 28 | `HC_ADM_SOURCE_C_NAME` | VARCHAR | org | This item contains the source the patient was admitted from. |
| 29 | `HC_DC_DISPOSITION_C_NAME` | VARCHAR | org | This item stores the patient's discharge disposition. |
| 30 | `NUM_PREV_EPSD_C_NAME` | VARCHAR |  | Holds the Previous Number of Consecutive Home Health Episodes |
| 31 | `RFL_SRC_RPT_C_NAME` | VARCHAR | org | This item contains a customer defined list of referral sources. |
| 32 | `HSPC_DC_REAS_C_NAME` | VARCHAR | org | This item stores the reason for discharge for a hospice admission. |
| 33 | `PRIM_DX_RPT_C_NAME` | VARCHAR | org | Custom item for customers to fill in. |
| 34 | `EPISODE_TYPE_ID_EPISODE_DEF_NAME` | VARCHAR |  | This column displays the name of the episode / block definition record. |
| 35 | `COMP_ASMT_COMP_DTTM` | DATETIME (UTC) |  | This item marks the instant at which the hospice comprehensive assessment was first completed. This happens automatically when all sections of the comprehensive assessment have been documented at least once. |
| 36 | `COMP_ASMT_COMP_CSN` | NUMERIC |  | This column stores the contact serial number (CSN) of the patient encounter in which the comprehensive assessment was first completed. That is, the first encounter closed in which all of the sections of the comprehensive assessment have been documented at least once. |
| 37 | `HH_LINKED_UIC_ID` | NUMERIC |  | In traveler mode each patient will have one episode per unit. This item allows an episode to be linked to a particular unit. Hence, facilitating retrieval of episode information of patients assigned to a specific unit. |
| 38 | `HH_LINKED_UIC_ID_RECORD_NAME` | VARCHAR |  | This column stores the name of the military unit's record. |
| 39 | `HOSPICE_EFF_DT` | DATETIME |  | The date the hospice agency began taking care of the patient. |
| 40 | `PECOS_COMPLY_YN` | VARCHAR |  | This column stores whether the episode is PECOS compliant. An episode is PECOS compliant if all necessary providers (referring provider, plan of care provider) are PECOS enrolled. |
| 41 | `HOME_CARE_COUNTY_C_NAME` | VARCHAR | org | This item stores the county of the patient's home care address. The home care address is the address where the patient will be receiving home health or hospice care. |
| 42 | `HSPC_PRIOR_DAYS_ON_SVC` | INTEGER |  | Stores the number of CMS-qualified days the patient was in hospice care prior to this admission - This number persists between episodes, but resets to 0 after 60 days discharged. |
| 43 | `HH_COVCHG_IND_DT` | DATETIME |  | This item is used to flag a Home Health episode as needing a coverage change. When the coverage change workflow is completed, this date is removed. |
| 44 | `HH_COVCHG_IND_COVERAGE_ID` | NUMERIC |  | This item stores the new primary coverage for a coverage change. When the coverage change workflow is completed, this ID is removed. |
| 45 | `DISCH_SOURCE_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the contact serial number (CSN) of the encounter from which this episode's Discharge Date, Disposition, and Reason for Discharge are populated. |
| 46 | `HOME_CARE_COUNTRY_2_C_NAME` | VARCHAR | org | This column stores the country of the patient's home care address. The home care address is the address where the patient will be receiving home health or hospice care. |
| 47 | `HOME_CARE_HOUSE_NUMBER` | VARCHAR |  | This column stores the house number of the patient's home care address. The home care address is the address where the patient will be receiving home health or hospice care. |
| 48 | `HOME_CARE_DISTRICT_C_NAME` | VARCHAR | org | This column stores the district of the patient's home care address. The home care address is the address where the patient will be receiving home health or hospice care. |
| 49 | `HC_ADDR_LATITUDE` | VARCHAR |  | The geocoded latitude for the home care address in numerical degrees with up to 6 decimals of accuracy. |
| 50 | `HC_ADDR_LONGITUDE` | VARCHAR |  | The geocoded longitude for the home care address in numerical degrees with up to 6 decimals of accuracy. |
| 51 | `HC_ADDR_GEO_RATING` | VARCHAR |  | The HC_ADDR_GEO_RATING rates the accuracy of latitude and longitude for the home care address. The rating is a calculated value determined by taking the lesser of the request-to-response granularity and vendor confidence scores. A is a perfect match to house number with perfect vendor confidence. B is equivalent to a street level specificity or a vendor confidence level in the 100-90 range. Ratings less than that are at best city or county specific and degrade in alphabetical order until E. |
| 52 | `EPI_STATUS_C_NAME` | VARCHAR |  | Current status of this episode. |
| 53 | `COVCHG_IND_PAT_STATUS_C_NAME` | VARCHAR |  | The discharge disposition recorded for a truncated hospital account following a coverage change. |
| 54 | `COVCHG_IND_HH_COVCHG_TYPE_C_NAME` | VARCHAR |  | The type of coverage change needed on the Home Health episode. |
| 55 | `INBASKET_MSG` | VARCHAR |  | InBasket Message IDs within this episode. |
| 56 | `UNKNOWN_REF_PROV_YN` | VARCHAR |  | Set if the referring provider is unidentified. |
| 57 | `INTAKE_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique patient contact serial number for the intake encounter for a home health/hospice episode. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 58 | `HC_COMP_ASMT_OVRD_C_NAME` | VARCHAR | org | This item, when populated, may override the default comprehensive assessment configured for a patient's Hospice intake department. The department needs to map the value populated in this item with the new comprehensive assessment to use. |
| 59 | `HSPC_ELECTION_DATE_RTE_SRC_C_NAME` | VARCHAR |  | Stores whether the election was pulled from RTE or not. |
| 60 | `HSPC_PRIOR_DAYS_RTE_SRC_C_NAME` | VARCHAR |  | Stores whether the prior days on service was pulled from RTE or not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DISCH_SOURCE_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `INTAKE_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

