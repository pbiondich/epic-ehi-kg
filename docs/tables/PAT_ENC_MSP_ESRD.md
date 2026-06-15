# PAT_ENC_MSP_ESRD

> This table contains the ESRD (End Stage Renal Disease) part of the Medicare Secondary Payor Information from the Patient (EPT) master file.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 25  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date (calendar format) on which the encounter took place. |
| 3 | `END_STAGE_RNL_YN` | VARCHAR | org | YES if the patient is entitled to Medicare because of End Stage Renal Disease |
| 4 | `DIALYSIS_BGN_DATE` | DATETIME |  | Date when dialysis began. |
| 5 | `COORD_PERIOD_YN` | VARCHAR | org | YES if the patient is still in the coordination period. |
| 6 | `RECVG_TRNG_YN` | VARCHAR | org | YES if the patient is receiving training for self-dialysis. |
| 7 | `DIAL_TRN_BEGN_DATE` | DATETIME |  | Date when self-dialysis training began. |
| 8 | `MEDIC_INIT_ESRD_YN` | VARCHAR |  | YES if the patient's initial entitlement to Medicare was based on End Stage Renal Disease (ESRD). |
| 9 | `PART_A_EFF_DATE` | DATETIME |  | Part A effective date. |
| 10 | `RNAL_TRANSPLT_YN` | VARCHAR |  | YES if the patient has had a kidney transplant because of End Stage Renal Disease (ESRD). |
| 11 | `RNAL_TRANSPLT_DATE` | DATETIME |  | Date of the transplant. |
| 12 | `BLACK_LUNG_YN` | VARCHAR | org | YES if the patient is entitled to benefits under the Black LungProgram. |
| 13 | `BLACK_LUNG_NUM` | VARCHAR |  | Black Lung program ID number. |
| 14 | `BLCK_LUNG_COVD_YN` | VARCHAR | org | YES if the services being received are on the list of covered procedures for treatment of Black Lung. |
| 15 | `BLK_LUNG_BNFT_DATE` | DATETIME |  | Date the benefits for the Black Lung program began. |
| 16 | `PHS_YN` | VARCHAR |  | YES if the services are covered by a Public Health Service or Research Program. |
| 17 | `PHS_START_DATE` | DATETIME |  | Start date of the Public Health Service (PHS) or research program. |
| 18 | `PHS_END_DATE` | DATETIME |  | End date of the Public Health Service (PHS) or research program. |
| 19 | `PHS_PROGRM_NAME` | VARCHAR |  | Name of the Public Health Service (PHS) or research program. |
| 20 | `PHS_PROGRM_ADR_1` | VARCHAR |  | Line 1 of Public Health Service (PHS) program address. |
| 21 | `PHS_PROGRM_ADR_2` | VARCHAR |  | Line 2 of the Public Health Service (PHS) program address. |
| 22 | `PHS_PROGRM_CITY` | VARCHAR |  | City of the Public Health Service (PHS) or research program. |
| 23 | `PHS_PROGRM_ZIP` | VARCHAR |  | ZIP Code of the Public Health Service (PHS) or research program. |
| 24 | `IS_MSP_DIALYSIS_YN` | VARCHAR |  | Indicates whether the patient has received maintenance dialysis treatments. |
| 25 | `MSP_GHP_PRIOR_YN` | VARCHAR |  | MSP Item: tracks if the patient was receiving Group Health Plan (GHP) coverage prior to their coverage through Medicare. This has an influence on how the filing order is calculated after the MSPQ has been completed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

