# INFECTION_ABSTNS

> This table contains basic information from infection abstractions.

**Overflow family:** [INFECTION_ABSTNS_2](INFECTION_ABSTNS_2.md)  
**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 96  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `ICON_CASE_NOTE_ID` | VARCHAR |  | The unique identifier (.1 item) for the HNO record associated with the infection case's case note. |
| 3 | `INF_CLASS_C_NAME` | VARCHAR | org | The determined source of an infection. |
| 4 | `INF_DATE` | DATETIME |  | The infection date associated with the case. |
| 5 | `PRIMARY_INF_C_NAME` | VARCHAR | org | The primary type of the infection. |
| 6 | `SECONDARY_INF_C_NAME` | VARCHAR |  | The secondary infection type, if one was documented. |
| 7 | `LAB_IDENTIFIED_ORG_C_NAME` | VARCHAR | org | The type of organism the lab identified. |
| 8 | `NHSN_VERSION_C_NAME` | VARCHAR |  | The category ID for the NHSN version to use for the abstraction. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 9 | `INF_TRANSFER_DT` | DATETIME |  | The date the patient was transfered into the unit in which the specimen was collected. |
| 10 | `INF_DISCHARGE_DT` | DATETIME |  | The date the patient was discharged from the unit in which the specimen was collected. |
| 11 | `INF_PROC_DT` | DATETIME |  | The date of the procedure associated with this case. |
| 12 | `OR_LOG_ID` | VARCHAR |  | The unique identifier of the surgical log (ORL .1) associated with the infection case. |
| 13 | `CUR_STAT_USER_ID` | VARCHAR |  | The internal ID of the user who set the current status. |
| 14 | `CUR_STAT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 15 | `CUR_STAT_DTTM` | DATETIME (UTC) |  | The instant at which the current status (RDI-10024) was set. |
| 16 | `INF_ADMISSION_DT` | DATETIME |  | The abstracted admission date for submission to the CDC. |
| 17 | `CUR_STAT_C_NAME` | VARCHAR | org | The current status of the case. |
| 18 | `PAT_ID` | VARCHAR | FK→ | The unique identifier (.1 item) for the associated patient (EPT) record. |
| 19 | `PAT_DATE` | DATETIME |  | The date of case creation. |
| 20 | `REGISTRY_TYPE_C_NAME` | VARCHAR | org | The registry type of the abstraction. |
| 21 | `BSI_LAB_RESULT_C_NAME` | VARCHAR |  | The BSI lab result category ID for the infection. |
| 22 | `UTI_TYPE_C_NAME` | VARCHAR |  | The UTI type category ID for the infection. |
| 23 | `UTI_CATHETER_STATUS_C_NAME` | VARCHAR |  | The UTI catheter status category ID on the infection date. |
| 24 | `SSI_EVENT_TYPE_C_NAME` | VARCHAR |  | The SSI event type category ID for the infection. |
| 25 | `SSI_DETECTED_DURING_C_NAME` | VARCHAR |  | The SSI detection event category ID for the infection. |
| 26 | `VAE_SPECIFIC_EVENT_C_NAME` | VARCHAR |  | The VAE specific event category ID for the infection. |
| 27 | `POST_PROC_INFECTION_YN` | VARCHAR |  | Indicates whether the infection happened after a surgical procedure. |
| 28 | `MDRO_INFECTION_SURVEILLANCE_YN` | VARCHAR |  | Indicates whether the pathogen and location for this infection are in-plan for Infection Surveillance in the MDRO/CDI Module. |
| 29 | `SECONDARY_BSI_YN` | VARCHAR |  | Indicates whether a secondary BSI resulted from this infection. |
| 30 | `PATIENT_DIED_YN` | VARCHAR |  | Indicates whether the patient died. The patient's death does not need to be related to this infection. |
| 31 | `INFECTION_CONTRIBUTED_DEATH_YN` | VARCHAR |  | Indicates whether the patient's death was related to this infection. |
| 32 | `OUTPAT_PROC_YN` | VARCHAR |  | Indicates whether the procedure happened in an outpatient setting for this infection. |
| 33 | `DAILY_MIN_FIO2_YN` | VARCHAR |  | Indicates whether the patient's daily minimum FiO2 value meets VAE criteria for this infection. |
| 34 | `DAILY_MIN_PEEP_YN` | VARCHAR |  | Indicates whether the patient's daily minimum PEEP value meets VAE criteria for this infection. |
| 35 | `TEMPERATURE_OUTSIDE_RANGE_YN` | VARCHAR |  | Indicates whether a temperature strictly outside of 36 to 38 degrees C was a symptom of this VAE. |
| 36 | `WBC_OUTSIDE_RANGE_YN` | VARCHAR |  | Indicates whether a WBC equal to or outside of 4000 to 12000 cells per cubic mm was a symptom of this VAE. |
| 37 | `NEW_ANTIMICROBIAL_AGENT_YN` | VARCHAR |  | Indicates whether the patient was started on a new antimicrobial agent during this VAE. |
| 38 | `PURULENT_RESP_SECRETIONS_YN` | VARCHAR |  | Indicates whether purulent respiratory secretions were a symptom of the infection. |
| 39 | `POSITIVE_CULTURE_SPUTUM_YN` | VARCHAR |  | Indicates whether a positive culture of sputum was found for this infection. |
| 40 | `POS_CULTURE_ENDOTRACHEAL_YN` | VARCHAR |  | Indicates whether a positive culture of endotracheal aspirate was found for this infection. |
| 41 | `POS_CULTURE_BRONCHOALVEOLAR_YN` | VARCHAR |  | Indicates whether a positive culture of bronchoalveolar lavage was found for this infection. |
| 42 | `POS_CULTURE_LUNG_TISSUE_YN` | VARCHAR |  | Indicates whether a positive culture of lung tissue was found for this infection. |
| 43 | `POS_CULTURE_SPEC_BRUSHING_YN` | VARCHAR |  | Indicates whether a positive culture of protected specimen brushing was found for this infection. |
| 44 | `POSITIVE_PLEURAL_FLUID_YN` | VARCHAR |  | Indicates whether a positive pleural fluid culture was found for this infection. |
| 45 | `POS_LUNG_HISTOPATHOLOGY_YN` | VARCHAR |  | Indicates whether a positive lung histopathology was found for this infection. |
| 46 | `POSITIVE_LEGIONELLA_SPP_YN` | VARCHAR |  | Indicates whether legionella spp. was found for this VAE. |
| 47 | `POSITIVE_VIRAL_PATHOGENS_YN` | VARCHAR |  | Indicates whether viral pathogens were found for this VAE. |
| 48 | `NHSN_MEDICARE_BENEFICIARY_NUM` | VARCHAR |  | The Medicare Beneficiary Number for the patient at the time of the infection. |
| 49 | `VENT_INIT_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 50 | `VENTILATOR_INITIATED_DATE` | DATETIME |  | The date when mechanical ventilation was initiated on the patient. |
| 51 | `IS_APRV_VENT_YN` | VARCHAR |  | Indicates whether the patient was on APRV ventilation. |
| 52 | `PX_REGISTRY_DATA_ID` | NUMERIC |  | Links from a NHSN SSI numerator record to its procedure denominator. |
| 53 | `SSI_PRESENT_AT_SURG_YN` | VARCHAR |  | Indicates whether the patient's surgical site infection was present at the time of surgery. |
| 54 | `LAB_POSVIBOLGCH_YN` | VARCHAR |  | Indicates the criterion "Positive culture of virus, Bordetella, Legionella, or Chlamydia" for a VAP infection. |
| 55 | `LAB_POSNONCULT_YN` | VARCHAR |  | Indicates the criterion "Positive non-culture diagnostic test of respiratory secretions or tissue for virus, Bordetella, Chlamydia, Mycoplasma, Legionella" for a VAP infection. |
| 56 | `SYMPTOM_DIARRHEA_YN` | VARCHAR |  | Column for the "Diarrhea" criterion on a GI case. RDI-66300. |
| 57 | `SYMPTOM_BILASP_YN` | VARCHAR |  | Column for the "Bilious aspirate" criterion on a GI case. RDI-66301. |
| 58 | `SYMPTOM_ABDDIST_YN` | VARCHAR |  | Column for the "Abdominal distention" criterion on a GI case. RDI-66302. |
| 59 | `SYMPTOM_STOOLBLD_YN` | VARCHAR |  | Column for the "Occult or gross blood in stools (with no rectal fissure)" criterion on a GI case. RDI-66303. |
| 60 | `SYMPTOM_BOWELNEC_YN` | VARCHAR |  | Column for the "Surgical evidence of extensive bowel necrosis (>2 cm of bowel affected)" criterion on a GI case. RDI-66304. |
| 61 | `SYMPTOM_PNEUMINT_YN` | VARCHAR |  | Column for the "Surgical evidence of pneumatosis intestinalis with or without intestinal perforation" criterion on a GI case. RDI-66305. |
| 62 | `LAB_PNEUMINT_YN` | VARCHAR |  | Column for the "Pneumatosis intestinalis on radiograph" criterion on a GI case. RDI-66306. |
| 63 | `LAB_PORTVENGAS_YN` | VARCHAR |  | Column for the "Portal venous gas (hepatobiliary gas) by radiograph" criterion on a GI case. RDI-66307. |
| 64 | `LAB_15COLIV_YN` | VARCHAR |  | Column for the "> 15 colonies cultured from IV cannula tip using semiquantitative culture method" criterion on a GI case. RDI-66308. |
| 65 | `LAB_PNEUMPER_YN` | VARCHAR |  | Column for the "Pneumoperitoneum by radiograph" criterion on a CVS case. RDI-66309. |
| 66 | `BRONCHOALVEOLAR_WITH_GROWTH_YN` | VARCHAR |  | Represents the abbreviation lab_quanPosBal from the NHSN specifications, known as the Infection Data Model. Indicates that an infection presented with a positive culture from bronchoalveolar lavage with sufficient growth. |
| 67 | `ENDOTRACHEAL_WITH_GROWTH_YN` | VARCHAR |  | Represents the abbreviation lab_quanPosEndo from the NHSN specifications, known as the Infection Data Model. Indicates that an infection presented with a positive culture from endotracheal aspirate with sufficient growth. |
| 68 | `LUNG_TISSUE_WITH_GROWTH_YN` | VARCHAR |  | Represents the abbreviation lab_quanPosLung from the NHSN specifications, known as the Infection Data Model. Indicates that an infection presented with a positive culture from lung tissue with sufficient growth. |
| 69 | `PROT_SPEC_BRUSH_WITH_GROWTH_YN` | VARCHAR |  | Represents the abbreviation lab_quanPosBrush from the NHSN specifications, known as the Infection Data Model. Indicates that an infection presented with a positive culture from protected specimen brush with sufficient growth. |
| 70 | `HOW_CREATED_C_NAME` | VARCHAR |  | The category ID for the method used to create the case. |
| 71 | `ASSOCIATED_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 72 | `NHSN_DISCH_OTH_FAC_C_NAME` | VARCHAR |  | The discharged from other facility category ID for the registry data record. |
| 73 | `NHSN_PAT_LAST_OVERNIGHT_STAY_C_NAME` | VARCHAR |  | The last overnight physical location of the patient prior to hospitalization category ID for the registry data record. |
| 74 | `ASSOCIATED_LOC_NHSN_DEF_ID_CMS_MU_NAME` | VARCHAR |  | The name of the CMS Meaningful Use record. |
| 75 | `NHSN_LABID_ONSET_C_NAME` | VARCHAR |  | The onset category ID of the LabID event. This column distinguishes between MDRO and C. diff LabID events that are attributed to a healthcare setting and those attributed to the community. This value is most reliable when only selecting records with a current status of Ready for Export (15) or Exported (20). |
| 76 | `LINE_INSERTION_DTTM` | DATETIME (Local) |  | The instant when the LDA was inserted. |
| 77 | `LINE_INSERTION_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 78 | `PERM_LN_INSRT_DTTM` | DATETIME (Local) |  | The instant when the permanent LDA was inserted. |
| 79 | `PERM_LN_INSRT_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 80 | `TEMP_LN_INSRT_DTTM` | DATETIME (Local) |  | The instant when the temporary LDA was inserted. |
| 81 | `TEMP_LN_INSRT_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 82 | `NHSN_LABID_FACUNQ_YN` | VARCHAR |  | Indicates whether a LabID event is a facility-wide, non-duplicate event. |
| 83 | `NHSN_EVENT_ID` | VARCHAR |  | Stores the NHSN Event ID from the NHSN database. Storing these values makes matching RDI records in Epic to NHSN-returned events easier and makes imports safer. |
| 84 | `NHSN_ECMO_PRESENT_YN` | VARCHAR |  | Indicates whether an extracorporeal life support device was present. |
| 85 | `NHSN_VAD_PRESENT_YN` | VARCHAR |  | Indicates whether a ventricular assist device was present. |
| 86 | `CARBAPENEMASE_TESTED_C_NAME` | VARCHAR |  | The carbapenemase tested category ID associated with the NHSN LabID Event registry record. |
| 87 | `OTHER_CARBAPENEMASE_TEST` | VARCHAR |  | This stores a free text entry for other carbapenemase tests performed for the CRE LabID sample. |
| 88 | `POSITIVE_CARBAPENEMASE_TEST_C_NAME` | VARCHAR |  | The positive carbapenemase found category ID for the NHSN LabID Event registry record. |
| 89 | `OTHER_POSITIVE_CARBAPENEMASE` | VARCHAR |  | This stores a free text entry for other positive carbapenemases for the CRE LabID sample. |
| 90 | `SURV_ABSTN_REGISTRY_DATA_ID` | NUMERIC | FK→ | The unique ID of the surveillance abstraction (RDI) record associated with the infection case. |
| 91 | `NHSN_MUNCHAUSEN_SYNDROME_YN` | VARCHAR |  | Indicates whether the patient had known or suspected Munchausen Syndrome by Proxy during current admission. |
| 92 | `NHSN_PATIENT_SELF_INJECTION_YN` | VARCHAR |  | Indicates observed or suspected patient injection into vascular line(s) within the BSI infection window period. |
| 93 | `NHSN_EPIDERMOLYSIS_BULLOSA_YN` | VARCHAR |  | Indicates Epidermolysis bullosa during current admission. |
| 94 | `MATCHING_ORGANISM_SITE_C_NAME` | VARCHAR |  | Site which has a matching organism identified with a separate blood specimen, both collected within the infection window period and pus is present. |
| 95 | `BSI_HEMODIALYSIS_LINE_YN` | VARCHAR |  | Indicates whether a hemodialysis line was in place for the BSI registry record. |
| 96 | `NHSN_COVID19_STATUS_C_NAME` | VARCHAR |  | The COVID-19 status category ID for the associated infection case. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `SURV_ABSTN_REGISTRY_DATA_ID` | [SURVEILLANCE_ABSTRACTION](SURVEILLANCE_ABSTRACTION.md) | sole_pk | high |

