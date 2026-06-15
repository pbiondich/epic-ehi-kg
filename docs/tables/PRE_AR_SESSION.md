# PRE_AR_SESSION

> This table stores single response items for charges. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`  
**Columns:** 37  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the temporary transaction. |
| 2 | `TX_SOURCE_C_NAME` | VARCHAR |  | The source of the charge session. |
| 3 | `LK_IN_PCONC_VAL` | VARCHAR |  | Concurrency Value locked in anesthesia charge summary. |
| 4 | `LK_IN_PCONC_USR_ID` | VARCHAR |  | The ID of the user who locked-in preconcurrency in anesthesia charge summary. |
| 5 | `LK_IN_PCONC_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `LK_IN_PCONC_IN_DTTM` | DATETIME (Local) |  | The timestamp when preconcurrency was locked in anesthesia charge summary. |
| 7 | `TREATMENT_PLAN_ID` | VARCHAR | shared | The treatment plan on the charge session. |
| 8 | `ANES_TYPE_C_NAME` | VARCHAR | org | The type category for the temporary anesthesia transaction. |
| 9 | `EMERG_STAT_YN` | VARCHAR |  | Indicates where this charge is associated with an admitted patient with an emergency status. |
| 10 | `PHYSICAL_STAT_C_NAME` | VARCHAR | org | Physical status of the patient who had the anesthesia procedure. |
| 11 | `SUP_MOD_OVRIDE_YN` | VARCHAR |  | Override the normal modifier with the modifier corresponding to a medically supervised case. |
| 12 | `ORIGINAL_CRNA_TX` | NUMERIC |  | Original CRNA transaction ID. |
| 13 | `POS_TYPE_C_NAME` | VARCHAR | org | The place of service type category ID for the temporary transaction. |
| 14 | `ACCOUNT_ID` | NUMERIC | FK→ | The unique ID of the guarantor account on the charge session. |
| 15 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient on the charge session. |
| 16 | `PERF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 17 | `BILL_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 18 | `REFERRING_PROV_ID` | VARCHAR | FK→ | The unique ID of the referral provider on the charge session. |
| 19 | `REFERRING_PROV_ID_REFERRING_PROV_NAM` | VARCHAR |  | The name of the referral source. |
| 20 | `DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 21 | `POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 22 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 23 | `LOC_ID` | VARCHAR | FK→ | The unique ID of the location on the charge session. |
| 24 | `TX_TYPE_C_NAME` | VARCHAR |  | Tells what this transaction record is used for (e.g. charge, payment, adjustment, etc...). |
| 25 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | This column contains the patient encounter serial number for the charge session. |
| 26 | `RQG_ID` | NUMERIC |  | This column contains the reference lab requisition grouper ID. |
| 27 | `ANES_SUP_UNIT_PROC_TOT_UNIT` | NUMERIC |  | The total number of units of supplemental unit procedures for this charge session. |
| 28 | `CHARGE_SLIP_NUMBER` | VARCHAR |  | This is the number used to associate PB charge sessions with encounters. |
| 29 | `DENTAL_CHARGE_TYPE_C_NAME` | VARCHAR |  | Indicates what type of dental charge it is. |
| 30 | `OVERRIDE_PAYER_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 31 | `OVERRIDE_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 32 | `ORIGINAL_HTR_ID` | NUMERIC |  | The original hospital billing transaction ID. |
| 33 | `CODED_DATE` | DATETIME |  | Coded date for charge session. |
| 34 | `SPECIMEN_ID` | VARCHAR | shared | The lab specimen ID associated with the temporary charge session. |
| 35 | `TEST_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 36 | `REFERRAL_ID` | NUMERIC | FK→ | The referral number for the referral associated to this charge. |
| 37 | `REQUISITION_ID` | NUMERIC | shared | Reference Lab Requisition ID associated with the temporary charge session. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | name_stem | high |
| `LOC_ID` | [CLARITY_LOC](CLARITY_LOC.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |
| `REFERRING_PROV_ID` | [REFERRAL_SOURCE](REFERRAL_SOURCE.md) | sole_pk | high |

