# ALERT

> The ALERT table contains one record for every alert that was created in Hyperspace. Each record is based on the alert ID and contains key information about the alert such as the patient, patient CSN, alert type, and whether it was seen by a user.

**Primary key:** `ALT_ID`  
**Columns:** 22  
**Org-specific columns:** 1  
**Joined by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALT_ID` | NUMERIC | PK | The unique identifier for the alert. |
| 2 | `ALERT_DESC` | VARCHAR |  | A brief description of the alert. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique patient ID of the patient for whom the alert fired. You could link it to PATIENT.PAT_ID to get patient specific information. |
| 4 | `PAT_CSN` | NUMERIC | FK→ | The contact serial number for the patient encounter in which the alert was fired. This number is unique across all patients and encounters in your system. If alerts are triggered in a patient-specific encounter, they are saved in a corresponding encounter. This can be used to join to PAT_ENC.PAT_ENC_CSN_ID to get the encounter information. |
| 5 | `PUMP_ID` | VARCHAR |  | The unique external device ID of the pump selected in response to the warning after trying to program the pump. |
| 6 | `PUMP_ID_DEVICE_NAME` | VARCHAR |  | The name for this device. |
| 7 | `MAR_ACTION_C_NAME` | VARCHAR | org | The MAR action category ID selected in response to the warning after trying to program the pump. |
| 8 | `MED_ALERT_SUBTYPE_C_NAME` | VARCHAR |  | Subtype of medication alert type. This is currently used only for alerts of type 23 - Error while checking interactions |
| 9 | `NBA_LOCATOR_ID_LOCATOR_NAME` | VARCHAR |  | The name of the Locator record. |
| 10 | `NBA_GUARANTOR_ACCT_ID` | NUMERIC |  | The guarantor account correlated with this next best action event. |
| 11 | `NBA_PROSPECT_RECORD_ID` | NUMERIC |  | The prospective patient correlated with this next best action event. |
| 12 | `BLOOD_ALERT_BUCKET_C_NAME` | VARCHAR |  | The blood alert bucket category ID for the alert. |
| 13 | `RECORD_STATUS_C_NAME` | VARCHAR |  | This column contains a record status flag of soft deleted, hidden, or hidden and soft deleted. Use it in conjunction with the record archived flag (REC_ARCHIVED_YN) for encounter archiving. |
| 14 | `EXPECTED_WKFL_ACTVTIES_C_NAME` | VARCHAR |  | The activity which triggered the warning. Only used when the warning type is Expected Workflow Step Not Complete. |
| 15 | `HM_TOPIC_ID` | NUMERIC | FK→ | This column contains the ID of the Health Maintenance topic correlated with this alert record. |
| 16 | `HM_TOPIC_ID_NAME` | VARCHAR |  | The name of the health maintenance topic. |
| 17 | `SVV_LEAF_LPP_ID` | NUMERIC |  | Stores the Extension ID of the record that generated the Sign Visit Validation message, if the message came from an extension. |
| 18 | `SVV_LEAF_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 19 | `SVV_PROFILE_LPP_ID` | NUMERIC |  | Stores the Extension ID listed in the user's profile that resulted in this Sign Visit Validation message. This is only saved if it is different than the value in item 41000. |
| 20 | `SVV_PROFILE_LPP_ID_LPP_NAME` | VARCHAR |  | The name of the extension. |
| 21 | `SVV_RULE_ID` | VARCHAR |  | Stores the Rule (CER) ID if this Sign Visit Validation is based on a rule record. |
| 22 | `SVV_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `HM_TOPIC_ID` | [CLARITY_HM_TOPIC](CLARITY_HM_TOPIC.md) | sole_pk | high |
| `PAT_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (7)

| From | Column | Confidence |
|------|--------|------------|
| [ALT_ALLERGY_REACT](ALT_ALLERGY_REACT.md) | `ALT_ID` | high |
| [ALT_CLINIC_EFFECT](ALT_CLINIC_EFFECT.md) | `ALT_ID` | high |
| [ALT_DRUG_DOSE_RSN](ALT_DRUG_DOSE_RSN.md) | `ALT_ID` | high |
| [ALT_HISTORY](ALT_HISTORY.md) | `ALT_ID` | high |
| [ALT_HISTORY_2](ALT_HISTORY_2.md) | `ALT_ID` | high |
| [ALT_HISTORY_3](ALT_HISTORY_3.md) | `ALT_ID` | high |
| [ALT_ORDINFO](ALT_ORDINFO.md) | `ALT_ID` | high |

