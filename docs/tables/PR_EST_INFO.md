# PR_EST_INFO

> General information about the price estimate, such as status, expected service date, patient, contact information, and various amount totals.

**Overflow family:** [PR_EST_INFO_2](PR_EST_INFO_2.md), [PR_EST_INFO_3](PR_EST_INFO_3.md)  
**Primary key:** `ESTIMATE_ID`  
**Columns:** 86  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESTIMATE_ID` | NUMERIC | PK shared | The unique identifier for the price estimate record. |
| 2 | `ESTIMATE_CREATE_DT` | DATETIME |  | The date the estimate was created. |
| 3 | `USER_ID` | VARCHAR | FK→ | User who created the estimate |
| 4 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `SERVICE_DATE` | DATETIME |  | The service date specified in the price estimate. |
| 7 | `ESTIMATE_STATUS_C_NAME` | VARCHAR |  | The price estimate's status within the estimate workflow. |
| 8 | `PAT_ID` | VARCHAR | FK→ | The patient requesting the price estimate. |
| 9 | `CONTACT_NAME` | VARCHAR |  | The person requesting a price estimate, if they do not currently have a patient record (EPT). If the person requesting the estimate does have a patient record, use PAT_ID to find their contact information. |
| 10 | `CONTACT_CITY` | VARCHAR |  | The city of the contact person's address. Used only if the person requesting the estimate does not currently have a patient record. |
| 11 | `CONTACT_ZIP_CODE` | VARCHAR |  | The zip code of the contact person's address. Used only if the person requesting the price estimate does not currently have a patient record (EPT). |
| 12 | `CONTACT_STATE_C_NAME` | VARCHAR | org | The state of the contact person's address. Used only if the person requesting the price estimate does not currently have a patient record (EPT). |
| 13 | `CONTACT_COUNTRY_C_NAME` | VARCHAR | org | The country of the contact person's address. Used only if the person requesting the estimate does not currently have a patient record (EPT). |
| 14 | `CONTACT_PHONE_NUM` | VARCHAR |  | The phone number of the person requesting the price estimate. Used only if that person does not have a patient record (EPT). |
| 15 | `CONTACT_ALT_PHONE` | VARCHAR |  | The alternate phone number of the person requesting the price estimate. Used only if that person does not have a patient record (EPT). |
| 16 | `COVERAGE_ID` | NUMERIC | FK→ | The primary coverage of the patient specified in the estimate. |
| 17 | `BENEFITS_INFO_ID` | NUMERIC |  | Benefit information record (BEN) that is linked to the estimate. |
| 18 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 19 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 20 | `REQUIRED_PREPAY_AMT` | NUMERIC |  | Required patient prepayment amount. |
| 21 | `PARENT_ESTIMATE_ID` | NUMERIC |  | Reference to the record from which this record was created as a copy. |
| 22 | `CONTACT_COUNTY_C_NAME` | VARCHAR | org | The county of the person requesting the price estimate. Used only if that person does not have a patient record (EPT) |
| 23 | `EXTERNAL_ID` | VARCHAR |  | This items stores the external ID for the record. |
| 24 | `ACCOUNT_ID` | NUMERIC | FK→ | The unique ID of the guarantor account associated with the estimate. This can be populated if the patient has an existing guarantor account in the service area associated with the estimate, and will not be populated for prospective patients (when PAT_ID is blank). |
| 25 | `OVERALL_PERCENT_DISCOUNT` | NUMERIC |  | Stores percent discount for the entire estimate. If set, this overrides all system-calculated discounts. |
| 26 | `AMOUNT_DUE_OVERRIDE` | NUMERIC |  | Stores amount due for the entire estimate. If set, this overrides all system-calculated discounts. |
| 27 | `CONTACT_HOUSE_NUM` | VARCHAR |  | The house number of the contact person's address. Used only if the value has been manually specified in the estimate. |
| 28 | `CONTACT_DISTRICT_C_NAME` | VARCHAR | org | The district of the contact person's address. Used only if the value has been manually specified in the estimate. |
| 29 | `CREATE_MYPT_ID` | VARCHAR |  | The original MyChart user that created this estimate. |
| 30 | `HB_TTL_CHG_AMT` | NUMERIC |  | The total of all HB charge amounts on an estimate. |
| 31 | `PB_TTL_CHG_AMT` | NUMERIC |  | The total of all PB charge amounts on an estimate. |
| 32 | `TTL_CHG_AMT` | NUMERIC |  | The total charge amount on an estimate. On Resolute estimates, this does not include external provider charges. |
| 33 | `HB_SYS_TTL_CHG_AMT` | NUMERIC |  | The total of the HB system-calculated charge amounts on an estimate. |
| 34 | `PB_SYS_TTL_CHG_AMT` | NUMERIC |  | The total of the PB system-calculated charge amounts on an estimate. |
| 35 | `SYS_TTL_CHG_AMT` | NUMERIC |  | The total of all system-calculated charge amounts on an estimate. |
| 36 | `HB_TTL_ALLOW_AMT` | NUMERIC |  | The total of all HB allowed amounts on an estimate. |
| 37 | `PB_TTL_ALLOW_AMT` | NUMERIC |  | The total of all PB allowed amounts on an estimate. |
| 38 | `TTL_ALLOW_AMT` | NUMERIC |  | The total of all allowed amounts on an estimate. |
| 39 | `HB_SYS_TTL_ALLOW` | NUMERIC |  | The total of all Hospital Billing (HB) system-calculated allowed amounts on an estimate. |
| 40 | `PB_SYS_TTL_ALLOW` | NUMERIC |  | The total of all Professional Billing system-calculated allowed amounts on an estimate. |
| 41 | `SYS_TTL_ALLOW_AMT` | NUMERIC |  | The total of all system-calculated allowed amounts on an estimate. |
| 42 | `HB_TTL_SP_AMT` | NUMERIC |  | The total of all HB self-pay amounts on an estimate. |
| 43 | `PB_TTL_SP_AMT` | NUMERIC |  | The total of all PB self-pay amounts on an estimate. |
| 44 | `TTL_SP_AMT` | NUMERIC |  | The total self-pay amount on an estimate. On Resolute estimates, this does not include external provider self-pay amounts. |
| 45 | `HB_SYS_TTL_SP_AMT` | NUMERIC |  | The total of all HB system-calculated self-pay amounts on an estimate. |
| 46 | `PB_SYS_TTL_SP_AMT` | NUMERIC |  | The total of all PB system-calculated self-pay amounts on an estimate. |
| 47 | `SYS_TTL_SP_AMT` | NUMERIC |  | The total of all system-calculated self-pay amounts on an estimate. |
| 48 | `HB_TTL_DISCNT_AMT` | NUMERIC |  | The total of all HB discount amounts on an estimate. |
| 49 | `PB_TTL_DISCNT_AMT` | NUMERIC |  | The total of all PB discount amounts on an estimate. |
| 50 | `TTL_DISCNT_AMT` | NUMERIC |  | The total of all discount amounts on an estimate. |
| 51 | `HB_SYS_TTL_DISCNT_AMT` | NUMERIC |  | The total of all HB system-calculated discount amounts on an estimate. |
| 52 | `PB_SYS_TTL_DISCNT_AMT` | NUMERIC |  | The total of all PB system-calculated discount amounts on an estimate. |
| 53 | `SYS_TTL_DISCNT_AMT` | NUMERIC |  | The total of all system-calculated discount amounts on an estimate. |
| 54 | `HB_TTL_TAX_AMT` | NUMERIC |  | The total of all HB tax amounts on an estimate. |
| 55 | `PB_TTL_TAX_AMT` | NUMERIC |  | The total of all PB tax amounts on an estimate. |
| 56 | `TTL_TAX_AMT` | NUMERIC |  | The total of all tax amounts on an estimate. |
| 57 | `HB_SYS_TTL_TAX_AMT` | NUMERIC |  | The total of all HB system-calculated tax amounts on an estimate. |
| 58 | `PB_SYS_TTL_TAX_AMT` | NUMERIC |  | The total of all PB system-calculated tax amounts on an estimate. |
| 59 | `SYS_TTL_TAX_AMT` | NUMERIC |  | The total of all system-calculated tax amounts on an estimate. |
| 60 | `SOURCE_VISIT_CSN` | NUMERIC |  | The contact serial number of the patient contact associated with the visit when the estimate was created, if applicable. |
| 61 | `FOLLOW_UP_REASON_C_NAME` | VARCHAR |  | The reason this estimate requires follow-up. |
| 62 | `SOURCE_DETAIL_C_NAME` | VARCHAR |  | Indicates where the information on this estimate originated from. |
| 63 | `ADJUDICATION_SRC_C_NAME` | VARCHAR |  | The adjudication source category ID for the estimate. |
| 64 | `CUR_ACTIVE_ESTIMATE_ID` | NUMERIC |  | This column stores the currently active estimate in a replacement chain for any given estimate. If the estimate is not in a replacement chain, this item will match the estimate ID. |
| 65 | `EMAIL_ADDRESS` | VARCHAR |  | Stores the email address of the patient or guest (shopper). |
| 66 | `ALTERNATES_ESTIMATE_ID` | NUMERIC |  | Link to the estimate that holds the alternate procedures. |
| 67 | `OUTSTANDING_ESTIMATE_ID` | NUMERIC |  | Link to the estimate that holds the outstanding procedures. |
| 68 | `HB_TTL_INS_PAID_AMT` | NUMERIC |  | The total of all Hospital Billing (HB) insurance paid amounts on an estimate. |
| 69 | `PB_TTL_INS_PAID_AMT` | NUMERIC |  | The total of all Professional Billing (PB) insurance paid amounts on an estimate. |
| 70 | `TTL_INS_PAID_AMT` | NUMERIC |  | The total of all insurance paid amounts on an estimate. |
| 71 | `EST_SPAN_C_NAME` | VARCHAR |  | This item defines an estimate as a single or multi-visit type record: 0 - single visit estimate, 1 - multiple visit, treatment (parent) level estimate, 2 - multiple visit, visit (child) level estimate, 3 - outstanding, holds outstanding procedures, 4 - alternate, holds alternate procedures. |
| 72 | `HB_TOTAL_PMT_AMT` | NUMERIC |  | The total of all estimated HB insurance and patient payment amounts. |
| 73 | `PB_TOTAL_PMT_AMT` | NUMERIC |  | The total of all estimated PB insurance and patient payment amounts. |
| 74 | `TOTAL_PAYMENT_AMT` | NUMERIC |  | The total of all estimated insurance and patient payment amounts. |
| 75 | `TOTAL_COPAY_AMT` | NUMERIC |  | The total copay amount passed on to the patient. For treatment estimates, this is the total copay amount passed on to the patient for all visits within the treatment. |
| 76 | `TOTAL_COINS_AMT` | NUMERIC |  | The total coinsurance amount passed on to the patient. For treatment estimates, this is the total coinsurance amount passed on to the patient for all visits within the treatment. |
| 77 | `TOTAL_DEDUCTIBLE_AMT` | NUMERIC |  | The total deductible amount passed on to the patient. For treatment estimates, this is the total deductible amount passed on to the patient for all visits within the treatment. |
| 78 | `TOTAL_ADDL_SP_AMT` | NUMERIC |  | The total self-pay passed on to the patient due to reaching the insurance maximum. For treatment estimates, this is the total excess self-pay due to reaching the insurance maximum for all visits within the treatment. |
| 79 | `TOTAL_UPGRADE_SP_AMT` | NUMERIC |  | The total upgrade amount passed on to the patient. For treatment estimates, this is the total upgrade amount passed on to the patient for all visits within the treatment. This only shows a value for PB dental estimates. |
| 80 | `TOTAL_DOWNGRADE_SP_AMT` | NUMERIC |  | The total downgrade amount passed on to the patient. For treatment estimates, this is the total downgrade amount passed on to the patient for all visits within the treatment. This only shows a value for PB dental estimates. |
| 81 | `TOTAL_HMO_COPAY_AMT` | NUMERIC |  | The total HMO copay amount passed on to the patient. For treatment estimates, this is the total HMO copay amount passed on to the patient for all visits within the treatment. This only shows a value for PB dental estimates. |
| 82 | `TOT_NON_COVERED_AMT` | NUMERIC |  | The total noncovered amount passed on to the patient. For treatment estimates, this is the total noncovered amount passed on to the patient for all visits within the treatment. |
| 83 | `VISIT_GROUPER_ESTIMATE_ID` | NUMERIC |  | If this is a visit-level estimate record on a multi-visit estimate, this item stores the grouper estimate record containing this visit estimate. |
| 84 | `FINALIZED_USER_ID` | VARCHAR |  | Returns the user who finalized the estimate. |
| 85 | `FINALIZED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 86 | `EST_REPLACE_REASON_C_NAME` | VARCHAR |  | Stores the primary reason that this estimate's parent was automatically replaced. This item will only be set if this is an automatic replacement estimate. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

