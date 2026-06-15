# UNOS_CLIN_INFO_5

> Additional information reported to the United Network for Organ Sharing (UNOS) for each of the registry records or forms.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 42  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `UNOS_TXP_TZ_C_NAME` | VARCHAR |  | The time zone in which the patient's transplant procedure took place. |
| 3 | `UNOS_TXP_DTTM` | DATETIME (Local) |  | The instant the transplant procedure took place. |
| 4 | `UNOS_LK_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the left kidney arrived at the transplant hospital. |
| 5 | `UNOS_LK_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the left kidney arrived at the transplant hospital. |
| 6 | `UNOS_LK_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the left kidney check-in date and time is blank. |
| 7 | `UNOS_RK_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the right kidney arrived at the transplant hospital. |
| 8 | `UNOS_RK_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the right kidney arrived at the transplant hospital. |
| 9 | `UNOS_RK_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the right kidney check-in date and time is blank. |
| 10 | `UNOS_BK_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the en bloc kidneys arrived at the transplant hospital. |
| 11 | `UNOS_BK_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the en bloc kidneys arrived at the transplant hospital. |
| 12 | `UNOS_BK_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the en bloc kidneys check-in date and time is blank. |
| 13 | `UNOS_P_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the pancreas arrived at the transplant hospital. |
| 14 | `UNOS_P_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the pancreas arrived at the transplant hospital. |
| 15 | `UNOS_P_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the pancreas check-in date and time is blank. |
| 16 | `UNOS_L_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the liver arrived at the transplant hospital. |
| 17 | `UNOS_L_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the liver arrived at the transplant hospital. |
| 18 | `UNOS_L_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the liver check-in date and time is blank. |
| 19 | `UNOS_H_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the heart arrived at the transplant hospital. |
| 20 | `UNOS_H_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the heart arrived at the transplant hospital. |
| 21 | `UNOS_H_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the heart check-in date and time is blank. |
| 22 | `UNOS_LL_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the left lung arrived at the transplant hospital. |
| 23 | `UNOS_LL_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the left lung arrived at the transplant hospital. |
| 24 | `UNOS_LL_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the left lung check-in date and time is blank. |
| 25 | `UNOS_RL_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the right lung arrived at the transplant hospital. |
| 26 | `UNOS_RL_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the right lung arrived at the transplant hospital. |
| 27 | `UNOS_RL_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the right lung check-in date and time is blank. |
| 28 | `UNOS_BL_CHKIN_DTTM` | DATETIME (Local) |  | The date and time the en bloc lungs arrived at the transplant hospital. |
| 29 | `UNOS_BL_CHKIN_TZ_C_NAME` | VARCHAR |  | The time zone in which the en bloc lungs arrived at the transplant hospital. |
| 30 | `UNOS_BL_CHKIN_ST_C_NAME` | VARCHAR |  | The reason the en bloc lungs check-in date and time is blank. |
| 31 | `UNOS_KI_FAIL_TRR_C_NAME` | VARCHAR |  | The primary reason for the transplant patient's kidney graft failure for TRFs. Submitted to UNOS for field name grf_fail_cause_ty. |
| 32 | `SRTR_SODIUM` | NUMERIC |  | The transplant patient's serum sodium in mg/dl, as used to calculate MELD. Used to calculate SRTR metrics. |
| 33 | `SRTR_BMI` | NUMERIC |  | The patient's BMI. Used to calculate SRTR metrics. |
| 34 | `SRTR_CPRA` | INTEGER |  | The transplant candidate's cPRA score. Used to calculate SRTR metrics. |
| 35 | `SRTR_YRS_WITH_ESRD` | INTEGER |  | Years since the patient initially developed ESRD. Used for calculating kidney SRTR metrics. |
| 36 | `SRTR_ASCITES_C_NAME` | VARCHAR | org | Clinical findings of ascites, as defined by UNOS. Used to calculate SRTR metrics. |
| 37 | `SRTR_RCNT_DIAL_YN` | VARCHAR |  | Whether the patient had dialysis twice in the last week. Used for SRTR Liver metric calculations. |
| 38 | `SRTR_ENCEPH_C_NAME` | VARCHAR | org | Clinical findings of encephalopathy, as defined by UNOS. Used to calculate SRTR metrics. |
| 39 | `SRTR_HAS_EXCEPT_YN` | VARCHAR |  | Whether the patient had a MELD Exception. Used to calculate SRTR liver metrics. |
| 40 | `SRTR_MELD_AT_LISTING` | INTEGER |  | The patient's lab MELD as of listing, or in the case of pre-waitlist patients, the most recent lab MELD. Used for SRTR liver pre-transplant metrics. |
| 41 | `SRTR_PREEMPTIVE_YN` | VARCHAR |  | Whether the patient was preemptively listed. Used for calculating SRTR kidney metrics. |
| 42 | `UNOS_KP_OP_TECH_C_NAME` | VARCHAR |  | Shows the operative technique used during the kidney/pancreas transplant procedure. Submitted to UNOS for KPRR field name oper_tech. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

