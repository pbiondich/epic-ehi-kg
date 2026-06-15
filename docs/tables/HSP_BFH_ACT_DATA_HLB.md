# HSP_BFH_ACT_DATA_HLB

> This table stores billing activity history action-specific data. Every time a billing activity (ATM) is performed on a record or group of records, an activity history record (BFH) is logged. These activity history records store specific data related to each action that was performed on the activity. Each action (and its related data) is logged as a line in related group BFH 300. This table is specifically for actions performed on liability buckets (HLB).

**Primary key:** `BFH_ID`, `LINE`  
**Columns:** 70  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BFH_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the billing activity history record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTION_C_NAME` | VARCHAR |  | The action category ID for this row in the billing activity history. The other data in this row represent specific values associated with this action performed. |
| 4 | `ACT_BDC_RECORD_TYPE_C_NAME` | VARCHAR |  | This column stores the denial/correspondence record type category ID that is created as a result of this bucket action. |
| 5 | `ACT_BDC_RECEIVED_DATE` | DATETIME |  | This column stores the denial/correspondence record received date that is set as a result of this bucket action. |
| 6 | `ACT_BDC_RECORD_SOURCE_C_NAME` | VARCHAR | org | This column stores the denial/correspondence record source category ID that is set as a result of this bucket action. |
| 7 | `ACT_BDC_INVOICE_NUM` | VARCHAR |  | This column stores the denial/correspondence record invoice number that is set as a result of this bucket action. |
| 8 | `ACT_BDC_AMOUNT` | NUMERIC |  | This column stores the denial/correspondence record amount that is set as a result of this bucket action. |
| 9 | `ACT_BDC_REMIT_CODE_ID` | VARCHAR |  | This column stores the denial/correspondence record reason code ID that is set as a result of this bucket action. |
| 10 | `ACT_BDC_REMIT_CODE_ID_REMIT_CODE_NAME` | VARCHAR |  | The name of each remittance code. |
| 11 | `ACT_BDC_IMAGE_MNEM_C_NAME` | VARCHAR | org | This column stores the denial/correspondence record image mnemonic category ID that is set as a result of this bucket action. |
| 12 | `ACT_BDC_IMAGE_KEY` | VARCHAR |  | This column stores the denial/correspondence record image key that is set as a result of this bucket action. |
| 13 | `ACT_SURCHARGE_OVERRIDE_TYPE_C_NAME` | VARCHAR |  | This item stores the type of surcharge override performed during a billing activity (ATM) action. |
| 14 | `ACT_OUTLIER_AMOUNT` | NUMERIC |  | The outlier amount that is set as a result of this bucket action. |
| 15 | `ACT_ADDON_AMOUNT` | NUMERIC |  | The add-on amount that is set as a result of this bucket action. |
| 16 | `ACT_XR_OVERRIDE_TYPE_C_NAME` | VARCHAR |  | The type of expected reimbursement override that was performed during this bucket action. |
| 17 | `ACT_OVERRIDE_ICN` | VARCHAR |  | This column stores the internal control number that is set as a result of this bucket action. |
| 18 | `ACT_PMT_RECON_REPORT_TYPE_C_NAME` | VARCHAR | org | The report type category ID that was set through this bucket action. |
| 19 | `ACT_SETTLMENT_NUM` | VARCHAR |  | Documents the changes in the settlement number. |
| 20 | `ACT_NRP_TYPE_C_NAME` | VARCHAR |  | This column stores the next responsible party type performed as part of this activity. |
| 21 | `ACT_EXPECTED_ALLOWED_AMT` | NUMERIC |  | The expected allowed amount used for this action. |
| 22 | `ACT_PAYER_ALLOWED_AMT` | NUMERIC |  | The payer allowed amount used for this action. |
| 23 | `ACT_USE_PREV_CLAIM_DATA_YN` | VARCHAR |  | Indicates whether we are using data from the previous claim for this billing activity. Yes (Y) means we are reusing previous claim data, No (N) means we are not. |
| 24 | `ACT_TOB` | VARCHAR |  | The override Type of Bill used by the billing activity. |
| 25 | `ACT_PROCESS_IP_PART_B_YN` | VARCHAR |  | Indicates whether the billing activity processed the claim as an Inpatient Part B claim. Yes (Y) means the claim was processed as Inpatient Part B, No (N) means it was not. |
| 26 | `ACT_CLM_CHNG_COND_CODE_C_NAME` | VARCHAR | org | The claim change reason code category ID for the billing activity. |
| 27 | `ACT_NRP_AMOUNT` | NUMERIC |  | This column stores the next responsible party amount. |
| 28 | `ACT_COPAY_AMOUNT` | NUMERIC |  | Stores the copay amount |
| 29 | `ACT_DEDUCTIBLE_AMOUNT` | NUMERIC |  | Stores the deductible amount |
| 30 | `ACT_COINSURANCE_AMOUNT` | NUMERIC |  | Stores the coinsurance amount |
| 31 | `ACT_NON_COVERED_AMOUNT` | NUMERIC |  | Stores the non-covered amount |
| 32 | `ACT_RESUB_CLM_AFTER_ACT_YN` | VARCHAR |  | Stores whether the user chose to resubmit the resulting bucket's claim after the action completes |
| 33 | `ACT_PMT_RECON_REPORT_DATE` | DATETIME |  | Stores the report date |
| 34 | `ACT_PMT_RECON_TOTAL_CHG_AMOUNT` | NUMERIC |  | Stores the total charge amount |
| 35 | `ACT_PMT_RECON_NOT_ALWD_AMOUNT` | NUMERIC |  | Stores the not allowed amount for a bucket |
| 36 | `ACT_PMT_RECON_PAYMENT_AMOUNT` | NUMERIC |  | Stores the payment amount |
| 37 | `ACT_CONTRACT_DATE` | DATETIME |  | Stores the contract date of a contract on the bucket |
| 38 | `ACT_EXP_NOT_ALLOWED_AMOUNT` | NUMERIC |  | Stores the expected not allowed amount |
| 39 | `ACT_SURCHARGE_AMOUNT` | NUMERIC |  | Stores the surcharge amount |
| 40 | `ACT_TRANSFER_TO_BUCKET_ID` | NUMERIC |  | Stores the bucket that a record was transferred to |
| 41 | `ACT_EXTERNAL_SENT_DATE` | DATETIME |  | Stores the date that a claim was sent to an external source |
| 42 | `ACT_PAYER_RECEIVED_DATE` | DATETIME |  | Stores the date that a payer received a claim |
| 43 | `ACT_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 44 | `ACT_ADJUSTMENT_AMOUNT` | NUMERIC |  | Stores the adjustment amount |
| 45 | `ACT_SURCHARGE_ASSIGNMENT_C_NAME` | VARCHAR |  | Stores how the surcharge is assigned |
| 46 | `ACT_REV_EXISTING_WO_ADJ_YN` | VARCHAR |  | Whether to reverse existing write-offs for the bucket |
| 47 | `ACT_UNDO_TYPE_C_NAME` | VARCHAR |  | Type of undo billing that was performed on the bucket |
| 48 | `ACT_POST_CONTRACTUAL_ADJ_YN` | VARCHAR |  | Stores whether the user chose to post a contractual adjustment for closed buckets alongside the action |
| 49 | `ACT_REFUND_AMOUNT` | NUMERIC |  | Stores the refund amount for the Post Refund bucket action |
| 50 | `ACT_REFUND_REASON_C_NAME` | VARCHAR | org | Stores the category value of the refund reason for the Post Refund bucket action |
| 51 | `ACT_REFUND_COMMENT` | VARCHAR |  | Stores the additional comment that goes along with the refund reason for the Post Refund bucket action |
| 52 | `ACT_REFUND_SEND_TO_OPTION_C_NAME` | VARCHAR |  | Stores the category value of the option to whom to send the refund in the Post Refund bucket action |
| 53 | `ACT_REFUND_CUSTOM_PAYEE_ID` | VARCHAR |  | This column stores the unique identifier for the agency record for the custom payee to whom to send the refund for the Post Refund bucket action. |
| 54 | `ACT_REFUND_CUSTOM_PAYEE_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 55 | `ACT_REFUND_COVERAGE_ID` | NUMERIC |  | This column stores the unique identifier for the coverage for where to send the refund for the Post Refund bucket action. |
| 56 | `ACT_REFUND_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 57 | `ACT_REFUND_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 58 | `ACT_ADDR_NAME` | VARCHAR |  | Stores the name for an address specified in a billing activity action |
| 59 | `ACT_ADDR_LINE_1` | VARCHAR |  | Stores the first line of an address specified in a billing activity action |
| 60 | `ACT_ADDR_LINE_2` | VARCHAR |  | Stores the second line of an address specified in a billing activity action |
| 61 | `ACT_ADDR_CITY` | VARCHAR |  | Stores the city of an address specified in a billing activity action |
| 62 | `ACT_ADDR_STATE_C_NAME` | VARCHAR | org | Stores the category value of the state/province in a country for an address specified in a billing activity action |
| 63 | `ACT_ADDR_ZIP_CODE` | VARCHAR |  | Stores the zip code for an address specified in a billing activity action |
| 64 | `ACT_ADDR_HOUSE_NUMBER` | VARCHAR |  | Stores the house number for an address specified in a billing activity action. This may be blank for some addresses. |
| 65 | `ACT_ADDR_COUNTY_C_NAME` | VARCHAR | org | Stores the category value of the county for an address specified in a billing activity action |
| 66 | `ACT_ADDR_DISTRICT_C_NAME` | VARCHAR | org | Stores the category value of the district for an address specified in a billing activity action |
| 67 | `ACT_ADDR_COUNTRY_C_NAME` | VARCHAR | org | Stores the category value of the country for an address specified in a billing activity action |
| 68 | `ACT_TRANSFER_FROM_BUCKET_ID` | NUMERIC |  | This column stores the unique identifier of the source bucket when transferring a denial/correspondence record. |
| 69 | `ACT_PMT_RECON_NON_CVD_AMOUNT` | NUMERIC |  | Stores the additional payment reconciliation non-covered amount |
| 70 | `ACT_ADDL_NRP_AMT` | NUMERIC |  | Stores the additional NRP Amount |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BFH_ID` | [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | sole_pk | high |

