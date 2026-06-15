# MDS_RECS

> This table contains data on Minimum Data Set (MDS) assessments. An MDS assessment is represented by a Registry Data (RDI) record with a Registry Type (I RDI 26) value of Minimum Data Set.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 41  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | This column stores the record status (hidden, soft-deleted, etc.). |
| 3 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | This column stores the type of registry. |
| 4 | `PAT_ID` | VARCHAR | FK→ | This column contains the associated patient's ID (EPT .1). |
| 5 | `ARD_TARGET_DATE` | DATETIME |  | This column contains the Target Date or Assessment Reference Date. |
| 6 | `CUR_STAT_C_NAME` | VARCHAR | org | This column indicates the current state of the RDI record. |
| 7 | `MDS_REC_TYPE_C_NAME` | VARCHAR |  | This column indicates what type of record (A0050) the MDS represents. |
| 8 | `OBRA_TYPE_C_NAME` | VARCHAR |  | The MDS record's type of OBRA assessment. (RDI 35010) - A0310A. |
| 9 | `PPS_TYPE_C_NAME` | VARCHAR |  | The MDS record's type of PPS Assessment (RDI 35011) - MDS A0310B. |
| 10 | `OMRA_TYPE_C_NAME` | VARCHAR |  | The MDS record's type of PPS OMRA reason for assessment (RDI 35012) - A0310C. |
| 11 | `MDS_REQT_C_NAME` | VARCHAR |  | This column indicates who requires the submission of this assessment (MDS A0410) - whether it is a federal required submission, state but not federal required submission, or neither federal nor state required submission. |
| 12 | `ENTRY_DISCHRG_C_NAME` | VARCHAR |  | This column indicates the kind of tracking record this MDS record serves as. |
| 13 | `PREV_CORR_ARD_DT` | DATETIME |  | This column indicates the ARD of the assessment to be corrected. |
| 14 | `PART_A_HIPPS` | VARCHAR |  | This column contains the HIPPS code for Medicare Part A. |
| 15 | `PART_A_RUG_VER` | VARCHAR |  | This column contains the version code used for MDS Z0100A. |
| 16 | `PART_A_SHORT_STAY_YN` | VARCHAR |  | This column indicates whether or not this is a Medicare Short Stay assessment. |
| 17 | `PART_A_NT_HIPPS` | VARCHAR |  | This column contains the HIPPS code for Medicare Part A non-therapy. |
| 18 | `PART_A_NT_RUG_VER` | VARCHAR |  | This column contains the version code used for MDS Z0150A. |
| 19 | `STATE_RUG_CASE_GRP` | VARCHAR |  | This column contains the RUG Case Mix group for state Medicaid billing. |
| 20 | `STATE_RUG_VER` | VARCHAR |  | This column contains the Version code used for MDS Z0200A. |
| 21 | `ALT_STATE_RUG_GRP` | VARCHAR |  | This column contains the RUG Case Mix group for alternate state Medicaid billing on an MDS assessment. |
| 22 | `ALT_STATE_RUG_VER` | VARCHAR |  | This column contains the version code used for MDS Z0250A. |
| 23 | `INSURANCE_RUG_CODE` | VARCHAR |  | This column contains the RUG billing code used for a private payor. |
| 24 | `INSURANCE_RUG_VER` | VARCHAR |  | This column contains the version code used for MDS Z0300A. |
| 25 | `CAA_SIG_USER_ID` | VARCHAR |  | This column contains the ID of the RN coordinator who signed for the Care Area Assessment process. |
| 26 | `CAA_SIG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 27 | `CAA_SIG_DTTM` | DATETIME (Attached) |  | This column contains the date of the signature in MDS V0200B1. |
| 28 | `CARE_PLAN_SIG_USER_ID` | VARCHAR |  | This column contains the ID of the individual who signed for completing care plan decisions. |
| 29 | `CARE_PLAN_SIG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `CARE_PLAN_SIG_DTTM` | DATETIME (Attached) |  | This column contains the instant of the signature in MDS V0200C1. |
| 31 | `CORR_RN_AC_SIG_USER_ID` | VARCHAR |  | This column contains the ID of the RN assessment coordinator attesting to the completion of the correction record. |
| 32 | `CORR_RN_AC_SIG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 33 | `CORR_RN_AC_SIG_DTTM` | DATETIME (Attached) |  | This column contains the instant of the signature in MDS X1100D. |
| 34 | `MDS_ASSESS_INDIC_C_NAME` | VARCHAR |  | This column contains the assessment indicator. |
| 35 | `RN_AC_COMP_SIG_DTTM` | DATETIME (Attached) |  | This column contains the date of the signature in MDS Z0500A. |
| 36 | `RN_AC_COMP_SIG_USER_ID` | VARCHAR |  | This column contains the ID of the RN assessment coordinator verifying assessment completion. |
| 37 | `RN_AC_COMP_SIG_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 38 | `MDS_REGION_C_NAME` | VARCHAR |  | Stores which region the MDS applies to as documented in the Resident's State field in Section S. |
| 39 | `PPS_DISCHRG_YN` | VARCHAR |  | Stores the value of MDS item A0310H which indicates whether the MDS is a SNF PPS Part A Discharge (End of Stay) assessment |
| 40 | `MDS_OPT_STATE_ASMT_YN` | VARCHAR |  | A0300A |
| 41 | `MDS_STATE_ASMT_TYPE_C_NAME` | VARCHAR |  | Current value of MDS A0300B - State Payment Assessment Type |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

