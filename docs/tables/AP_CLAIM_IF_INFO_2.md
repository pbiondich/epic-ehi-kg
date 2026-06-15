# AP_CLAIM_IF_INFO_2

> The table contains information sent to or returned from a prospective payment systems (PPS) pricer.

**Overflow of:** [AP_CLAIM_IF_INFO](AP_CLAIM_IF_INFO.md)  
**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 95

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BMI_FCTR_SEP_PYBL` | VARCHAR |  | Separately payable portion of bundled BMI factor utilized for cost outlier calculation. |
| 4 | `BSA` | VARCHAR |  | Body Surface Area (BSA) of patient. |
| 5 | `BSA_FCTR_SEP_PYBL` | VARCHAR |  | Separately payable portion of bundled BSA factor utilized for cost outlier calculation. |
| 6 | `AGE_FCTR_BUND_PPS` | VARCHAR |  | Age adjustment utilized for the bundled prospective payment of dialysis services. |
| 7 | `BMI_FCTR_BUND_PPS` | VARCHAR |  | BMI factor for the bundled prospective payment of dialysis services. |
| 8 | `BSA_FCTR_BUND_PPS` | VARCHAR |  | BSA factor for the bundled prospective payment of dialysis services. |
| 9 | `COMORB_FCTR` | VARCHAR |  | Comorbidity adjustment utilized for the prospective payment of dialysis services. |
| 10 | `COMORB_FCT_SEP_PBL` | VARCHAR |  | Separately payable portion of comorbidity factor utilized for cost outlier calculation. |
| 11 | `LOW_VOL_ADJ` | VARCHAR |  | Low volume adjustment utilized for the bundled prospective payment of dialysis services. |
| 12 | `LOW_VOL_ADJ_SEP_PBL` | VARCHAR |  | Separately payable portion of low volume factor utilized for cost outlier calculation. |
| 13 | `PASS_THRU_PMT` | VARCHAR |  | Additional payment for pass-through expenses. |
| 14 | `MEAN_LOS` | VARCHAR |  | Mean Length of Stay. |
| 15 | `ADDL_MEAN_LOS` | VARCHAR |  | Additional Mean Length of Stay |
| 16 | `DRG_WEIGHT` | VARCHAR |  | DRG-specific weight utilized for patient pricing. |
| 17 | `PER_DIEM` | VARCHAR |  | Per Diem Reimbursement. |
| 18 | `TIERED_PER_DIEM` | VARCHAR |  | Tiered Per-Diem Reimbursement. |
| 19 | `DRG_PAYTYPE` | VARCHAR |  | DRG Specific Pricing Rule. |
| 20 | `INLIER_RATE` | VARCHAR |  | Inlier Rate. |
| 21 | `TRANSFER_FLAG` | VARCHAR |  | Transfer Flag. |
| 22 | `OPR_IME_PMT` | VARCHAR |  | Operating Indirect Medical Education (IME) Payment. |
| 23 | `OPR_DSH_PMT` | VARCHAR |  | Operating Disproportionate Hospital (DSH) Payment. |
| 24 | `CAP_IME_PMT` | VARCHAR |  | Capital Indirect Medical Education (IME) Payment. |
| 25 | `CAP_DSH_PMT` | VARCHAR |  | Capital Disproportionate Hospital (DSH) Payment. |
| 26 | `REIMB_DRG` | VARCHAR |  | Reimbursement DRG. |
| 27 | `PAYMENT_CMG` | VARCHAR |  | Contains a payment-related Case Mix Group (CMG). |
| 28 | `PAYMENT_HIPPS` | VARCHAR |  | Health Insurance Prospective Payment System (HIPPS) code returned by the pricer. |
| 29 | `PPS_PENALTY_AMT` | VARCHAR |  | This field contains the dollar amount of any applicable penalty. |
| 30 | `PAYMENT_FLAG_CMG` | VARCHAR |  | Payment flag for Inpatient Rehabilitation Facility (IRF) priced claims. |
| 31 | `TRANSFER_FLAG_CMG` | VARCHAR |  | Transfer flag for IRF priced claims. |
| 32 | `PENALTY_FLAG` | VARCHAR |  | Penalty flag. |
| 33 | `PENALTY_PERCENT` | VARCHAR |  | This field contains the percentage the facility was penalized. |
| 34 | `HIPPS_WEIGHT` | VARCHAR |  | Relative weight for payment HIPPS code. |
| 35 | `HIPPS_AVG_LOS` | VARCHAR |  | Average length of stay for payment HIPPS code. |
| 36 | `OUTLIER_CHRGS` | VARCHAR |  | Charges used to determine applicable cost outlier payments. |
| 37 | `OUTLIER_THRESHOLD` | VARCHAR |  | Cost outlier threshold for payment HIPPS code. |
| 38 | `ASSESSMNT_TDATE` | VARCHAR |  | Assessment transmission date. |
| 39 | `AIDS_ADJ_FACTOR` | VARCHAR |  | AIDS adjustment factor. |
| 40 | `TOT_THIRD_PARTY_PMT` | VARCHAR |  | Total third party payment is the total reimbursement for this claim minus patient coinsurance. |
| 41 | `OR_PROC_FOR_DRG` | VARCHAR |  | First three operating room procedures that influenced DRG assignment. |
| 42 | `NOR_PROC_FOR_DRG` | VARCHAR |  | First and second non-operating room procedures that influenced DRG assignment. |
| 43 | `COMRBD_DX_FOR_DRG` | VARCHAR |  | Diagnosis code that satisfied the complication/comorbidity (CC) criteria and influenced DRG assignment. |
| 44 | `DX_FOR_DRG` | VARCHAR |  | First three diagnoses (other than principal) that influenced DRG assignment. |
| 45 | `NUM_OF_MCCS` | VARCHAR |  | Number of major complications/comorbidities in the claim not excluded by the principle diagnosis. |
| 46 | `NUM_OF_CCS` | VARCHAR |  | Number of complications/comorbidities in the claim not excluded by the principle diagnosis. |
| 47 | `ADM_MOTOR_SCR_CALC` | VARCHAR |  | Total motor score calculated from IRF-PAI admission motor scores. |
| 48 | `ADM_MOTOR_SCR_FLAG` | VARCHAR |  | Admission motor score flag. |
| 49 | `ADM_COGN_SCR_CALC` | VARCHAR |  | Sum of fields 39N through 39R on the Inpatient Rehabilitation Facility Patient Assessment Instrument (IRF-PAI). |
| 50 | `ADM_COGN_SCR_FLAG` | VARCHAR |  | Admission cognitive score flag. |
| 51 | `DEMOG_ERR_CNT` | VARCHAR |  | Count of total demographic errors encountered for the input record. |
| 52 | `AGE_EDIT` | VARCHAR |  | Age edit. |
| 53 | `SEX_EDIT` | VARCHAR |  | Sex edit. |
| 54 | `DISCHRG_DISP_EDIT` | VARCHAR |  | Discharge disposition edit. |
| 55 | `BWGT_EDIT` | VARCHAR |  | Birthweight edit. |
| 56 | `MCE_DX_ERR_CNT` | VARCHAR |  | Count of total diagnosis errors encountered. |
| 57 | `PRINC_DX_ERRS` | VARCHAR |  | Principal diagnosis errors. |
| 58 | `PRINC_DX_SURG_EDIT` | VARCHAR |  | Principal Diagnosis/Surgery Edit. |
| 59 | `ADMIT_DX_ECODE_ERR` | VARCHAR |  | Admit Diagnosis External Cause of Injury Code/Manifestation Code. |
| 60 | `MCE_PX_ERR_CNT` | VARCHAR |  | Count of total procedure errors encountered. |
| 61 | `NON_SPEC_PX_EDIT` | VARCHAR |  | Nonspecific Procedure Edit. |
| 62 | `BILAT_CODING_EDIT` | VARCHAR |  | Bilateral coding edit. |
| 63 | `ADMIT_DX_INVALID` | VARCHAR |  | Admit Diagnosis Invalid. |
| 64 | `ADMIT_DX_AGE_SEX` | VARCHAR |  | Admit Diagnosis Age/Sex |
| 65 | `ADM_DX_MED_SEC_ALRT` | VARCHAR |  | Admit Diagnosis Medicare as Secondary Payer Alert. |
| 66 | `MCE_TOT_ERRS` | VARCHAR |  | Total Date-Sensitive Code Editor/Medicare Code Editor errors for this claim. |
| 67 | `PERCENT_CHRGS` | VARCHAR |  | Percent of Charges Value. |
| 68 | `GRPR_SEV_ILLNESS` | VARCHAR |  | Identifies severity of illness associated with claim level diagnosis. Data received in GOB1.DRG block on incoming message. |
| 69 | `GRPR_RSK_MORTALITY` | VARCHAR |  | Identifies risk of mortality associated with claim level diagnosis. Data received in GOB1.DRG block on incoming message. |
| 70 | `AGE_DAYS_OF_ADMISSION` | VARCHAR |  | Age in days as the number of days between birth date and the date of admission. Required for neonates. Data sent in PCB2.ICD block on the outgoing message. |
| 71 | `AGE_DAYS_OF_DISCHARGE` | VARCHAR |  | Age in days as the number of days between the birth date and the date of discharge. Required for neonates. Data sent in PCB2.ICD block on the outgoing message. |
| 72 | `OR_PROC_01` | VARCHAR |  | Identifies the first three operating room procedures that influenced DRG assignment. Data received in GOB1.DRG block on incoming message. |
| 73 | `NON_OR_PROC_01` | VARCHAR |  | Identifies the first and second non-operating room procedures that influenced DRG assignment. Data received in GOB1.DRG block on incoming message. |
| 74 | `COMORBIDITY_DX_01` | VARCHAR |  | Identifies diagnosis code that satisfied the Complication/Comorbidity (CC) criteria and influenced DRG assignment. Data received in GOB1.DRG block on incoming message. |
| 75 | `DX_FOR_DRG_01` | VARCHAR |  | Identifies the first three diagnoses (other than principal) that influenced DRG assignment. Data received in GOB1.DRG block on incoming message. |
| 76 | `ADMISSION_DRG` | VARCHAR |  | Identifies the admission Diagnosis Related Group (DRG). Data received in GOB1.DRG block on incoming message. |
| 77 | `ADMISSION_SOI` | VARCHAR |  | Identifies level of severity of illness at admission. Data received in GOB1.DRG block on incoming message. |
| 78 | `ADMISSION_ROM` | VARCHAR |  | Identifies risk of mortality at admission. Data received in GOB1.DRG block on incoming message. |
| 79 | `ADMIT_MOTOR_SCORE_CALC_2` | VARCHAR |  | Identifies motor-out score redefined with 3 digits following the decimal. Data received in GOB1.CMG block on incoming message. |
| 80 | `ADMIT_COGNITIVE_SCORE_CALC_2` | VARCHAR |  | Identifies cognitive-out score redefined with 3 digits following the decimal. Data received in GOB1.CMG block on incoming message. |
| 81 | `ICD10_COMORBIDITY_01` | VARCHAR |  | Identifies comorbidity code that is at the highest comorbidity tier for the case. Data received in GOB1.CMG block on incoming message. |
| 82 | `ICD10_COMORBIDITY_02` | VARCHAR |  | Identifies comorbidity code that is at the highest comorbidity tier for the case and part of an ICD-10 code pair. Data received in GOB1.CMG block on incoming message. |
| 83 | `SHORT_STAY_OUTL_TRIM` | VARCHAR |  | Identifies short stay or day outliers. Data received in POB1.DRG block on incoming message. |
| 84 | `LONG_STAY_OUTL_TRIM` | VARCHAR |  | Identifies long stay or day outliers. Data received in POB1.DRG block on incoming message. |
| 85 | `COST_OUTL_THRESHOLD` | VARCHAR |  | Identifies predicted map plus fixed dollar loss amount that is utilized for the cost outlier calculation. |
| 86 | `TOT_PRED_ESRD_OUTL_PMT` | VARCHAR |  | Identifies total predicted amount of separately payable services per dialysis treatment on monthly bill. For ESRD only. Data received in POB1.APC block on incoming message. |
| 87 | `NUM_DIALYSIS_LN_ITEM` | VARCHAR |  | Identifies number of dialysis claim lines. For ESRD only. Data received in POB1.APC block on incoming message. |
| 88 | `CORE_BASE_STAT_AREA` | VARCHAR |  | Identifies core based statistical area. For ESRD only. Data received in POB1.APC block on incoming message. |
| 89 | `RET_CODE_38_OVR_FLG` | VARCHAR |  | Flag indicating whether or not the claim-level Pricer Return Code 38 (Invalid or Missing Required Claims Data) has been overridden. For ESRD only. Data received in POB1.APC block on incoming message. |
| 90 | `AGE_EDIT_IND` | VARCHAR |  | Indicates an age edit. Data received in MEB1 block on incoming message. |
| 91 | `NUM_OF_VISITS` | VARCHAR |  | Identifies total number of visits on the claim. |
| 92 | `CAPITAL_ADDON` | VARCHAR |  | Identifies total capital add-on for the claim. |
| 93 | `BLEND_FACTOR` | VARCHAR |  | Identifies portion of Ambulatory Patient Group (APG) payment applied to the claim. |
| 94 | `RATE_CODE_INDICATOR` | VARCHAR |  | Identifies payment rules applied to the claim, based on the APG rate code supplied on claim. |
| 95 | `TOTAL_EXISTING_PAYMENT` | VARCHAR |  | Identifies total payment for non-APG portion of visits on claim. Only applies to facility types subject to transitions. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

