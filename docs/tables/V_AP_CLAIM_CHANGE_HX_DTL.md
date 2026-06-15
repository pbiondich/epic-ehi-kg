# V_AP_CLAIM_CHANGE_HX_DTL

> Contains detailed information about changes made to an AP claim.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 69

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier of the accounts payable claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | The Change History Action category ID for the claim record. Indicates the item changed on the claim (i.e. workflow, workflow other status, etc.). |
| 4 | `PREV_VAL_RAW` | VARCHAR |  | The value of the item before the change was made to the claim. IDs are not translated, so if Intraconnect is used, mapping to CIDs is necessary. |
| 5 | `NEW_VAL_RAW` | VARCHAR |  | The value of the item after the change was made to the claim. IDs are not translated, so if Intraconnect is used, mapping to CIDs is necessary. |
| 6 | `PREV_CLAIM_ID` | NUMERIC |  | The claim ID stored in the item before the change was made to the claim. This column only contains data for items that store claim IDs. |
| 7 | `NEW_CLAIM_ID` | NUMERIC |  | The claim ID stored in the item after the change was made to the claim. This column only contains data for items that store claim IDs. |
| 8 | `PREV_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 9 | `NEW_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 10 | `PREV_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 11 | `NEW_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 12 | `PREV_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 13 | `NEW_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 14 | `PREV_COVERAGE_ID` | NUMERIC |  | The coverage ID stored in the item before the change was made to the claim. This column only contains data for items that store coverage IDs. |
| 15 | `NEW_COVERAGE_ID` | NUMERIC |  | The coverage ID stored in the item after the change was made to the claim. This column only contains data for items that store coverage IDs. |
| 16 | `PREV_REFERRAL_ID` | NUMERIC |  | The referral ID stored in the item before the change was made to the claim. This column only contains data for items that store referral IDs. |
| 17 | `NEW_REFERRAL_ID` | NUMERIC |  | The referral ID stored in the item after the change was made to the claim. This column only contains data for items that store referral IDs. |
| 18 | `PREV_RUL_ID` | NUMERIC |  | The third party pricing rule, entity or grouper ID stored in the item before the change was made to the claim. This column only contains data for items that store third party pricing rule, entity or grouper IDs. |
| 19 | `PREV_RUL_ID_RUL_NAME` | VARCHAR |  | The name of the third-party pricing entity, grouper, or rule. |
| 20 | `NEW_RUL_ID` | NUMERIC |  | The third party pricing rule, entity or grouper ID stored in the item after the change was made to the claim. This column only contains data for items that store third party pricing rule, entity or grouper IDs. |
| 21 | `NEW_RUL_ID_RUL_NAME` | VARCHAR |  | The name of the third-party pricing entity, grouper, or rule. |
| 22 | `PREV_FRZN_STATUS_C` | INTEGER |  | The category ID of the frozen status stored in the item before the change was made to the claim. This column only contains data for items that store frozen status category IDs. |
| 23 | `NEW_FRZN_STATUS_C` | INTEGER |  | The category ID of the frozen status stored in the item after the change was made to the claim. This column only contains data for items that store frozen status category IDs. |
| 24 | `PREV_CLM_STATUS_C` | INTEGER |  | The category ID of the claim status stored in the item before the change was made to the claim. This column only contains data for items that store claim status category IDs. |
| 25 | `NEW_CLM_STATUS_C` | INTEGER |  | The category ID of the claim status stored in the item after the change was made to the claim. This column only contains data for items that store claim status category IDs. |
| 26 | `PREV_AP_STATUS_C` | INTEGER |  | The category ID of the AP status stored in the item before the change was made to the claim. This column only contains data for items that store AP status category IDs. |
| 27 | `NEW_AP_STATUS_C` | INTEGER |  | The category ID of the AP status stored in the item after the change was made to the claim. This column only contains data for items that store AP status category IDs. |
| 28 | `PREV_WKFLW_OTHER_STATUS_C` | INTEGER |  | The category ID of the workflow other status stored in the item before the change was made to the claim. This column only contains data for items that store workflow other status category IDs. |
| 29 | `NEW_WKFLW_OTHER_STATUS_C` | INTEGER |  | The category ID of the workflow other status stored in the item after the change was made to the claim. This column only contains data for items that store workflow other status category IDs. |
| 30 | `PREV_WKFLW_PRINT_STATUS_C` | INTEGER |  | The category ID of the workflow print status stored in the item before the change was made to the claim. This column only contains data for items that store workflow print status category IDs. |
| 31 | `NEW_WKFLW_PRINT_STATUS_C` | INTEGER |  | The category ID of the workflow print status stored in the item after the change was made to the claim. This column only contains data for items that store workflow print status category IDs. |
| 32 | `PREV_CLAIM_TRAIT_1_C` | INTEGER |  | The category ID of the first claim trait stored in the item before the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 33 | `NEW_CLAIM_TRAIT_1_C` | INTEGER |  | The category ID of the first claim trait stored in the item after the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 34 | `PREV_CLAIM_TRAIT_2_C` | INTEGER |  | The category ID of the second claim trait stored in the item before the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 35 | `NEW_CLAIM_TRAIT_2_C` | INTEGER |  | The category ID of the second claim trait stored in the item after the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 36 | `PREV_CLAIM_TRAIT_3_C` | INTEGER |  | The category ID of the third claim trait stored in the item before the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 37 | `NEW_CLAIM_TRAIT_3_C` | INTEGER |  | The category ID of the third claim trait stored in the item after the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 38 | `PREV_CLAIM_TRAIT_4_C` | INTEGER |  | The category ID of the fourth claim trait stored in the item before the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 39 | `NEW_CLAIM_TRAIT_4_C` | INTEGER |  | The category ID of the fourth claim trait stored in the item after the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 40 | `PREV_CLAIM_TRAIT_5_C` | INTEGER |  | The category ID of the fifth claim trait stored in the item before the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 41 | `NEW_CLAIM_TRAIT_5_C` | INTEGER |  | The category ID of the fifth claim trait stored in the item after the change was made to the claim. This column only contains data for items that store claim trait category IDs. |
| 42 | `PREV_HELD_FOR_AP_RSN_C` | INTEGER |  | The category ID of the held for AP reason stored in the item before the change was made to the claim. This column only contains data for items that store held for AP reason category IDs. |
| 43 | `NEW_HELD_FOR_AP_RSN_C` | INTEGER |  | The category ID of the held for AP reason stored in the item after the change was made to the claim. This column only contains data for items that store held for AP reason category IDs. |
| 44 | `PREV_POS_TYPE_C` | INTEGER |  | The category ID of the place of service type stored in the item before the change was made to the claim. This column only contains data for items that store place of service type category IDs. |
| 45 | `NEW_POS_TYPE_C` | INTEGER |  | The category ID of the place of service type stored in the item after the change was made to the claim. This column only contains data for items that store place of service type category IDs. |
| 46 | `PREV_CLAIM_SPEC_C` | VARCHAR |  | The category ID of the claim specialty stored in the item before the change was made to the claim. This column only contains data for items that store claim specialty category IDs. |
| 47 | `NEW_CLAIM_SPEC_C` | VARCHAR |  | The category ID of the claim specialty stored in the item after the change was made to the claim. This column only contains data for items that store claim specialty category IDs. |
| 48 | `PREV_OVRIDE_DISALW_AMT_RSN_C` | INTEGER |  | The category ID of the override disallow amount reason stored in the item before the change was made to the claim. This column only contains data for items that store override disallow amount reason category IDs. |
| 49 | `NEW_OVRIDE_DISALW_AMT_RSN_C` | INTEGER |  | The category ID of the override disallow amount reason stored in the item after the change was made to the claim. This column only contains data for items that store override disallow amount reason category IDs. |
| 50 | `PREV_OVRIDE_ALLOW_AMT_RSN_C` | INTEGER |  | The category ID of the override allow amount reason stored in the item before the change was made to the claim. This column only contains data for items that store override allow amount reason category IDs. |
| 51 | `NEW_OVRIDE_ALLOW_AMT_RSN_C` | INTEGER |  | The category ID of the override allow amount reason stored in the item after the change was made to the claim. This column only contains data for items that store override allow amount reason category IDs. |
| 52 | `PREV_TYPE_OF_SERVICE_C` | INTEGER |  | The category ID of the type of service stored in the item before the change was made to the claim. This column only contains data for items that store type of service category IDs. |
| 53 | `NEW_TYPE_OF_SERVICE_C` | INTEGER |  | The category ID of the type of service stored in the item after the change was made to the claim. This column only contains data for items that store type of service category IDs. |
| 54 | `PREV_WORKFLOW_C` | INTEGER |  | The category ID of the claim workflow stored in the item before the change was made to the claim. This column only contains data for items that store claim workflow category IDs. |
| 55 | `NEW_WORKFLOW_C` | INTEGER |  | The category ID of the claim workflow stored in the item after the change was made to the claim. This column only contains data for items that store claim workflow category IDs. |
| 56 | `PREV_VAL_YN` | VARCHAR |  | The Yes/No value stored in the item before the change was made to the claim. This column only contains data for items that store Yes/No values. |
| 57 | `NEW_VAL_YN` | VARCHAR |  | The Yes/No value stored in the item after the change was made to the claim. This column only contains data for items that store Yes/No values. |
| 58 | `PREV_NDC_ID` | VARCHAR |  | The NDC code ID stored in the item before the change was made to the claim. This column only contains data for items that store NDC code IDs. |
| 59 | `PREV_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 60 | `NEW_NDC_ID` | VARCHAR |  | The NDC code ID stored in the item after the change was made to the claim. This column only contains data for items that store NDC code IDs. |
| 61 | `NEW_NDC_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |
| 62 | `PREV_NDC_UNITS_C` | INTEGER |  | The category ID of the NDC Units before the change was made to the claim. This column only contains data for items that store NDC Units category IDs. |
| 63 | `NEW_NDC_UNITS_C` | INTEGER |  | The category ID of the NDC Units after the change was made to the claim. This column only contains data for items that store NDC Units category IDs. |
| 64 | `PREV_DENY_CLAIM_SOURCE_C` | INTEGER |  | The category ID of the deny claim source stored in the item before the change was made to the claim. This column only contains data for items that store deny claim source category IDs. |
| 65 | `NEW_DENY_CLAIM_SOURCE_C` | INTEGER |  | The category ID of the deny claim source stored in the item after the change was made to the claim. This column only contains data for items that store deny claim source category IDs. |
| 66 | `PREV_HCFA_UNCLEAN_YN` | VARCHAR |  | The category ID of the CMS (un)clean status stored in the item before the change was made to the claim. This column only contains data for items that store the CMS (un)clean status of a claim. |
| 67 | `NEW_HCFA_UNCLEAN_YN` | VARCHAR |  | The category ID of the CMS (un)clean status stored in the item after the change was made to the claim. This column only contains data for items that store the CMS (un)clean status of a claim. |
| 68 | `PREV_AP_CLM_AR_STATUS_C` | INTEGER |  | The category ID of the AR status stored in the item before the change was made to the claim. This column only contains data for items that store AR status category IDs. |
| 69 | `NEW_AP_CLM_AR_STATUS_C` | INTEGER |  | The category ID of the AR status stored in the item after the change was made to the claim. This column only contains data for items that store AR status category IDs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

