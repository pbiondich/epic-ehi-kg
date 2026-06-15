# CAP_PAYMENT

> The CAP_PAYMENT table contains information about capitation payments.

**Primary key:** `TX_ID`  
**Columns:** 52  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The internal ID of the transaction. |
| 2 | `TX_TYPE_C_NAME` | VARCHAR |  | The type of the transaction. |
| 3 | `TX_STATUS_C_NAME` | VARCHAR |  | The status of the transaction. |
| 4 | `SPECIAL_TX_TYPE_C_NAME` | VARCHAR | org | The special transaction type of the transaction. |
| 5 | `EFFECTIVE_DATE` | DATETIME |  | The effective date of the transaction. |
| 6 | `POSTING_DATE` | DATETIME |  | The posting date of the transaction. |
| 7 | `ELIGIBILITY_DATE` | DATETIME |  | The eligibility date of the transaction. |
| 8 | `USER_ID` | VARCHAR | FK→ | The ID of the user who created the transaction. |
| 9 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `COMMENT_LINE` | VARCHAR |  | The free text comment of the transaction. |
| 11 | `MEM_DOB_DT` | DATETIME |  | The date of birth of the member in the transaction. |
| 12 | `MEM_SEX_C_NAME` | VARCHAR | org | The sex of the member in the transaction. |
| 13 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 14 | `CARRIER_ID` | VARCHAR | FK→ | The carrier ID of the transaction. |
| 15 | `CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 16 | `NETWORK_ID` | VARCHAR | FK→ | The network ID of the transaction. |
| 17 | `NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 18 | `PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 19 | `PLAN_GRP_ID` | VARCHAR | FK→ | The employer group ID of the transaction. |
| 20 | `PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 21 | `LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 22 | `PCP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 23 | `COVERAGE_ID` | NUMERIC | FK→ | The coverage ID of the member in the transaction. |
| 24 | `SPECIALTY_C_NAME` | VARCHAR | org | The specialty of the transaction. |
| 25 | `SPEC_RATE` | NUMERIC |  | The rate for specialty of the transaction. |
| 26 | `VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 27 | `TX_CANC_TX_ID` | NUMERIC |  | The transaction ID which cancels this transaction. |
| 28 | `REPLACES_DTX_ID` | NUMERIC |  | The transaction that this transaction replaces. |
| 29 | `REPLACED_BY_DTX_ID` | NUMERIC |  | The transaction which replaced this transaction. |
| 30 | `RTRO_CNCL_BY_ID` | NUMERIC |  | The retro transaction ID that canceled this transaction. |
| 31 | `RTRO_CNCL_RSN_C_NAME` | VARCHAR |  | The category of the retro mismatch code. |
| 32 | `SPEC_MEMBER_MONTHS` | INTEGER |  | The specialty member months of the transaction. |
| 33 | `DIST_LOB_ID` | VARCHAR |  | The capitation payment line of business. |
| 34 | `DIST_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 35 | `DIST_RKP_ID` | VARCHAR |  | The unique ID of the risk panel for capitation distribution. |
| 36 | `DIST_RKP_ID_RISK_PANEL_NAME` | VARCHAR |  | The name of the risk panel. |
| 37 | `DIST_MGRP_ID_MEM_GRP_NAME` | VARCHAR |  | The name of the member group |
| 38 | `CAP_RETRO_LEVEL` | INTEGER |  | Retro level capitation transactions. |
| 39 | `RELEASED_TO_AP_YN` | VARCHAR |  | Whether the transaction has been released to accounts payable (AP). |
| 40 | `CAP_COUNTY_C_NAME` | VARCHAR | org | The member's county used in outgoing capitation. |
| 41 | `CAP_CVG_ATTRIBUTES_EXTERNAL` | VARCHAR |  | The coverage's attributes used in outgoing capitation formatted by category list CVG 2001. |
| 42 | `MCARE_CONTRACT_NUM` | VARCHAR |  | The medicare advantage contract number that matches the Member Group's medicare advantage contract number. |
| 43 | `WITHHOLD_REASON_C_NAME` | VARCHAR |  | The capitation payment withhold reason category ID for the transaction. |
| 44 | `CAPITATION_CODE_C_NAME` | VARCHAR | org | The capitation code associated with the transaction. |
| 45 | `REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 46 | `MEDICAL_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 47 | `PRODUCT_TYPE_C_NAME` | VARCHAR | org | The product type associated with the transaction. |
| 48 | `PCP_AMOUNT` | NUMERIC |  | The amount for this transaction. This is only populated for PCP capitation transactions. |
| 49 | `MEM_LIST_ID` | NUMERIC | shared | The unique ID of the associated transaction member list. It is only populated for Specialty Capitation transactions that utilize a new member list. |
| 50 | `MEM_COUNT` | INTEGER |  | The number of members listed for the transaction. This data is only populated for Specialty Capitation transactions. |
| 51 | `ELIGIBILITY_PORTION` | NUMERIC |  | If a member is only eligible for capitation for a portion of a computed month and the member group is configured to prorate capitation, this item will store the decimal value of the prorated portion. |
| 52 | `RATE_FACTOR` | NUMERIC |  | When the benefit plan associated with a member includes a capitation rate factor, this item will store the value so an accurate rate calculation can be reconstructed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARRIER_ID` | [CLARITY_CARRIER](CLARITY_CARRIER.md) | sole_pk | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `NETWORK_ID` | [CLARITY_NETWORK](CLARITY_NETWORK.md) | sole_pk | high |
| `PLAN_GRP_ID` | [PLAN_GRP](PLAN_GRP.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

