# HSP_BUCKET

> This table contains hospital liability bucket information from the Hospital Liability Buckets (HLB) master file. This table does not include information for pre-allocated HLB records that are not yet in use.

**Overflow family:** [HSP_BUCKET_2](HSP_BUCKET_2.md)  
**Primary key:** `BUCKET_ID`  
**Columns:** 45  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BUCKET_ID` | NUMERIC | PK shared | This column stores the unique identifier for the liability bucket. |
| 2 | `BUCKET_NAME` | VARCHAR |  | The name of the liability bucket. |
| 3 | `HSP_ACCOUNT_ID` | NUMERIC | FK→ | This column stores the unique identifier for the hospital account to which the liability bucket is linked. |
| 4 | `BKT_TYPE_HA_C_NAME` | VARCHAR |  | The type of the liability bucket. |
| 5 | `CLAIM_TYPE_HA_C_NAME` | VARCHAR |  | The type of claim associated with the liability bucket. |
| 6 | `BKT_STS_HA_C_NAME` | VARCHAR |  | The status of the liability bucket. |
| 7 | `CLOSE_REASON_HA_C_NAME` | VARCHAR |  | The reason why the liability bucket was closed. |
| 8 | `COVERAGE_ID` | NUMERIC | FK→ | This column stores the unique identifier for the coverage associated with the liability bucket. |
| 9 | `PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 10 | `BENEFIT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 11 | `CURRENT_BALANCE` | NUMERIC |  | The current balance on the liability bucket. |
| 12 | `PREVIOUS_CREDITS` | NUMERIC |  | The total monetary amount of credits on buckets from which liability was transferred to the bucket in question. |
| 13 | `CHARGE_TOTAL` | NUMERIC |  | The total monetary amount of charges on the liability bucket. |
| 14 | `PAYMENT_TOTAL` | NUMERIC |  | The total monetary amount of payments on the liability bucket. |
| 15 | `ADJUSTMENT_TOTAL` | NUMERIC |  | The total monetary amount of adjustments on the liability bucket. |
| 16 | `NEXT_RESP_AMT` | NUMERIC |  | The amount of liability that was transferred from this liability bucket to another bucket. |
| 17 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 18 | `INTERIM_START_DATE` | DATETIME |  | For an interim liability bucket, the billing start date. The first charge service date that is included in the bucket. |
| 19 | `INTERIM_END_DATE` | DATETIME |  | For an interim liability bucket, the billing end date. The last charge service date that is included in the bucket. |
| 20 | `INTERIM_TYPE_C_NAME` | VARCHAR |  | For an interim liability bucket, the interim bucket type. Choices are First Claim, Middle Claim, and Last Claim. |
| 21 | `LAST_CLAIM_DATE` | DATETIME |  | The date of the last claim for the liability bucket. |
| 22 | `PMT_DIST_COMP_YN` | VARCHAR |  | This column stores whether payment distribution is complete. |
| 23 | `EXP_NA_WOFF_AMT` | NUMERIC |  | This column stores the expected not-allowed write-off amount. |
| 24 | `ACT_NA_WOFF_AMT` | NUMERIC |  | This column stores the payer not-allowed amount. |
| 25 | `CURR_AUTO_WO_TX_ID` | NUMERIC |  | This column stores the unique identifier for the current auto write-off transaction. |
| 26 | `RVSE_AUTO_WO_TX_ID` | NUMERIC |  | This column stores the unique identifier for the automatic write-off transaction's reversal on the liability bucket. |
| 27 | `WO_ADJ_STATUS_C_NAME` | VARCHAR |  | This column stores the write-off adjustment status. |
| 28 | `MDCRE_B_CLM_FLG_C_NAME` | VARCHAR |  | Indicates that the charges in the liability bucket should be submitted for Medicare part B claims processing. |
| 29 | `CLAIM_FORM_TYPE_C_NAME` | VARCHAR | org | The form type of the last claim on the bucket. |
| 30 | `EXTERN_AR_FLAG_YN` | VARCHAR |  | External A/R Flag. This flag determines if a bucket's balance is to be counted as belonging to an external agency. |
| 31 | `BAD_DEBT_FLAG_YN` | VARCHAR |  | Bad Debt Flag. This flag determines if a bucket's balance is to be counted as belonging to a bad debt agency. |
| 32 | `PYR_RCVD_DATE` | DATETIME |  | This column stores the date on which the latest claim for the associated liability bucket was received by a payer. |
| 33 | `FST_PYR_RCVD_DATE` | DATETIME |  | This column stores the date on which the first claim for the associated liability bucket was received by a payer. |
| 34 | `WO_CPTN_TX_ID` | NUMERIC |  | This column stores the unique identifier for the transaction used to write off non-covered charges using a system action. |
| 35 | `LEVEL_OF_CARE_C_NAME` | VARCHAR | org | The category number of the patient's Level of Care on the interim bill start date associated with this bucket. |
| 36 | `USE_EXIST_DATA_YN` | VARCHAR |  | Indicates whether the claims processor should use data from an existing claim when resubmitting or demanding a new claim. |
| 37 | `ALT_PAY_YN` | VARCHAR |  | This column stores whether this bucket resulted from alternate payer routing logic. Yes - It is an alternate payer; No - It is not an alternate payer; " - Not been evaluated, status unknown. |
| 38 | `EXPECTED_REIMB_CMT` | VARCHAR |  | Stores the expected reimbursement comment |
| 39 | `SURCHARGE_HTR_ID` | NUMERIC |  | Stores the current transaction for the surcharge. |
| 40 | `COPAY_AMOUNT` | NUMERIC |  | Total current copay due on the bucket as specified by last payment on the insurance bucket or last user override. |
| 41 | `COINS_AMOUNT` | NUMERIC |  | Total current coinsurance due on the bucket as specified by last payment on the insurance bucket or last user override. |
| 42 | `DEDUCTIBLE_AMOUNT` | NUMERIC |  | Total current deductible due on the bucket as specified by last payment on the insurance bucket or last user override. |
| 43 | `NON_COVERED_AMT` | NUMERIC |  | Total current non covered due on the bucket as specified by last payment on the insurance bucket or last user override. |
| 44 | `USER_COMMENT` | VARCHAR |  | This column stores the comment the user entered when overriding self-pay explanation of benefits (EOB) information. |
| 45 | `XR_BILLED_AMOUNT` | NUMERIC |  | Stores the expected reimbursement billed amount. It is the billed amount of the claim where the expected reimbursement is calculated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |
| `HSP_ACCOUNT_ID` | [HSP_ACCOUNT](HSP_ACCOUNT.md) | name_stem | high |

