# CL_RMT_INP_ADJ_INF

> This table contains inpatient adjudication information from the Remittance Image.

**Primary key:** `IMAGE_ID`  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with inpatient adjudication information. |
| 2 | `COVERED_DAYS` | INTEGER |  | Covered days or visit count for the claim for inpatient adjudication information. |
| 3 | `PPS_OPER_OUTL_AMT` | NUMERIC |  | Prospective payment system operating outlier amount for inpatient adjudication information. |
| 4 | `LIFETIME_PSYC_DAYS` | INTEGER |  | Lifetime psychiatric days count for inpatient adjudication information. |
| 5 | `CLAIM_DRG_AMT` | NUMERIC |  | Monetary amount for the diagnosis related group for inpatient adjudication information. |
| 6 | `REMARK_CODE_1` | VARCHAR |  | Remark code 1 for inpatient adjudication info. |
| 7 | `CLM_DISP_SHAR_AMT` | NUMERIC |  | Monetary amount for the claim disproportionate share for inpatient adjudication information. |
| 8 | `CLAIM_MSP_PASS_AMT` | NUMERIC |  | Monetary amount for the claim Medicare secondary payor pass through for inpatient adjudication information. |
| 9 | `CLAIM_PPS_CAP_AMT` | NUMERIC |  | Monetary amount for the prospective payment system capital for inpatient adjudication information. |
| 10 | `PPSCAP_FSP_DRG_AMT` | NUMERIC |  | Monetary amount for the prospective payment system's capital federal-specific portion for the diagnosis-related group for inpatient adjudication information. |
| 11 | `PPSCAP_HSP_DRG_AMT` | NUMERIC |  | Monetary amount for the prospective payment system's capital hospital-specific portion for the diagnosis-related group for inpatient adjudication information. |
| 12 | `PPS_DSH_DRG_AMT` | NUMERIC |  | Monetary amount for the prospective payment system's capital disproportionate share diagnosis related group for inpatient adjudication information. |
| 13 | `OLD_CAPITAL_AMT` | NUMERIC |  | Monetary amount of old capital for inpatient adjudication information. |
| 14 | `PPS_CAPTL_IME_AMT` | NUMERIC |  | Monetary amount for the prospective payment system capital's indirect medical education for inpatient adjudication information. |
| 15 | `PPS_OP_HSP_DRG_AMT` | NUMERIC |  | Monetary amount for the prospective payment system's operating hospital's specific diagnosis related group for inpatient adjudication information. |
| 16 | `COST_REPORT_DAYS` | NUMERIC |  | The number of days that may be claimed as Medicare patient days on a cost report for inpatient adjudication information. |
| 17 | `PPS_FED_DRG_AMT` | NUMERIC |  | Monetary amount for the prospective payment system's operating federal specific diagnosis related group for inpatient adjudication information. |
| 18 | `CLAIM_PPS_CAPT_AMT` | NUMERIC |  | Monetary amount for the prospective payment system's capital outlier for inpatient adjudication information. |
| 19 | `CLAIM_INDR_TCH_AMT` | NUMERIC |  | The monetary amount for the claim indirect teaching amount for inpatient adjudication information. |
| 20 | `NONPY_PROF_COM_AMT` | NUMERIC |  | The monetary amount for the nonpayable professional component for inpatient adjudication information. |
| 21 | `REMARK_CODE_2` | VARCHAR |  | Remark code 2 for inpatient adjudication info. |
| 22 | `REMARK_CODE_3` | VARCHAR |  | Remark code 3 for inpatient adjudication info. |
| 23 | `REMARK_CODE_4` | VARCHAR |  | Remark code 4 for inpatient adjudication info. |
| 24 | `REMARK_CODE_5` | VARCHAR |  | Remark code 5 for inpatient adjudication info. |
| 25 | `PPS_EXCEPTION_AMT` | NUMERIC |  | Monetary amount for the prospective payment system's capital exception for inpatient adjudication information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

