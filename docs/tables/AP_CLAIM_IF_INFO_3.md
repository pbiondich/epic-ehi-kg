# AP_CLAIM_IF_INFO_3

> Additional information sent to prospective payment systems (PPS) groupers/pricers.

**Overflow of:** [AP_CLAIM_IF_INFO](AP_CLAIM_IF_INFO.md)  
**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 63

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLINICAL_TRIAL_REGISTRY_NUM` | VARCHAR |  | Identifies the clinical trial registry number. |
| 4 | `DISCHARGE_DATE` | VARCHAR |  | For inpatient, the date the patient was discharged from the facility. For outpatient, the end date of the period covered on the claim. |
| 5 | `NONCOVERED_CHARGES` | VARCHAR |  | The portion of the claim's total charges that is not recognized for payment. |
| 6 | `ADMIT_DX_USED` | VARCHAR |  | The admit diagnosis code that was used during processing. |
| 7 | `ANALYSIS_PAYMENT` | VARCHAR |  | The standard payment for the claim including applicable add-ons or adjustments, but excluding transfers and outliers. |
| 8 | `CAPITAL_COST_OUTLIER_PAYMENT` | VARCHAR |  | Additional payment for high cost cases, allowing for reimbursement for capital expenses. |
| 9 | `CAPITAL_COST_OUTLIER_THRESHOLD` | VARCHAR |  | Capital portion of the cost threshold. |
| 10 | `CAPITAL_COSTS` | VARCHAR |  | Charges reduced to capital portion of costs. |
| 11 | `CAPITAL_DSH_FACTOR` | VARCHAR |  | Calculated amount that is multiplied by the capital federal specific portion (FSP) payment to derive the capital disproportionate share hospital (DSH) payment. |
| 12 | `CAPITAL_EXCEPTION_PAYMENT` | VARCHAR |  | A set amount per claim to reimburse for capital expenses. |
| 13 | `CAPITAL_FSP_PAYMENT` | VARCHAR |  | Federal specific portion payment for capital, the standard prospective payment to reimburse for capital expenses. |
| 14 | `CAPITAL_HSP_PAYMENT` | VARCHAR |  | The hospital specific portion payment for capital. |
| 15 | `CAPITAL_IME_FACTOR` | VARCHAR |  | Calculated amount that is multiplied by the capital federal specific portion (FSP) payment to derive the capital indirect medical education (IME) payment. |
| 16 | `CAPITAL_OLD_HOLD_HARMLESS_PMT` | VARCHAR |  | Cost payment for old capital. |
| 17 | `CAPITAL_PAYMENT` | VARCHAR |  | The total capital payment for the claim. |
| 18 | `CLINICAL_TRIAL_ADDON_PAYMENT` | VARCHAR |  | The add-on payment for agency approved procedure codes determined to be a part of clinical trials. |
| 19 | `DEVICE_AMOUNT` | VARCHAR |  | The vendor credit amount for a replacement device as reported with value code FD. |
| 20 | `DEVICE_CREDIT_FLAG` | VARCHAR |  | Indicates whether the diagnosis related group is subject to a device credit. |
| 21 | `DISCHARGE_STATUS_USED` | VARCHAR |  | Indicates the discharge status used in grouping. |
| 22 | `DSH_PAYMENT` | VARCHAR |  | The disproportionate share hospital payment. |
| 23 | `HAC_CAT_SATISFIED_COUNT` | VARCHAR |  | Number of unique hospital-acquired condition categories satisfied on the claim. |
| 24 | `HAC_REDUCTION_PROGRAM_ADJ` | VARCHAR |  | Amount the total claim payment was reduced due to the Hospital-Acquired Condition reduction program. |
| 25 | `HAC_STATUS` | VARCHAR |  | Indicates overall results of hospital-acquired condition processing at the claim level. |
| 26 | `HEMOPHILIA_ADDON_PAYMENT` | VARCHAR |  | Add-on payment for blood clotting factor administered to hemophilia inpatients. |
| 27 | `HOSP_READMIT_REDUCT_PROG_ADJ` | VARCHAR |  | Adjustment to the claim payment in accordance with the hospital readmissions reduction program. |
| 28 | `ICD_VERSION_QUALIFIER_USED` | VARCHAR |  | Indicates whether the code set used for processing was ICD-9 or ICD-10. |
| 29 | `INDIRECT_MEDICAL_EDU_PAYMENT` | VARCHAR |  | Reimbursement for indirect medical education. |
| 30 | `INIT_DX_RELATED_GROUP` | VARCHAR |  | The diagnosis related group (DRG) calculated before CMS Hospital-Acquired Conditions are considered. |
| 31 | `INIT_MAJOR_DX_CAT` | VARCHAR |  | The major diagnostic category (MDC) assigned before CMS hospital-acquired conditions are considered. |
| 32 | `INIT_MEDICAL_SURGICAL_DRG_FLAG` | VARCHAR |  | Flag indicating if the initial diagnosis related group (DRG) is medical, surgical, or neither. |
| 33 | `INITIAL_RETURN_CODE` | VARCHAR |  | Error return code for the initial diagnosis related group assignment. |
| 34 | `LENGTH_OF_STAY` | VARCHAR |  | The number of days the patient was hospitalized. |
| 35 | `LOW_VOLUME_ADDON_PAYMENT` | VARCHAR |  | The portion of the total payment that is additional due to the provider qualifying as a Medicare low volume hospital. |
| 36 | `LOW_VOLUME_ADJ_PERCENT` | VARCHAR |  | The percentage adjustment used to determine the Low Volume Add-on Payment. |
| 37 | `MARGINAL_COST_FACTOR` | VARCHAR |  | The variable is used in the calculation of an outlier payment. |
| 38 | `MEDICAL_SURGICAL_DRG_FLAG` | VARCHAR |  | Indicates if the Diagnosis Related Group is medical, surgical, or neither. |
| 39 | `NATIONAL_FSP_AMOUNT` | VARCHAR |  | The operating base rate, which is multiplied by the weight to determine the Operating Federal Specific Portion payment. |
| 40 | `NEW_TECHNOLOGY_ADDON_PAYMENT` | VARCHAR |  | Add-on payment for certain devices, which CMS approves for an additional payment. |
| 41 | `OPERATING_COST_OUTLIER_PAYMENT` | VARCHAR |  | Extra payment for a high cost case to reimburse operating expenses. |
| 42 | `OPERATING_COST_OUTLIER_THRESH` | VARCHAR |  | Operating portion of the cost threshold. |
| 43 | `OPERATING_COSTS` | VARCHAR |  | Charges reduced to operating portion of costs. |
| 44 | `OPERATING_DSH_FACTOR` | VARCHAR |  | Used to determine if the hospital qualifies for a Disproportionate Share Hospital (DSH) adjustment and the size of capital and operating DSH adjustments. |
| 45 | `OPERATING_FSP_PAYMENT` | VARCHAR |  | The federal specific portion reimbursed for operating expenses. |
| 46 | `OPERATING_HSP_PAYMENT` | VARCHAR |  | The hospital specific portion reimbursed for operating expenses. |
| 47 | `OPERATING_IME_FACTOR` | VARCHAR |  | A calculated value based around the provider intern to bed ratio, which is multiplied by the relative weight to calculate the operating indirect medical education (IME) payment. |
| 48 | `PAYMENT_STATUS` | VARCHAR |  | Payment status for the claim. |
| 49 | `POST_ACUTE_CARE_TRANSFER_DRG` | VARCHAR |  | Indicates whether or not the DRG is subject to the post acute care transfer reimbursement policy. |
| 50 | `PX_USED_COUNT` | VARCHAR |  | Number of procedure codes used for grouping. |
| 51 | `SECONDARY_DX_USED_COUNT` | VARCHAR |  | Number of secondary diagnosis codes and External Cause of Injury Codes that were used during processing. |
| 52 | `SERVICE_LOCATION_ID_IN` | VARCHAR |  | A unique identifier for the facility service location. |
| 53 | `SPEC_POST_ACUTE_CARE_TRANS_DRG` | VARCHAR |  | Indicates whether or not the DRG is subject to the special post acute care transfer reimbursement policy. |
| 54 | `SUGGESTED_PRINCIPAL_PX` | VARCHAR |  | The suggested principal procedure based on coding practice and policies. |
| 55 | `TOTAL_EXCL_PASS_THROUGH_PMT` | VARCHAR |  | The total expected payment without miscellaneous per diem amounts. |
| 56 | `TOTAL_OPERATING_PAYMENT` | VARCHAR |  | Claim reimbursement for operating expenses. |
| 57 | `TOTAL_PAYMENT` | VARCHAR |  | The total payment for the claim. |
| 58 | `TRANSFER_IMPACT` | VARCHAR |  | Amount calculated for transfer claims to show the change in payment caused by the transfer status. |
| 59 | `UNCOMPENSATED_CARE_PAYMENT` | VARCHAR |  | Interim uncompensated care payment according to the Affordable Care Act for disproportionate share hospital payments. |
| 60 | `VBP_PROGRAM_ADJ` | VARCHAR |  | Adjustment to the total payment in accordance with the Hospital Value-Based Purchasing Program. |
| 61 | `PROV_MEDICARE_NUM` | VARCHAR |  | The Medicare number of the provider associated with the claim. |
| 62 | `DISCHRG_STAT_RET_CD` | VARCHAR |  | Error code assigned to the discharge status mapping assignment. |
| 63 | `BIRTH_WEIGHT` | VARCHAR |  | The birth weight, in grams. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

