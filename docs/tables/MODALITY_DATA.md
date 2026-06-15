# MODALITY_DATA

> This table contains basic information about imaging data from the performing modality. It also contains cumulative radiation dose information.

**Primary key:** `IMY_ID`  
**Columns:** 26  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the modality data record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record to which the modality data pertains. |
| 3 | `SOP_INSTANCE_UID` | VARCHAR |  | The DICOM SOP Instance unique identifier of the message from modality. This ID is uniquely assigned for every image in a study. |
| 4 | `AET_FDD_ID` | NUMERIC |  | The unique ID of the Application Entity Title record from the FDD master file which specifies DICOM definitions for the performing modality. |
| 5 | `AET_FDD_ID_DICOM_NAME` | VARCHAR |  | The name of an Application Entity (modality). This is not the AE Title. |
| 6 | `PPS_STATUS_C_NAME` | VARCHAR |  | The PPS status category ID for the DICOM instance record. |
| 7 | `PPS_START_DTTM` | DATETIME (Local) |  | The DICOM Performed Procedure Step Start Date and Time. |
| 8 | `PPS_END_DTTM` | DATETIME (Local) |  | The DICOM Performed Procedure Step End Date and Time. |
| 9 | `SOP_CLASS_FDD_ID` | NUMERIC |  | The DICOM SOP Class of the message from the performing modality. DICOM capabilities are all expressed as Service-Object Pair Classes, identified by SOP Class names and unique identifiers. |
| 10 | `SOP_CLASS_FDD_ID_DICOM_NAME` | VARCHAR |  | The name of an Application Entity (modality). This is not the AE Title. |
| 11 | `RDSR_MFR` | VARCHAR |  | The manufacturer of the machine sending the data. |
| 12 | `RDSR_MFR_MODEL_NAME` | VARCHAR |  | The model name of the machine sending the data. |
| 13 | `RDSR_STATION_NAME` | VARCHAR |  | The station sending the data. |
| 14 | `RDSR_PROC_RPTD_C_NAME` | VARCHAR |  | The procedure reported category ID for the procedure reported to be performed for the DICOM instance record. |
| 15 | `RDSR_IRRD_STRT_DTTM` | DATETIME (Local) |  | The start time of irradiation. |
| 16 | `RDSR_IRRD_STOP_DTTM` | DATETIME (Local) |  | The end time of irradiation. |
| 17 | `RDSR_SCP_ACCUMLTN_C_NAME` | VARCHAR | org | The scope of accumulation category ID for the DICOM instance record. |
| 18 | `RDSR_TOTAL_EFF_DOSE` | NUMERIC |  | The aggregate effective dose. |
| 19 | `RDSR_TTL_MSR_MTHD_C_NAME` | VARCHAR | org | The total dose measurement method category ID for the DICOM instance. |
| 20 | `RDSR_PAT_MODEL` | VARCHAR |  | The effective does patient model. |
| 21 | `RDSR_REF_AUTH` | VARCHAR |  | The effective dose reference authority. |
| 22 | `RDSR_TTL_DOSE_PHNTM` | VARCHAR |  | The total effective dose phantom type. |
| 23 | `RDSR_DOSIMETER_TYPE` | VARCHAR |  | The total effective dose dosimeter type. |
| 24 | `RDSR_DOSE_CMT` | VARCHAR |  | The comment associated with the accumulated radiation dose. |
| 25 | `RDSR_PROC_INTENT_C_NAME` | VARCHAR | org | The procedure intent category ID for the DICOM instance record. |
| 26 | `PPS_DESC` | VARCHAR |  | The DICOM Performed Procedure Step Description. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

