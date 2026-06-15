# ARPB_TRANSACTIONS3

> This table contains information about professional billing transactions.

**Primary key:** `TX_ID`  
**Columns:** 47  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `IS_SCANNED_CHECK_YN` | VARCHAR |  | Indicates if a transaction was made using a scanned check. |
| 3 | `SUSP_NRP_SRC_COVERAGE_ID` | NUMERIC |  | This column stores the coverage when the next responsible party (NRP) action was suspended. |
| 4 | `SUSP_NRP_DST_COVERAGE_ID` | NUMERIC |  | This column stores the coverage for the suspended NRP action. |
| 5 | `SUSP_NRP_AMT` | NUMERIC |  | This column stores the amount of the suspended NRP action. |
| 6 | `SUSP_NRP_ASSIGN_C_NAME` | VARCHAR |  | This column stores the assignment value for the suspended NRP action. |
| 7 | `SUSP_NRP_SOURCE_MODULE_C_NAME` | VARCHAR |  | This column stores the module for the suspended NRP action. |
| 8 | `SUSP_NRP_COMMENT` | VARCHAR |  | This column stores the comment for the suspended NRP action. |
| 9 | `EB_PMT_HTT_ID` | NUMERIC |  | The Enterprise payment hospital temporary transaction ID. |
| 10 | `IS_CSA_PAYMENT_YN` | VARCHAR |  | Indicates that a payment was identified as coming from a consumer spending account during professional billing remittance processing. |
| 11 | `BFD_COVERAGE_ID` | NUMERIC |  | This item stores the coverage used to compute reimbursement and pricing contracts for charge lines that qualify for bill for denial workflows. |
| 12 | `ADV_PRICING_DESCRIPTION` | VARCHAR |  | Description of the advanced pricing line in ECP used for this charge. |
| 13 | `ADV_PRICING_INDEX_ID` | VARCHAR |  | Component or component group used in advanced pricing. |
| 14 | `ADV_PRICING_INDEX_ID_COMPONENT_INDEX_NAME` | VARCHAR |  | The name of the component index record |
| 15 | `ADV_PRICING_RULE_ID` | VARCHAR |  | Rule used for advanced pricing. |
| 16 | `ADV_PRICING_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 17 | `ADV_PRICING_MECHANISM_C_NAME` | VARCHAR |  | Advanced pricing mechanism used. |
| 18 | `ADV_PRICING_FSC1_ID` | NUMERIC |  | Fee schedule 1 used in advanced pricing. |
| 19 | `ADV_PRICING_FSC1_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 20 | `ADV_PRICING_FSC2_ID` | NUMERIC |  | Fee schedule 2 used in advanced pricing. |
| 21 | `ADV_PRICING_FSC2_ID_FEE_SCHEDULE_NAME` | VARCHAR |  | The name of each fee schedule. |
| 22 | `ADV_PRICING_FSC_PERC_1` | NUMERIC |  | Percent of specified fee schedule 1 used in advanced pricing. |
| 23 | `ADV_PRICING_FSC_PERC_2` | NUMERIC |  | Percent of specified fee schedule 2 used in advanced pricing. |
| 24 | `ADV_PRICING_PERC_BASE` | INTEGER |  | Percent of base price used in advanced pricing. |
| 25 | `ADV_PRICING_LPP_ID` | NUMERIC |  | Pricing extension used in advanced pricing. |
| 26 | `ADV_PRICING_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 27 | `PRIM_TIMELY_FILE_DEADLINE_DATE` | DATETIME |  | The primary timely filing deadline date. |
| 28 | `PAT_PMT_COLL_WKFL_C_NAME` | VARCHAR |  | This column contains the workflow category ID performed to collect a patient payment from the point of view of the user. For example, MyChart eCheck-in vs. MyChart One-Touch. |
| 29 | `MYC_SIGNIN_METHOD_C_NAME` | VARCHAR |  | This column denotes how the patient or guarantor logged in to MyChart to either post the payment or create an agreement that will post a payment via Auto Pay. Only populated for agreements made via MyChart. |
| 30 | `POSTING_MYPT_ID` | VARCHAR |  | This column contains either the MyChart account that created the agreement that resulted in the self-pay payment (if applicable) or the MyChart account that posted the self-pay payment. |
| 31 | `POSTING_MYC_STATUS_C_NAME` | VARCHAR | org | This item contains either the status of the MyChart account that created the agreement that resulted in the self-pay payment (if applicable) or the status of the MyChart account that posted the self-pay payment. An active MyChart account status is defined as whether a MyChart user could log into the account with a user name and password. Accounts that are not yet active, deactivated, or are proxy accounts are considered inactive. |
| 32 | `EB_TX_SOURCE_C_NAME` | VARCHAR |  | This column stores the enterprise posting module for the transaction. This is calculated based on the professional billing transaction source for the transaction. |
| 33 | `IMPLIED_QTY` | NUMERIC |  | The implied quantity for a charge. |
| 34 | `IMPLIED_QTY_UNIT_C_NAME` | VARCHAR | org | The implied quantity's unit. |
| 35 | `IMPLIED_UNIT_TYPE_C_NAME` | VARCHAR |  | The unit type of the implied quantity. |
| 36 | `OVR_REIMB_CONTRACT_ID` | NUMERIC |  | The override reimbursement contract that was entered. |
| 37 | `OVR_REIMB_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 38 | `OVR_REIMB_CONTRACT_DATE` | DATETIME |  | The contact that should be used of the override reimbursement contract that was entered. |
| 39 | `OVR_EXPECTED_REIMB_AMOUNT` | NUMERIC |  | Stores the expected reimbursement override amount for the charge. This override amount was entered by a user. |
| 40 | `PMT_PLAN_AGRMT_SCHED_PMT_ID` | NUMERIC |  | The unique ID of the transaction's target guarantor's active payment plan agreement record at the time of filing. |
| 41 | `IS_EST_PRE_SERVICE_PLAN_PMT_YN` | VARCHAR |  | Indicates whether this payment was made on an estimated balance on a payment plan at time of filing ('Y'). 'N' or NULL indicates that the transaction is not a payment, the payment is not on a balance on a payment plan, or the balance was not estimated at the time of filing. |
| 42 | `IS_PRE_SERVICE_PLAN_PMT_YN` | VARCHAR |  | Indicates whether this payment was made toward a hospital account on a payment plan that was added by an estimate ('Y'). 'N' or NULL indicates that the transaction is not a payment or the payment was not made toward a hospital account on a payment plan that was added by an estimate. |
| 43 | `EST_VARIANCE_WO_ESTIMATE_ID` | NUMERIC |  | If this transaction is part of an automatic estimate variance write-off, this item stores the estimate that this is a write off towards. |
| 44 | `INTEND_VISIT_ACCT_CALC_MTHD_C_NAME` | VARCHAR |  | The calculation method of the Intended Visit Account HAR. |
| 45 | `NCC_OVERRIDE_COVERAGE_ID` | NUMERIC |  | When a coverage other than the normal reimbursement coverage is used to override the reimbursement contract used by a charge, this item contains that coverage. |
| 46 | `POST_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant the charge was posted |
| 47 | `IS_PREPAY_PMT_YN` | VARCHAR |  | Indicates whether this is a prepay payment. This includes visit prepay payments and copay payments (such as during check-in). This column is only populated for self-pay payments. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

