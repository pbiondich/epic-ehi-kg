# EPISODE_2

> This table supplements the EPISODE table. It contains additional information about episodes. When a provider sees a patient several times for an ongoing condition, such as prenatal care, these encounters can be linked to a single Episode of Care.

**Overflow of:** [EPISODE](EPISODE.md)  
**Primary key:** `EPISODE_ID`  
**Columns:** 43  
**Org-specific columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EPISODE_ID` | NUMERIC | PK | The unique ID of the episode of care record. NOTE: This table is filtered to include only non-inpatient episodes. Inpatient episode data can be found in the table IP_EPISODE_LINK (first released with system 2002). |
| 2 | `DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 3 | `RXENROLL_LAST_EDIT_USER_ID` | VARCHAR |  | The user ID for whoever last updated the pharmacy enrollment. |
| 4 | `RXENROLL_LAST_EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `RXENROLL_LAST_EDIT_DTTM` | DATETIME (Local) |  | The date and time the pharmacy enrollment was last updated. |
| 6 | `ENROLL_PROG_C_NAME` | VARCHAR | org | The current enrollment program for the pharmacy. |
| 7 | `RXENROLL_NOTE_ID` | VARCHAR |  | Summary note documented on this episode |
| 8 | `RXENROLL_ENROLLMENT_DATE` | DATETIME |  | The date the patient was enrolled in the program |
| 9 | `RXENROLL_DISENROLL_DATE` | DATETIME |  | The date the patient was unenrolled from the program. |
| 10 | `RXENROLL_DECLINE_DATE` | DATETIME |  | The date the patient was declined enrollment (or declined to enroll) in the program |
| 11 | `RXENROLL_STATUS_C_NAME` | VARCHAR |  | The current enrollment status |
| 12 | `CRT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The patient contact serial number that auto created this episode. |
| 13 | `CMGMT_STATUS_C_NAME` | VARCHAR |  | Stores the status of the case episode. Enrolling - The manager is working to enroll the patient in a case management program. Open - The manager is performing ongoing outreach with the patient. Closed - The patient is no longer enrolled in case management, or they opted out of case management. |
| 14 | `CMGMT_SENSITIVITY_C_NAME` | VARCHAR | org | Store the sensitivity flag for security restricted case episodes. If your organization has implemented break-the-glass, this sensitivity flag can be used to restrict access to the case episode. |
| 15 | `CMGMT_ENROLLMENT_RSN_C_NAME` | VARCHAR | org | Stores the reason the patient was enrolled in case management. |
| 16 | `CMGMT_ENROLLING_STEP_C_NAME` | VARCHAR | org | Stores the enrolling step that specifies the current step of enrollment for the case episode. |
| 17 | `CMGMT_CLOSED_REASON_C_NAME` | VARCHAR | org | Stores the reason the case episode is closed. |
| 18 | `ENROLL_ID` | NUMERIC | FK→ | The research study-patient association (LAR) record ID for this episode. |
| 19 | `PREG_CHORIONIC_C_NAME` | VARCHAR |  | For a pregnancy with multiple fetuses, indicates if the fetuses have individual or a shared chorionic and amniotic sacs. |
| 20 | `PLAN_ADOPT_TYPE_C_NAME` | VARCHAR | org | This item indicates if the mother plans to give the baby up for adoption and if so, what type of adoption or arrangement is planned. |
| 21 | `SUSPECTED_FD_YN` | VARCHAR |  | This item indicates whether a suspected fetal demise has occurred in the pregnancy. |
| 22 | `PLAN_CIRCUMCISION_C_NAME` | VARCHAR |  | This item is used to indicate whether the parents have requested a circumcision after the baby is born. |
| 23 | `PLAN_DELIVER_BY_GA` | INTEGER |  | This item represents the gestational age (in weeks of pregnancy) at when the patient and provider expect the delivery to occur. |
| 24 | `PLAN_DEL_METHOD_C_NAME` | VARCHAR |  | This item captures the planned method of delivery as documented prior to labor. |
| 25 | `CMGMT_DECLINE_REASON_C_NAME` | VARCHAR | org | Documents the reason a patient/client refused coordinated case management services. |
| 26 | `HSPC_ADD_DISCUSSED_WITH_PAT_YN` | VARCHAR |  | This item indicates whether or not a hospice election addendum was discussed with the patient for this episode. |
| 27 | `HSPC_ADD_REQUESTED_WITH_PAT_YN` | VARCHAR |  | This item indicates whether or not a hospice election addendum was requested for this episode. |
| 28 | `HSPC_ADD_DISCUSSED_USER_ID` | VARCHAR |  | The unique user record ID that is frequently used to link to the CLARITY_EMP table. |
| 29 | `HSPC_ADD_DISCUSSED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 30 | `HSPC_ADD_DISCUSSED_DATE` | DATETIME |  | The date the addendum was discussed with the patient. |
| 31 | `CMGMT_ENROLL_DATE` | DATETIME |  | Documents the enrollment date, which is the date on which a patient or client's status becomes active and the patient or client starts receiving Coordinated Care Management services. Refer to CMGMT_CALC_ENROLL_DATE for more robust reporting. |
| 32 | `CMGMT_ENROLL_CALC_DATE` | DATETIME |  | This virtual item contains a calculated enrollment date determined from the user- documented enrollment date (CMGMT_ENROLL_DATE, HSB-18030) or the Case Management History related group (I HSB 18400). If the overall episode status (CMGMT_STATUS_C, I HSB 18010) is 1-Enrolling, the value will be blank. If the overall status is anything besides 1-Enrolling, the value will be set to the user- documented Enrollment Date, if it exists. Otherwise, the value will be set to the date (ACTION_UTC_DTTM) the status (ASSOC_CMGMT_STATUS_C) originally changed to 2-Active, unless the status was changed to 1-Enrolling more recently. |
| 33 | `CMGMT_TRIGGERING_CLASSIFIER_ID` | VARCHAR |  | The classifier (CFR record) that triggered the creation of this case. |
| 34 | `CMGMT_TRIGGERING_CLASSIFIER_ID_CLASSIFIER_NAME` | VARCHAR |  | The title of the classifier record. |
| 35 | `CMGMT_TRIGGERING_CLAIM_ID` | NUMERIC |  | The claim that caused the creation of this case. |
| 36 | `PREG_CORD_BLOOD_PLANS_C_NAME` | VARCHAR | org | This item indicates the patient's plans for umbilical cord blood. |
| 37 | `LINKED_SERVICE_PLAN_ID` | NUMERIC |  | The service plan associated with this episode. |
| 38 | `MC_TG_RSLV_DATE` | DATETIME |  | Stores the resolve date for this Tapestry bundle. |
| 39 | `BPC_ID` | NUMERIC | FK→ | Stores the bundled episode terms id. |
| 40 | `BPC_ID_BPC_NAME` | VARCHAR |  | The name of the bundled episode terms record. |
| 41 | `BPC_CSN_ID` | NUMERIC |  | Stores the bundled episode terms contact serial number. |
| 42 | `TREATMENT_CAREPLAN_ID` | VARCHAR |  | Link to the treatment list |
| 43 | `CMGMT_COMPLEXITY_C_NAME` | VARCHAR | org | The complexity category ID of the episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BPC_ID` | [BND_EPSD_TERMS](BND_EPSD_TERMS.md) | sole_pk | high |
| `CRT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

## Joined in

Inbound joins are tracked on the logical base [EPISODE](EPISODE.md).

