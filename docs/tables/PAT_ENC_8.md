# PAT_ENC_8

> This table supplements the PAT_ENC, PAT_ENC_2, PAT_ENC_3, PAT_ENC_4, PAT_ENC_5, PAT_ENC_6, and PAT_ENC_7 tables. It contains additional information related to patient encounters or appointments.

**Overflow of:** [PAT_ENC](PAT_ENC.md)  
**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 27  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `EST_PREPAY_CALC_PP_PROPOSED_YN` | VARCHAR |  | Indicates whether the patient was offered an estimated payment plan for this visit ('Y'). 'N' or NULL indicates that the patient was not offered an estimated payment plan for this visit. |
| 6 | `EST_PREPAY_CALC_ELIG_C_NAME` | VARCHAR |  | The eligibility for remaining balances category ID for the payment plan associated with this visit. |
| 7 | `PMT_PLAN_AGRMT_SCHED_PMT_ID` | NUMERIC |  | The unique ID of the payment plan agreement created from this visit's pre-service sign up. |
| 8 | `RSLT_FOL_UP_CREAT_SRC_C_NAME` | VARCHAR |  | Contains the source workflow which created the Results Follow-Up encounter. |
| 9 | `BILL_DECIS_FIN_ASST_TRACKER_ID` | NUMERIC |  | The ID of the decision for which this encounter is used to generate charges. This is set only by an automated process that requires the decision service grid to function. |
| 10 | `NO_FOLLOW_UP_YN` | VARCHAR |  | This indicates whether no follow-ups are needed for a visit. |
| 11 | `MCAID_INCARCERATION_BILL_CODE` | VARCHAR |  | A code that indicates the encounter is billable to Medicaid due to a state-specific program for reimbursing care offered to incarcerated patients. |
| 12 | `MCAID_INCAR_BILL_START_DATE` | DATETIME |  | The earliest date associated with this encounter that Medicaid is billable due to a state-specific program for reimbursing care offered to incarcerated patients. |
| 13 | `MEDICARE_CHANGE_C_NAME` | VARCHAR |  | Question on the MSPQ RTE Integration version of the MSPQ. The question asks if there has been a change in Medicare entitlement. The three possible answers are Yes, No, and Could Not Answer. |
| 14 | `MSP_RTE_VERI_STAT_C_NAME` | VARCHAR |  | The verification status for MSPQ RTE Integration. If the user manually completes the full MSPQ, this status is set to one that starts with "User Filled Out" based on the reason manual completion was required. Otherwise, it's set to the outcome of comparing eligibility messages from Medicare to determine if the MSPQ for this encounter can be shortened by reusing information from one of the patient's previous MSPQs. |
| 15 | `MSP_COMP_REALTIME_TX_CSN_ID` | NUMERIC |  | The unique RTE contact serial number of the 271 Eligibility Response associated with the encounter's date of service, compared with prior responses for MSPQ RTE Integration. |
| 16 | `MSP_RTE_COMP_PAT_ENC_CSN_ID` | NUMERIC |  | The unique contact serial number (CSN) of the encounter being used for RTE message comparison for MSPQ RTE Integration. |
| 17 | `TAKING_PULL_REJECTED_YN` | VARCHAR |  | Indicates whether a user has clicked the "Clear Selections" button to dismiss suggested medication taking values from the current encounter. |
| 18 | `HOSP_SERV_C_NAME` | VARCHAR | org | The category value corresponding to the hospital service for this patient contact. |
| 19 | `LEVEL_OF_CARE_C_NAME` | VARCHAR | org | The category value corresponding to the level of care for this patient contact. |
| 20 | `ACCOMMODATION_C_NAME` | VARCHAR | org | The category value corresponding to the room accommodation for this patient contact. |
| 21 | `ACCOM_REASON_C_NAME` | VARCHAR | org | The category value corresponding to the reason for the room accommodation for this patient contact. |
| 22 | `APPT_NEEDS_BED_C_NAME` | VARCHAR |  | Indicates whether the appointment needs bed utilization. |
| 23 | `APPT_BED_PREDEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 24 | `APPT_BED_HOSP_SERV_C_NAME` | VARCHAR |  | For an appointment that needs bed utilization, the hospital service where the bed is needed. |
| 25 | `APPT_BED_POST_LEVEL_OF_CARE_C_NAME` | VARCHAR |  | For an appointment that needs bed utilization, the level of care where the bed is needed. |
| 26 | `APPT_BED_CMT_S` | VARCHAR |  | The comments associated with an appointment's bed utilization needs. |
| 27 | `SEPARATED_GROUP_YN` | VARCHAR |  | For group appointments, indicates whether the appointment was scheduled with the patients separated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in

Inbound joins are tracked on the logical base [PAT_ENC](PAT_ENC.md).

