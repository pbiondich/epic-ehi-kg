# HV_ORDER_PROC

> This table contains data on order procedures related to a hospital visit.

**Primary key:** `ORDER_PROC_ID`  
**Columns:** 54  
**Org-specific columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record. |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 4 | `DISCR_FREQ_ID` | VARCHAR |  | The discrete frequency associated with the order. |
| 5 | `DISCR_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 6 | `TRANSPORT_C_NAME` | VARCHAR | org | Determines how the patient associated with this order is to be transported. |
| 7 | `ORD_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `STAND_CNT` | INTEGER |  | The standing count for the order. |
| 9 | `STND_TP_C_NAME` | VARCHAR |  | The standing count type for the order (i.e. days, weeks, etc.) |
| 10 | `ADM_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 11 | `ADMIT_SERVICE_C_NAME` | VARCHAR | org | The admission service associated with the order. |
| 12 | `ADM_LVL_OF_CARE_C_NAME` | VARCHAR | org | The admission level of care associated with the order. |
| 13 | `ADMIT_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 14 | `ADM_COND_C_NAME` | VARCHAR | org | The admission condition associated with the order. |
| 15 | `ADMIT_LEN_STAY` | INTEGER |  | The admission expected length of stay. |
| 16 | `ADMIT_DISCHG_DATE` | DATETIME |  | The admission expected date of discharge. |
| 17 | `ADMIT_RES_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `ADM_INTRN_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 19 | `EXP_ADMIT_DT` | DATETIME |  | The expected admission date. |
| 20 | `TF_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 21 | `TRANFER_SVC_C_NAME` | VARCHAR |  | The service associated with the transfer department. |
| 22 | `TF_LVL_OF_CARE_C_NAME` | VARCHAR |  | The transfer level of care associated with the order. |
| 23 | `TRANFER_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 24 | `TRANFER_COND_C_NAME` | VARCHAR |  | The condition specified with the transfer order. |
| 25 | `TRANFER_LEN_STAY` | INTEGER |  | The expected length of stay associated with the transfer order. |
| 26 | `TRANFER_DISCHR_DT` | DATETIME |  | The expected discharge date associated with the transfer order. |
| 27 | `TRANFER_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 28 | `DCHRG_EXP_TIME` | DATETIME (Local) |  | The expected discharge date and time associated with the discharge order. |
| 29 | `DISCH_DISP_C_NAME` | VARCHAR | org | The discharge disposition associated with the discharge order. |
| 30 | `DISCH_DEST_C_NAME` | VARCHAR | org | The discharge destination associated with the discharge order. |
| 31 | `ISOLATION_C_NAME` | VARCHAR | org | The isolation status of the patient associated with the order. |
| 32 | `CODESTATUS_C_NAME` | VARCHAR | org | The code status of the patient associated with the order. |
| 33 | `DIET_C_NAME` | VARCHAR | org | The diet status of the patient associated with the order. |
| 34 | `INST_OF_UPDATE_TM` | DATETIME (Local) |  | The day and time the order record was last updated. |
| 35 | `PAT_UPD_DTTM` | DATETIME (Local) |  | The effective date and time of the patient update that should be generated from this order. |
| 36 | `PAT_UPD_PAT_CLS_C_NAME` | VARCHAR | org | The patient class of the patient update that should be generated from this order. |
| 37 | `PAT_UPD_SVC_C_NAME` | VARCHAR |  | The service of the patient update that should be generated from this order. |
| 38 | `PAT_UPD_ACCOM_CD_C_NAME` | VARCHAR | org | The accommodation code of the patient update that should be generated from this order. |
| 39 | `PAT_UPD_ACCOM_RSN_C_NAME` | VARCHAR | org | The accommodation reason of the patient update that should be generated from this order. |
| 40 | `PAT_UPD_LOC_C_NAME` | VARCHAR |  | The level of care of the patient update that should be generated from this order. |
| 41 | `PAT_UPD_RSN_C_NAME` | VARCHAR | org | The reason for change of the patient update that should be generated from this order. |
| 42 | `CONSULTANT_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 43 | `LEAVE_OF_ABSENCE_REASON_C_NAME` | VARCHAR | org | The category ID for the reason that the patient is to go on leave from the current admission. This column is only likely to be populated for Leave of Absence orders. |
| 44 | `LEAVE_OF_ABSENCE_LEAVE_DTTM` | DATETIME (Local) |  | The date and time that the patient is expected to go out on leave. This column is only likely to be populated for Leave of Absence orders. |
| 45 | `LEAVE_OF_ABSENCE_RETURN_DTTM` | DATETIME (Local) |  | The date and time that the patient is expected to return from leave. This column is only likely to be populated for Leave of Absence orders. |
| 46 | `LEAVE_OF_ABSENCE_HOLD_BED_YN` | VARCHAR |  | Whether or not the patient's current bed should be held during the upcoming leave. This column is only likely to be populated for Leave of Absence orders. |
| 47 | `DCHRG_EXP_DATE` | DATETIME |  | The expected discharge date associated with the discharge order. |
| 48 | `TRANSFER_REQUEST_TYPE_C_NAME` | VARCHAR | org | The type of transfer request being ordered. |
| 49 | `ADT_PATIENT_CLASS_C_NAME` | VARCHAR |  | Patient class used for transfer request orders. |
| 50 | `HOSP_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 51 | `TRANSFER_CENTER_REGION_ID` | NUMERIC |  | Stores the Transfer Center region. |
| 52 | `TRANSFER_CENTER_REGION_ID_RECORD_NAME` | VARCHAR |  | The name of this cleaning sector. |
| 53 | `CODE_STATUS_COMMENTS` | VARCHAR |  | The code status comments associated with the order. |
| 54 | `EXP_DIS_APPROX_TM_C_NAME` | VARCHAR | org | The approximate expected discharge time category ID for the order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

