# HSP_CLAIM_DETAIL1

> This table contains claim print record information for claims associated with a given hospital account or liability bucket.

**Primary key:** `CLAIM_PRINT_ID`  
**Columns:** 48  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | Stores the claim record ID associated with a single hospital account. |
| 2 | `CLAIM_CAT_C_NAME` | VARCHAR | org | The claim category. |
| 3 | `MAIL_NAME` | VARCHAR |  | The mailing name for this claim. |
| 4 | `MAIL_CITY_STATE_ZIP` | VARCHAR |  | The mailing city, state, and ZIP code for this claim. |
| 5 | `MAIL_PHONE` | VARCHAR |  | The mailing phone number for this claim. |
| 6 | `SRC_OF_ADDR_C_NAME` | VARCHAR | org | The source of the mailing address for this claim. |
| 7 | `LINE_SOURCE_CLP_ID` | VARCHAR |  | The source claim record for resubmit and demand claims. |
| 8 | `PARTIAL_CLAIM_YN` | VARCHAR |  | Indicates whether the claim is a partial resubmit. |
| 9 | `ORIG_HAR_RES_ACT_ID` | NUMERIC |  | Stores the original hospital account when research charges have been added to the account. |
| 10 | `EXPECTED_PYMT` | NUMERIC |  | Claim level expected reimbursement. |
| 11 | `DRG_ID` | VARCHAR | FK→ | Contract adjudication will populate this item with the calculated diagnosis related group (DRG) used for expected reimbursement calculations. This item will be populated if the claim uses an Epic contract for calculating expected reimbursement, the contract is set to price this claim by DRG, and the system is able to choose a DRG to use in the calculation, either from the claim or the HAR. This item will not be populated if the claim uses a non-Epic expected reimbursement source, or if an end user overrides the expected reimbursement for the claim with a user-entered value through a bucket activity. |
| 12 | `DRG_ID_DRG_NAME` | VARCHAR |  | The name of the Diagnoses Related Group name. |
| 13 | `CLAIM_BILLED_AMOUNT` | NUMERIC |  | Billed amount determined from reimbursement information for Diagnosis Related Group priced claims. |
| 14 | `CLM_CONTRACTUAL` | NUMERIC |  | The contract price for this claim. If the expected reimbursement is calculated with an Epic contract and is priced by DRG, this is the reimbursement amount calculated for the DRG before any reimbursement caps are applied. If the expected reimbursement is calculated from an external source that supports line-level reimbursement, this is the claim's total payment amount. |
| 15 | `CLM_EXPECTED_PRICE` | NUMERIC |  | The expected reimbursement amount for this claim. If the expected reimbursement is calculated with an Epic contract and is priced by DRG, this is the reimbursement amount calculated for the DRG after any reimbursement caps are applied. If the expected reimbursement is calculated from an external source that supports line-level reimbursement, this is the claim's total payment amount. |
| 16 | `CLAIM_PMT_METHOD_C_NAME` | VARCHAR |  | Payment method determined from reimbursement information for Diagnosis Related Group priced claims. |
| 17 | `CLAIM_PRIM_PMT_RATE` | VARCHAR |  | The primary payment rate describing how this claim was primarily reimbursed by. The structure of this item is a delimited string based on what the payment mechanism in I CLP 840 is set to. See the help text for I CLP 741 for details on the structure of this item. |
| 18 | `CLM_PRIMARY_CVD_QTY` | NUMERIC |  | Quantity covered by primary method. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 19 | `CLM_ADDL_PMT_MTHDS` | VARCHAR |  | Additional payment methods. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 20 | `CLM_ADDL_PMT_RATES` | VARCHAR |  | Additional payment rates. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 21 | `CLM_ADDL_CVD_QTY` | VARCHAR |  | Additional payment quantity. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 22 | `CLM_LINE_PNLTY_PER` | VARCHAR |  | Line/Service level penalties imposed on the claim. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 23 | `CLAIM_LATE_DAYS` | INTEGER |  | Late submission days. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 24 | `CLM_SUB_PNLTY_PER` | VARCHAR |  | Late submission penalty percent applied. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 25 | `CLM_U_AND_C_AMT` | NUMERIC |  | Usual and customary amount for the claim. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 26 | `CLAIM_INS_PORTION` | NUMERIC |  | Insurance portion of the expected amount. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 27 | `CLM_PATIENT_PORTION` | NUMERIC |  | Portion of the expected amount the patient is responsible for. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 28 | `CLAIM_MTHD_DESC` | VARCHAR |  | A text description of the method used to price the claim. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 29 | `CLAIM_TERM_DESC` | VARCHAR |  | This item stores the term description from the matching contract line. |
| 30 | `OPERATING_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 31 | `CONTRACT_ID` | NUMERIC | shared | The unique ID of the contract that was used for this claim. Zero means that the contract is from an external system. |
| 32 | `CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 33 | `CONTRACT_DATE_REAL` | FLOAT |  | A numerical representation of the contact date for the contract used in this claim. Used to help link to the VEN_NET_CONT_SVC table. |
| 34 | `CONTRACT_USED_DT` | DATETIME |  | The date that the contract was used for this claim. |
| 35 | `CONTRACT_NOT_USED` | VARCHAR |  | Indicates whether the contract was used for this claim. Y indicates that the contract was not used. |
| 36 | `EDITED_TOB` | VARCHAR |  | Indicates the claim type of bill was edited. |
| 37 | `EDITED_EOB` | VARCHAR |  | Indicates the claim explanation of benefits was edited. |
| 38 | `MAIL_ADDR1` | VARCHAR |  | First line of the mailing address for a given claim record. |
| 39 | `MAIL_ADDR2` | VARCHAR |  | Second line of the mailing address for a given claim record. |
| 40 | `REIMB_COST_THRESH` | NUMERIC |  | The cost threshold of this claim's outlier data. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 41 | `REIMB_COST_OUT` | NUMERIC |  | The cost outlier of this claim's outlier data. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 42 | `REIMB_DAY_THRESH` | NUMERIC |  | The day threshold of this claim's outlier data. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 43 | `REIMB_DAY_OUT` | NUMERIC |  | The day outlier of this claim's outlier data. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 44 | `REIMB_OTH_THRESH` | NUMERIC |  | The other threshold of this claim's outlier data. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 45 | `REIMB_OTH_OUT` | NUMERIC |  | The other outlier of this claim's outlier data. Determined from reimbursement information for Diagnosis Related Group priced claims. |
| 46 | `MAIL_COUNTRY_C_NAME` | VARCHAR | org | Stores the mailing address country. |
| 47 | `EXPECT_PAT_RESP_AMT` | NUMERIC |  | Stores the total expected patient responsibility for the claim. |
| 48 | `CLM_CAP_XR_REDUCT` | NUMERIC |  | Amount that the expected reimbursement was reduced due to a reimbursement cap. If the expected reimbursement is calculated with an Epic contract, this is the difference between claim contractual amount and expected amount if DRG pricing is used. Otherwise, this is the sum of the differences of the line contractual amounts and line expected amount. If expected reimbursement is calculated from an external source or manually overridden, this will always return zero. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `DRG_ID` | [CLARITY_DRG](CLARITY_DRG.md) | sole_pk | high |

