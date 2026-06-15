# PAT_ENC_6

> This table supplements the PAT_ENC, PAT_ENC_2, PAT_ENC_3, PAT_ENC_4, and PAT_ENC_5 tables. It contains additional information related to patient encounters or appointments.

**Overflow of:** [PAT_ENC](PAT_ENC.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 54  
**Org-specific columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `LINKED_ENC_CSN` | NUMERIC |  | The unique contact serial number of the visit that represents the official visit. Intended for (FINLAND) ad hoc encounters that need to be associated with an official visit. |
| 5 | `LMP_PRECISION_C_NAME` | VARCHAR | org | The uncertainty of the last menstrual period date stored in the PAT_ENC.LMP_DATE column. |
| 6 | `PLANNED_BILL_AREA_ID` | NUMERIC |  | Used to track what the bill area was for an appointment at the time of check in. |
| 7 | `PLANNED_BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 8 | `BCRA_BRCA_GENE_MUT_C_NAME` | VARCHAR |  | The patient's risk factor category number for the Presence of BRCA 1/2 Mutation breast cancer risk factor. |
| 9 | `SVC_TARGET_EFFORT_YN` | VARCHAR |  | Flag to indicate that additional effort was needed on behalf of staff to work this encounter in order to meet service targets. |
| 10 | `OUTPAT_VISIT_GRP_C_NAME` | VARCHAR | org | Used to indicate additional visit type information for reporting purposes. |
| 11 | `PSYCH_ARRIVAL_C_NAME` | VARCHAR | org | Indicates the method of arrival for the patient for psychiatric care. |
| 12 | `PLAN_RECUR_TREAT_YN` | VARCHAR |  | Indicates whether the visit is part of a planned recurring treatment period. |
| 13 | `HUS_VISIT_TYPE_C_NAME` | VARCHAR | org | Additional visit type information required for HUS visits for reporting purposes. |
| 14 | `SOCIAL_SRVC_AREA_C_NAME` | VARCHAR | org | Indicates the social care service area for the visit. |
| 15 | `EXT_LTC_PAT_YN` | VARCHAR |  | Indicates whether a patient is a long term care patient at an external organization. |
| 16 | `VETERAN_ENC_MED_CVG_C_NAME` | VARCHAR | org | This holds the medical coverage level for a given patient encounter. The medical coverage denotes the level of coverage a patient is using for a given encounter. The coverage level determines how much the patient will be billed. This column is frequently used to link to the ZC_VETERAN_MED_CVG table. |
| 17 | `VETERAN_BILLING_CODE_C_NAME` | VARCHAR | org | This holds the veteran billing code for a given patient encounter. The billing code denotes the type of appointment that was given which in turns determines how much the patient should be billed. This column is frequently used to link to the ZC_VETERAN_BILLING_CODE table. |
| 18 | `ED_REF_CALLBAK_D_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 19 | `RFV_USED_TO_SCHED_C_NAME` | VARCHAR | org | Stores the reason for visit the user selected to schedule an appointment through MyChart. |
| 20 | `BMI_PERCENTILE` | NUMERIC |  | This item stores the patient's BMI percentile. This item will be null for ages greater than 20, and is calculated based on the patient's height, weight, and sex. |
| 21 | `CREATION_ORD_ID` | NUMERIC |  | The ID number of the order which created the patient contact. |
| 22 | `EXT_TX_STATUS_C_NAME` | VARCHAR | org | An optional item used to document the encounter's External Transportation Status/Needs. There is no standard functionality that is driven by this item. This item can be used to drive reporting, confirmation errors, or WQ activities. |
| 23 | `EXT_TX_STATUS_CMT` | VARCHAR |  | An optional item used to document the encounter's External Transportation Comments. There is no standard functionality that is driven by this item. This item can be used to driver reporting, confirmation errors, or WQ activities. |
| 24 | `EXT_ACCM_STATUS_C_NAME` | VARCHAR | org | An optional item used to document the encounter's External Accommodation Status/Needs. There is no standard functionality that is driven by this item. This item can be used to driver reporting, confirmation errors, or workqueue activities. |
| 25 | `EXT_ACCM_STATUS_CMT` | VARCHAR |  | An optional item used to document the encounter's External Accommodation Comments. There is no standard functionality that is driven by this item. This item can be used to driver reporting, confirmation errors, or workqueue activities. |
| 26 | `SG_AT_RISK_IND_C_NAME` | VARCHAR | org | Stores the at risk indicator for a specific visit. |
| 27 | `SG_FC_STATUS_C_NAME` | VARCHAR | org | Stores the financial counselling status for a specific visit. |
| 28 | `ELIG_PLAN_SELECT_YN` | VARCHAR |  | This item indicates if an eligibility plan is currently selected for this encounter. |
| 29 | `SG_MOH_URGENCY_C_NAME` | VARCHAR | org | Used to indicate whether an appointment is urgent or non-urgent for Ministry of Health regulatory reporting. |
| 30 | `SG_NAMED_REFERRAL_YN` | VARCHAR |  | Used for validation of the patient class and regulatory reporting for whether a patient was referred to a particular provider. |
| 31 | `SG_PAT_REQUEST_YN` | VARCHAR |  | Used to indicate whether a patient requested to see a particular doctor and thus should be a private patient. |
| 32 | `SG_TREATMENT_PROG_C_NAME` | VARCHAR | org | Used to indicate the type of service programme that the appointment is assigned to. |
| 33 | `SG_APPT_RATIONALE_C_NAME` | VARCHAR | org | Used to indicate whether an appointment was the earliest possible, at a patient request, at a doctor request, or force booked. This drives regulatory reporting functionality. |
| 34 | `EVISIT_RFV_C_NAME` | VARCHAR | org | The category value of the reason for the e-visit. This number links to the value stored in the ON_DEMAND_VIDEO_VISIT_C of the ZC_ON_DEMAND_VIDEO_VISIT table. |
| 35 | `EVISIT_YN` | VARCHAR |  | Indicates whether this encounter is an E-Visit. This will be set only for appointment-based E-Visits. |
| 36 | `EVISIT_TLH_ALLOWED_SUBLOC_C_NAME` | VARCHAR |  | The sublocation where the patient indicated they were currently located for a video visit or an e-visit. This information comes from a category value stored in I SER 32510. |
| 37 | `EVISIT_TLH_ALLOWED_LOC_C_NAME` | VARCHAR | org | The country where the patient indicated they were currently located for a video visit or an e-visit. This information comes from a category value stored in I ECT 70150. |
| 38 | `APPT_AUTH_STATUS_C_NAME` | VARCHAR |  | The authorization status of an appointment based on the information stored in any authorization records linked to an appointment (EPT-23025). |
| 39 | `EVISIT_NEW_STATUS_C_NAME` | VARCHAR |  | The current workflow status of an e-visit encounter. Values include 1-In Progress, 2-Submitted, 3-Under Review, 4-Complete, 5-Expired, 6-Returned to Patient, and 7-Cancelled |
| 40 | `LAB_RESP_USER_ID` | VARCHAR |  | The unique ID of the phlebotomist (EMP) currently responsible for the patient's lab draws for this encounter. |
| 41 | `LAB_RESP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 42 | `EXT_MEDS_UPD_INST_UTC_DTTM` | DATETIME (UTC) |  | Contains the most recent instant of update for external medications in external orders encounters. |
| 43 | `INTF_PRIMARY_PAT_ENC_CSN_ID` | NUMERIC |  | Contains the CSN of the primary interface contact for this encounter. |
| 44 | `OVERRIDE_BCRA_NUM_BIOPSY_C_NAME` | VARCHAR |  | The override value for the number of biopsies. The override value is used in the calculation of the Gail model risk score. |
| 45 | `OVERRIDE_BCRA_RACE_C_NAME` | VARCHAR |  | The override value for patient race. The override value is used in the calculation of the Gail model risk score. |
| 46 | `OVERRIDE_GAIL_FACTOR_USER_ID` | VARCHAR |  | The user who overrode the factors for the Gail model. |
| 47 | `OVERRIDE_GAIL_FACTOR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 48 | `OVERRIDE_GAIL_FACTOR_DTTM` | DATETIME (Local) |  | The instant when the Gail factors were overridden. |
| 49 | `VETERAN_COVERAGE_ENC_YN` | VARCHAR |  | Indicates whether the patient's encounter is expected to be covered by their VA coverage |
| 50 | `ADJUD_TO_PHARMACY_COVERAGE_YN` | VARCHAR |  | Indicates whether we are adjudicating one or more of the medications administered to the patient to a pharmacy coverage. 'Y' indicates that medications will be adjudicated. 'N' or NULL indicate that no medications will be adjudicated to a pharmacy coverage. |
| 51 | `TLH_APRV_SUBLOC_C_NAME` | VARCHAR |  | This contains the latest approved patient sublocation for an encounter. Sublocations are considered approved if a patient is able to schedule a video visit in that sublocation, or if it is manually set by a staff member during or after scheduling. |
| 52 | `TLH_APRV_LOC_C_NAME` | VARCHAR |  | This contains the latest approved patient location for an encounter. Locations are considered approved if a patient is able to schedule a video visit in that location, or if it is manually set by a staff member during or after scheduling. |
| 53 | `ENC_CLOSE_UTC_DTTM` | DATETIME (UTC) |  | The instant the visit was closed |
| 54 | `SPLIT_FILING_ORDER_YN` | VARCHAR |  | Indicates whether we are planning to use a separate filing order to bill pumps, per diems, kit codes, and supplies to a medical account for a Med Access investigation. 'Y' indicates that a separate filing order will be created. 'N' or NULL indicate that only one filing order will be used. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [PAT_ENC](PAT_ENC.md).

