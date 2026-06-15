# TIMEOUT_ANSWERS

> This table stores the answers to the timeout questions.

**Overflow family:** [TIMEOUT_ANSWERS_2](TIMEOUT_ANSWERS_2.md)  
**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 99  
**Org-specific columns:** 69

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the timeout record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The contact serial number (CSN) of the contact. |
| 6 | `CONTACT_NUM` | INTEGER |  | This stores the contact number for the contact. |
| 7 | `CNCT_TYPE_C_NAME` | VARCHAR |  | The contact type category number for the timeout record. |
| 8 | `CORRECT_PAT_C_NAME` | VARCHAR | org | The correct patient category number for the timeout question. This stores the result of the "Is this the correct patient?" question for the timeout. |
| 9 | `CORRECT_SITE_C_NAME` | VARCHAR | org | The correct site category number for the timeout question. This stores the result of the "Is this the correct site?" question for the timeout. |
| 10 | `CORRECT_SIDE_C_NAME` | VARCHAR | org | The correct side category number for the timeout question. This stores the result of the "Is this the correct side?" question for the timeout. |
| 11 | `CORRECT_POSITION_C_NAME` | VARCHAR | org | The correct position category number for the timeout question. This stores the result of the "Is this the correct position?" question for the timeout. |
| 12 | `CORRECT_EQUIPMENT_C_NAME` | VARCHAR | org | The correct equipment category number for the timeout question. This stores the result of the "Is this the correct equipment?" question for a the timeout. |
| 13 | `CORRECT_PROC_C_NAME` | VARCHAR | org | The correct procedure category number for the timeout question. This stores the result of the "Is this the correct procedure?" question for the timeout. |
| 14 | `SITE_MARKED_C_NAME` | VARCHAR | org | The site marked status category number for the timeout question. This stores the result of the "Is the site marked?" question for the timeout. |
| 15 | `IMPLANTS_PRESENT_C_NAME` | VARCHAR | org | The implants present category number for the timeout question. This item stores the result of the "Are the implants present?" question for the timeout. |
| 16 | `ANTIBIOTICS_ORDER_C_NAME` | VARCHAR | org | The antibiotics ordered and given status category number for the timeout question. This stores the result of the "Have the antibiotics been ordered and given?" question for the timeout. |
| 17 | `HP_NOTE_COMP_C_NAME` | VARCHAR | org | The H&P note complete status category number for the timeout question. This stores the result of the "H&P note complete?" question for the timeout. |
| 18 | `CONSENTS_VERIFIED_C_NAME` | VARCHAR | org | The consent verified category number for the timeout question. This stores the result of the "Are consents verified?" question for the timeout. |
| 19 | `RAD_STUDIES_AVAIL_C_NAME` | VARCHAR | org | The radiology studies available status category number for the timeout question. This stores the result of the "Are the radiology studies available?" question for the timeout. |
| 20 | `REL_LAB_AVAIL_C_NAME` | VARCHAR | org | The relevant lab result available status category number for the timeout question. This stores the result of the "Are the relevant lab results available?" question for the timeout. |
| 21 | `SAFETY_PREC_C_NAME` | VARCHAR | org | The safety precautions reviewed status category number for the timeout question. This stores the result of the "Are safety precautions reviewed?" question for the timeout. |
| 22 | `ALLERGIES_REVW_C_NAME` | VARCHAR | org | The allergy reviewed status category number for the timeout question. This stores the result of the "Are allergies reviewed?" question for the timeout. |
| 23 | `SURGEON_READY_C_NAME` | VARCHAR | org | The surgeon/physician ready status category number for the timeout question. This stores the result of the "Is the surgeon/physician ready?" question for the timeout. |
| 24 | `PULSE_OXIMETER_ON_C_NAME` | VARCHAR | org | The pulse oximeter is on patient status category number for the timeout question. This stores the result of the "Is a pulse oximeter on the patient?" question for the timeout. |
| 25 | `DIFFICULT_AIRWAY_C_NAME` | VARCHAR | org | The patient has a difficult airway for intubation status category number for the timeout question. This stores the result of the "Does the patient have a difficult airway for intubation?" question for the timeout. |
| 26 | `AIR_ASSIST_AVAIL_C_NAME` | VARCHAR | org | The assistance available for a difficult patient airway status category number for the timeout question. This stores the result of the "Is there assistance available for a difficult patient airway?" question for the timeout. |
| 27 | `HIGH_BLOOD_RISK_C_NAME` | VARCHAR | org | The risk of high blood loss status category number for the timeout question. This stores the result of the "Is there risk of high blood loss?" question for the timeout. |
| 28 | `FLUIDS_AVAIL_C_NAME` | VARCHAR | org | The fluids available for blood status category number for the timeout question. This stores the result of the "Are there adequate fluids available to replenish high blood loss?" question for the timeout. |
| 29 | `ANES_SAFETY_C_NAME` | VARCHAR | org | The anesthesia safety check complete status category number for the timeout question. This stores the result of the "Is the anesthesia safety checklist complete?" question for the timeout. |
| 30 | `REQ_PRODUCTS_C_NAME` | VARCHAR | org | The required products category number for the timeout question. This stores the result of the "Are any blood products & devices required for the procedure available?" question for the timeout. |
| 31 | `OTHER_DOC_VERIFY_C_NAME` | VARCHAR | org | The other documentation verified status category number for the timeout question. This stores the result of the "Is documentation verified?" question for the timeout. |
| 32 | `TEAM_INTRODUCED_C_NAME` | VARCHAR | org | The all team members introduced status category number for the timeout question. This stores the result of the "Have all team members been introduced?" question for the timeout. |
| 33 | `SURGEON_REVIEW_C_NAME` | VARCHAR | org | The surgeon/physician reviewed critical steps status category number for the timeout question. This stores the result of the "Has the surgeon/physician reviewed the critical steps?" question for the timeout. |
| 34 | `ANES_REVIEW_C_NAME` | VARCHAR | org | The anesthesiologist has reviewed patient status category number for the timeout question. This stores the result of the "Has the anesthesiologist reviewed the patient?" question for the timeout. |
| 35 | `STERILE_REVIEW_C_NAME` | VARCHAR | org | The reviewed sterility status category number for the timeout question. This stores the result of the "Has the nursing team reviewed the sterility?" question for the timeout. |
| 36 | `EQUIP_REVIEW_C_NAME` | VARCHAR | org | The reviewed equipment problems status category number for the timeout question. This stores the result of the "Has the nursing staff reviewed the equipment for potential problems?" question for the timeout. |
| 37 | `FLUID_AVAIL_IRRIG_C_NAME` | VARCHAR | org | The fluids available for irrigation status category number for the timeout question. This stores the result of the "Are adequate antibiotics and irrigation fluids available?" question for the timeout. |
| 38 | `COUNTS_CORRECT_C_NAME` | VARCHAR | org | The counts are correct status category number for the timeout question. This stores the result of the "Are counts correct?" question for the timeout. |
| 39 | `SPECIMEN_LABELED_C_NAME` | VARCHAR | org | The specimen labeled status category number for the timeout question. This stores the result of the "Have specimens been labeled?" question for the timeout. |
| 40 | `EQUIP_PROB_ADDR_C_NAME` | VARCHAR | org | The equipment problems addressed status category number for the timeout question. This stores the result of the "Have all new equipment problems been addressed?" question for the timeout. |
| 41 | `RECOVERY_REVIEW_C_NAME` | VARCHAR | org | The recovery issue reviewed status category number for the timeout question. This stores the result of the "Have all recovery issues been reviewed?" question for the timeout. |
| 42 | `INSTANT_OF_ENT_DTTM` | DATETIME (Attached) |  | Stores the instant of entry when a record is edited |
| 43 | `UNOS_ID_VERIFIED_C_NAME` | VARCHAR | org | The United Network for Organ Sharing (UNOS) ID verified status category number for the timeout question. This stores the result of the "Is the UNOS ID verified?" question for the timeout. |
| 44 | `BLOOD_TYPE_VER_C_NAME` | VARCHAR | org | The blood type verified status category number for the timeout question. This stores the result of the "Is the blood type verified?" question for the timeout. |
| 45 | `ORGAN_TYPE_VER_C_NAME` | VARCHAR | org | The blood type verified status category number for the timeout question. This stores the result of the "Is the organ type verified?" question for the timeout. |
| 46 | `ANS_FLT_ID` | VARCHAR |  | Stores the flowsheet template ID used for the timeout. Flowsheets can be used in place of SmartForms to answer questions pertaining to the timeout being performed. |
| 47 | `ANS_FLT_ID_DISPLAY_NAME` | VARCHAR |  | The display name associated with this template. |
| 48 | `FLOWSHEET_DTTM` | DATETIME (Local) |  | This item stores the instant that the flowsheet responses used for the timeout were saved. Flowsheets can be used in place of SmartForms to answer questions pertaining to the timeout being performed. |
| 49 | `STATUS_C_NAME` | VARCHAR | org | The timeout status category number for the timeout. |
| 50 | `PAT_ID_BAND_ON_C_NAME` | VARCHAR |  | The patient ID band on status category number for the timeout question. |
| 51 | `RAD_IMGS_AVAIL_C_NAME` | VARCHAR |  | The radiology images and result available status category number for the timeout question. |
| 52 | `BRIEFING_OCCURRED_C_NAME` | VARCHAR |  | The briefing has occurred status category number for the timeout question. |
| 53 | `TEAM_PRESENT_C_NAME` | VARCHAR |  | The all team members present during timeout status category number for the timeout question. |
| 54 | `HANDOFF_TO_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 55 | `HANDOFF_TO_STAFF_C_NAME` | VARCHAR | org | The procedural staff type category number for the handoff to staff type question in the timeout. This stores the result of "Handoff to (staff type)?" question for the timeout. |
| 56 | `HNDOFF_FRM_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 57 | `SITE_MARK_VISIBLE_C_NAME` | VARCHAR |  | The site marks visible after prep status category number for the timeout question. |
| 58 | `FIRE_RISK_C_NAME` | VARCHAR | org | The fire risk level category number for the timeout question. |
| 59 | `TEAM_AGREE_C_NAME` | VARCHAR | org | The all team members agreed to proceed status category number for the timeout question. |
| 60 | `ANES_PREOP_NOTE_C_NAME` | VARCHAR |  | The anesthesia pre-op note complete status category number for the timeout question. |
| 61 | `MEDS_LABELED_C_NAME` | VARCHAR |  | The medication labeled status category number for the timeout question. This item is used during the timeout workflow. |
| 62 | `PT_MED_HX_REVIEW_C_NAME` | VARCHAR | org | The patient medical history reviewed status category number for the timeout question. |
| 63 | `ASA_CLASS_REVIEW_C_NAME` | VARCHAR | org | The American Society of Anesthesiologists (ASA) classification reviewed status category number for the timeout question. |
| 64 | `ANES_TYPE_REVIEW_C_NAME` | VARCHAR | org | The anesthesia type reviewed status category number for the timeout question. |
| 65 | `PT_USE_ANTICOAG_C_NAME` | VARCHAR | org | The patient use of anticoagulants reviewed status category number for the timeout question. |
| 66 | `PRE_SURG_MEDS_C_NAME` | VARCHAR | org | The pre-procedure medications reviewed status category number for the timeout question. |
| 67 | `CORRECT_PROC_DOC_C_NAME` | VARCHAR | org | The correct procedure documented status category number for the timeout question. |
| 68 | `SURG_INSTR_REVIEW_C_NAME` | VARCHAR | org | The procedural instructions reviewed status category number for the timeout question. |
| 69 | `ANES_INSTR_REVIEW_C_NAME` | VARCHAR | org | The anesthesia instructions reviewed status category number for the timeout question. |
| 70 | `LDA_REVIEW_C_NAME` | VARCHAR | org | The Lines, Drains, and Airways (LDAs) reviewed status category number for the timeout question. |
| 71 | `PT_READY_TRANSFER_C_NAME` | VARCHAR | org | The patient ready to transfer status category number for the timeout question. |
| 72 | `NEXT_DEPT_CONTACT_C_NAME` | VARCHAR | org | The receiving department contact category number for the timeout question. |
| 73 | `PERI_PRO_COD_DISC_C_NAME` | VARCHAR | org | The peri-procedural code discussed status category number for the timeout question. |
| 74 | `MEDS_VERB_CONF_C_NAME` | VARCHAR | org | The available meds verbally confirmed status category number for the timeout question. This stores the response category number for whether the meds are available on the procedural field. The goal is to do a quick verification prior to incision and state what meds are on the field for physician use. |
| 75 | `VTE_PROPH_START_C_NAME` | VARCHAR | org | The VTE prophylaxis started status category number for the timeout question. This stores the response category number for whether the patient had a Venous Thromboembolism (VTE) prophylaxis started prior to the start of the procedure. |
| 76 | `AUTH_USER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 77 | `MEDS_SECURED_C_NAME` | VARCHAR | org | The Medications Secured category number which indicates whether medications not administered have been secured. |
| 78 | `PAT_USE_BETABLOCK_C_NAME` | VARCHAR | org | The patient use of beta blockers category number for the timeout which indicates whether a beta blocker plan was reviewed. |
| 79 | `PREFCARD_CHNG_REV_C_NAME` | VARCHAR |  | The preference card changes reviewed category number for the timeout which indicates whether preference card changes were reviewed. |
| 80 | `ANES_PROC_COMP_C_NAME` | VARCHAR | org | The anesthesia procedure complete category number for the timeout which indicates whether necessary anesthesia procedures are complete. |
| 81 | `PROC_LEN_REV_C_NAME` | VARCHAR | org | The anticipated procedure length category number for the timeout which indicates whether the anticipated length of procedure has been confirmed. |
| 82 | `NORMOTHRM_ASSURED_C_NAME` | VARCHAR | org | The normothermia assured category number for the timeout which indicates whether normothermia has been assured for the patient. |
| 83 | `SITE_PREP_READY_C_NAME` | VARCHAR | org | The site prep completed category number for the timeout which indicates whether the skin prep (Betadine, Alcohol, etc.) is complete. |
| 84 | `ANESTH_SITE_MARK_C_NAME` | VARCHAR |  | The anesthesia site marked category number for the timeout which indicates whether the anesthesia site has been marked. |
| 85 | `CORRECT_LAT_C_NAME` | VARCHAR | org | The correct laterality category number for the timeout which indicates whether the laterality of the procedure has been verified. |
| 86 | `PAT_REP_EDU_C_NAME` | VARCHAR | org | The patient or legal representative educated on policies category number for the timeout which indicates whether the patient and family have been educated on organizational policies. |
| 87 | `PREP_SOL_DRIED_C_NAME` | VARCHAR |  | The status category number for the procedural timeout question that indicates if the solution used for surgical skin prep was dry or not before draping. |
| 88 | `PREPSOL_POOL_PREV_C_NAME` | VARCHAR |  | The status category number for the procedural timeout question that indicates if the surgical site prep solution was prevented from pooling. |
| 89 | `PREPSOL_INSTR_FOL_C_NAME` | VARCHAR |  | The status category number for the procedural timeout question that indicates if the pre-op site prep solution instructions were followed. |
| 90 | `COMP_AT_APPROP_TM_C_NAME` | VARCHAR | org | The status category number for the procedural timeout question that indicates whether or not a timeout was completed at the appropriate time according to organizational policies. |
| 91 | `BLOOD_PRODUCT_ORD_C_NAME` | VARCHAR |  | The status category number for the procedural timeout question that indicates whether or not blood products were ordered. |
| 92 | `PREG_TEST_COMP_C_NAME` | VARCHAR | org | The status category number for the procedural timeout question that indicates whether a pregnancy test was completed prior to surgery. |
| 93 | `EBL_CONFIRMED_C_NAME` | VARCHAR | org | The status category number for the procedural timeout question that indicates if all surgical staff and surgeons present agree on the patient's estimated blood loss during surgery. |
| 94 | `FIRE_SURG_SITE_HT_C_NAME` | VARCHAR | org | The category number for the Fire Risk Surgical Site Height item. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 95 | `FIRE_OXYGEN_SRC_C_NAME` | VARCHAR | org | The category number for the Fire Risk Open Oxygen Source item. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 96 | `FIRE_IGNITION_SRC_C_NAME` | VARCHAR | org | The category number for the Fire Risk Ignition Source item. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 97 | `HIGH_RISK_DTTM` | DATETIME (Local) |  | The date and time that the fire risk was upgraded to a high fire risk. |
| 98 | `HIGH_RISK_CMT` | VARCHAR |  | A comment associated with the fire risk upgrade to a high fire risk. |
| 99 | `SHARPS_SAFETY_C_NAME` | VARCHAR |  | The sharps safety category number for the timeout question that indicates if sharp safety was followed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

