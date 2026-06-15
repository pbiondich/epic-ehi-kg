# AP_CLAIM_IF_INFO_5

> Overflow table for claim data that can be sent or received by prospective payment systems (PPS) Pricers.

**Overflow of:** [AP_CLAIM_IF_INFO](AP_CLAIM_IF_INFO.md)  
**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 56

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `MUE_IMPACT` | VARCHAR |  | Impact of MUE edits on grouping results |
| 4 | `MUE_OPTIONS` | VARCHAR |  | Types of MUE editing to be applied during processing |
| 5 | `NCCI_IMPACT` | VARCHAR |  | Impact of NCCI edits on grouping results |
| 6 | `NCCI_OPTIONS` | VARCHAR |  | Types of NCCI editing to be applied during processing |
| 7 | `BILLING_NOTE` | VARCHAR |  | Remarks needed for adjudicating a claim |
| 8 | `MDC` | VARCHAR |  | Major Diagnostic Category |
| 9 | `UNDETER_POA_INTERP` | VARCHAR |  | Indicates the behavior for handling an undetermined POA indicator |
| 10 | `SCHED_SUBTYPE` | VARCHAR |  | Subtype of the schedule to be used for processing |
| 11 | `ADD_ON_PAYMENT` | VARCHAR |  | Amount to reimburse for things such as capital costs |
| 12 | `ADJ_WEIGHT` | VARCHAR |  | Final APR DRG related factor used to calculate the standard payment. Includes any increases due to patient age or facility factors. |
| 13 | `ADJ_USED_TEXT` | VARCHAR |  | Description associated with the adjuster used to process the claim |
| 14 | `AUTO_TRANS_PMT` | VARCHAR |  | Hospital specific additional claim payment amount for Inter-Governmental Transfers. |
| 15 | `CHG_CAP_ADJ` | VARCHAR |  | Amount the total payment is reduced when the total payment exceeds the covered charges. |
| 16 | `CHG_CAP_CUT` | VARCHAR |  | Difference between the original payment and the charges, when the charge cap is applied. |
| 17 | `CHG_REDUCT_FACTOR` | VARCHAR |  | Ratio of the total charges to the initial total payment. |
| 18 | `CLM_ADJ` | VARCHAR |  | Claim adjustment percent used in the claim reimbursement |
| 19 | `CLM_TYP` | VARCHAR |  | Type of claim being processed |
| 20 | `COST_OUTLIER` | VARCHAR |  | Portion of the high cost outlier payment for the claim that is the reimbursement for the claim costs above the claim high cost threshold and below the agency second cost threshold. |
| 21 | `COST_OUTLIER_2` | VARCHAR |  | Portion of the high cost outlier payment for the claim that is the reimbursement for the claim costs above the agency second cost threshold. |
| 22 | `COST_CHG_RATIO` | VARCHAR |  | Ratio of costs to charges as defined in the SSM schedule that was used for processing. |
| 23 | `COVERED_LOS` | VARCHAR |  | The number of days in a claim length of stay that are recognized for payment. |
| 24 | `EMERG_REDUCT_FLAG` | VARCHAR |  | Indicates that the claim is a preventable ER encounter based on the diagnosis codes. |
| 25 | `FINAL_SEVERITY` | VARCHAR |  | Final severity |
| 26 | `FINAL_SEVERITY_DESC` | VARCHAR |  | Description of final severity |
| 27 | `HIGH_LOS_PMT` | VARCHAR |  | Portion of the total payment for the claim that includes reimbursement for care where the LOS is greater than the agency defined high LOS threshold. |
| 28 | `HIGH_LOS_THRESHOLD` | VARCHAR |  | Length of stay that if the claim LOS is greater, makes the claim eligible for a High LOS outlier payment. |
| 29 | `ICU_INTENSITY` | VARCHAR |  | Identifies patients with diagnoses or procedures that are generally associated with the need for treatment in an Intensive Care Unit |
| 30 | `INITIAL_SEV` | VARCHAR |  | Initial Severity |
| 31 | `INITIAL_SEV_DESC` | VARCHAR |  | Description for initial severity |
| 32 | `INT_GV_TRNSFR_ADJ` | VARCHAR |  | Claim adjustment percent used in the claim intergovernmental transfer reimbursement |
| 33 | `LOW_COST_OUT_REDUCT` | VARCHAR |  | Portion of the claim total payment due to the claim qualifying as a low cost outlier |
| 34 | `PPC_REDUCT_AMT` | VARCHAR |  | Portion of the total payment that is subtracted from the claim as a result of the PPC ratio adjustment |
| 35 | `PPR_REDUCT_AMT` | VARCHAR |  | Percent reduction to the claim total payment due to the hospital PPR ratio |
| 36 | `PREV_MED_DX_FLAG` | VARCHAR |  | Identifies the presence of a diagnosis code indicative of a preventive or screening diagnosis |
| 37 | `SCHED_DATA_IND` | VARCHAR |  | Indicates how the schedule data, that was provided in the request with the claim data, was used during processing. |
| 38 | `SDA_APPLIED` | VARCHAR |  | The Standard Dollar Amount utilized to calculate claim payment. |
| 39 | `SELF_FUND_TRANS_PMT` | VARCHAR |  | Hospital specific additional claim payment amount for Inter-Governmental Transfers. |
| 40 | `SVC_ADJ_NICU` | VARCHAR |  | Percent the relative weight is incremented due to the facility having an agency designated neonatal intensive care unit |
| 41 | `SVC_ADJ_OBESTERICS` | VARCHAR |  | Percent the relative weight is incremented due to obstetrical service. |
| 42 | `THRD_PRTY_LIAB_PMT` | VARCHAR |  | Amount paid by another payer to be subtracted from the claim payment before final adjustments are made. |
| 43 | `TRNS_PMT` | VARCHAR |  | Portion of the claim total payment due to the claim qualifying as a transfer. |
| 44 | `TRAUMA_SUPP_PMT` | VARCHAR |  | Portion of the claim total payment associated with the supplemental payment for specific hospitals |
| 45 | `ADMIT_DX_CODE` | VARCHAR |  | Chief or primary complaint of the patient at admission. |
| 46 | `ADMIT_DX_CODE_DESC` | VARCHAR |  | Description for Admit Diagnosis Code |
| 47 | `CODE_VERSION_MAPPING_BASED_ON` | VARCHAR |  | The date that drives the Automatically Determine Code Mapping field. |
| 48 | `TOTAL_PAYMENT_WITHOUT_ACCESS` | VARCHAR |  | The total payment of the claim without the access payment. |
| 49 | `SURGICAL_MORTALITY_INDICATOR` | VARCHAR |  | Indicator that drives mortality measures by identifying cases beyond the provider's control. |
| 50 | `ESRD_PAYER_EXCEPTIONS` | VARCHAR |  | Indicator to apply state-specific editing and grouping rules. |
| 51 | `MEDSURG_DRG_IND` | VARCHAR |  | Identifies DRGs that are classified as medical or surgical. |
| 52 | `OUTLIER_DAYS` | VARCHAR |  | The number of days the length of stay is over the high threshold for the returned DRG code. |
| 53 | `DENTAL_ADDON_PAYMENT` | VARCHAR |  | An additional addon payment for certain dental services. |
| 54 | `GROUPER_VERSION_OUTGOING` | VARCHAR |  | The Grouper Version Number sent out on a claim to be PPS priced. |
| 55 | `FUNCTION_RETURN_CODE` | VARCHAR |  | High-level return codes describing issues in the overall function, involving grouper, pricer, editor, date, and rate file errors. |
| 56 | `USER_DEF_ADJ_AMT_WO_ACCESS_PMT` | VARCHAR |  | Portion of the total payment attributable to the user defined adjustment value without access payment |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

