# ALT_HISTORY

> This table contains general history information for each type of medication warning or advisory. Since each warning could be triggered in different activities at different times, it contains general warning information for each time the warning was triggered. To get patient information, link this table to the ALERT table and then link the ALERT table to the PATIENT or PAT_ENC table. To get order related information for each medication warning or advisory, link this table to ALT_ORDINFO. To get specific medication or condition information for each medication warning type, link this table to specific medication warning related tables, such as the ALT_DRUG_ALLERGY table for drug-allergy warnings; the ALT_DRUG_DFALC table for drug-drug, drug-food, and drug-alcohol warnings; the ALT_DRUG_DUPTHERPY and ALT_DRUG_DUPTHYMED tables for duplicate therapy warnings; the ALT_DRUG_IV and ALT_DRUG_IVMED tables for IV warnings; and the ALT_DRUG_PREGNANCY and ALT_DRUG_PREGMED tables for pregnancy warnings.

**Overflow family:** [ALT_HISTORY_2](ALT_HISTORY_2.md), [ALT_HISTORY_3](ALT_HISTORY_3.md)  
**Primary key:** `ALT_CSN_ID`  
**Columns:** 37  
**Org-specific columns:** 7  
**Joined by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ALT_ID` | NUMERIC | FK→ | The unique warning ID for each warning. You could link it to ALERT.ALT_ID to get patient and vendor information in table ALERT. |
| 2 | `ALT_DATE_REAL` | FLOAT |  | This is a numeric representation of the date of the contact. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple times on one day. |
| 3 | `ALT_CSN_ID` | NUMERIC | PK | A unique serial number for this contact. This number is unique across all warnings in the system. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ALT_STATUS_C_NAME` | VARCHAR |  | The status category number for the warning after it was viewed in Hyperspace. This describes any actions the user took on the warning. Link it to ZC_ALT_STATUS.ALT_STATUS_C to get the name, title, and abbreviation information for the warning status. |
| 6 | `USER_ID` | VARCHAR | FK→ | The unique ID of the user who triggered the warning. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `SHOWN_PLACE_C_NAME` | VARCHAR |  | The place where you see the warning. You could link it to ZC_SHOWN_PLACE.SHOWN_PLACE_C to get name, title, and abbreviation for shown place. |
| 9 | `OVERALL_OVR_RSN_C_NAME` | VARCHAR | org | For medication interactions, when you override & accept them, if an overall override reason is given at the bottom of the warning pop-up form, it will be saved here. You could link it to ZC_ALRT_SP_OVR_RSN.ALRT_SP_OVR_RSN_C to get name, title, and abbreviation for the reason. |
| 10 | `OVERALL_OVR_CMNT` | VARCHAR |  | For medication interactions, when you override & accept the warning pop-up form, if an overall override comment is given at the bottom of the form, it will be saved here. We only extract the first 255 characters. |
| 11 | `SPEC_OVR_RSN_C_NAME` | VARCHAR |  | The specific override reason given for an overridden medication interaction. Link to ZC_ALRT_SP_OVR_RSN.ALRT_SP_OVR_RSN_C to get the name, title, and abbreviation for the override reason. |
| 12 | `SPEC_OVR_CMNT` | VARCHAR |  | For medication interactions, when you override & accept the warning pop-up form, if a specific override comment is given on the right of the form, it will be saved here. We only extract the first 1000 characters. |
| 13 | `IMMUNIZATION_LPL_ID` | NUMERIC |  | The patient’s immunization problem list ID for a specific immunization-allergy interaction. |
| 14 | `IMPORTANCE_LVL_C_NAME` | VARCHAR | org | Stores the importance level of a warning, a value that is used to determine which warnings are displayed at the top of the interactions popup. Can be used to compare the importance of different warning types. |
| 15 | `PROVIDER_TYPE_C_NAME` | VARCHAR | org | Stores a provider type for the user who triggered the warning. |
| 16 | `SPECIFIC_DEFR_RSN_C_NAME` | VARCHAR | org | For medication interactions, when you override & accept the warnings pop-up, if the warning is deferred and if a specific deferral reason is given in the defer window of the warning, it will be saved here. You could link it to ZC_SPECIFIC_DEFR_R.SPECIFIC_DEFR_R_C to get the name, title, and abbreviation for the deferral reason. |
| 17 | `DOSING_WEIGHT` | NUMERIC |  | Weight used for dose checking. Always stored in kilograms. |
| 18 | `WT_RECORD_DATETIME` | DATETIME (Local) |  | The instant at which the weight was recorded. |
| 19 | `WT_SOURCE_C_NAME` | VARCHAR | org | The weight source. |
| 20 | `WT_COMMENTS` | VARCHAR |  | Generated comment for weight. |
| 21 | `DOSING_HEIGHT` | NUMERIC |  | Height used for dosing warning. Always stored in inches. |
| 22 | `HT_RECORD_DATETIME` | DATETIME (Local) |  | The instant at which the height was recorded. |
| 23 | `HT_SOURCE_C_NAME` | VARCHAR | org | The height source. |
| 24 | `DOSING_BSA` | NUMERIC |  | The body surface area used for dosing checking. Always stored in m2. |
| 25 | `BSA_SOURCE_C_NAME` | VARCHAR | org | The body surface area source. |
| 26 | `BSA_CALC_DETAIL` | VARCHAR |  | The body surface area calculation details with weight, height and recorded instants. |
| 27 | `ALERT_ALLERGEN_ID` | NUMERIC |  | The allergen ID of drug-allergy warning. |
| 28 | `ALERT_ALLERGEN_ID_ALLERGEN_NAME` | VARCHAR |  | The name of the allergen record. |
| 29 | `INACT_INGRED_IND_YN` | VARCHAR |  | It indicates whether the warning is fired because of inactive ingredient. |
| 30 | `ALERT_ROOT_ALLER_ID` | NUMERIC |  | This column stores the allergen ID of the allergen that caused the warning to fire. |
| 31 | `ALERT_ROOT_ALLER_ID_ALLERGEN_NAME` | VARCHAR |  | The name of the allergen record. |
| 32 | `ALERT_MED_CLASS_ID` | NUMERIC |  | Contains the allergen class of the medication for a cross-sensitive warning. |
| 33 | `ALERT_MED_CLASS_ID_ALLERGEN_NAME` | VARCHAR |  | The name of the allergen record. |
| 34 | `PATIENT_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 35 | `ALERT_ALLERGY_ID` | NUMERIC |  | The problem list record that contains the allergen for a drug-allergy warning. |
| 36 | `CONTACT_NUM` | INTEGER |  | The number of the ALT contacts for the given ALT record. |
| 37 | `IS_NONFILTERED_YN` | VARCHAR |  | Indicate whether the warning is non-filtered. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALT_ID` | [ALERT](ALERT.md) | sole_pk | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

## Joined in — referenced by (13)

| From | Column | Confidence |
|------|--------|------------|
| [ALERT_ACTION](ALERT_ACTION.md) | `ALT_CSN_ID` | high |
| [ALERT_CRITERIA](ALERT_CRITERIA.md) | `ALT_CSN_ID` | high |
| [ALT_ALLERGY_REACT](ALT_ALLERGY_REACT.md) | `ALT_CSN_ID` | high |
| [ALT_CLINIC_EFFECT](ALT_CLINIC_EFFECT.md) | `ALT_CSN_ID` | high |
| [ALT_DRUG_DOSE_RSN](ALT_DRUG_DOSE_RSN.md) | `ALT_CSN_ID` | high |
| [ALT_DUPLICATE_LDA_CONTENT](ALT_DUPLICATE_LDA_CONTENT.md) | `ALT_CSN_ID` | high |
| [ALT_DUPLICATE_LDA_INFO](ALT_DUPLICATE_LDA_INFO.md) | `ALT_CSN_ID` | high |
| [ALT_ORDINFO](ALT_ORDINFO.md) | `ALT_CSN_ID` | high |
| [ALT_ORD_VALID_SOURCES](ALT_ORD_VALID_SOURCES.md) | `ALT_CSN_ID` | high |
| [BPA_FUP_RSH_STUDY](BPA_FUP_RSH_STUDY.md) | `ALT_CSN_ID` | high |
| [BPA_TRGR_RSH_STUDY](BPA_TRGR_RSH_STUDY.md) | `ALT_CSN_ID` | high |
| [ORDER_MED_ALTCSN](ORDER_MED_ALTCSN.md) | `ALT_CSN_ID` | high |
| [OUTCOME_EVAL_GOALS](OUTCOME_EVAL_GOALS.md) | `ALT_CSN_ID` | high |

