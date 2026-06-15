# AP_CLM_RX_2

> This table contains information from pharmacy claims.

**Overflow of:** [AP_CLM_RX](AP_CLM_RX.md)  
**Primary key:** `CLAIM_ID`  
**Columns:** 32  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record |
| 2 | `PRIM_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 3 | `BCDA_GROUP_IDENT` | VARCHAR |  | Claim group identifier provided by Beneficiary Claims Data API (BCDA) |
| 4 | `TOT_PAT_PORTION` | NUMERIC |  | Total patient portion |
| 5 | `MOST_RECENT_INCOMING_CEV_ID` | NUMERIC |  | The most recent incoming Claim External Values (CEV) record ID |
| 6 | `CLAIM_HEADER_ID` | VARCHAR |  | Holds the claim header ID for the claim received from raw data |
| 7 | `ADJ_SEQUENCE` | VARCHAR |  | Holds the adjustment sequence for the claim received from raw data |
| 8 | `ADJ_TO_CLAIM_ID` | VARCHAR |  | Holds the adjustment to claim ID for the claim received from raw data |
| 9 | `REV_TO_CLAIM_ID` | VARCHAR |  | Holds the reversal to claim ID for the claim received from raw data |
| 10 | `IS_CLINICALLY_VALID_YN` | VARCHAR |  | Stores whether a claim is considered valid for the purpose of clinical data derivation |
| 11 | `KLCTCEV_RECORD_ID` | NUMERIC |  | Holds the CEV ID containing the KLCT metadata for a reversal claim. |
| 12 | `WORKFLOW_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 13 | `SOURCE_ORG_ID` | NUMERIC |  | The source organization of the external record. |
| 14 | `SOURCE_ORG_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 15 | `LOOP_OR_SPLIT_YN` | VARCHAR |  | Indicates whether a claim is part of an adjustment sequence that contains a split claim or an adjustment sequence loop. This CLM does not have to be in the split or loop istelf, just a part of the adjustment sequence. |
| 16 | `EXTERNAL_DEMOG_ID` | NUMERIC |  | Holds a pointer to the REQ record that holds the identifier and demographics that this claim was received with, linking this claim into an ID bundle. |
| 17 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 18 | `CLM_LOB_ID` | VARCHAR |  | Stores the unique identifier of the line of business associated with the claim. This is the LOB determined at adjudication. |
| 19 | `CLM_LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 20 | `IN_OUT_OF_NET_C_NAME` | VARCHAR | org | Contains the network level of a claim. |
| 21 | `CLAIM_PAID_DATE` | DATETIME |  | The date that the claim was paid, which is determined by the date the claim reaches the AP Status EOB Generated |
| 22 | `CLAIM_NAT_KEY_HASH` | VARCHAR |  | The hashed value of the mapped claim natural key. |
| 23 | `CLAIM_NAT_KEY_ORDER` | VARCHAR |  | The ordering value for the claim natural key. |
| 24 | `CLM_ADJ_TYPE_C_NAME` | VARCHAR |  | The Claim Adjustment Type Code |
| 25 | `NAT_KEY_FINAL_YN` | VARCHAR |  | Indicates whether a claim is the final action of an adjustment sequence that is tracking adjustments via natural keys. Natural key adjustments are tracked using superitem CLM 18690. A claim is the final action of its natural key if it has the maximum order value (item 18692) for a given natural key (item 18691). If there is a tie, the claim with the largest claim header id (item 18681) is deemed the final action. |
| 26 | `CLAIM_SVC_CLASS_CTX_C_NAME` | VARCHAR |  | Represents a high-level clinical classification context of the services billed for on this claim. |
| 27 | `CLAIM_SVC_CLASS_C_NAME` | VARCHAR |  | Represents a clinical classification for the services billed on this claim. |
| 28 | `CLIN_FILTER_UTC_DTTM` | DATETIME (UTC) |  | Last UTC instant clinical data derivation filters (I CLM 18625) were updated or calculated without changes for this claim. |
| 29 | `CLIN_FILTER_DTTM` | DATETIME (Local) |  | Last local instant clinical data derivation filters (I CLM 18625) were updated or calculated without changes for this claim. Calculated using EPIC_UTC_TO_LOCAL on I CLM 18626. |
| 30 | `REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 31 | `MEDICAL_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 32 | `SERVICE_DATE_FROM_LINE_YN` | VARCHAR |  | Indicates whether the service date was received at the header level, or was determined based on service lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

