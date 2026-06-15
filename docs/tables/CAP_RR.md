# CAP_RR

> The CAP_RR table contains information on capitation receipt and reconciliation transactions.

**Primary key:** `TX_ID`  
**Columns:** 57  
**Org-specific columns:** 3

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
| 11 | `RCPT_MEM_DOB` | DATETIME |  | The date of birth of the received member. |
| 12 | `RCPT_MEM_SEX_C_NAME` | VARCHAR | org | The sex of the received member. |
| 13 | `RCPT_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 14 | `RCPT_CARRIER_ID` | VARCHAR |  | The internal ID of the received carrier. |
| 15 | `RCPT_CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 16 | `RCPT_NETWORK_ID` | VARCHAR |  | The internal ID of the received network. |
| 17 | `RCPT_NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 18 | `RCPT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 19 | `RCPT_PLAN_GRP_ID` | VARCHAR |  | The internal ID of the received plan group. |
| 20 | `RCPT_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 21 | `RCPT_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 22 | `RCPT_PCP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 23 | `RCPT_SUB_ID` | VARCHAR |  | The ID of the received subscriber. |
| 24 | `RCPT_ADJ_CODE_C_NAME` | VARCHAR |  | The category value for the received adjustment code. |
| 25 | `RCPT_AMOUNT` | NUMERIC |  | The amount received for the transaction. |
| 26 | `CANCELED_BY_ID` | NUMERIC |  | The internal ID of the transaction which cancels this transaction. |
| 27 | `CANCELS_TX_ID` | NUMERIC |  | The internal ID of the transaction cancelled by this transaction. |
| 28 | `RCNCL_DISC_TYPE_C_NAME` | VARCHAR |  | The category value of the reconciliation discrepancy type. |
| 29 | `RCNCL_MEM_DOB` | DATETIME |  | The date of birth for the reconciled member. |
| 30 | `RCNCL_SEX_C_NAME` | VARCHAR |  | The sex of the reconciled member. |
| 31 | `RCNCL_NETWORK_ID` | VARCHAR |  | The internal ID of the reconciled network. |
| 32 | `RCNCL_NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 33 | `RCNCL_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 34 | `RCNCL_PLAN_GRP_ID` | VARCHAR |  | The internal ID of the reconciled plan group. |
| 35 | `RCNCL_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 36 | `RCNCL_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 37 | `RCNCL_PCP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 38 | `RCNCL_CVG_ID` | NUMERIC |  | The internal ID of the reconciled coverage. |
| 39 | `RCNCL_SUB_ID` | VARCHAR |  | The ID of the reconciled subscriber. |
| 40 | `RCNCL_AMOUNT` | NUMERIC |  | The amount reconciled. |
| 41 | `RCPT_MGRP_ID_MEM_GRP_NAME` | VARCHAR |  | The name of the member group |
| 42 | `RCPT_LOB_ID` | VARCHAR |  | The capitation receipt line of business. |
| 43 | `RCPT_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 44 | `RCPT_RKP_ID` | VARCHAR |  | The unique ID of the risk panel used for capitation receipt. |
| 45 | `RCPT_RKP_ID_RISK_PANEL_NAME` | VARCHAR |  | The name of the risk panel. |
| 46 | `RCNCL_LOB_ID` | VARCHAR |  | The capitation reconciliation line of business. |
| 47 | `RCNCL_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 48 | `RCNCL_RKP_ID` | VARCHAR |  | The unique ID of the risk panel used for capitation reconciliation. |
| 49 | `RCNCL_RKP_ID_RISK_PANEL_NAME` | VARCHAR |  | The name of the risk panel. |
| 50 | `RCPT_MEM_ID_CVG` | VARCHAR |  | The member ID from an incoming capitation file. |
| 51 | `RCNCL_MEMBER_ID_CVG` | VARCHAR |  | The member ID used for reconciling incoming capitation. |
| 52 | `RCPT_ADJ_TYPE_C_NAME` | VARCHAR | org | Stores the type of the capitation payment adjustment. |
| 53 | `RCNCL_DISC_DETAILS` | VARCHAR |  | Stores additional information about the discrepancy that is logged for this transaction. |
| 54 | `RCNCL_MONTHLY_AMT` | NUMERIC |  | Stores the full monthly amount used when calculating the expected capitation payment amount prior to proration settings if the payment was calculated using a capitation age/sex rate table. |
| 55 | `RCNCL_ELIG_PORTION` | NUMERIC |  | If a member is only eligible for capitation for a portion of a computed month and the member group is configured to prorate capitation, this item will store the decimal value of the prorated portion. |
| 56 | `RCNCL_RATE_FACTOR` | NUMERIC |  | When the benefit plan associated with a member includes a capitation rate factor, this item will store the value so an accurate rate calculation can be reconstructed. |
| 57 | `CAP_RR_PRORATION_C_NAME` | VARCHAR |  | Stores the proration method used during capitation reconciliation to calculate the expected amount for a capitation monthly payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

