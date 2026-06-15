# PAT_ENC_MSP_EGHP

> This table contains the Primary Employer Group Health Plan Info part of the Medicare Secondary Payor Information from the Patient (EPT) master file. Some questionnaires use this as the patient's EGHP info rather than the 'primary' EGHP info.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 25  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | A unique serial number for this encounter. This number is unique across all patients and encounters in the system. |
| 2 | `CONTACT_DATE` | DATETIME |  | The date (calendar format) on which the encounter took place. |
| 3 | `SELF_EGHP_YN` | VARCHAR | org | YES if the patient has employer group health plan (EGHP) coverage based on own or a family member's current or former employment. |
| 4 | `OTHER_EGHP_YN` | VARCHAR | org | YES if the patient is covered by another employer group health plan (EGHP) in addition to the one listed under Primary EGHP. |
| 5 | `EGHP_INSURED_NAME` | VARCHAR |  | Name of the person whose employer group health plan (EGHP) covers the patient. |
| 6 | `EGHP_REL_SUBSCRB_C_NAME` | VARCHAR | org | Relationship of the subscriber to the patient. |
| 7 | `EGHP_PCP` | VARCHAR |  | Name of the patient's Primary Care Provider. |
| 8 | `EGHP_EMPLOYER_NAME` | VARCHAR |  | The employer that sponsors the employer group health plan (EGHP). |
| 9 | `EGHP_EMPL_ADR_1` | VARCHAR |  | Employer group health plan (EGHP) subscriber's employer address line 1. |
| 10 | `EGHP_EMPL_ADR_2` | VARCHAR |  | Employer group health plan (EGHP) subscriber's employer address line 2. |
| 11 | `EGHP_EMPL_PHONE` | VARCHAR |  | Employer group health plan (EGHP) subscriber's employer phone number. |
| 12 | `EGHP_EMPL_CITY` | VARCHAR |  | Employer group health plan (EGHP) subscriber's employer city. |
| 13 | `EGHP_EMPL_ZIP` | VARCHAR |  | Employer group health plan (EGHP) subscriber's employer zip |
| 14 | `EGHP_INSUR_COMPANY` | VARCHAR |  | Name of the employer group health plan (EGHP). |
| 15 | `CVG_HMO_YN` | VARCHAR | org | YES if coverage is an HMO. |
| 16 | `EGHP_POLICY_NUMBER` | VARCHAR |  | Patient's member number for the employer group health plan (EGHP). |
| 17 | `EGHP_GROUP_NUMBER` | VARCHAR |  | Group number of the employer group health plan (EGHP). |
| 18 | `EGHP_INSUR_ADR_1` | VARCHAR |  | Employer group health plan (EGHP) address line 1. |
| 19 | `EGHP_INSUR_ADR_2` | VARCHAR |  | Employer group health plan (EGHP) address line 2. |
| 20 | `EGHP_INSUR_CITY` | VARCHAR |  | Employer group health plan (EGHP) city. |
| 21 | `EGHP_INSUR_ZIP` | VARCHAR |  | Employer group health plan (EGHP) Zip. |
| 22 | `EGHP_PAT_SUP_INF_C` | VARCHAR |  | Used to store whether or not the patient refused to provide information pertaining to the MSPQ EGHP question. |
| 23 | `EGHP_BEN_PKG` | VARCHAR |  | The benefit package number or policy ID number for the employer group health plan. |
| 24 | `EGHP_CUR_EMPL_YN` | VARCHAR |  | Yes if the employer group health plan is through the subscriber's current employment. Some questionnaires use this instead of Covered by Employer Group Health Plan (I EPT 4672). |
| 25 | `MSP_SELF_NUMBER_EMPLOYEES_C_NAME` | VARCHAR |  | MSP Item: tracks the number of employees of the patient's GHP provider |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

