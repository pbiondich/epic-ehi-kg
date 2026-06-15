# AP_CLAIM_IF_INFO

> The table contains information sent to or returned from a prospective payment systems (PPS) pricer.

**Overflow family:** [AP_CLAIM_IF_INFO_2](AP_CLAIM_IF_INFO_2.md), [AP_CLAIM_IF_INFO_3](AP_CLAIM_IF_INFO_3.md), [AP_CLAIM_IF_INFO_4](AP_CLAIM_IF_INFO_4.md), [AP_CLAIM_IF_INFO_5](AP_CLAIM_IF_INFO_5.md)  
**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 97

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMM_STAT_C_NAME` | VARCHAR |  | The Interface communication status. |
| 4 | `GROUPER_RETURN_CODE` | VARCHAR |  | The Grouper Return Code field from APC Grouper output fields. |
| 5 | `GROUPER_TYPE` | VARCHAR |  | The Grouper Type field from APC Grouper output fields. |
| 6 | `GROUPER_VERSION` | VARCHAR |  | The Grouper Version field from APC Grouper output fields. |
| 7 | `PAT_VISIT_TYPE` | VARCHAR |  | The Patient or Visit Type field from APC Grouper output fields. |
| 8 | `APC_STATUS_CODE` | VARCHAR |  | The ambulatory payment classification (APC) status code field from APC grouper output fields. |
| 9 | `PRICER_RETURN_CODE` | VARCHAR |  | The Pricer Return Code field from APC Pricer output fields. |
| 10 | `PRICER_TYPE` | VARCHAR |  | The Pricer Type field from APC Pricer output fields. |
| 11 | `BASE_APC_REIMB` | VARCHAR |  | The Base APC Reimbursement field from APC Pricer output fields. |
| 12 | `PAT_COPAY` | VARCHAR |  | The Patient Co-payment field from APC Pricer output fields. |
| 13 | `OUTLIER_PMT` | VARCHAR |  | The Outlier Payment field from APC Pricer output fields. |
| 14 | `PPS_CHRGS` | VARCHAR |  | The PPS Charges field from APC Pricer output fields. |
| 15 | `PPS_PMT` | VARCHAR |  | The PPS Payment field from APC Pricer output fields. |
| 16 | `TRANS_COR_HOLD_HARM` | VARCHAR |  | The Transitional Corridor/Hold Harmless Add-on field from APC Pricer output fields. |
| 17 | `CLM_DEDUCT` | VARCHAR |  | The Claim Deductible field from APC Pricer output fields. |
| 18 | `TOTAL_APC_REIMB` | VARCHAR |  | The Total APC Reimbursement field from APC Pricer output fields. |
| 19 | `OUTLIER_FLAG` | VARCHAR |  | The Outlier Flag field from APC Pricer output fields. |
| 20 | `BASE_RATE_FLAG` | VARCHAR |  | The Base Rate Flag field from APC Pricer output fields. |
| 21 | `COST_REDUCT_FACTOR` | VARCHAR |  | The Cost Reduction Factor field from APC Pricer output fields. |
| 22 | `RURAL` | VARCHAR |  | The Rural field from APC Pricer output fields. |
| 23 | `OUTPAT_RCC` | VARCHAR |  | The outpatient ratio of cost to charge (RCC) field from APC pricer output fields. |
| 24 | `MARKUP_DISCNT_FACT` | VARCHAR |  | The Mark-up/Discount Factor field from APC Pricer output fields. |
| 25 | `PRICER_METHOD` | VARCHAR |  | The Method field from APC Pricer output fields. |
| 26 | `ACE_RETURN_CODE` | VARCHAR |  | The editor return code field from Ambulatory Code Editor (ACE), Medicare Code Editor (MCE), or Medicaid Outpatient Editor (MOE) output fields. |
| 27 | `ACE_VERSION` | VARCHAR |  | The editor version field from Ambulatory Code Editor (ACE), Medicare Code Editor (MCE), or Medicaid Outpatient Editor (MOE) output fields. |
| 28 | `ACE_RLS_VERSION` | VARCHAR |  | The ACE Release Version field from ACE output fields. |
| 29 | `NUM_CLM_ERRORS` | VARCHAR |  | The Number of Claim Errors field from ACE output fields. |
| 30 | `NUM_DX_ERRORS` | VARCHAR |  | The Number of Diagnosis Errors field from ACE output fields. |
| 31 | `NUM_PX_ERRORS` | VARCHAR |  | The Number of Procedure Errors field from ACE output fields. |
| 32 | `NUM_CCI_ERRORS` | VARCHAR |  | The Number of CCI Errors field from ACE output fields. |
| 33 | `NUM_ADMIT_DX_ERRORS` | VARCHAR |  | The Number of Admit Diagnosis Errors field from ACE output fields. |
| 34 | `TOT_NUM_ERRORS` | VARCHAR |  | The Total Number of Errors field from ACE output fields. |
| 35 | `ADMIT_DX_DISP` | VARCHAR |  | The Admit Diagnosis Disposition field from ACE output fields. |
| 36 | `OVERALL_CLM_DISP` | VARCHAR |  | The Overall Claim Disposition field from ACE output fields. |
| 37 | `OCE_ERROR_DISP` | VARCHAR |  | The OCE Error Disposition field from ACE output fields. |
| 38 | `CLM_ERROR_DETAIL` | VARCHAR |  | The Claim Error Detail field from ACE output fields. |
| 39 | `RSN_VIS_DX_ERRORS` | VARCHAR |  | The Reason for Visit Diagnosis Errors field from ACE output fields. |
| 40 | `ADJUD_TIME_DTTM` | DATETIME (Local) |  | The timestamp for each communication. |
| 41 | `OPTIMIZER_RET_VAL` | VARCHAR |  | The Optimizer return value. |
| 42 | `MOST_RECENT_ADJU_YN` | VARCHAR |  | Indicate if the adjudication is the most recent adjudication that we get APC values. |
| 43 | `OUT_FROM_DATE` | VARCHAR |  | The admission from date of the claim. |
| 44 | `OUT_THRU_DATE` | VARCHAR |  | The admission through date of the claim. |
| 45 | `OUT_BIRTH_DATE` | VARCHAR |  | The patient birth date. |
| 46 | `OUT_PROV` | VARCHAR |  | The provider of the claim. If your organization uses Tapestry's generic APC interface, this column saves the vendor identity ID of the claim. |
| 47 | `OUT_PAYOR` | VARCHAR |  | The payor of the claim. |
| 48 | `OUT_AGE` | VARCHAR |  | The patient age. |
| 49 | `OUT_SEX` | VARCHAR |  | The patient sex. |
| 50 | `OUT_MRN` | VARCHAR |  | The patient medical record number. |
| 51 | `OUT_PAT_CONTROL_NUM` | VARCHAR |  | The patient control number. |
| 52 | `OUT_TOB` | VARCHAR |  | The type of bill of the claim. |
| 53 | `OUT_DISCHRG_STAT` | VARCHAR |  | The patient discharge status of the claim. |
| 54 | `OUT_TTL_CHRG` | VARCHAR |  | The total charge of the claim. |
| 55 | `OUT_LEN_STAY` | VARCHAR |  | The length of stay of the claim. |
| 56 | `OUT_ADMIT_SRC` | VARCHAR |  | The source of admission listed on the claim. |
| 57 | `OUT_ADMSN_DX` | VARCHAR |  | The admission diagnosis of the claim. |
| 58 | `OUT_ADMSN_TYPE` | VARCHAR |  | The admission type of the claim. |
| 59 | `OUT_NPI` | VARCHAR |  | The National Provider Identifier (NPI) of the claim. |
| 60 | `OUT_TAXONOMY` | VARCHAR |  | The taxonomy of the claim. |
| 61 | `OUT_COND_CODES` | VARCHAR |  | The condition codes of the claim. |
| 62 | `OUT_ACE_OVRIDE` | VARCHAR |  | The ACE override ID of the claim. |
| 63 | `CCI_EDIT_SUM` | VARCHAR |  | The Correct Coding Initiative (CCI) edit summary returned by the APC interface. |
| 64 | `OCE_EDIT_SUM` | VARCHAR |  | The outpatient code editor (OCE) edit summary returned by the APC interface. |
| 65 | `TRACE_INFO` | VARCHAR |  | The trace info of the claim. |
| 66 | `OUT_PAT_ID_NUM` | VARCHAR |  | The patient identity ID of the claim. |
| 67 | `OUT_PROV_ID_NUM` | VARCHAR |  | The provider identity ID of the claim. |
| 68 | `OUT_POS_ID_NUM` | VARCHAR |  | The ID of the Place of Service (POS) on the claim. |
| 69 | `OUT_CLM_SVC_DATE` | VARCHAR |  | The claim service date. |
| 70 | `OUT_AUTHCODE` | VARCHAR |  | Authorization code |
| 71 | `OUT_ADMIT_DATE` | VARCHAR |  | Admission date. |
| 72 | `OUT_ESRD_ONSET_DATE` | VARCHAR |  | End-stage Renal Disease (ESRD) onset date sent to the Prospective Payment System (PPS) pricer. |
| 73 | `ALTERNATE_HHRG` | VARCHAR |  | Alternate home health resource group (HHRG) for home health agency (HHA) pricer. |
| 74 | `ALTERNATE_HHRG_FLAG` | VARCHAR |  | Alternate HHRG flag. |
| 75 | `HOME_HEALTH_RES_GRP` | VARCHAR |  | HHRG - Home Health Resource Group. |
| 76 | `NON_RESRC_SUPPLIES` | VARCHAR |  | Non-resource supplies code. |
| 77 | `TREATMNT_AUTH_VALID` | VARCHAR |  | Treatment authorization code validity flag. |
| 78 | `MAJOR_DIAG_CATEGORY` | VARCHAR |  | Major Diagnostic Category. |
| 79 | `DRG` | VARCHAR |  | Diagnostic Related Group (DRG). |
| 80 | `ALTERNATE_DRG` | VARCHAR |  | Alternate diagnosis related group (DRG) |
| 81 | `RIC` | VARCHAR |  | Rehabilitation Impairment Category. |
| 82 | `CLINICAL_CMG` | VARCHAR |  | Original/Clinical Casemix Group. |
| 83 | `HIPPS` | VARCHAR |  | Health Insurance Prospective Payment System (HIPPS) code |
| 84 | `COMORBIDITY_CODE` | VARCHAR |  | Comorbidity code used for health insurance prospective payment system (HIPPS) assignment. |
| 85 | `ALTERNATE_PMT` | VARCHAR |  | Alternate payment. |
| 86 | `ALT_ADDON_PMT` | VARCHAR |  | Alternate add-on payment. |
| 87 | `COMORBIDITY_CAT` | VARCHAR |  | Comorbidity category. |
| 88 | `QUALITY_FLAG` | VARCHAR |  | Quality flag. |
| 89 | `ADJUSTED_BASE_RATE` | VARCHAR |  | Adjusted base rate without patient-case mix adjustment. |
| 90 | `ADJUSTED_OUTL_MAP` | VARCHAR |  | Outlier services Medicare anticipated payment used for cost outlier calculation. |
| 91 | `AVG_PERTREAT` | VARCHAR |  | Actual amount of formerly separately payable services per dialysis treatment on monthly bill. |
| 92 | `AVG_PERTREAT_BLEND` | VARCHAR |  | Predicted amount of separately payable services per dialysis treatment on monthly bill. |
| 93 | `DISPENSE_FEE` | VARCHAR |  | Dispensing fee for oral-only drugs with an injectable equivalent. |
| 94 | `FIXED_LOSS_AMT` | VARCHAR |  | Fixed dollar loss amount that is added to the predicted Medicare Allowable Payment to determine the cost outlier threshold. |
| 95 | `MONTHLY_SERV_AMT` | VARCHAR |  | Total amount of formerly separately payable services utilized for the cost outlier calculation. |
| 96 | `AGE_FCTR_SEP_PYBL` | VARCHAR |  | Separately payable portion of bundled age adjustment utilized for cost outlier calculation. |
| 97 | `BMI` | VARCHAR |  | The Body Mass Index (BMI) of the patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

