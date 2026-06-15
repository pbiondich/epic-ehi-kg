# CL_RMT_PRV_SUP_INF

> This table contains the provider supplemental summary information for the remittance record.

**Primary key:** `IMAGE_ID`  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMAGE_ID` | VARCHAR | PK shared | This is the ID for the remittance image record with related remit claim references. |
| 2 | `TOT_DRG_AMT` | NUMERIC |  | This is the total diagnosis related group amount for the remittance record. |
| 3 | `FED_AMT` | NUMERIC |  | This is the total federal-specific amount for the remittance record. |
| 4 | `HOSP_AMT` | NUMERIC |  | This is the total hospital-specific amount for the remittance record. |
| 5 | `DISP_SHARE_AMT` | NUMERIC |  | This is the total disproportionate share amount for the remittance record. |
| 6 | `TOT_CAP_AMT` | NUMERIC |  | This is the total capital amount for the remittance record. |
| 7 | `MED_EDU_AMT` | NUMERIC |  | This is the total indirect medical education amount for the remittance record. |
| 8 | `TOT_OUT_DAY_CNT` | NUMERIC |  | This is the total number of outlier days for the remittance record. |
| 9 | `DAY_OUT_AMT` | NUMERIC |  | This is the total day outlier amount for the remittance record. |
| 10 | `COST_OUT_AMT` | NUMERIC |  | This is the total cost outlier amount for the remittance record. |
| 11 | `AVG_DRG_LEN_STAY` | INTEGER |  | This is the diagnosis related group (DRG) average length of stay for the remittance record. |
| 12 | `TOT_DISCHARGE_CNT` | INTEGER |  | This is the total number of discharges for the remittance record. |
| 13 | `COST_REP_DAY_CNT` | INTEGER |  | This is the total number of cost report days for the remittance record. |
| 14 | `CVRD_DAY_CNT` | INTEGER |  | This is the total number of covered days for the remittance record. |
| 15 | `NONCVRD_DAY_CNT` | INTEGER |  | This is the total number of non-covered days for the remittance record. |
| 16 | `MSP_PASS_THRU_AMT` | NUMERIC |  | This is the total Medicare Secondary Payer (MSP) pass- through amount calculated for a non-Medicare payer for the remittance record. |
| 17 | `AVG_DRG_WEIGHT` | NUMERIC |  | This is the average diagnosis-related group (DRG) weight for the remittance record. |
| 18 | `PPS_CAP_FSP_DRG_AM` | NUMERIC |  | This is the total prospective payment system (PPS) capital, federal-specific portion, diagnosis-related group (DRG) amount for the remittance record. |
| 19 | `PPS_CAP_HSP_DRG` | NUMERIC |  | This is the total prospective payment system (PPS) capital, hospital-specific portion, diagnosis-related group (DRG) amount for the remittance record. |
| 20 | `TOT_PPS_DSH_DRG_AM` | NUMERIC |  | This is the total prospective payment system (PPS) disproportionate share, hospital diagnosis-related group (DRG) amount for the remittance record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

