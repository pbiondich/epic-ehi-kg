# HSP_CLAIM_DETAIL2

> This table contains detailed claim print record information for claims associated with the hospital liability bucket.

**Primary key:** `CLAIM_PRINT_ID`  
**Columns:** 67  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The ID of the claim record associated with a single hospital liability bucket. |
| 2 | `SA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 3 | `INACTV_CLP_YN` | VARCHAR |  | This column has a value of yes when the claim is inactive. |
| 4 | `CLAIM_ACCEPT_DTTM` | DATETIME (Local) |  | This column holds the instant the claim was accepted. |
| 5 | `SG_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 6 | `SG_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 7 | `SG_CVG_ID` | NUMERIC |  | The coverage ID for this claim. |
| 8 | `INVOICE_NUM` | VARCHAR |  | The invoice number for this claim. |
| 9 | `SG_PAT_ID` | VARCHAR | FK→ | The patient ID for this claim. |
| 10 | `SG_GR_ACCT_ID` | NUMERIC |  | The guarantor account ID for this claim. |
| 11 | `HOSPITAL_ACCT_ID` | NUMERIC |  | The hospital account ID for this claim. |
| 12 | `HLB_ID` | NUMERIC |  | The liability bucket ID for this claim. |
| 13 | `SG_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 14 | `SG_REF_SRC_ID` | VARCHAR |  | The referring source ID for this claim. |
| 15 | `SG_REF_SRC_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 16 | `SG_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 17 | `SG_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 18 | `SG_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 19 | `SG_CLM_ID` | NUMERIC |  | The claim information ID used by this claim. |
| 20 | `SG_RQG_ID` | NUMERIC |  | The requisition grouper ID for this claim. |
| 21 | `CLAIM_CLASS_C_NAME` | VARCHAR | org | The account class used to evaluate this claim. |
| 22 | `CLAIM_BASE_CLASS_C_NAME` | VARCHAR |  | The base account class used to evaluate this claim. |
| 23 | `MIN_SERVICE_DT` | DATETIME |  | The minimum service date for this claim. |
| 24 | `MAX_SERVICE_DT` | DATETIME |  | The maximum service date for this claim. |
| 25 | `UB_FROM_DT` | DATETIME |  | The uniform billing claim from date. |
| 26 | `UB_THROUGH_DT` | DATETIME |  | The uniform billing claim through date. |
| 27 | `CLAIM_TYPE_C_NAME` | VARCHAR | org | The claim type. |
| 28 | `CLAIM_FRM_TYPE_C_NAME` | VARCHAR |  | The form type. This is either paper or electronic. |
| 29 | `TTL_CHRGS_AMT` | NUMERIC |  | Total charges amount. |
| 30 | `TTL_DUE_AMT` | VARCHAR |  | Total due amount. |
| 31 | `TTL_NONCVD_AMT` | NUMERIC |  | Total non-covered amount. |
| 32 | `TTL_PMT_AMT` | NUMERIC |  | Total payment amount. |
| 33 | `TTL_ADJ_AMT` | NUMERIC |  | Total adjustment amount. |
| 34 | `UB_BILL_TYPE` | VARCHAR |  | Type of bill. |
| 35 | `HM_HLTH_BILL_TYP_C_NAME` | VARCHAR |  | Home Health bill type. |
| 36 | `UB_SG_GRP_NUM` | VARCHAR |  | Group number. |
| 37 | `CNCL_CLAIM` | INTEGER |  | Indicates whether this is a cancel claim. |
| 38 | `REPL_CLAIM` | INTEGER |  | Indicates whether this is a replacement claim. |
| 39 | `UB_CVD_DAYS` | INTEGER |  | Covered days. |
| 40 | `UB_COINS_DAYS` | INTEGER |  | Coinsurance days. |
| 41 | `UB_NON_CVD_DAYS` | INTEGER |  | Non-covered days. |
| 42 | `UB_PRINC_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 43 | `CNCL_CLAIM_CODE` | VARCHAR |  | The value code associated with this claim if it is a cancel claim. |
| 44 | `REPL_CLAIM_CODE` | VARCHAR |  | The value code associated with this claim if it is a replacement claim. |
| 45 | `SG_ALTPYR_CLM_YN` | VARCHAR |  | Flag used to indicate that claim is for alternate payer. |
| 46 | `FILING_ORDER_C_NAME` | VARCHAR |  | This column holds the filing order position of the claim coverage at the time claims were processed. |
| 47 | `CLM_EXT_VAL_ID` | NUMERIC |  | The ID of the claim record. |
| 48 | `SG_TREAT_PLAN_ID` | VARCHAR |  | The unique ID of the treatment plan that is associated with the claim. |
| 49 | `UB_COMB_CLM_TYP_C_NAME` | VARCHAR | org | If this column is set to 1, the claim is a combined claim. |
| 50 | `REND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 51 | `RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 52 | `SRC_INV_NUM` | VARCHAR |  | In PB, this column holds the original invoice number during refresh and resubmit. In HB, this column holds the invoice number associated with the primary claim in a crossover scenario. |
| 53 | `CLAIM_TAX_AMOUNT` | NUMERIC |  | Gross tax amount at a claim level, this is the sum of all the tax amounts sent on a claim. |
| 54 | `DRG_XR_AMOUNT` | NUMERIC |  | The Diagnosis Related Group expected reimbursement amount. This will be stored for accounts billed with Diagnosis Related Group that need tax calculated specifically for the Diagnosis Related Group without any outliers or add-ons, as compared to the total expected reimbursement on the claim. |
| 55 | `DRG_TAX_AMOUNT` | NUMERIC |  | The Diagnosis Related Group tax amount. This will be stored for accounts billed with Diagnosis Related Group that have tax calculated based on expected reimbursement values. |
| 56 | `CLAIM_APEC_OUTLIER` | NUMERIC |  | This item stores the Adjudicated Payment per Episode of Care Outlier amount for a claim. |
| 57 | `SNF_CLAIM_TYPE_C_NAME` | VARCHAR |  | This item identifies the type of Skilled Nursing Facility claim produced. |
| 58 | `DEPT_TYPE_C_NAME` | VARCHAR | org | The type of department. For Norway claims, this identifies the department as a GP Office, Trust, or Municipality. |
| 59 | `CLM_REBILL_REASON_C_NAME` | VARCHAR |  | This column stores the reason why we sent the claim again to payer. It holds onto the rebill reason with the highest precedence from the category list. |
| 60 | `CLM_REBILL_USER_ID` | VARCHAR |  | This column stores the user who resubmitted the claim. |
| 61 | `CLM_REBILL_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 62 | `FAC_ACTOR_TYPE_C_NAME` | VARCHAR |  | This item stores the type of facility. For Norway claims, this identifies the facility as a GP Office, Trust, or Municipality. |
| 63 | `BENEFIT_RECORD_ID` | NUMERIC |  | Stores the ID of the benefit (BEN) record used to calculate the patient responsibility. |
| 64 | `PREDICTED_PAY_DATE` | DATETIME |  | The predicted payment response date for a claim based on historical trends for the payer. |
| 65 | `SUGGESTED_FOL_UP_DATE` | DATETIME |  | The suggested initial follow-up date for a claim based on historical trends for the payer. |
| 66 | `CLM_CLOSED_TIMELY_YN` | VARCHAR |  | Denotes if the claim closed prior to its Suggested Initial Follow-up Date, whereby it was no longer outstanding to insurance. |
| 67 | `REIMB_DRG_SOI` | VARCHAR |  | The severity of illness (SOI) used for expected reimbursement calculations. Only set for expected reimbursement calculations through an Epic contract, the contract was set to price by DRG, and the DRG used had a severity attached. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SG_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

