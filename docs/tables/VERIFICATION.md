# VERIFICATION

> The VERIFICATION table contains information about your verification records. These records include verification information for patients, guarantors, coverages, coverage members, hospital accounts, and encounters.

**Primary key:** `RECORD_ID`  
**Columns:** 27  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the verification record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `VERIF_RECORD_INI` | VARCHAR |  | INI of the verified record |
| 4 | `VERIF_RECORD_IDNT` | VARCHAR |  | ID of the verified record. This item is not networked, because it can contain an EPT, EAR, CVG, or HAR ID, depending on the verification type. |
| 5 | `VERIFICATION_TYPE_C_NAME` | VARCHAR | org | The verification type of the record. This can be patient, encounter, guarantor, hospital account, coverage, or member. |
| 6 | `VERIF_STATUS_C_NAME` | VARCHAR | org | The current verification status |
| 7 | `LAST_VERIF_DATETIME` | DATETIME (UTC) |  | Date and time of the last successful verification |
| 8 | `LAST_VERIF_USER_ID` | VARCHAR |  | User who performed the most recent verification |
| 9 | `LAST_VERIF_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `NEXT_REVIEW_DATE` | DATETIME |  | The date on which the verification status needs review |
| 11 | `LAST_STAT_CHNG_DTTM` | DATETIME (UTC) |  | The date on which the status was last changed |
| 12 | `LAST_CHANGE_USER_ID` | VARCHAR |  | The user who last changed the verification status |
| 13 | `LAST_CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `ENC_PAT_ID` | VARCHAR | FK→ | ID for the patient of this encounter |
| 15 | `ENC_PAT_VERIF_ID` | NUMERIC |  | Verification record for the encounter patient |
| 16 | `ENC_CSN` | NUMERIC |  | Contact Serial Number (CSN) for the patient encounter associated with the verification. Applies to encounter and hospital account verification. |
| 17 | `ENC_GUARANTOR_ID` | NUMERIC |  | Responsible guarantor for this encounter |
| 18 | `ENC_GUAR_VERIF_ID` | NUMERIC |  | Verification record for the guarantor of this encounter |
| 19 | `ENC_GUAR_SNAPSHOT_C_NAME` | VARCHAR |  | The status of the encounter guarantor at the time the encounter was verified |
| 20 | `ENC_HOSP_ACCT_ID` | NUMERIC |  | Hospital account for this encounter |
| 21 | `ENC_HAR_VERIF_ID` | NUMERIC |  | Verification record of the hospital account for this encounter |
| 22 | `ENC_PAT_SNAPSHOT_C_NAME` | VARCHAR |  | The status of the patient at the time the encounter or hospital account was verified. |
| 23 | `VERIF_SUBTYPE_C_NAME` | VARCHAR | org | The verification subtype of the record. Subtypes can include things like address or BSN. |
| 24 | `SUB_PARENT_VRX_ID` | NUMERIC |  | The parent verification record of the subtype verification record. |
| 25 | `SUB_ORIGIN_EAF_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 26 | `LAST_SELF_VERIF_DATE` | DATETIME |  | The date on which the verification status was changed the last time by patient (using the Welcome kiosk). |
| 27 | `VERIF_RECORD_IDNT_NUMERIC` | NUMERIC |  | ID of the verified record if the record's INI has a numeric ID type, or null if the verified record's ID is a string. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENC_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

