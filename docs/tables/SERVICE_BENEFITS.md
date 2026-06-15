# SERVICE_BENEFITS

> The SERVICE_BENEFITS table contains service-level benefit information about the coverages for the encounter or estimate to which this benefit record is attached.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 55  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the benefit record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CVG_FOR_SVC_TYPE_ID` | NUMERIC |  | This related group contains benefit information specific to a coverage and service type. |
| 4 | `CVG_SVC_TYPE_ID` | VARCHAR |  | The service type for which the listed insurance benefits apply. |
| 5 | `CVG_SVC_TYPE_ID_SERVICE_TYPE_NAME` | VARCHAR |  | The name of this benefit service type. |
| 6 | `EVALUATION_STATUS_C_NAME` | VARCHAR | org | The current evaluated status of the coverage benefits for this service type (coverage, not covered, in progress, etc.). |
| 7 | `COPAY_AMOUNT` | NUMERIC |  | The copay for this coverage and service type. |
| 8 | `DEDUCTIBLE_AMOUNT` | NUMERIC |  | Deductible for this coverage and service type. |
| 9 | `DEDUCTIBLE_MET_AMT` | NUMERIC |  | The amount of the deductible for this coverage and service type that has already been paid. |
| 10 | `COINS_PERCENT` | INTEGER |  | The coinsurance percentage for this coverage and service type. |
| 11 | `COINS_AMOUNT` | NUMERIC |  | The coinsurance amount for this coverage and service type. |
| 12 | `OUT_OF_POCKET_MAX` | NUMERIC |  | The maximum out-of-pocket payment for this coverage and service type. |
| 13 | `OUT_OF_PCKT_REMAIN` | NUMERIC |  | The remaining out-of-pocket payment for this coverage and service type. |
| 14 | `OUT_OF_PCKET_MET_YN` | VARCHAR |  | Has the out-of-pocket cost been met for this coverage and service type? |
| 15 | `OOP_INCL_DEDUCT_YN` | VARCHAR |  | Does the out-of-pocket payment include the deductible cost? |
| 16 | `COVERED_DAYS` | INTEGER |  | Track covered days -- this is normally used for Medicare. |
| 17 | `NON_COVERED_DAYS` | INTEGER |  | The non-covered days - this is normally used for Medicare |
| 18 | `COINS_DAYS` | INTEGER |  | Track the coinsurance days -- this is normally used for Medicare |
| 19 | `LTR_DAYS` | INTEGER |  | Track the lifetime reserve days -- this is usually used for Medicare. |
| 20 | `ANNUAL_BEN_MAX_AMT` | NUMERIC |  | The maximum annual benefits for this coverage and service type. |
| 21 | `ANNUAL_BEN_REMAIN` | NUMERIC |  | The annual benefits remaining for this coverage and service type. |
| 22 | `LIFETIME_BEN_MAX` | NUMERIC |  | The maximum lifetime benefits for this coverage and service type. |
| 23 | `LIFETIME_BEN_REMAIN` | NUMERIC |  | The lifetime benefits remaining for this coverage and service type. |
| 24 | `SPEND_DOWN_AMT` | NUMERIC |  | The spend down amount for this coverage and service type during the defined interval. |
| 25 | `SPEND_DOWN_REMAIN` | NUMERIC |  | The spend down amount remaining for this coverage and service type during the specified interval. |
| 26 | `SPEND_DOWN_INTRVL_C_NAME` | VARCHAR | org | The interval at which the spend down amount will reset. |
| 27 | `PREEXISTING_COND_YN` | VARCHAR |  | Do any pre-existing conditions apply for this coverage and service type? |
| 28 | `PREEXIST_COND_DESC` | VARCHAR |  | The description of any pre-existing conditions that apply for this coverage and service type. |
| 29 | `IN_NETWORK_YN` | VARCHAR |  | Is in-network care required for this coverage and service type? |
| 30 | `PREFERRED_NETWORK` | VARCHAR |  | The preferred network, if any, for this coverage and service type. |
| 31 | `TRACKING_CODE` | VARCHAR |  | The tracking code for payor communication about this coverage and service type. |
| 32 | `DEDUCT_REMAIN_AMT` | NUMERIC |  | The amount of the deductible for this coverage and service type that has yet to be paid. |
| 33 | `DAILY_COPAY_AMOUNT` | NUMERIC |  | The amount that is multiplied by the length of stay to calculate the total inpatient copay for this coverage and service type. This is different from the visit copay amount. |
| 34 | `MAX_DAILY_COPAY` | NUMERIC |  | The maximum total amount the patient may be charged in daily copays for this coverage and service type. |
| 35 | `FAMILY_TIER_SVC_C_NAME` | VARCHAR | org | Family tier for this line's coverage and service type. |
| 36 | `MAX_VISITS` | INTEGER |  | The maximum number of visits for this coverage and service type. |
| 37 | `REMAINING_VISITS` | INTEGER |  | The remaining number of visits for this coverage and service type. |
| 38 | `NET_LVL_SVC_C_NAME` | VARCHAR | org | Network level of this line's coverage and service type. |
| 39 | `NON_COVERED_SVC_C_NAME` | VARCHAR |  | Notes when a service is not covered by the payor for this encounter. |
| 40 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 41 | `SVC_ANNUAL_BEN_USED_AMT` | NUMERIC |  | The amount that has already been used for this coverage and service type for a given year. |
| 42 | `RTE_COPAY_AMOUNT` | NUMERIC |  | Stores the last copay value filed by RTE at the service level |
| 43 | `RTE_DEDUCT_AMOUNT` | NUMERIC |  | Stores the last deductible amount filed by RTE at the service level |
| 44 | `RTE_DEDUCT_MET` | NUMERIC |  | Stores the last deductible met amount filed by RTE at the service level |
| 45 | `RTE_DEDUCT_REMAIN` | NUMERIC |  | Stores the last deductible remaining amount filed by RTE at the service level |
| 46 | `RTE_COINS_PERCENT` | INTEGER |  | Stores the last coinsurance percent filed by RTE at the service level |
| 47 | `RTE_OOP_MAX` | NUMERIC |  | Stores the last OOP max amount filed by RTE at the service level |
| 48 | `RTE_OOP_REMAIN` | NUMERIC |  | Stores the last OOP remaining amount filed by RTE at the service level |
| 49 | `PAYER_BEN_CAT` | VARCHAR |  | The benefit category identifier used by the payer. It will only be set for reference benefit records. |
| 50 | `VISIT_BEN_MAX_AMT` | NUMERIC |  | The maximum visit benefits for this coverage and service type. |
| 51 | `VISIT_OUT_OF_POCKET_MAX_AMT` | NUMERIC |  | The maximum visit out-of-pocket payment for this coverage and service type. |
| 52 | `BENEFITS_LAST_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant that benefits data for this line's service type and coverage was last collected. This instant reflects the time that these benefits were entered originally, even if that entry was made on a different benefits record and the benefits were later copied to the current one. |
| 53 | `BENEFITS_LAST_UPDATE_USER_ID` | VARCHAR |  | The user who last made changes to this line's service type benefits values. This reflects the time that these benefits were entered originally, even if that entry was made on a different benefits record and the benefits were later copied to the current one. |
| 54 | `BENEFITS_LAST_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 55 | `BENEFITS_LAST_UPDATE_SRC_C_NAME` | VARCHAR |  | The method that was last used to make changes to this line's service type benefits values. This reflects the original entry of the benefits, even if the entry was made on a different benefits record and the benefits were later copied to the current one. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

