# MPPS_EXPO_DOSE_SEQ

> This table contains radiation exposure dose sequence data received from Modality Performed Procedure Step (MPPS) or Radiation Dose Structured Reporting (RDSR) messages. Each MPPS message contains radiation exposure information corresponding to one performed procedure step. Each performed procedure step may, however, consist of multiple slices depending on the sophistication of the modality. Each such slice of radiation exposure administered on the patient is recorded as a separate radiation exposure dose sequence in the MPPS message. Similarly one RDSR message may contain radiation exposure information from multiple irradiation events. Each row in this table will correspond to a slice of radiation exposure information from an MPPS message or an irradiation event from an RDSR.

**Primary key:** `IMY_ID`, `LINE`  
**Columns:** 23  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IMY_ID` | NUMERIC | PK shared | The unique identifier for the modality data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `KVP` | NUMERIC |  | Peak kilo voltage output of the x-ray generator used during the current exposure dose sequence. It holds an average value in the case of fluoroscopy (continuous radiation mode). |
| 4 | `XRAY_TUBE_CURRENT` | NUMERIC |  | The current in the x-ray tube measured in µA during the current radiation exposure dose sequence. This holds an average value in the case of fluoroscopy (continuous radiation mode). |
| 5 | `EXPOSURE_TIME` | NUMERIC |  | Time of x-ray exposure or fluoroscopy in milliseconds for the current exposure dose sequence. |
| 6 | `FILTER_TYPE` | VARCHAR |  | Type of filters inserted into the x-ray beam during the current exposure dose sequence. |
| 7 | `SEQ_COMMENTS` | VARCHAR |  | User-defined comments on any special conditions related to radiation dose encountered during the episode described by the current exposure dose sequence. |
| 8 | `RADIATION_MODE` | VARCHAR |  | Specifies x-ray radiation mode during the current exposure dose sequence. |
| 9 | `SEQ_CTDIVOL` | NUMERIC |  | Computed Tomography Dose Index (CTDIvol) in mGy. It describes the average dose for this image during the current exposure dose sequence for the selected CT conditions of operation. |
| 10 | `SEQ_DLP` | NUMERIC |  | Dose Length Product (DLP) for the current exposure dose sequence. |
| 11 | `RDSR_TARGET_REGN_C_NAME` | VARCHAR | org | The anatomical region category ID for the target region of the DICOM instance record. |
| 12 | `RDSR_ACQUISTN_TYP_C_NAME` | VARCHAR | org | The acquisition type category ID for the DICOM instance record. |
| 13 | `RDSR_PROC_CONTEXT_C_NAME` | VARCHAR | org | The procedure context category ID for the DICOM instance record. |
| 14 | `RDSR_IRRADIATN_UID` | VARCHAR |  | The order instance of the irradiation event. |
| 15 | `RDSR_SCANG_LENGTH` | NUMERIC |  | The scanning length. |
| 16 | `RDSR_SINGLE_COLLIMATION_WIDTH` | NUMERIC |  | The single collimation width. |
| 17 | `RDSR_TOTAL_COLLIMATION_WIDTH` | NUMERIC |  | The total collimation width. |
| 18 | `RDSR_PITCH_FACTOR` | NUMERIC |  | The pitch factor. |
| 19 | `RDSR_NUM_XRAY_SRC` | INTEGER |  | The number of x-ray sources. |
| 20 | `RDSR_CTDIW_PHNTM_C_NAME` | VARCHAR | org | The CTDIW phantom type category ID for the DICOM instance record. |
| 21 | `RDSR_MSR_METHOD_C_NAME` | VARCHAR | org | The total dose measurement method category ID for a particular irradiation event DICOM instance record. |
| 22 | `RDSR_XRAY_MOD_TYPE` | VARCHAR |  | The x-ray modulation type. |
| 23 | `RDSR_EFF_DOSE` | NUMERIC |  | The effective dose for a particular irradiation event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

