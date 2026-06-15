# NSQIP_INFO_2

> The NSQIP_INFO_2 table contains NSQIP registry data for the surgeries that are selected for NSQIP submission.

**Overflow of:** [NSQIP_INFO](NSQIP_INFO.md)  
**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 93

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `NSQIP_ER_PREADM_COUNSEL_YN` | VARCHAR |  | Indicates whether or not the patient received counseling before admission describing expectations and detailing the postoperative care plan. |
| 3 | `NSQIP_ER_LIQUID_BEFORE_C_NAME` | VARCHAR |  | Indicates whether or not patient received clear liquids between midnight and 3 hours prior to surgery. |
| 4 | `NSQIP_ER_THORACIC_EPIDURAL_C_NAME` | VARCHAR |  | Indicates whether a thoracic epidural was placed pre-operatively. |
| 5 | `NSQIP_ER_PAIN_MGMT_YN` | VARCHAR |  | Indicates whether a multi-modal approach to pain management was used. |
| 6 | `NSQIP_ER_NORMAL_TEMP_PACU_YN` | VARCHAR |  | Indicates whether the first measured temperature on arrival to PACU is >= 36.0° C / 96.8° F. |
| 7 | `NSQIP_ER_GOAL_THERAPY_YN` | VARCHAR |  | Indicates whether intraoperative intravenous fluid was administered based on optimization of hemodynamic measurements. |
| 8 | `NSQIP_ER_ANTI_EMETIC_YN` | VARCHAR |  | Indicates whether intraoperative anti-emetic interventions were used. |
| 9 | `NSQIP_ER_MOB_POD0_YN` | VARCHAR |  | Indicates whether there is ambulation within the first 24 hours following surgery. |
| 10 | `NSQIP_ER_LIQUID_POD0_YN` | VARCHAR |  | Indicates whether clear liquids were provided to the patient within the first 24 hours following surgery. |
| 11 | `NSQIP_ER_IV_DIS_POD0_YN` | VARCHAR |  | Indicates whether the maintenance intravenous fluids were discontinued within the first 24 hours after surgery. |
| 12 | `NSQIP_ER_MOB_BID_POD1_YN` | VARCHAR |  | Indicates whether there were at least two episodes of mobilization on post-operative day #1. |
| 13 | `NSQIP_ER_SOLID_POD1_YN` | VARCHAR |  | Indicates whether solid food was provided anytime within the first 48 hours following surgery. |
| 14 | `NSQIP_ER_FOLEY_REMOVED_POD1_C_NAME` | VARCHAR |  | Indicates whether the urinary catheter was removed within the first 48 hours following surgery. |
| 15 | `NSQIP_ER_MOB_BID_POD2_YN` | VARCHAR |  | Indicates whether there were at least two episodes of mobilization on post-operative day #2. |
| 16 | `NSQIP_ER_BOWEL_RETURN_DATE` | DATETIME |  | The first date on which return of bowel function occurred. |
| 17 | `NSQIP_ER_DIET_TOLERATING_DATE` | DATETIME |  | The first date on which the patient tolerated a diet. |
| 18 | `NSQIP_ER_PAIN_CONTROLLED_DATE` | DATETIME |  | The first date on which the patient has adequate pain control without use of intravenous or epidural pain medications. |
| 19 | `NSQIP_ER_CRYSTALLOID_ADMIN` | INTEGER |  | The total volume of balanced crystalloid administered intravenously during the operation. |
| 20 | `NSQIP_ER_COLLOID_ADMIN` | INTEGER |  | The total volume of colloid fluid administered intravenously during the operation. |
| 21 | `NSQIP_SURGEON_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 22 | `NSQIP_EXT_SURGEON_IDENTIFIER` | VARCHAR |  | The surgeon's NSQIP ID associated with the NSQIP case. |
| 23 | `NSQIP_SURGEON_FIRST_NAME` | VARCHAR |  | The first name of the surgeon associated with the NSQIP case. |
| 24 | `NSQIP_SURGEON_LAST_NAME` | VARCHAR |  | The last name of the surgeon associated with the NSQIP case. |
| 25 | `NSQIP_EOL_OR_WITHDRAW_CARE_YN` | VARCHAR |  | Indicates whether there were end of life or withdrawal of care considerations. |
| 26 | `NSQIP_PATIENT_EMAIL_ADDRESS` | VARCHAR |  | The patient's email address |
| 27 | `NSQIP_PAYOR_STATUS_C_NAME` | VARCHAR |  | The category number for the NSQIP primary payor status. |
| 28 | `NSQIP_PREOP_SURG_PLAN_COMM_C_NAME` | VARCHAR |  | Indicates if the pre-op surgical plan was communicated or not, or if the communication is not applicable. |
| 29 | `NSQIP_MJR_COMORBID_MED_COND_C_NAME` | VARCHAR |  | Indicates if major co-morbid medical conditions were identified, or if it's not applicable. |
| 30 | `NSQIP_TOBACCO_SCREENING_C_NAME` | VARCHAR |  | Indicates if tobacco screening was performed, or if tobacco screening is not applicable. |
| 31 | `NSQIP_PERIOP_COMPOSITE_YN` | VARCHAR |  | Indicates if there was a perioperative composite. Y indicates there was a composite. N or null indicates there was not. |
| 32 | `NSQIP_INTRAOP_TIMEOUT_YN` | VARCHAR |  | Indicates if an intraoperative timeout safety checklist was used. Y indicates a checklist was used. N or null indicates one was not used. |
| 33 | `NSQIP_POSTOP_CARE_COORD_YN` | VARCHAR |  | Indicates if postoperative care coordination was done. Y indicates there was coordination. N or null indicates there was not. |
| 34 | `NSQIP_NUM_EMAIL_ATTEMPTS` | INTEGER |  | The number of attempts to follow up with the patient via email. |
| 35 | `NSQIP_ER_PREOP_VTE_C_NAME` | VARCHAR |  | The category ID for if pre-op VTE chemoprophylaxis was performed. |
| 36 | `NSQIP_ER_REGIONAL_ANES_C_NAME` | VARCHAR |  | The category ID for the type of regional anesthesia used. |
| 37 | `NSQIP_ER_POSTOP_VTE_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the first post-op VTE chemoprophylaxis dose was given. |
| 38 | `NSQIP_ER_POSTOP_VTE_PRPH_NA_YN` | VARCHAR |  | Indicates that post-op VTE chemoprophylaxis is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 39 | `NSQIP_ER_POST_MOBILE_UTC_DTTM` | DATETIME (UTC) |  | The date and time of the first post-op mobilization. |
| 40 | `NSQIP_ER_POSTOP_MOBILE_NA_YN` | VARCHAR |  | Indicates that post-op mobilization is not applicable. Y indicates it is not applicable. N or null indicates that it is applicable. |
| 41 | `NSQIP_ER_POST_LIQUID_UTC_DTTM` | DATETIME (UTC) |  | Date and time of the first post-op intake of liquids. |
| 42 | `NSQIP_ER_POSTOP_LIQUID_NA_YN` | VARCHAR |  | Indicates that post-op intake of liquids is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 43 | `NSQIP_ER_BID_MOBILE_UTC_DTTM` | DATETIME (UTC) |  | Date and time of the first BID mobilization. |
| 44 | `NSQIP_ER_BID_MOBILE_NA_YN` | VARCHAR |  | Indicates that BID mobilization is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 45 | `NSQIP_ER_POSTOP_SOLID_UTC_DTTM` | DATETIME (UTC) |  | Date and time of the first post-op intake of solids. |
| 46 | `NSQIP_ER_POSTOP_SOLID_NA_YN` | VARCHAR |  | Indicates that post-op intake of solids is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 47 | `NSQIP_ER_FOLEY_REMOVE_UTC_DTTM` | DATETIME (UTC) |  | Date and time of Foley removal. |
| 48 | `NSQIP_ER_FOLEY_REMOVAL_NA_YN` | VARCHAR |  | Indicates that Foley removal is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 49 | `NSQIP_ER_PRLNGED_FOLEY_C_NAME` | VARCHAR |  | Indicates if prolonged Foley catheterization reason was documented |
| 50 | `NSQIP_ER_FLUIDS_STOP_UTC_DTTM` | DATETIME (UTC) |  | Date and time of IV fluid discontinuation. |
| 51 | `NSQIP_ER_FLUIDS_STOP_NA_YN` | VARCHAR |  | Indicates that IV fluid discontinuation is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 52 | `NSQIP_ER_BOWEL_RETURN_NA_YN` | VARCHAR |  | Indicates that the date of return of bowel function is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 53 | `NSQIP_ER_DIET_TOLERATING_NA_YN` | VARCHAR |  | Indicates that the date tolerating diet is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 54 | `NSQIP_ER_PAIN_CONTROLLED_NA_YN` | VARCHAR |  | Indicates that the date pain controlled with PO medication is not applicable. Y indicates it is not applicable. N or null indicates it is applicable. |
| 55 | `NSQIP_HOME_PHONE_PREFERRED_YN` | VARCHAR |  | Indicates if the home phone is the patient's preferred phone number. Y indicates home phone is preferred. N or null indicates it is not preferred. |
| 56 | `NSQIP_WORK_PHONE_PREFERRED_YN` | VARCHAR |  | Indicates if the work phone is the patient's preferred phone number. Y indicates work phone is preferred. N or null indicates it is not preferred. |
| 57 | `NSQIP_CELL_PHONE_PREFERRED_YN` | VARCHAR |  | Indicates if the cell phone is the patient's preferred phone number. Y indicates cell phone is preferred. N or null indicates it is not preferred. |
| 58 | `NSQIP_ER_MECH_BOWEL_PREP_YN` | VARCHAR |  | Indicates if pre-op mechanical bowel prep was performed for the patient. Y indicates it was performed. N or null indicates it was not performed. |
| 59 | `NSQIP_ER_ORAL_ANTIBIOTICS_YN` | VARCHAR |  | Indicates if the patient received pre-op oral antibiotics. Y indicates antibiotics were given. N or null indicates they weren't given. |
| 60 | `NSQIP_OTHER_LANGUAGE` | VARCHAR |  | The preferred language spoken by the patient. NSQIP_INFO__NSQIP_PREF_LANG_C also contains the preferred language of the patient, but is limited to the NSQIP preferred language category list. |
| 61 | `NSQIP_PAT_RISK_ASMT_COMM_C_NAME` | VARCHAR |  | Indicates whether the patient-centered surgical risk assessment & communication was performed or if it was not applicable. |
| 62 | `NSQIP_SUBSTANCE_SCREENING_C_NAME` | VARCHAR |  | Indicates whether substance use screening & intervention composite was performed or if it was not applicable. |
| 63 | `NSQIP_OPIOID_RISK_TOOL_SCORE` | INTEGER |  | This column stores the opioid risk tool score. |
| 64 | `NSQIP_HM_SUPPORT_STAT_C_NAME` | VARCHAR |  | The category ID for the patient's home support status. |
| 65 | `NSQIP_FALL_HISTORY_C_NAME` | VARCHAR |  | The category ID for the patient's fall history. |
| 66 | `NSQIP_HX_COGNITIVE_IMPAIR_YN` | VARCHAR |  | Indicates the history of dementia or cognitive impairment. Y indicates it is confirmed. N or null indicates no conclusive evidence was found. |
| 67 | `NSQIP_POSTOP_DELIRIUM_C_NAME` | VARCHAR |  | The category ID for the presence of post-op delirium in a patient. |
| 68 | `NSQIP_HOME_DISCHRG_SVC_C_NAME` | VARCHAR |  | The category ID for whether a patient was discharged home with or without services. |
| 69 | `NSQIP_FHS_DISCHRG_C_NAME` | VARCHAR |  | The category ID for the functional health status of a patient when they are discharged. |
| 70 | `NSQIP_OXYGEN_SUPPORT_YN` | VARCHAR |  | Indicates whether the patient is on oxygen support. Y indicates the patient uses external oxygen. N or null indicates the patient does not use external oxygen. |
| 71 | `NSQIP_IMMUNOSUP_OTHER` | VARCHAR |  | The type of immunosuppressants used by the patient. NSQIP_IMMUNOSUP_USE.NSQIP_IMMUNOSUP_C also contains the type of immunosuppressants, but is limited to the NSQIP immunosuppressant category category list. |
| 72 | `NSQIP_CASE_ACUITY_C_NAME` | VARCHAR |  | This category ID for the case acuity variable. It indicates the priority in which this surgery was performed. |
| 73 | `NSQIP_COVID_PRE_DX_C_NAME` | VARCHAR |  | The category ID of the pre-op COVID diagnosis variable. It indicates the patient status of COVID-19 diagnosis confirmation prior to surgery. |
| 74 | `NSQIP_COVID_POST_DX_C_NAME` | VARCHAR |  | The category ID of the post-op COVID diagnosis variable. It indicates the patient status of COVID-19 diagnosis confirmation after surgery. |
| 75 | `NSQIP_RACE_OTHER` | VARCHAR |  | The race of the patient. NSQIP_RACES.NSQIP_RACE_C also contains the patient race, but is limited to the category list defined in NSQIP. |
| 76 | `NSQIP_OTHER_MIS` | VARCHAR |  | The free-text minimally invasive surgical approach that is not covered in the discrete options in NSQIP_OPERATIVE_APPROACH. |
| 77 | `NSQIP_ROBOT_USED_YN` | VARCHAR |  | Indicates whether the performed surgery involved robotic assistance. Y indicates the there was robotic assistance. N or null indicates there was not robotic assistance. |
| 78 | `NSQIP_OPEN_ASSIST_YN` | VARCHAR |  | Indicates whether the performed surgical technique involved hand or open assistance. Y indicates the there was hand or open assistance. N or null indicates there was no hand or open assistance. |
| 79 | `NSQIP_CONV_OPEN_YN` | VARCHAR |  | Indicates whether the operative approach was unexpectedly converted to open. Y indicates the surgery wasn't planned with an open technique, but switched during operation. N or null indicates there was no unexpected conversion to open. |
| 80 | `NSQIP_CREAT_INCREASE_C_NAME` | VARCHAR |  | The category ID corresponding to the most severe level of creatinine increase preoperatively. |
| 81 | `NSQIP_LOW_URINE_OUTPUT_C_NAME` | VARCHAR |  | The category ID corresponding to the lowest level of urine output preoperatively. |
| 82 | `NSQIP_POST_DELIRIUM_YN` | VARCHAR |  | Indicates if the patient experienced delirium postoperatively. Y indicates the patient experienced postoperative delirium. N or null indicates there was no postoperative delirium. |
| 83 | `NSQIP_POST_DEL_SCR_YN` | VARCHAR |  | Indicates if the patient was screened for postoperative delirium. Y indicates the patient had a delirium screen postoperatively. N or null indicates there was no delirium screen postoperatively. |
| 84 | `NSQIP_POST_DEL_SCR_RES_C_NAME` | VARCHAR |  | Indicates the result of the postoperative delirium screen. 1 indicates a positive result. 2 indicates a negative result. |
| 85 | `NSQIP_OPIOID_DIS_YN` | VARCHAR |  | Indicates if patient was prescribed an opioid at discharge. |
| 86 | `NSQIP_NUM_PAT_PORTAL` | INTEGER |  | The number of attempts to follow up with the patient via patient portal messages. |
| 87 | `NSQIP_NUM_TEXTS` | INTEGER |  | The number of attempts to follow up with the patient via text messages. |
| 88 | `NSQIP_GENDER_IDENTITY_C_NAME` | VARCHAR |  | This item stores the patient's gender identity. |
| 89 | `NSQIP_HORMONE_THERAPY_C_NAME` | VARCHAR |  | This item stores the patient's gender affirming hormone therapy status. |
| 90 | `NSQIP_PREOP_OPIOID_USE_C_NAME` | VARCHAR |  | This item stores the patient's preoperative opioid use. |
| 91 | `NSQIP_CHRONIC_OPIOID_USE_YN` | VARCHAR |  | This item stores a patient's chronic opioid use. |
| 92 | `NSQIP_PREOP_BENZO_USE_YN` | VARCHAR |  | This item stores the patient's preoperative benzodiazepine use. |
| 93 | `NSQIP_CHRONIC_BENZO_USE_YN` | VARCHAR |  | This item stores a patient's chronic benzodiazepine use. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

