# HH_PAT_ENC

> This table contains Home Care overtime single items that are stored in the Patient (EPT) master file.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 60  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTACT_DATE_REAL` | FLOAT |  | Unique identifier for this contact for this patient. |
| 2 | `CHIEF_COMPLAINT_ID_REASON_VISIT_NAME` | VARCHAR |  | The name of the Reason for Visit record. |
| 3 | `HH_TYPE_OF_SVC_C_NAME` | VARCHAR | org | Home Health type of service category list selections for the encounter. Links to category table ZC_HH_TYPE_OF_SVC. |
| 4 | `HH_CONTACT_TYPE_ID_CONTACT_TYPE_NAME` | VARCHAR |  | Home Health Contact Type name |
| 5 | `HH_ENC_CREAT_INST` | DATETIME (Local) |  | Instant of creation for the encounter. |
| 6 | `HH_VST_CHRG_UCLID` | VARCHAR |  | The Universal Charge Line record ID for the visit change for this encounter. |
| 7 | `HH_ASMT_CHRG_UCLID` | VARCHAR |  | The Universal Charge Line record ID for the assessment change for this encounter. |
| 8 | `INPAT_DISCHRG_DT` | DATETIME |  | Inpatient discharge date. |
| 9 | `PRIMARY_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 10 | `PRIM_DX_START_DATE` | DATETIME |  | Primary diagnosis start date. |
| 11 | `PRIM_DX_SEVERITY` | INTEGER |  | Primary diagnosis severity. |
| 12 | `PROGNOSIS_C_NAME` | VARCHAR |  | Prognosis category list selections. Links to category table ZC_PROGNOSIS. |
| 13 | `REHAB_POTENTIAL_C_NAME` | VARCHAR |  | Rehab potential category list selections. Links to category table ZC_REHAB_POTENTIAL. |
| 14 | `POC_FLAG_YN` | VARCHAR |  | Was there a cert period created? Yes or no. |
| 15 | `POC_HDR_ID` | VARCHAR |  | Text entered for plan of care header. |
| 16 | `CERT_PER_STRT_DT` | DATETIME |  | Cert period start date. |
| 17 | `CERT_PERIOD_END_DT` | DATETIME |  | Cert period end date. |
| 18 | `POC_VERBAL_ORD_ID` | VARCHAR |  | Identifier for the plan of care verbal order. Links to table HH_VO_INFO. |
| 19 | `POC_GOALS_ID` | VARCHAR |  | Identifier for the plan of care goals. |
| 20 | `POC_ORDERS_ID` | VARCHAR |  | Identifier for the plan of care orders. |
| 21 | `IS_BILLABLE_YN` | VARCHAR |  | Whether the encounter is billable. |
| 22 | `EOW_LINK_CT_ID` | VARCHAR |  | The record ID of a message in the In Basket task and messaging system. Links to table IB_MESSAGES. |
| 23 | `SCHED_TM_TBD` | VARCHAR |  | Schedule time to be determined. |
| 24 | `OASIS_DATA_LINK_ID` | NUMERIC |  | Numeric link to an OASIS data set. |
| 25 | `ROC_DATE` | DATETIME |  | Resumption of care assessment date. |
| 26 | `DISCHARGE_REASON_C_NAME` | VARCHAR | org | Discharge reason category list selection. Links to category table ZC_REASON_DISCH. |
| 27 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 28 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 29 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |
| 30 | `STATED_WEIGHT` | NUMERIC |  | The stated weight entered for a patient during an encounter. |
| 31 | `HC_ADM_DECISION_YN` | VARCHAR | org | This item contains the home care admission decision. |
| 32 | `IP_PROC_NA_YN` | VARCHAR |  | This item stores whether the "NA - Not Applicable" check box is checked for Home Health OASIS question M1012. |
| 33 | `IP_PROC_UKNWN_YN` | VARCHAR |  | This item stores whether the "UK - Unknown" check box is checked for Home Health OASIS question M1012 - Inpatient Procedures. |
| 34 | `REGIMEN_CHG_NA_YN` | VARCHAR |  | This item stores whether the "NA - Not Applicable" check box is checked for Home Health OASIS question M1016. |
| 35 | `POC_PHYS_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 36 | `POC_PHYS_NA_YN` | VARCHAR |  | This item stores whether the Unknown checkbox is checked on Home Health OASIS question M0018. |
| 37 | `POC_VERBAL_SOC` | VARCHAR |  | This field holds the clinician who received the verbal start of care order and the date the order was received. |
| 38 | `POC_F2F_HNO_ID` | VARCHAR |  | HH Face to Face attestation note for the plan of care |
| 39 | `PRIM_DX_FLAG_C_NAME` | VARCHAR | org | The Primary DX - Flag item is a customer defined category list that can be used to further describe a diagnosis entry. An example of the use of this item would be for flagging a diagnosis as an exacerbation or onset. The flag will be carried over to the plan of care |
| 40 | `VISIT_START_DTTM` | DATETIME (Local) |  | The start time and date of a home visit. |
| 41 | `VISIT_END_DTTM` | DATETIME (Local) |  | The end time and date of a home visit. |
| 42 | `HH_EPS_CHRG_UCL_ID` | VARCHAR |  | The Universal Charge Line record ID for the EPS Assessment charge for NY Medicaid. |
| 43 | `POC_PHYS_EST_HNO_ID` | VARCHAR |  | This stores a link to the note that stores Home Health's physician recertification estimate attestation statement for the Plan of Care verbal order. |
| 44 | `SOC_DATE` | DATETIME |  | If this is a start of care contact, this is the M0030 date. |
| 45 | `VOL_DRIVING_ST_TM` | DATETIME (Local) |  | The driving start time for a home health or hospice volunteer visit. |
| 46 | `VOL_DRIVING_END_TM` | DATETIME (Local) |  | The driving end time for a home health or hospice volunteer visit. |
| 47 | `VOL_MILEAGE` | FLOAT |  | The mileage for driving to a home health or hospice volunteer visit. |
| 48 | `VOL_NAME` | VARCHAR |  | The volunteer's name for a home health or hospice volunteer visit. |
| 49 | `TRANSCRIBE_USER_ID` | VARCHAR |  | The transcribing user for a home health or hospice volunteer visit. |
| 50 | `TRANSCRIBE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 51 | `HH_POC_PHYS_ADDR_ID` | VARCHAR |  | This item stores the unique address ID corresponding to M0018 provider (attending physician) who is expected to sign the Home Health patient's Plan of Care. |
| 52 | `POC_SUBMIT_UTC_DTTM` | DATETIME (UTC) |  | This item stores the POC submission instant in UTC when the POC was submitted. |
| 53 | `DECEASED_BEFORE_YN` | VARCHAR |  | This item determines if the patient was deceased before the visit. If this is set to Yes, the whole visit will be considered as post-mortem visit. |
| 54 | `NO_SECONDARY_DX_C_NAME` | VARCHAR |  | Whether the patient has a secondary diagnoses. |
| 55 | `ENC_CLOSE_METHOD_C_NAME` | VARCHAR |  | The encounter close method category ID for the encounter. |
| 56 | `REPORTING_DISC_C_NAME` | VARCHAR |  | This item stores the reporting discipline of the provider who completed the encounter. |
| 57 | `POC_MENTAL_NOTE_ID` | VARCHAR |  | This stores a link to the note that stores the mental, psychosocial, and cognitive observations for the Plan of Care verbal order. |
| 58 | `HH_HSPC_EPISODE_ID` | NUMERIC |  | The ID of the first home health/hospice episode to which the encounter is linked. |
| 59 | `DISCH_W_DECLN_RSN_C_NAME` | VARCHAR | org | Reason for discharging a patient who has declined or not improved outcomes |
| 60 | `DISCH_W_DECLN_CMT` | VARCHAR |  | Additional optional comments for explaining why the patient was discharged with declined outcomes |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

