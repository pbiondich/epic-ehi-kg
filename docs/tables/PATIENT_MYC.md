# PATIENT_MYC

> This table contains web-based chart system-related data items that are stored in the Patient (EPT) master file. These items generally relate to web-based chart system account activation and account status, and also include the last verification date for different types of patient information that can be verified through the web-based chart system.

**Primary key:** `PAT_ID`  
**Columns:** 25  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `PAT_ACCESS_CODE` | VARCHAR |  | The patient's current web-based chart system access code. This value is checked when a patient attempts to log in to the web-based chart system for the first time. |
| 3 | `PAT_ACCESS_CODE_TM` | DATETIME (UTC) |  | This is a timestamp indicating when the access code in field PAT_ACCESS_CODE was created. |
| 4 | `PAT_ACCESS_STAT_C_NAME` | VARCHAR |  | The access code status category number for the patient. 0 corresponds to "Not Used". 1 corresponds to "Used". |
| 5 | `MYCHART_STATUS_C_NAME` | VARCHAR |  | The web-based chart system status category number for the patient. |
| 6 | `ACCESSCODE_STAT_C_NAME` | VARCHAR |  | The access code generation status category number for the patient. |
| 7 | `DEACT_ACCT_YN` | VARCHAR |  | Indicates whether the patient's web-based chart system account is deactivated. Y indicates that the account is deactivated. N or a null value indicates that the account is active. |
| 8 | `CODE_FOR_PROXY_YN` | VARCHAR |  | Indicates whether the access code was generated for a proxy to use on behalf of the patient. Y indicates that the access code was generated. N or a null value indicates that the access code was not generated. |
| 9 | `MYCHART_EXP_DATE` | DATETIME |  | The expiration date (if one has been set) of the web-based chart system account. When this date is reached, the web-based chart system user is no longer allowed to login to the system. |
| 10 | `MYPT_ID` | VARCHAR | shared | The unique ID of the web-based chart system patient account. |
| 11 | `LAST_MERGE_FROM` | VARCHAR |  | If this patient record is the destination of a previous merging, and the source record has web-based chart system activity, then this item stores the time instant of the merging. |
| 12 | `ALT_WEBSTE_STAT_C_NAME` | VARCHAR |  | The alternate website activation status category number for the patient. |
| 13 | `MYC_PAT_TYPE_C_NAME` | VARCHAR | org | The web-based chart system patient type category number for the patient. |
| 14 | `DEM_VERIF_DT` | DATETIME |  | Date of last demographics verification by patient or his/her proxy from MyChart. |
| 15 | `INS_VERIF_DT` | DATETIME |  | Date of last insurance verification by patient or his/her proxy from MyChart |
| 16 | `R_E_L_PAT_VERIF_DT` | DATETIME |  | The date when race, ethnicity, and language information was last verified by the patient online using the patient portal. |
| 17 | `PCP_PAT_VERIF_DT` | DATETIME |  | The date that patients last used Welcome to verify and/or update their primary care provider. |
| 18 | `HCA_PAT_VERIF_DT` | DATETIME |  | The date that the patient last used MyChart or Welcome to verify and/or update their health care agents. |
| 19 | `PAT_MYC3_ENR_STAT_C_NAME` | VARCHAR |  | Returns the status of enrollment in MyChart Care Companion. |
| 20 | `LAST_LABS_VIEW_DTTM` | DATETIME (Local) |  | The last time when the patient or proxies viewed patient's result list (including IP results) in MyChart. |
| 21 | `PREF_PHR_VERIF_INST_UTC_DTTM` | DATETIME (UTC) |  | The last instant that a patient's preferred pharmacies were updated or verified. |
| 22 | `PREF_PHR_VERIF_AUDIT_CONTEXT_C_NAME` | VARCHAR |  | The context of the last update or verification of a patient's preferred pharmacies. |
| 23 | `PREF_PHR_VERIF_USER_ID` | VARCHAR |  | The user that last updated or verified the patient's preferred pharmacies. |
| 24 | `PREF_PHR_VERIF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 25 | `PREF_PHR_VERIF_MYPT_ID` | VARCHAR |  | The MyChart user that last updated or verified the patient's preferred pharmacies. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

