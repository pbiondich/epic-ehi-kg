# TIMEOUT

> This table stores basic information about the timeout or Procedure Pass. For timeouts: The answers to the timeout questions, comments, procedure info, verification info and staff info can be found in tables that start with the TIMEOUT_ prefix. For Procedure Passes: the task information, review status, checkpoints, and other information can be found in tables that start with the PXPASS_ prefix.

**Primary key:** `TIMEOUT_ID`  
**Columns:** 25  
**Org-specific columns:** 2  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TIMEOUT_ID` | NUMERIC | PK | The unique identifier for the timeout record for this row. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_CSN` | NUMERIC | FK→ | A serial number for the encounter in which the alert was fired. This number is unique across all patients and encounters in the system. |
| 5 | `TIMEOUT_TYPE_C_NAME` | VARCHAR | org | Stores the type of timeout. |
| 6 | `RECORD_CREATION_DT` | DATETIME |  | Stores the date the record was created. |
| 7 | `ATTEST_TYPE_C_NAME` | VARCHAR | org | Stores the type of attestation performed. |
| 8 | `VERIF_CLASS_C_NAME` | VARCHAR |  | The type of verification data this record will have. |
| 9 | `STORYBOARD_ID` | NUMERIC |  | The storyboard record that was used to document the intervention that the timeout record is associated with. |
| 10 | `STORYBOARD_ID_RECORD_NAME` | VARCHAR |  | The name of the Scripting Template. |
| 11 | `UNVERIFY_PERF_DTTM` | DATETIME (UTC) |  | The instant an unverified timeout is performed. When the timeout is verified, the instant it is performed will be stored in VERIFY_PERF_IN_DTTM column of TIMEOUT_VERIFY table. |
| 12 | `LAST_COMPLETE_DTTM` | DATETIME (UTC) |  | This item keeps track of the date and time when the screening form is completed |
| 13 | `PXPASS_TARGET_DTTM` | DATETIME (Local) |  | The scheduled start instant of the target case or appointment associated with the Procedure Pass. |
| 14 | `TXP_DONOR_RQG_ID` | NUMERIC |  | Stores the donor record for the organ check-in. |
| 15 | `TXP_DONOR_VEL_ID` | NUMERIC |  | Stores the donor organ for an organ check-in. |
| 16 | `TXP_DONOR_VEL_ID_RECORD_NAME` | VARCHAR |  | Stores record name (.2) |
| 17 | `TXP_DONOR_OPO_ORG_C_NAME` | VARCHAR |  | The United Network for Organ Sharing (UNOS) and Organ Procurement Operations (OPO)-defined organ type that was checked in. |
| 18 | `PXPASS_EPISODE_ID` | NUMERIC |  | The episode that the procedure pass links to. This will be set for episode-based procedure passes, which are used for linking episode-based tasks to documentation that can complete the task. |
| 19 | `SMARTFORM_ID` | VARCHAR |  | The SmartForm used when creating this timeout. |
| 20 | `SMARTFORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 21 | `PRIMARY_PXPASS_ID` | NUMERIC |  | The primary Procedure Pass. |
| 22 | `PAT_ABO` | VARCHAR |  | This item stores the blood type of the patient associated with this verification. |
| 23 | `PAT_ABO_RESULT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the resulted instant of the blood type result for the patient associated with this verification. |
| 24 | `PAT_UNOSID` | VARCHAR |  | Stores the patient's UNOS ID. |
| 25 | `HAS_PAT_INFO_YN` | VARCHAR |  | This item stores if patient information was discretely stored with this verification. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [PAT_TIMEOUT](PAT_TIMEOUT.md) | `TIMEOUT_ID` | high |
| [TIMEOUT_AIRWAY_REVIEWED](TIMEOUT_AIRWAY_REVIEWED.md) | `TIMEOUT_ID` | high |
| [TIMEOUT_SED_PLAN_VERIFIED](TIMEOUT_SED_PLAN_VERIFIED.md) | `TIMEOUT_ID` | high |

