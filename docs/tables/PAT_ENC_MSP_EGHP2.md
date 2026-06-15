# PAT_ENC_MSP_EGHP2

> This table contains the Secondary Employer Group Health Plan Info part of the Medicare Secondary Payor Information from the Patient (EPT) master file. Some questionnaires use this as the spouse's EGHP info rather than the 'secondary' EGHP info.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 24  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date (calendar format) on which the encounter took place. |
| 3 | `OTHER_EGHP_YN` | VARCHAR | org | YES if the patient is covered by another employer group health plan (EGHP) in addition to the one listed under Primary EGHP. |
| 4 | `EGHP_EMPLOYEE_NAME` | VARCHAR |  | Name of the person whose employer group health plan (EGHP) covers the patient. |
| 5 | `OTHR_EGHP_REL_C_NAME` | VARCHAR | org | The coverage subscriber's relationship to the patient. |
| 6 | `OTHR_EGHP_PCP` | VARCHAR |  | Name of the patient's Primary Care Provider. |
| 7 | `OTH_EGHP_EMPL_NAME` | VARCHAR |  | The employer that sponsors the employer group health plan (EGHP). |
| 8 | `OTH_EGHP_EMPL_PHON` | VARCHAR |  | The employer's phone number. |
| 9 | `OTH_EGHP_EMPL_AD_1` | VARCHAR |  | Secondary employer group health plan (EGHP) address line 1. |
| 10 | `OTH_EGHP_EMPL_AD_2` | VARCHAR |  | Secondary employer group health plan (EGHP) address line 2. |
| 11 | `OTH_EGHP_EMPL_CITY` | VARCHAR |  | Secondary employer group health plan (EGHP) subscriber's employer city. |
| 12 | `OTH_EGHP_EMPL_ZIP` | VARCHAR |  | Secondary employer group health plan (EGHP) subscriber's employer zip |
| 13 | `OTH_EGHP_INSR_COMP` | VARCHAR |  | Name of the secondary employer group health plan (EGHP). |
| 14 | `OTH_CVG_HMO_YN` | VARCHAR | org | YES if coverage is an HMO. |
| 15 | `OTH_EGHP_POLCY_NUM` | VARCHAR |  | Patient's member number for the secondary employer group health plan (EGHP). |
| 16 | `OTH_EGHP_GROUP_NUM` | VARCHAR |  | Group number of the secondary employer group health plan (EGHP). |
| 17 | `OTH_EGHP_INSR_AD_1` | VARCHAR |  | Secondary employer group health plan (EGHP) address line 1. |
| 18 | `OTH_EGHP_INSR_AD_2` | VARCHAR |  | Secondary employer group health plan (EGHP) address line 2. |
| 19 | `OTH_EGHP_INSR_CITY` | VARCHAR |  | Secondary employer group health plan (EGHP) city. |
| 20 | `OTH_EGHP_INSR_ZIP` | VARCHAR |  | Secondary employer group health plan (EGHP) Zip. |
| 21 | `OTH_EGHP_20_EMP_YN` | VARCHAR |  | Does the employer that sponsors this group health plan have 20 or more employees? |
| 22 | `OTH_EGHP_100_EMP_YN` | VARCHAR |  | Does the employer that sponsors this group health plan have 100 or more employees? |
| 23 | `OTH_EGHP_BEN_PKG` | VARCHAR |  | The benefit package number or policy ID number for the employer group health plan. |
| 24 | `OTH_EGHP_CUR_EMP_YN` | VARCHAR |  | Yes if the employer group health plan is through the subscriber's current employment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

