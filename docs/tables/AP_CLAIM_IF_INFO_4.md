# AP_CLAIM_IF_INFO_4

> Overflow table for claim data that can be sent or received by prospective payment systems (PPS) Pricers.

**Overflow of:** [AP_CLAIM_IF_INFO](AP_CLAIM_IF_INFO.md)  
**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 95

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADMIT_DX_FOR_HAC_PROCESSING` | VARCHAR |  | The admit diagnosis code that was used during hospital-acquired condition adjusted diagnosis-related group processing. |
| 4 | `ADMIT_MEDICAL_SURGICAL_DRG_FLG` | VARCHAR |  | Medical/Surgical Flag assigned at admission. |
| 5 | `ADMIT_RETURN_CODE` | VARCHAR |  | Return code at admission. |
| 6 | `BIRTH_WEIGHT_OPTION_USED` | VARCHAR |  | Birth weight data entry method used during processing. |
| 7 | `DISCHARGE_DRG_OPTION_USED` | VARCHAR |  | The discharge diagnosis-related group (DRG) option used during processing. |
| 8 | `HAC_ADJ_DRG` | VARCHAR |  | Diagnosis Related Group (DRG) following Hospital-Acquired Condition (HAC) adjusted DRG processing. |
| 9 | `HAC_ADJ_MDC` | VARCHAR |  | The MDC following HAC-adjusted APR DRG Processing. |
| 10 | `HAC_ADJ_MED_SURG_DRG_FLAG` | VARCHAR |  | Medical or surgical DRG flag following HAC-adjusted DRG Processing. |
| 11 | `HAC_ADJ_RETURN_CODE` | VARCHAR |  | Return code following Hospital-Acquired Condition (HAC) adjusted Diagnosis Related Group (DRG) processing. |
| 12 | `HAC_ADJ_ROM` | VARCHAR |  | Risk of mortality (ROM) following HAC-adjusted DRG processing. |
| 13 | `HAC_ADJ_SOI` | VARCHAR |  | Severity of illness (SOI) following HAC-adjusted DRG processing. |
| 14 | `HAC_VERSION_USED` | VARCHAR |  | Hospital-acquired condition version used for processing. |
| 15 | `HAC_PROCESSING_ICD_VERSION` | VARCHAR |  | ICD version qualifier used for hospital-acquired condition adjusted diagnosis related group processing. |
| 16 | `PAYER_LOGIC_INDICATOR_USED` | VARCHAR |  | Type of payer logic applied during 3M APR DRG grouping. |
| 17 | `USER_ID_IN` | VARCHAR |  | Unique identifier for the user, required for processing the claim when using Super Certificates. |
| 18 | `FINANCIAL_PAYER` | VARCHAR |  | Classification of the financial payer of the claim. |
| 19 | `MEMBER_BENEFIT_PLAN` | VARCHAR |  | Classification of the member benefit plan. |
| 20 | `PAT_RESPONSIBILITY` | VARCHAR |  | Amount the patient is expected to pay for the claim. |
| 21 | `GROUPER_ICD_VERSION_QUALIFIER` | VARCHAR |  | Specifies the grouper ICD version to use for processing. |
| 22 | `ACCESS_FEE_AMOUNT` | VARCHAR |  | Portion of the total claim payment attributed to access fees. |
| 23 | `AGE_ADJ` | VARCHAR |  | The decimal representation of the adjustment rate to the claim due to agency defined age considerations. |
| 24 | `BASE_DRG_ADJ_USED` | VARCHAR |  | Max of the provider adjuster, age adjuster & service line adjuster. |
| 25 | `COVERED_COST` | VARCHAR |  | Portion of the total charges that is represented in cost dollars. |
| 26 | `DRG_BASE_AMOUNT` | VARCHAR |  | Initial estimate of portion of claim total payment qualifying as an inlier. |
| 27 | `DRG_BASE_PAYMENT` | VARCHAR |  | Portion of the claim total payment paid for claim qualifying as an inlier. |
| 28 | `HAC_ADJ_PAYMENT_FLAG` | VARCHAR |  | Indicates whether HAC-adjusted DRG and severity of illness (SOI) logic from the APR grouper was used. |
| 29 | `OUTLIER_TRIM_POINT_USED` | VARCHAR |  | Outlier trim point value used to determine outlier threshold. |
| 30 | `SERVICE_ADJ` | VARCHAR |  | Amount the relative weight is incremented for a facility. |
| 31 | `TOTAL_ALLOWED_AMOUNT` | VARCHAR |  | Payment before withholding & access payment adjustments. |
| 32 | `TOTAL_NON_CVRD_AMOUNT_USED` | VARCHAR |  | Non-covered charges used in determining cost of charges. |
| 33 | `USER_DEFINED_ADJ_AMT` | VARCHAR |  | Portion of total payment attributable to user-defined adjustment values. |
| 34 | `VARIABLE_COST_FACTOR_USED` | VARCHAR |  | Variable cost factor value used in cost outlier calculation. |
| 35 | `WITHHOLDING_AMOUNT` | VARCHAR |  | Reduction due to Pay for Performance adjustment. |
| 36 | `CHARGE_OUTLIER_THRESHOLD` | VARCHAR |  | The dollar amount, in charge dollars, that the claim charges must exceed to determine the claim eligibility for a high cost outlier payment. |
| 37 | `ADMIT_MDC` | VARCHAR |  | The Major Diagnostic Category (MDC) at admission. |
| 38 | `ADJUSTED_EAPG_WEIGHT` | VARCHAR |  | The Enhanced Ambulatory Payment Group weight after discounting and consolidation. |
| 39 | `CLAIM_RECORD_TYPE` | VARCHAR |  | The overall record type for the claim. |
| 40 | `FULL_EAPG_WEIGHT` | VARCHAR |  | Weight(s) obtained directly from the weight file before adjustment. |
| 41 | `RURAL_ADJUSTMENT_FACTOR` | VARCHAR |  | Line level rural adjustment factor |
| 42 | `RURAL_ADJUSTMENT_FACT_SEP_BILL` | VARCHAR |  | Line level, separately billable rural payment adjustment for adult ESRD beneficiaries utilizing ESRD facilities located in rural core-based statistical areas (CBSA) (that are non-urban CBSAs). |
| 43 | `STATE_PRICING_INDICATOR` | VARCHAR |  | Indicates the state rules that were used when pricing the claim. |
| 44 | `STATE_IDENT` | VARCHAR |  | State ID returned by Prospective Payment System pricer for diagnosis related group pricing. |
| 45 | `TOTAL_ERRORS` | VARCHAR |  | Total errors returned in PPS Medicare Code Editor (MCE) editor block. |
| 46 | `TAXPAYER_IDENT` | VARCHAR |  | Taxpayer ID Number from outgoing EasyGroup PPS Pricer |
| 47 | `ALT_PDGM` | VARCHAR |  | Alternate Patient-Driven Groupings Model (PDGM) from incoming Ambulatory Payment Classification (APC) grouper using EasyGroup PPS Pricer. |
| 48 | `PDGM` | VARCHAR |  | PDGM from incoming APC grouper using EasyGroup PPS Pricer |
| 49 | `ADJUSTED_DRG_WT` | VARCHAR |  | Adjusted Diagnosis Related Group (DRG) Weight from incoming DRG pricer using EasyGroup PPS Pricer. |
| 50 | `VAL_CODE` | VARCHAR |  | Payer Value Code from incoming Ambulatory Code Editor using EasyGroup PPS Pricer. |
| 51 | `VAL_AMT` | VARCHAR |  | Payer Value Code Amount from incoming Ambulatory Code Editor using EasyGroup PPS Pricer. |
| 52 | `ER_REDUCT_FLAG` | VARCHAR |  | Flag to determine to apply ER payment reduction from incoming APG Grouper using EasyGroup PPS Pricer |
| 53 | `APL_FLAG` | VARCHAR |  | Missing Ambulatory Procedures Listing (APL) Flag from incoming APG Pricer using EasyGroup PPS Pricer |
| 54 | `NPI_USED` | VARCHAR |  | National Provider Identifier (NPI) used for processing from incoming ECB2 block using EasyGroup PPS Pricer |
| 55 | `TAXONOMY_USED` | VARCHAR |  | Taxonomy used for processing from incoming ECB2 block using EasyGroup PPS Pricer |
| 56 | `FACILITY_USED` | VARCHAR |  | Facility used for processing from incoming ECB2 block using EasyGroup PPS Pricer |
| 57 | `PAYSRC_USED` | VARCHAR |  | Payer ID Used for processing from incoming ECB2 block using EasyGroup PPS Pricer |
| 58 | `ADMIT_DX_USED_DESCRIPTION` | VARCHAR |  | The description of the admission diagnosis used. |
| 59 | `DRG_DESCRIPTION` | VARCHAR |  | The description of the Diagnosis Related Group (DRG). |
| 60 | `INITIAL_DRG_DESCRIPTION` | VARCHAR |  | The description of the initial Diagnosis Related Group (DRG). |
| 61 | `INITIAL_MDC_DESCRIPTION` | VARCHAR |  | The description of the initial Major Diagnostic Category (MDC). |
| 62 | `MDC_DESCRIPTION` | VARCHAR |  | The description of the Major Diagnostic Category (MDC). |
| 63 | `SUGGESTED_PRINCIPAL_PX_DESC` | VARCHAR |  | Description of the suggested principal procedure. |
| 64 | `ADMIT_DX_HAC_PROCESSING_DESC` | VARCHAR |  | Description of admitting diagnosis code that was used during HAC Adjusted DRG processing. |
| 65 | `ADMIT_DRG_DESCRIPTION` | VARCHAR |  | Description of returned DRG assigned at admission. |
| 66 | `ADMIT_MDC_DESC` | VARCHAR |  | Description of the Major Diagnostic Category (MDC) assigned at admission |
| 67 | `ADMIT_ROM_DESC` | VARCHAR |  | Description of Risk of Mortality (ROM) assigned at admission. |
| 68 | `ADMIT_SOI_DESC` | VARCHAR |  | Description of Severity Of Illness (SOI) assigned at admission. |
| 69 | `HAC_ADJ_DRG_DESC` | VARCHAR |  | Description of the HAC adjusted Diagnosis Related Group. |
| 70 | `HAC_ADJ_MDC_DESC` | VARCHAR |  | Description of HAC adjusted Major Diagnostic Category. |
| 71 | `HAC_ADJ_ROM_DESC` | VARCHAR |  | Description of the HAC adjusted Risk of Mortality. |
| 72 | `HAC_ADJ_SOI_DESC` | VARCHAR |  | Description of HAC adjusted Severity of Illness. |
| 73 | `RISK_OF_MORTALITY_DESC` | VARCHAR |  | Description of the Risk of Mortality. |
| 74 | `SEVERITY_OF_ILLNESS_DESC` | VARCHAR |  | Description of the Severity of Illness. |
| 75 | `PRICER_BASE_RATE` | VARCHAR |  | Pricer data |
| 76 | `OVERALL_CLAIM_TYPE` | VARCHAR |  | The description of the overall claim type. |
| 77 | `PAYMENT_ACTION` | VARCHAR |  | The action for payment recommended by the pricer. |
| 78 | `TOTAL_CUTBACK_PAYMENT` | VARCHAR |  | Total cutback payment. |
| 79 | `TOTAL_CUTBACK_PERCENT` | VARCHAR |  | Total cutback percent. |
| 80 | `TOTAL_EXCLUDING_OUTLIERS_PMT` | VARCHAR |  | Total excluding outliers payment. |
| 81 | `TTL_ITEM_PMT_SUBJ_TO_CUTBACK` | VARCHAR |  | Total item payment subject to cutback. |
| 82 | `PPS_ASSOC_VEN_CONTRACT_ID` | NUMERIC |  | The unique ID of the vendor contract associated with one communication with a PPS pricer. |
| 83 | `PPS_ASSOC_VEN_CONTRACT_ID_CONTRACT_NAME` | VARCHAR |  | The name of the Vendor-Network contract. |
| 84 | `PPS_USED_IN_PRICE_C_NAME` | VARCHAR |  | Indicates whether a PPS data line is associated with the vendor contract that was used in the pricing of the claim at the time of adjudication. 1 indicates that the PPS data was used to price the claim. 2 indicates that the PPS data was not used to price the claim. Null indicates that there is no associated vendor contract or it is not known whether the PPS line was used for pricing. |
| 85 | `EDC_ANALYZER_FLAG` | VARCHAR |  | Indicates whether the EDC Analyzer was run and results are available. |
| 86 | `MOE_FLAG` | VARCHAR |  | Indicates whether the Medicaid Outpatient Editor was run and results are available. |
| 87 | `CALC_FLAG` | VARCHAR |  | Indicates whether the Calculation Control program was run and results are available. |
| 88 | `FILE_NOT_FOUND` | VARCHAR |  | Name of the missing program file. |
| 89 | `RAP_PENALTY_AMT` | VARCHAR |  | Amount the total payment has been reduced by due to an untimely RAP submission. |
| 90 | `RAP_PENALTY_AMT_ALT` | VARCHAR |  | Amount the alternate total payment has been reduced by due to an untimely RAP submission. |
| 91 | `PPR_ADJ_AMT` | VARCHAR |  | Potentially Preventable Readmissions adjustment amount. |
| 92 | `PPC_ADJ_AMT` | VARCHAR |  | Potentially Preventable Complications adjustment amount. |
| 93 | `EDITOR_RTN_TYPE` | VARCHAR |  | Editor Return Code Type from incoming ACE editor using EasyGroup PPS Pricer. |
| 94 | `DB_SERVER_AND_INST` | VARCHAR |  | Database server and instance used for processing from incoming ECB2 block using EasyGroup PPS Pricer. |
| 95 | `DB_NAME` | VARCHAR |  | Database name used for processing from incoming ECB2 block using EasyGroup PPS Pricer. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

