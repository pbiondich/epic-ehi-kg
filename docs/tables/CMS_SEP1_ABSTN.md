# CMS_SEP1_ABSTN

> This table containts basic information about CMS SEP-1 abstractions.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 34  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `PAT_ID` | VARCHAR | FK→ | The associated patient's EPT .1 |
| 3 | `PAT_DATE` | DATETIME |  | The date of linked EPT contacts to this record. |
| 4 | `UNOS_STAGE_C_NAME` | VARCHAR | org | The current state of the registry record |
| 5 | `RYN_WHT_ETHNICITY_C_NAME` | VARCHAR |  | The patient's Hispanic/Latino ethnicity category ID |
| 6 | `CLINICAL_TRIAL_YN` | VARCHAR |  | Indicates whether the patient was enrolled in a clinical trial for sepsis during the hospital stay. |
| 7 | `CMS_SEX_ASGN_AT_BIRTH_C_NAME` | VARCHAR |  | The patient's sex assigned at birth category ID for the CMS SEP-1 core measure. |
| 8 | `TJC_RACE_C_NAME` | VARCHAR |  | The patient's race category ID for the CMS SEP-1 core measure. |
| 9 | `DISCH_UTC_DTTM` | DATETIME (UTC) |  | The date and time the patient was discharged from acute care, discharged as left against medical advice, or discharged as expired during this stay. |
| 10 | `TRANS_YN` | VARCHAR |  | Indicates if the patient was received as a transfer from an inpatient, outpatient. or emergency/observation department of an outside hospital or from an ambulatory surgery center (ASC). |
| 11 | `PREG_OR_POST_DLVR_YN` | VARCHAR |  | Indicates if the patient was at least 20 weeks pregnant or within three days after delivery at the instant of severe sepsis presentation. |
| 12 | `SEP_SHOCK_YN` | VARCHAR |  | Indicates the presence of septic shock. |
| 13 | `SEP_SHOCK_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time on which the final criterion was met to establish the presence of septic shock. |
| 14 | `SEVERE_SEP_YN` | VARCHAR |  | Indicates the presence of severe sepsis. |
| 15 | `SEVERE_SEP_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time on which the final criterion was met to establish the presence of severe sepsis. |
| 16 | `SEP1_FINAL_STATUS_C_NAME` | VARCHAR | org | The final measure status category ID of the SEP-1 abstraction case. |
| 17 | `SEP_SHOCK_REFUSE_YN` | VARCHAR |  | Indicates if refusal of blood draw, IV fluid administration, or vasopressor administration is documented before or within six hours after the Septic Shock Presentation Instant. |
| 18 | `SEVERE_SEP_REFUSE_YN` | VARCHAR |  | Indicates if refusal of blood draw, IV fluid administration, or vasopressor administration is documented before or within six hours after the Severe Sepsis Presentation Instant. |
| 19 | `BLD_CULT_COLL_UTC_DTTM` | DATETIME (UTC) |  | The date and time when a blood culture sample was collected. |
| 20 | `LACT_COLL_UTC_DTTM` | DATETIME (UTC) |  | The date and time an initial lactate level was collected. |
| 21 | `SEP1_LACTATE_RESULT_C_NAME` | VARCHAR | org | The initial lactate level category ID for the CMS SEP-1 core measure. |
| 22 | `RE_LACT_COLL_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time the repeat lactate level was collected. |
| 23 | `ANTIBIO_ADMIN_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time a broad spectrum or other antibiotic was started. |
| 24 | `CRYS_FLUID_ADMIN_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time on which crystalloid fluids were initiated within six hours prior through three hours after either the Initial Hypotension Instant or the Septic Shock Presentation Instant, whichever is earlier. |
| 25 | `SEP_SHOCK_PAL_CARE_YN` | VARCHAR |  | Indicates if hospice or palliative care is ordered within the specific time frame for septic shock care. |
| 26 | `SEVERE_PAL_CARE_YN` | VARCHAR |  | Indicates if hospice or palliative care is ordered before or within six hours after the presentation of severe sepsis. |
| 27 | `HYPOTN_UTC_DTTM` | DATETIME (UTC) |  | The date and time of initial hypotension in the six hours prior to or within six hours following Severe Sepsis Presentation Instant and prior to the completion of the target ordered volume of crystalloid fluids. |
| 28 | `PRST_HYPOTN_UTC_DTTM` | DATETIME (UTC) |  | The date and time of persistent hypotension following the administration of the target ordered volume of crystalloid fluids. |
| 29 | `VSPR_ADMIN_UTC_DTTM` | DATETIME (UTC) |  | The date and time at which an IV or intraosseous vasopressor was administered within the Septic Shock Presentation Instant through six hours after the Septic Shock Presentation Instant. |
| 30 | `SIRS_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time two or more SIRS criteria were met. |
| 31 | `ORGAN_DSFX_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time of evidence of organ dysfunction. |
| 32 | `SEP_DOCU_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time a physician, APN, or PA documented sepsis. |
| 33 | `RE_VOL_ASMT_UTC_DTTM` | DATETIME (UTC) |  | The earliest date and time the repeat volume status and tissue perfusion assessment was documented. |
| 34 | `BLD_DELAY_YN` | VARCHAR |  | Indicates if there was an acceptable delay in blood culture collection. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

