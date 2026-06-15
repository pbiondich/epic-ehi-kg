# COVERAGE_BENEFITS

> The COVERAGE_BENEFITS table contains coverage-level benefit information for the encounter or estimate to which this benefit record is attached.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 80  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the benefit record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CVG_ID` | NUMERIC | FK→ | Each line in this related group contains benefit information for a coverage that is or was in use for this visit. |
| 4 | `CHECKED_BY_USER_ID` | VARCHAR |  | The user by whom the coverage benefits were checked. |
| 5 | `CHECKED_BY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CHECKED_ON_DT` | DATETIME |  | The date when the coverage benefits were checked. |
| 7 | `CHECKED_WITH_C_NAME` | VARCHAR | org | The organization or group with whom the benefits for this coverage were checked. |
| 8 | `CHECKED_WITH_AGY_ID` | VARCHAR |  | The agency with whom the benefits for this coverage were checked. |
| 9 | `CHECKED_WITH_AGY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 10 | `CHECKD_WITH_CONTACT` | VARCHAR |  | The contact with whom the benefits for this coverage were checked. |
| 11 | `CHECKED_WITH_PHONE` | VARCHAR |  | The phone number with which the benefits for this coverage were checked. |
| 12 | `CHECKED_WITH_FAX` | VARCHAR |  | The fax number with which the benefits for this coverage were checked. |
| 13 | `CVG_BEN_VERIF_ID` | NUMERIC |  | The verification record for visit-specific coverage benefits. |
| 14 | `EVALUATION_STATUS_C_NAME` | VARCHAR | org | The current evaluated status of the coverage benefits for this coverage (covered, not covered, in progress, etc.). |
| 15 | `EXPECTED_COLL_AMT` | NUMERIC |  | The amount expected to be collected from the patient for this coverage. |
| 16 | `COPAY_AMOUNT` | NUMERIC |  | The copay for this coverage. |
| 17 | `DEDUCTIBLE_AMOUNT` | NUMERIC |  | Deductible for this coverage. |
| 18 | `DEDUCTIBLE_MET_AMT` | NUMERIC |  | The amount of the deductible for this coverage that has already been paid. |
| 19 | `DEDUCT_REMAIN_AMT` | NUMERIC |  | The amount of the deductible for this coverage that has yet to be paid. |
| 20 | `COINS_PERCENT` | INTEGER |  | The coinsurance percentage for this coverage. |
| 21 | `COINS_AMOUNT` | NUMERIC |  | The coinsurance amount for this coverage. |
| 22 | `OUT_OF_POCKET_MAX` | NUMERIC |  | The maximum out-of-pocket payment for this coverage. |
| 23 | `OUT_OF_PCKT_REMAIN` | NUMERIC |  | The remaining out-of-pocket payment for this coverage. |
| 24 | `OUT_OF_PCKET_MET_YN` | VARCHAR |  | Has the out-of-pocket cost been met for this coverage. |
| 25 | `OOP_INCL_DEDUCT_YN` | VARCHAR |  | Does the out-of-pocket payment include the deductible cost? |
| 26 | `COVERED_DAYS` | INTEGER |  | Track covered days -- this is normally used for Medicare. |
| 27 | `NON_COVERED_DAYS` | INTEGER |  | The non-covered days - this is normally used for Medicare |
| 28 | `COINS_DAYS` | INTEGER |  | Track the coinsurance days -- this is normally used for Medicare |
| 29 | `LTR_DAYS` | INTEGER |  | Track the lifetime reserve days -- this is usually used for Medicare. |
| 30 | `ANNUAL_BEN_MAX_AMT` | NUMERIC |  | The maximum annual benefits for this coverage. |
| 31 | `ANNUAL_BEN_REMAIN` | NUMERIC |  | The annual benefits remaining for this coverage. |
| 32 | `LIFETIME_BEN_MAX` | NUMERIC |  | The maximum lifetime benefits for this coverage. |
| 33 | `LIFETIME_BEN_REMAIN` | NUMERIC |  | The lifetime benefits remaining for this coverage. |
| 34 | `SPEND_DOWN_AMT` | NUMERIC |  | The spend down amount for this coverage during the defined interval. |
| 35 | `SPEND_DOWN_REMAIN` | NUMERIC |  | The spend down amount remaining for this coverage during the specified interval. |
| 36 | `SPEND_DOWN_INTRVL_C_NAME` | VARCHAR | org | The interval at which the spend down amount will reset. |
| 37 | `PREEXISTING_COND_YN` | VARCHAR |  | Do any pre-existing conditions apply for this coverage? |
| 38 | `PREEXIST_COND_DESC` | VARCHAR |  | The description of any pre-existing conditions that apply for this coverage. |
| 39 | `IN_NETWORK_YN` | VARCHAR |  | Is in-network care required for this coverage and service type? |
| 40 | `PREFERRED_NETWORK` | VARCHAR |  | The preferred network, if any, for this coverage. |
| 41 | `TRACKINC_CODE` | VARCHAR |  | The tracking code for payor communication about this coverage. |
| 42 | `ESTIMATE_NEEDED_YN` | VARCHAR |  | Indicates whether an estimate should be collected for this encounter/coverage. |
| 43 | `CVG_UPDATE_DTTM` | DATETIME (UTC) |  | This item contains the last instant that data related to this coverage was written to the record. This includes changes to general benefits, changes to service type specific benefits, and copying from another benefits record. |
| 44 | `CVG_UPDATE_USER_ID` | VARCHAR |  | This item contains the ID of the user who last saved data related to this coverage to the record, or whose actions caused the system to save that data. Updates when general benefits or service type specific benefits are saved or when benefits are copied from one benefit record to this one. |
| 45 | `CVG_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 46 | `CVG_UPDATE_SRC_C_NAME` | VARCHAR |  | The method that was last used to make changes to the general benefits values. This reflects the original entry of the benefits, even if the entry was made on a different benefits record and the benefits were later copied to the current one. This only tracks changes to the general benefits, not to service type benefits. |
| 47 | `COST_SHARE_ACCT_BAL` | NUMERIC |  | This item stores the HRA account balance for the HRA account associated with the managed care coverage. It is a coverage specific item. |
| 48 | `ACTIVELY_ENROLLED_YN` | VARCHAR |  | This item indicates if the patient is actively enrolled in HRA. |
| 49 | `DAILY_COPAY_AMOUNT` | NUMERIC |  | The amount that is multiplied by the length of stay to calculate the total inpatient copay for this coverage. This is different from the visit copay amount. |
| 50 | `MAX_DAILY_COPAY` | NUMERIC |  | The maximum total amount the patient may be charged in daily copays for this coverage. |
| 51 | `WAIVE_ON_ADMIT_YN` | VARCHAR |  | Indicates if the copay is waived on an ED admission for this coverage. "YES" indicates the copay will be waived. If null or "NO", the copay will not be waived on ED admittance. |
| 52 | `FAMILY_TIER_C_NAME` | VARCHAR | org | Family tier for this line's coverage. |
| 53 | `MAX_VISITS` | INTEGER |  | The maximum number of visits for this coverage. |
| 54 | `REMAINING_VISITS` | INTEGER |  | The remaining number of visits for this coverage. |
| 55 | `LAST_IP_SNF_DATE` | DATETIME |  | This is the last date on which the patient received inpatient care or skilled nursing care. This is used in determining when a Medicare benefit period ends. |
| 56 | `NET_LVL_CVG_C_NAME` | VARCHAR | org | Network level for this line's coverage. |
| 57 | `CALC_NET_LVL_CVG_C_NAME` | VARCHAR |  | Stores the most recently calculated network level for this coverage. |
| 58 | `CALC_NET_SRC_CVG_C_NAME` | VARCHAR |  | Stores the source of the most recently calculated network level for this coverage. |
| 59 | `SEL_NET_LVL_CVG_C_NAME` | VARCHAR |  | Specifies which network level should be used for this encounter, at the coverage level. |
| 60 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 61 | `CVG_ANNUAL_BEN_USED_AMT` | NUMERIC |  | The amount that has already been used for this coverage for a given year. |
| 62 | `RTE_COPAY_AMOUNT` | NUMERIC |  | Stores the last copay value filed by RTE at the coverage level |
| 63 | `RTE_DEDUCT_AMOUNT` | NUMERIC |  | Stores the last deductible amount filed by RTE at the coverage level |
| 64 | `RTE_DEDUCT_MET` | NUMERIC |  | Stores the last deductible met amount filed by RTE at the coverage level |
| 65 | `RTE_DEDUCT_REMAIN` | NUMERIC |  | Stores the last deductible remaining amount filed by RTE at the coverage level |
| 66 | `RTE_COINS_PERCENT` | INTEGER |  | Stores the last coinsurance percent filed by RTE at the coverage level |
| 67 | `RTE_OOP_MAX` | NUMERIC |  | Stores the last OOP max amount filed by RTE at the coverage level |
| 68 | `RTE_OOP_REMAIN` | NUMERIC |  | Stores the last OOP remaining amount filed by RTE at the coverage level |
| 69 | `POSTERIOR_COMPOSITE_YN` | VARCHAR |  | Indicates whether or not posterior composite fillings are covered. 'Y' indicates that posterior composite fillings are covered. 'N' or NULL indicate that posterior composite fillings are not covered. |
| 70 | `POSTERIOR_PORCELAIN_YN` | VARCHAR |  | Indicates whether or not posterior porcelain crowns are covered. 'Y' indicates that posterior porcelain crowns are covered. 'N' or NULL indicate that posterior porcelain crowns are not covered. |
| 71 | `CVG_BEN_BEGIN_DATE` | DATETIME |  | The coverage-level annual benefit period start date. |
| 72 | `VISIT_BEN_MAX_AMT` | NUMERIC |  | The maximum visit benefits for this coverage. |
| 73 | `VISIT_OUT_OF_POCKET_MAX_AMT` | NUMERIC |  | The coverage level maximum patient out-of-pocket for a visit. |
| 74 | `BENEFITS_LAST_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant that general benefits data was last collected. This instant reflects the time that these benefits were entered originally, even if that entry was made on a different benefits record and the benefits were later copied to the current one. This only tracks changes to the general benefits, not to service type benefits. |
| 75 | `BENEFITS_LAST_UPDATE_USER_ID` | VARCHAR |  | The user who last made changes to the general benefits values. This reflects the time that these benefits were entered originally, even if that entry was made on a different benefits record and the benefits were later copied to the current one. This only tracks changes to the general benefits, not to service type benefits. |
| 76 | `BENEFITS_LAST_UPDATE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 77 | `BENEFITS_LAST_UPDATE_SRC_C_NAME` | VARCHAR |  | The method that was last used to make changes to the general benefits values. This reflects the original entry of the benefits, even if the entry was made on a different benefits record and the benefits were later copied to the current one. This only tracks changes to the general benefits, not to service type benefits. |
| 78 | `MISSING_TOOTH_EXCLUSION_YN` | VARCHAR |  | Whether the payer has a missing tooth exclusion |
| 79 | `SEALANT_AGE_LIMIT_FIRST_MOLAR` | INTEGER |  | Sealant age limit for first molar |
| 80 | `SEALANT_AGE_LIMIT_SECOND_MOLAR` | INTEGER |  | Sealant age limit for second molar |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

