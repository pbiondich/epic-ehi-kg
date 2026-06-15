# EXPOSURE_ABSTNS

> This table contains information about outbreak and exposure abstractions.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 47  
**Org-specific columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `EXPOSURE_NOTE_ID` | VARCHAR |  | The unique ID of the case note associated with the exposure abstraction. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient who was exposed. |
| 4 | `PATIENT_DIED_YN` | VARCHAR |  | Indicates whether the patient died. |
| 5 | `DEATH_DATE` | DATETIME |  | The date of the patient's death. |
| 6 | `MDR_TYPE_C_NAME` | VARCHAR | org | The MDR type category ID that the patient was exposed to. |
| 7 | `EXPOSURE_STATUS_C_NAME` | VARCHAR | org | The status category ID for the exposure case. |
| 8 | `DX_DATE` | DATETIME |  | The date that the exposed patient was diagnosed as positive with an infection. |
| 9 | `PASSIVATING_DATE` | DATETIME |  | The date by which the patient's exposure case should be resolved. |
| 10 | `MICROBE_ORGANISM_ID` | NUMERIC |  | The unique ID of the organism for the patient's exposure case. |
| 11 | `MICROBE_ORGANISM_ID_NAME` | VARCHAR |  | The name of the organism. |
| 12 | `SPA_TYPE_C_NAME` | VARCHAR | org | The SPA type category ID specifying the strain of MRSA for the patient's exposure. |
| 13 | `RISK_PERMANENCE_C_NAME` | VARCHAR | org | The degree of permanence category ID for the patient's exposure to the organism. |
| 14 | `RISK_CERTAINTY_C_NAME` | VARCHAR | org | The degree of certainty category ID that the patient was exposed to the microbe. |
| 15 | `RESOURCE_C_NAME` | VARCHAR | org | The source of information category ID for the exposure investigation. |
| 16 | `RISK_EDIT_REASON_C_NAME` | VARCHAR | org | The edit reason category ID for modifying the exposure case. |
| 17 | `RISK_END_REASON_C_NAME` | VARCHAR | org | The end reason category ID for closing the exposure case. |
| 18 | `RISK_REACTIVATE_REASON_C_NAME` | VARCHAR | org | The reactivation reason category ID for reopening a closed exposure case. |
| 19 | `OUTBREAK_REGISTRY_DATA_ID` | NUMERIC |  | The unique ID of the outbreak investigation that the exposure case is a part of. |
| 20 | `SAMPLE_TYPE_C_NAME` | VARCHAR | org | The sample type category ID which diagnosed the patient. |
| 21 | `DX_DISTRICT_C_NAME` | VARCHAR | org | The region category ID where the patient was diagnosed with the infection. |
| 22 | `DX_FACILITY_TYPE_C_NAME` | VARCHAR | org | The type of facility category ID where the patient was diagnosed with the infection. |
| 23 | `DX_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 24 | `DX_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 25 | `EPIDEMIC_CODE` | VARCHAR |  | The description of the outbreak event. |
| 26 | `CREATION_USER_ID` | VARCHAR |  | The unique ID of the user who created the abstraction |
| 27 | `CREATION_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 28 | `EXPOSER_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient who exposed other patients to the outbreak. |
| 29 | `EXPOSURE_SOURCE_C_NAME` | VARCHAR | org | The exposure source category ID for whether the exposure occurred domestically or abroad. |
| 30 | `HOSPITAL_CONTACT_C_NAME` | VARCHAR | org | The type of contact category ID for the visit where the patient was exposed. |
| 31 | `TRANSMISSION_TYPE_C_NAME` | VARCHAR | org | The transmission type category ID for whether the transmission was hospital-acquired or community-acquired. |
| 32 | `COUNTRY_C_NAME` | VARCHAR | org | The country category ID where the exposure occurred, if abroad. |
| 33 | `TRANSMISSION_DISTRICT_C_NAME` | VARCHAR | org | The region category ID where the patient was exposed to the microbe. |
| 34 | `TRANSMISSION_FAC_TYPE_C_NAME` | VARCHAR | org | The type of facility category ID where the patient was exposed to the microbe. |
| 35 | `TRANSMISSION_FACILITY_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 36 | `TRANSMISSION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 37 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | The registry type category ID for the exposure or outbreak abstraction. |
| 38 | `CUR_STAT_C_NAME` | VARCHAR | org | The current status category ID of the abstraction. |
| 39 | `CUR_STAT_USER_ID` | VARCHAR |  | The unique ID of the user who set the current abstraction status. |
| 40 | `CUR_STAT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 41 | `CUR_STAT_DTTM` | DATETIME (UTC) |  | The date and time when the current abstraction status was set. |
| 42 | `RECORD_CREATION_DATE` | DATETIME |  | The date the record was created. |
| 43 | `HOW_CREATED_C_NAME` | VARCHAR |  | The creation method category ID for the exposure abstraction. |
| 44 | `EXPOSURE_REMARKS` | VARCHAR |  | Information about how this exposure should impact patient care. |
| 45 | `DECLARED_DATE` | DATETIME |  | The date the outbreak was declared. |
| 46 | `DECLARED_OVER_DATE` | DATETIME |  | The date the outbreak was declared over. |
| 47 | `EXPOSED_DATE` | DATETIME |  | Date the patient was exposed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EXPOSER_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

