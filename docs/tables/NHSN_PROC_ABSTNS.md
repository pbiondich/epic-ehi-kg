# NHSN_PROC_ABSTNS

> This table contains basic information from procedure abstractions.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 36  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique identifier (.1 item) for the associated patient (EPT) record. |
| 3 | `CUR_STAT_C_NAME` | VARCHAR | org | The current status of the procedure abstraction. |
| 4 | `CUR_STAT_USER_ID` | VARCHAR |  | The internal ID of the user who set the current status. |
| 5 | `CUR_STAT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `CUR_STAT_DTTM` | DATETIME (UTC) |  | The instant at which the current status (RDI-10024) was set. |
| 7 | `NHSN_VERSION_C_NAME` | VARCHAR |  | The category ID for the NHSN version to use for the abstraction. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 8 | `NHSN_PROC_DT` | DATETIME |  | The date of the procedure. |
| 9 | `NHSN_PROC_DURATION_HOURS` | INTEGER |  | The hour piece of the duration of the procedure. |
| 10 | `NHSN_PROC_DURATION_MINS` | INTEGER |  | The minute piece of the duration of the procedure. |
| 11 | `NHSN_CPT_CODE` | VARCHAR |  | A procedure code associated with the procedure abstraction. This code is typically associated with a procedure (EAP) record. For NHSN procedure abstractions, this column contains the associated CPT code. |
| 12 | `NHSN_GEN_ANESTH_YN` | VARCHAR |  | Indicates whether general anesthesia was used for this operative procedure. |
| 13 | `NHSN_TRAUMA_CASE_YN` | VARCHAR |  | Indicates whether this operative procedure was performed because of blunt or penetrating traumatic injury to the patient. |
| 14 | `NHSN_SCOPE_USED_YN` | VARCHAR |  | Indicates whether this entire operative procedure was performed using a laparoscope/robotic assist. |
| 15 | `NHSN_DIABETES_YN` | VARCHAR |  | Indicates whether the patient has a diagnosis of diabetes requiring management with insulin or a non-insulin anti-diabetic agent. |
| 16 | `NHSN_HEIGHT` | NUMERIC |  | The patient's most recent height documented in the medical record in inches (in) prior to this operative procedure. |
| 17 | `NHSN_WEIGHT` | NUMERIC |  | The patient's most recent weight documented in the medical record in ounces (oz) prior to this operative procedure. |
| 18 | `NHSN_OUTPAT_YN` | VARCHAR |  | Indicates whether the operative procedure was performed on an NHSN Outpatient. |
| 19 | `NHSN_WOUND_CLASS_C_NAME` | VARCHAR |  | The wound classification category ID for the operative procedure. |
| 20 | `NHSN_ASA_SCORE_C_NAME` | VARCHAR |  | The ASA classification category ID for the operative procedure. |
| 21 | `NHSN_EMERG_YN` | VARCHAR |  | Indicates whether the operative procedure was a non-elective, unscheduled operative procedure. |
| 22 | `NHSN_CLOSURE_TECH_C_NAME` | VARCHAR |  | The closure technique category ID for the operative procedure. |
| 23 | `NHSN_SPINAL_LVL_C_NAME` | VARCHAR |  | The spinal fusion level category ID for the operative procedure. |
| 24 | `NHSN_SPINAL_TECH_C_NAME` | VARCHAR |  | The spinal fusion technique category ID for the operative procedure. |
| 25 | `NHSN_PROST_TYPE_C_NAME` | VARCHAR |  | The prosthesis type category ID for the operative procedure. |
| 26 | `NHSN_SURGEON_CODE` | VARCHAR |  | The code of the surgeon who performed the principal operative procedure. |
| 27 | `LOG_ID` | VARCHAR | shared | The unique identifier of the surgical log (ORL .1) associated with the procedure abstraction. |
| 28 | `NHSN_LABOR_DURATION` | INTEGER |  | The number of hours the patient was in labor in the hospital. |
| 29 | `NHSN_JOINT_INFECTION_YN` | VARCHAR |  | Stores whether the prosthesis is associated with an infection at the index joint. |
| 30 | `NHSN_OR_LOG_PANEL_C_NAME` | VARCHAR |  | The panel number from the OR log used to create an NHSN procedure abstraction. |
| 31 | `NHSN_ICD_PROC_ID` | VARCHAR |  | The unique ID of the HCD record representing a procedure code associated with the abstraction. For NHSN procedure abstractions, this is an ICD code. |
| 32 | `NHSN_ICD_PROC_ID_ICD_PX_NAME` | VARCHAR |  | The name of the ICD procedure record. |
| 33 | `HOW_CREATED_C_NAME` | VARCHAR |  | The category ID for the method used to create the procedure abstraction. |
| 34 | `ASSOCIATED_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 35 | `NHSN_ADMISSION_DT` | DATETIME |  | The date the patient was admitted for the purpose of submission to the CDC. |
| 36 | `ASSOC_RPT_HOSP_REGULATORY_ID_CMS_MU_NAME` | VARCHAR |  | The name of the CMS Meaningful Use record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

