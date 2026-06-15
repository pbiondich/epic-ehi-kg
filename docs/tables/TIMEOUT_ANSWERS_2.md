# TIMEOUT_ANSWERS_2

> This table stores the answers to the timeout questions.

**Overflow of:** [TIMEOUT_ANSWERS](TIMEOUT_ANSWERS.md)  
**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 81  
**Org-specific columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the timeout record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `ISOLATN_STAT_REVD_C_NAME` | VARCHAR |  | Indicates whether the isolation status of the patient was reviewed prior to surgery. |
| 5 | `PARALYSIS_NEEDED_C_NAME` | VARCHAR | org | Indicates if any paralytic drugs will be used during the surgery. |
| 6 | `BLD_GLUCOSE_REVD_C_NAME` | VARCHAR | org | Indicates if the patient's blood glucose was reviewed prior to surgery. |
| 7 | `VENT_NEEDED_POST_C_NAME` | VARCHAR |  | Indicates if a ventilator will be needed for the patient after the surgery. |
| 8 | `POSTOP_PAIN_PLAN_C_NAME` | VARCHAR |  | Indicates if the plans for post-op pain management were made and reviewed prior to surgery. |
| 9 | `WOUND_CLASS_CONF_C_NAME` | VARCHAR | org | This item stores whether or not wound classification was confirmed during the timeout. |
| 10 | `WARM_MEAS_ADDRD_C_NAME` | VARCHAR | org | This item stores whether or not warming measures were addressed during the timeout. |
| 11 | `DIABET_STAT_ADDRD_C_NAME` | VARCHAR | org | This item stores whether or not the patient's diabetic status has been addressed during the timeout. |
| 12 | `IMPLANT_SIZE_VER_C_NAME` | VARCHAR | org | Indicates whether implant sizes were confirmed for this procedure. |
| 13 | `PAT_LABELS_AVAIL_C_NAME` | VARCHAR |  | Indicates if the patient labels were available for a timeout. |
| 14 | `REV_NPO_STATUS_C_NAME` | VARCHAR |  | Indicates if the Nothing by Mouth (NPO) status was reviewed for a timeout. |
| 15 | `REV_INR_VALUE_C_NAME` | VARCHAR |  | Indicates if the International Normalized Ratio (INR) value was reviewed for a timeout. |
| 16 | `REV_APTT_VALUE_C_NAME` | VARCHAR |  | Indicates if the Activated Partial Thromboplastin Time (APTT) value was reviewed for a timeout |
| 17 | `REV_PAT_ANTIDIAB_C_NAME` | VARCHAR |  | Indicates if the patient's use of antidiabetics was reviewed for a timeout. |
| 18 | `REV_PAT_ANTIDIUR_C_NAME` | VARCHAR |  | Indicates if the patient's use of antidiuretics was reviewed for a timeout. |
| 19 | `REV_PAT_COAG_STAT_C_NAME` | VARCHAR |  | Indicates if the patient's coagulation status was reviewed for a timeout. |
| 20 | `DOC_OBJ_INT_LEFT_C_NAME` | VARCHAR |  | Indicates if objects intentionally left in patient were documented for a timeout. |
| 21 | `REV_OBJ_INT_LEFT_C_NAME` | VARCHAR |  | Indicates if objects intentionally left in patient were reviewed for a timeout. |
| 22 | `REV_IV_THER_INSTR_C_NAME` | VARCHAR |  | Indicates if the intravenous (IV) therapy instructions were reviewed for a timeout. |
| 23 | `REV_PAIN_MED_INST_C_NAME` | VARCHAR |  | Indicates if the pain medication instructions were reviewed for a timeout. |
| 24 | `REV_MED_INSTR_C_NAME` | VARCHAR |  | Indicates if the medication instructions were reviewed for a timeout. |
| 25 | `REV_VENT_OX_INSTR_C_NAME` | VARCHAR |  | Indicates if the ventilation/oxygenation instructions were reviewed for a timeout. |
| 26 | `REV_POSTOP_ASSMNT_C_NAME` | VARCHAR |  | Indicates if the post-operative assessment instructions were reviewed for a timeout. |
| 27 | `REV_LDA_INSTR_C_NAME` | VARCHAR |  | Indicates if the Lines, Drains, and Airways (LDA) instructions were reviewed for a timeout. |
| 28 | `REV_DIET_INSTR_C_NAME` | VARCHAR |  | Indicates if the dietary instructions were reviewed for a timeout. |
| 29 | `REV_LIQD_IN_INSTR_C_NAME` | VARCHAR |  | Indicates if the liquid intake instructions were reviewed for a timeout. |
| 30 | `REV_WND_CRE_INSTR_C_NAME` | VARCHAR |  | Indicates if the wound care instructions were reviewed for a timeout. |
| 31 | `REV_FOL_UP_PLAN_C_NAME` | VARCHAR |  | Indicates if the follow-up plan was reviewed for a timeout. |
| 32 | `DISCHRG_SUM_WRTTN_C_NAME` | VARCHAR |  | Indicates if the discharge summary was written for a timeout. |
| 33 | `REV_DISCHRG_INSTR_C_NAME` | VARCHAR |  | Indicates if the discharge instructions were reviewed for a timeout. |
| 34 | `REV_TRANSFER_FORM_C_NAME` | VARCHAR |  | Indicates if the transfer form was reviewed for a timeout. |
| 35 | `REV_PAT_HOME_MEDS_C_NAME` | VARCHAR |  | Indicates if the patient's use of home medications was reviewed for a timeout. |
| 36 | `REV_PAT_PROB_LIST_C_NAME` | VARCHAR |  | Indicates if the patient's problem list was reviewed for a timeout. |
| 37 | `IMMUNOSUPR_ORDER_C_NAME` | VARCHAR | org | Indicates whether immunosuppressants were ordered and given to the patient for this procedure. |
| 38 | `SURGICAL_ATTIRE_YN` | VARCHAR |  | Indicates whether everyone is wearing appropriate surgical attire for this procedure. |
| 39 | `PAT_ORAL_CAV_SRCH_C_NAME` | VARCHAR |  | Indicates whether the patient's oral cavity was searched for foreign objects after this procedure. |
| 40 | `CONSENTS_SIGNED_C_NAME` | VARCHAR | org | Stores the result of the "operative consents signed" question for a timeout. |
| 41 | `WEIGHT_REVIEWED_C_NAME` | VARCHAR | org | Verify that the patient's weight has been reviewed prior to the procedure. |
| 42 | `LAST_VOID_REVD_C_NAME` | VARCHAR | org | Verify that the time of the patient's last void (bathroom visit) has been reviewed prior to the procedure |
| 43 | `IMPROVMNT_OPP_REV_C_NAME` | VARCHAR | org | Verify that opportunities for improvement (i.e. communication, patient interaction, case outcomes, etc) were reviewed prior to procedure |
| 44 | `PREOP_DIAG_REV_C_NAME` | VARCHAR | org | Stores the result of the "Pre-Operative Diagnosis Reviewed?" question for a timeout. |
| 45 | `PAT_SPEC_NEEDS_C_NAME` | VARCHAR | org | Stores the result of the "Patient Special Needs Reviewed?" question for a timeout. |
| 46 | `PROC_SPEC_NEEDS_C_NAME` | VARCHAR | org | Stores the result of the "Procedure Special Needs Reviewed?" question for a timeout. |
| 47 | `CORRECT_INSTRUMNT_C_NAME` | VARCHAR | org | Stores the result of the "Correct Instruments?" question for a timeout. |
| 48 | `PAT_CLASS_REV_C_NAME` | VARCHAR | org | Stores the result of the "Patient Class Reviewed?" question for a timeout. |
| 49 | `POSTOP_DEST_REV_C_NAME` | VARCHAR | org | Stores the result of the "Post-op Destination Reviewed?" question for a timeout. |
| 50 | `SKIN_ASMT_COMP_C_NAME` | VARCHAR | org | This item stores if the skin assessment has been completed. |
| 51 | `ULC_PRV_ASMT_COMP_C_NAME` | VARCHAR | org | This item stores that the pressure ulcer prevention assessment has been completed. |
| 52 | `ADDL_INFO` | VARCHAR |  | This is a free-text item for additional notes. It can use a note template to document necessary comments during a timeout. |
| 53 | `VTE_PROPHYLAX_ORD_C_NAME` | VARCHAR | org | The category ID of whether a venous thromboembolism prophylaxis has been ordered prior to the start of a procedure. |
| 54 | `REV_POS_OUTCOME_C_NAME` | VARCHAR | org | The category ID of whether the positive outcomes were reviewed. |
| 55 | `PROT_ADHERED_C_NAME` | VARCHAR | org | The category ID of whether the safe surgery checklist protocol was adhered to. |
| 56 | `PROT_ADHERED_COM` | VARCHAR |  | The free text comments related to the whether the safe surgery checklist protocol was adhered to. |
| 57 | `CORRECT_ACCESS_C_NAME` | VARCHAR | org | Indicates whether the accessed vein/artery is the correct access. |
| 58 | `PAT_REEVALUATED_C_NAME` | VARCHAR | org | Indicates the patient was re-evaluated immediately prior to sedation. |
| 59 | `PRIM_SURG_SCRUB_YN` | VARCHAR |  | Whether or not the primary surgeon was scrubbed in during the timeout. |
| 60 | `VISUAL_VERBAL_VER_YN` | VARCHAR |  | Whether or not visual and verbal verification was performed by the primary surgeon during the timeout. |
| 61 | `MATCH_RUN_VER_YN` | VARCHAR |  | Whether or not the match run was verified during the timeout. |
| 62 | `SSN_9CH_OR_9FN_VER_YN` | VARCHAR |  | Whether or not the Social Security Number (SSN), 9CH, or 9FN was verified during the timeout. |
| 63 | `ATTEST_STATUS_C_NAME` | VARCHAR |  | This column indicates whether or not an attestation is active or deleted. |
| 64 | `POWI_REGISTRATION_DATE` | DATETIME |  | This item stores the post-op infection registration date. |
| 65 | `TXP_DONOR_OVD_RSN_C_NAME` | VARCHAR | org | An override reason for the organ check-in. |
| 66 | `ORGAN_VERIFIED_FOR_RECPNT_YN` | VARCHAR |  | Indicates whether the donor organ was verified to match the intended organ for the recipient. |
| 67 | `INTND_RECIP_UNIQ_IDNT_VERIF_YN` | VARCHAR |  | Indicates whether the unique identifier of the intended transplant recipient was verified during the pre-organ recovery verification. 'Y' indicates that the intended recipient's unique identifier had been marked as verified. 'N' and NULL indicate that the intended recipient's unique identifier was not marked as verified. |
| 68 | `VESSEL_VERIFY_TYPE_C_NAME` | VARCHAR | org | Select the type of vessel verification being performed. |
| 69 | `VESSEL_VERIFY_DONOR_IDENTIFIER` | VARCHAR |  | Enter the ID of the vessel donor. |
| 70 | `VESSEL_VERIFY_DONOR_ABO_C_NAME` | VARCHAR |  | Select the blood type of the vessel donor. |
| 71 | `VESSEL_VERIFY_RECIP_IDENTIFIER` | VARCHAR |  | Enter the ID of the vessel recipient. |
| 72 | `VESSEL_VERIFY_RECIP_ABO_C_NAME` | VARCHAR |  | Select the blood type of the vessel recipient. |
| 73 | `VESSEL_VERIFY_ABO_COMPAT_YN` | VARCHAR |  | Confirm that the vessel donor and recipient are blood type compatible or intended incompatible. |
| 74 | `VESSEL_VERIFY_14_DAYS_YN` | VARCHAR |  | Confirm that the vessels are within 14 days of their recovery date. |
| 75 | `VESSEL_VERIFY_INFECT_TEST_YN` | VARCHAR |  | Confirm that the vessel donor's infectious disease testing results have been verified. |
| 76 | `VESSEL_VERIFY_BEFORE_ANAST_YN` | VARCHAR |  | Confirm that vessel verification was completed before vessel anastomosis start time. |
| 77 | `SMARTTEXT_ID` | VARCHAR | FK→ | This column contains the note template ID associated with an Anesthesia attestation. |
| 78 | `SMARTTEXT_ID_SMARTTEXT_NAME` | VARCHAR |  | The name of the SmartText record. |
| 79 | `ORGAN_DONOR_HIV_POS_YN` | VARCHAR |  | Indicates whether the organ donor associated with this ABO timeout was positive for HIV. |
| 80 | `RECIP_CONSENT_HIV_YN` | VARCHAR |  | Indicates verification that the transplant recipient is living with HIV and is willing to accept an organ from a donor with HIV. |
| 81 | `RECOV_PROTOCOL_REVIEW_C_NAME` | VARCHAR | org | Indicates whether the patient's recovery protocol was discussed during the timeout process. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SMARTTEXT_ID` | [SMARTTEXT](SMARTTEXT.md) | sole_pk | high |

