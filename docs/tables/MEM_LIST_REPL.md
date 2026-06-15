# MEM_LIST_REPL

> This table contains member context information for capitation transactions.

**Primary key:** `MEM_LIST_ID`  
**Columns:** 20  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MEM_LIST_ID` | NUMERIC | PK shared | The ID of the transaction member list record computed as part of the specialty capitation payment process. |
| 2 | `EFFECTIVE_DATE` | DATETIME |  | The effective date of the specialty capitation payment computation. |
| 3 | `ELIGIBILITY_DATE` | DATETIME |  | The test date used to determine if a member is eligible for inclusion in specialty capitation payment computations. |
| 4 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 5 | `CARRIER_ID` | VARCHAR | FK→ | The ID of the carrier that defines the context of the specialty capitation payment computation. |
| 6 | `CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 7 | `NETWORK_ID` | VARCHAR | FK→ | The ID of the network that defines the context of the specialty capitation payment computation. |
| 8 | `NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 9 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 10 | `RKP_ID` | VARCHAR | FK→ | The unique ID of the risk panel for the member. |
| 11 | `RKP_ID_RISK_PANEL_NAME` | VARCHAR |  | The name of the risk panel. |
| 12 | `LOB_ID` | VARCHAR | FK→ | The unique ID of the line of business for the member. |
| 13 | `LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 14 | `MGRP_ID_MEM_GRP_NAME` | VARCHAR |  | The name of the member group |
| 15 | `MEM_LIST_TYPE_C_NAME` | VARCHAR |  | The type of member list that this record represents. |
| 16 | `ADJUST_ORIG_LIST_ID` | NUMERIC |  | The ID of the transaction member list that this list adjusts. |
| 17 | `LOAD_BATCH_DATE` | DATETIME |  | The date that the member list was loaded into the system. |
| 18 | `ASSOC_EXT_VAL_C_NAME` | VARCHAR | org | The member group association value for the member list. |
| 19 | `CAPITATION_CODE_C_NAME` | VARCHAR | org | The capitation code associated with the transaction. |
| 20 | `PRODUCT_TYPE_C_NAME` | VARCHAR | org | The product type associated with the member list. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CARRIER_ID` | [CLARITY_CARRIER](CLARITY_CARRIER.md) | sole_pk | high |
| `LOB_ID` | [CLARITY_LOB](CLARITY_LOB.md) | sole_pk | high |
| `NETWORK_ID` | [CLARITY_NETWORK](CLARITY_NETWORK.md) | sole_pk | high |
| `RKP_ID` | [CLARITY_RKP](CLARITY_RKP.md) | sole_pk | high |

