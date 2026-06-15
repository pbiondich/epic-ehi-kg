# PAT_ENC_HSP

> This table is the primary table for hospital encounter information. A hospital encounter is a contact in the patient record created through an ADT workflow such as preadmission, admission, ED Arrival, discharge, and hospital outpatient visit (HOV) contacts. These contact types have the ADT flag (I EPT 10101) set to 1. This table excludes all other contacts.

**Overflow family:** [PAT_ENC_HSP_2](PAT_ENC_HSP_2.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 89  
**Org-specific columns:** 40

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `ADT_PAT_CLASS_C_NAME` | VARCHAR | org | The category value corresponding to the patient classification for this patient contact. |
| 3 | `ADT_PATIENT_STAT_C_NAME` | VARCHAR |  | The category value corresponding to the patient status for this patient contact. |
| 4 | `LEVEL_OF_CARE_C_NAME` | VARCHAR | org | The category value corresponding to the level of care for this patient contact. |
| 5 | `PENDING_DISCH_TIME` | DATETIME (Local) |  | The date and time of the pending discharge for this patient contact. |
| 6 | `DISCH_CODE_C_NAME` | VARCHAR | org | The category value corresponding to the discharge code for this patient contact. |
| 7 | `ADT_ATHCRT_STAT_C_NAME` | VARCHAR | org | The category value corresponding to the authorization/certification status for this patient contact. |
| 8 | `PREADM_UNDO_RSN_C_NAME` | VARCHAR | org | The category value corresponding to the preadmission undo reason for this patient contact. |
| 9 | `EXP_ADMISSION_TIME` | DATETIME (Local) |  | The date and time of the expected admission for this patient contact. |
| 10 | `EXP_LEN_OF_STAY` | INTEGER |  | The expected length of stay in days of the admission for this patient contact. |
| 11 | `EXP_DISCHARGE_DATE` | DATETIME |  | The date of expected discharge of the admission for this patient contact. |
| 12 | `ADMIT_CATEGORY_C_NAME` | VARCHAR | org | The category value corresponding to the admission category for this patient contact. |
| 13 | `ADMIT_SOURCE_C_NAME` | VARCHAR | org | The category value corresponding to the admission source for this patient contact. |
| 14 | `TYPE_OF_ROOM_C_NAME` | VARCHAR | org | The category value corresponding to the type of room requested for this patient contact. |
| 15 | `TYPE_OF_BED_C_NAME` | VARCHAR | org | The category value corresponding to the type of bed requested for this patient contact. |
| 16 | `RSN_FOR_BED_C_NAME` | VARCHAR | org | The category value corresponding to the reason for the type of bed requested for this patient contact. |
| 17 | `DELIVERY_TYPE_C_NAME` | VARCHAR | org | The category value corresponding to the delivery type of the child for this patient contact. |
| 18 | `LABOR_STATUS_C_NAME` | VARCHAR |  | The category value corresponding to the labor status for this patient contact. |
| 19 | `ER_INJURY` | VARCHAR |  | Free text description of injury for this patient contact. |
| 20 | `ADT_ARRIVAL_TIME` | DATETIME (Local) |  | The date and time of arrival for this patient contact. |
| 21 | `ADT_ARRIVAL_STS_C_NAME` | VARCHAR | org | The category value corresponding to the arrival status for this patient contact. |
| 22 | `HOSP_ADMSN_TIME` | DATETIME (Local) |  | The date and time that the patient was first admitted to the facility, bedded in the ED, or confirmed for an HOV for this contact, regardless of patient's base patient class. |
| 23 | `ADMIT_CONF_STAT_C_NAME` | VARCHAR |  | The category value corresponding to the (admission) confirmation status for this patient contact. |
| 24 | `HOSP_DISCH_TIME` | DATETIME (Local) |  | The hospital discharge date and time for this patient contact. |
| 25 | `HOSP_ADMSN_TYPE_C_NAME` | VARCHAR | org | The category value corresponding to the admission type for the patient contact. |
| 26 | `ROOM_ID_ROOM_NAME` | VARCHAR |  | The name of the Room record. |
| 27 | `HOSP_SERV_C_NAME` | VARCHAR | org | The category value corresponding to the hospital service for this patient contact. |
| 28 | `MEANS_OF_DEPART_C_NAME` | VARCHAR | org | The category value corresponding to the means of departure of the patient for this patient contact. |
| 29 | `DISCH_DISP_C_NAME` | VARCHAR | org | The category value corresponding to the discharge disposition for this patient contact. |
| 30 | `DISCH_DEST_C_NAME` | VARCHAR | org | The category value corresponding to the discharge destination for this patient contact. |
| 31 | `TRANSFER_FROM_C_NAME` | VARCHAR | org | The category value corresponding to the transfer from location for this patient contact. |
| 32 | `MEANS_OF_ARRV_C_NAME` | VARCHAR | org | The category value corresponding to the means of arrival of the patient for this patient contact. |
| 33 | `ACUITY_LEVEL_C_NAME` | VARCHAR | org | The category value corresponding to the acuity level for this patient contact. |
| 34 | `HOSPIST_NEEDED_YN` | VARCHAR |  | Indicates whether a hospitalist needs to be assigned to the patient for this contact. |
| 35 | `ACCOMMODATION_C_NAME` | VARCHAR |  | The category value corresponding to the room accommodation for this patient contact. |
| 36 | `ACCOM_REASON_C_NAME` | VARCHAR | org | The category value corresponding to the reason for the room accommodation for this patient contact. |
| 37 | `INPATIENT_DATA_ID` | VARCHAR | shared | The unique ID of the Inpatient Data Store record. |
| 38 | `PVT_HSP_ENC_C_NAME` | VARCHAR | org | The category value corresponding to private encounter setting for this patient contact. |
| 39 | `ED_EPISODE_ID` | NUMERIC |  | The unique ID of the Inpatient episode record for the ED visit. |
| 40 | `ED_DISPOSITION_C_NAME` | VARCHAR | org | The disposition of the patient when discharged from the ED. |
| 41 | `ED_DISP_TIME` | DATETIME (Local) |  | The date and time that the disposition was entered. |
| 42 | `FOLLOWUP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 43 | `PROV_CONT_INFO` | VARCHAR |  | The contact information for the patient's follow-up provider. |
| 44 | `OSHPD_ADMSN_SRC_C_NAME` | VARCHAR | org | Office of Statewide Health Planning and Development (OSHPD) Source of Admission |
| 45 | `OSHPD_LICENSURE_C_NAME` | VARCHAR | org | Office of Statewide Health Planning and Development (OSHPD) Licensure of Site |
| 46 | `OSHPD_ROUTE_C_NAME` | VARCHAR | org | Office of Statewide Health Planning and Development (OSHPD) Route of Admission |
| 47 | `INP_ADM_DATE` | DATETIME (Local) |  | Date-time of the inpatient admission. This is the date/time during the hospital encounter when the patient first received a base patient class of inpatient. This can be different than the value for the admission date if the patient was assigned an emergency or outpatient base patient class. |
| 48 | `COPY_TO_PCP_YN` | VARCHAR |  | This item will indicate whether the PCP effective for the patient should be notified upon a pre-determined system event. |
| 49 | `ADOPTION_CASE_YN` | VARCHAR |  | Item to store whether the current contact is related to an adoption case. |
| 50 | `PREOP_TEACHING_C_NAME` | VARCHAR | org | This item describes whether a patient has been offered or given any pre-operative teaching. |
| 51 | `PREOP_PRN_EVAL_C_NAME` | VARCHAR | org | This is a category item that describes whether a patient has been offered or given a pre-operative nurse practitioner evaluation. |
| 52 | `PREOP_PH_SCREEN_C_NAME` | VARCHAR | org | This is a category list that describes whether a patient has been offered or given a pre-operative phone screening. |
| 53 | `LABOR_ACT_BIRTH_C_NAME` | VARCHAR | org | The category value corresponding to the actual birth status of the delivery. |
| 54 | `LABOR_FEED_TYPE_C_NAME` | VARCHAR | org | The category value corresponding to the infant feeding type during the delivery process |
| 55 | `PROC_SERV_C_NAME` | VARCHAR | org | Procedure Based Service Category |
| 56 | `ED_DEPARTURE_TIME` | DATETIME (Local) |  | Date and time the patient left the ED. |
| 57 | `TRIAGE_DATETIME` | DATETIME |  | The date and the time the patient was triaged. |
| 58 | `TRIAGE_STATUS_C_NAME` | VARCHAR | org | The triage status. |
| 59 | `INP_ADM_EVENT_ID` | NUMERIC |  | The event record for the hospital encounter where the patient first received a base patient class of inpatient, making them an inpatient. |
| 60 | `INP_ADM_EVENT_DATE` | DATETIME (Local) |  | Instant of the event creation of the event which caused a patient to become an inpatient patient class. |
| 61 | `INP_DWNGRD_EVNT_ID` | NUMERIC |  | Column to return the event ID of the event that last downgrades the patient from an inpatient patient class to a non-inpatient patient class. |
| 62 | `INP_DWNGRD_DATE` | DATETIME (Local) |  | Column that returns the effective date and time of a patients latest downgrade from an inpatient patient class. |
| 63 | `INP_DWNGRD_EVNT_DT` | DATETIME (Local) |  | Column to return the event date and time of the last event that downgrades a patient from an inpatient patient class to a non-inpatient patient class. |
| 64 | `OP_ADM_DATE` | DATETIME (Local) |  | The date and time during the hospital encounter when the patient first received a base patient class of outpatient. |
| 65 | `EMER_ADM_DATE` | DATETIME (Local) |  | The date and time during the hospital encounter when the patient first received a base patient class of emergency. |
| 66 | `OP_ADM_EVENT_ID` | NUMERIC |  | The event record for the hospital encounter where the patient first received a base patient class of outpatient. |
| 67 | `EMER_ADM_EVENT_ID` | NUMERIC |  | The event record for the hospital encounter where the patient first received a base patient class of emergency. |
| 68 | `PREREG_SOURCE_C_NAME` | VARCHAR | org | Preregistration source value. |
| 69 | `HOV_CONF_STATUS_C_NAME` | VARCHAR |  | This item stores a flag to prevent HOVs from being closed by the end of day batch. |
| 70 | `RELIG_NEEDS_VISIT_C_NAME` | VARCHAR | org | Used to track a patient's visit-specific religious needs. |
| 71 | `DISCHARGE_CAT_C_NAME` | VARCHAR | org | General Category Item for Discharges |
| 72 | `EXP_DISCHARGE_TIME` | DATETIME (Local) |  | The time of expected discharge of the admission for this patient contact. |
| 73 | `BILL_ATTEND_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 74 | `OB_LD_LABORING_YN` | VARCHAR |  | Indicates whether the patient was in labor upon arrival at the hospital. |
| 75 | `OB_LD_LABOR_TM` | DATETIME (Local) |  | The date and time at which labor began. |
| 76 | `TRIAGE_ID_TAG` | VARCHAR |  | The trauma identifier assigned to patient. This number is frequently associated with a pre-printed trauma packet that is used when an accident or other incident results in many patients arriving at the hospital in a short time period. |
| 77 | `TRIAGE_ID_TAG_CMT` | VARCHAR |  | A free-text comment that can be entered along with the trauma identifier or triage ID assigned to the patient. |
| 78 | `TPLNT_BILL_STAT_C_NAME` | VARCHAR | org | The category number for the Transplant Billing Status for a visit. |
| 79 | `ACTL_DELIVRY_METH_C_NAME` | VARCHAR |  | Indicates the delivery method of the last baby delivered on this encounter by this patient. For example, Spontaneous Vaginal Delivery, C-Section - Unspecified, etc. |
| 80 | `PRENATAL_CARE_C_NAME` | VARCHAR | org | Item used to indicate what type of prenatal care the patient has received. |
| 81 | `AMBULANCE_CODE_C_NAME` | VARCHAR | org | The category number for the ambulance code. |
| 82 | `MSE_DATE` | DATETIME (Local) |  | Indicates the date and time of the patient's medical screening exam (MSE). |
| 83 | `ADMIT_PROV_TEXT` | VARCHAR |  | The free text admitting provider for the encounter. |
| 84 | `ATTEND_PROV_TEXT` | VARCHAR |  | The free text attending provider for the encounter. |
| 85 | `PROV_PRIM_TEXT` | VARCHAR |  | The free text primary care provider for the encounter |
| 86 | `PROV_PRIM_TEXT_PHON` | VARCHAR |  | The free text phone number for the primary care provider. |
| 87 | `HOSPITAL_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 88 | `CHIEF_COMPLAINT_C_NAME` | VARCHAR | org | This holds the category number for the chief complaint if the free text chief complaint item is not being used. |
| 89 | `NEED_FIN_CLR_YN` | VARCHAR |  | Indicates whether the patient requires financial clearance on this encounter. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

