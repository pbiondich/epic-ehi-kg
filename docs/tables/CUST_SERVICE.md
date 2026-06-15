# CUST_SERVICE

> The CUST_SERVICE table stores information entered into system's Customer Service module. This can be used to report on communication between medical facility staff and patients.

**Overflow family:** [CUST_SERVICE_2](CUST_SERVICE_2.md)  
**Primary key:** `COMM_ID`  
**Columns:** 95  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the customer service communication. |
| 2 | `ENTRY_USER_ID` | VARCHAR |  | The unique ID of the user who created the customer service communication. |
| 3 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `ENTRY_DATE` | DATETIME |  | The date the customer service communication was entered. |
| 5 | `SOURCE_TYPE_C_NAME` | VARCHAR | org | The category value representing the source type of the customer service communication. Refers to the person or entity contacting your facility's customer service representative. |
| 6 | `SOURCE_MEMBER_ID` | VARCHAR |  | If the source of the customer service communication is a person who receives care at your facility or is a member of your health plan, this column contains the Patient (EPT) ID of that member. |
| 7 | `TOPIC_C_NAME` | VARCHAR | org | The category value of the topic of the customer service communication record. |
| 8 | `SUBJECT_TYPE_C_NAME` | VARCHAR | org | The category value representing the subject type of the customer service communication. Refers to the person or entity the customer service communication is about. |
| 9 | `RES_C_NAME` | VARCHAR | org | The resolution reason category value for the customer service communication. |
| 10 | `RES_USER_ID` | VARCHAR |  | The unique ID of the user who resolved the customer service communication. |
| 11 | `RES_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `RES_DATE` | DATETIME |  | The date the customer service communication was resolved. |
| 13 | `RES_SATISFACTION` | INTEGER |  | The recorded satisfaction of the customer service communication. |
| 14 | `PRIORITY_C_NAME` | VARCHAR | org | The category value associated with the priority of the customer service communication. |
| 15 | `SUMMARY` | VARCHAR |  | The summary of the customer service communication. |
| 16 | `SOURCE_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 17 | `SOURCE_PLAN_GRP_ID` | VARCHAR |  | If the source of the customer service communication is a plan group, this column contains the Payor Plan Group (PPG) ID of that plan group. |
| 18 | `SOURCE_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 19 | `SOURCE_CARRIER_ID` | VARCHAR |  | If the source of the customer service communication is a carrier, this column contains the Carrier (MCR) ID of that carrier. |
| 20 | `SOURCE_CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 21 | `SOURCE_ACCOUNT_ID` | NUMERIC |  | If the source of the customer service communication is a guarantor account, this column contains the Accounts Receivable (EAR) ID of that guarantor account. |
| 22 | `SOURCE_NETWORK_ID` | VARCHAR |  | If the source of the customer service communication is a provider network, this column contains the Network Database (NET) ID of that provider network. |
| 23 | `SOURCE_NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 24 | `SUBJ_MEMBER_ID` | VARCHAR |  | If the subject of the customer service communication is a person who receives care at your facility or is a member of your health plan, this column contains the Patient (EPT) ID of that member. |
| 25 | `SUBJ_STAFF_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 26 | `SUBJ_PLAN_GRP_ID` | VARCHAR |  | If the subject of the customer service communication is a plan group, this column contains the Payor Plan Group (PPG) ID of that plan group. |
| 27 | `SUBJ_PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 28 | `SUBJ_CARRIER_ID` | VARCHAR |  | If the subject of the customer service communication is a carrier, this column contains the Carrier (MCR) ID of that carrier. |
| 29 | `SUBJ_CARRIER_ID_CARRIER_NAME` | VARCHAR |  | The name of the carrier record. |
| 30 | `SUBJ_NETWORK_ID` | VARCHAR |  | If the subject of the customer service communication is a provider network, this column contains the Network Database (NET) ID of that provider network. |
| 31 | `SUBJ_NETWORK_ID_NETWORK_NAME` | VARCHAR |  | The name of the network. |
| 32 | `SUBJ_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 33 | `SUBJ_REFERRAL_ID` | NUMERIC |  | If the subject of the customer service communication is a referral, this column contains the Referral Database (RFL) ID of that referral. |
| 34 | `SUBJ_CLAIM_ID` | NUMERIC |  | If the subject of the customer service communication is a claim, this column contains the Claims System (CLM) ID of that claim. |
| 35 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique identifier of the patient encounter related to the customer service communication. |
| 36 | `RKP_ID` | VARCHAR | FK→ | The unique ID of the risk panel for the customer service communication. |
| 37 | `RKP_ID_RISK_PANEL_NAME` | VARCHAR |  | The name of the risk panel. |
| 38 | `LOB_ID` | VARCHAR | FK→ | The line of business for the customer service communication. |
| 39 | `LOB_ID_LOB_NAME` | VARCHAR |  | The name of the line of business record. |
| 40 | `REC_SENSITIVITY_C_NAME` | VARCHAR | org | The category value for the sensitivity type of the customer service communication. |
| 41 | `REC_COMM_ORIGIN_C_NAME` | VARCHAR |  | The category value of the application which initiated the customer service communication. |
| 42 | `SRC_CUSTOMER` | VARCHAR |  | If the source type of the customer service communication is a custom value, this column contains the free text source. For example, the name of the person who called your facility's customer service representative. |
| 43 | `SRC_VENDOR_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 44 | `SRC_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 45 | `RECORD_ENTRY_TIME` | DATETIME (Local) |  | The time the customer service communication was entered. |
| 46 | `SUB_CUSTOMER` | VARCHAR |  | If the subject type of the customer service communication is a custom value, this column contains the free text subject. For example, the name of the person the customer service communication is about. |
| 47 | `SUB_LOCATION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 48 | `SUB_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 49 | `SUB_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 50 | `REC_RES_TIME` | DATETIME (Local) |  | The time the customer service communication was resolved. |
| 51 | `LAB_SPECIMEN_ID` | VARCHAR |  | Laboratory specimen associated with this laboratory communication log. |
| 52 | `SUBJ_REQ_GRP_ID` | NUMERIC |  | The unique ID of the requisition grouper associated with the laboratory communication log. |
| 53 | `LAB_LOG_STATUS_C_NAME` | VARCHAR |  | The Lab Comm Log Status category value for the laboratory communication log. |
| 54 | `EXTERNAL_ID_NUM` | VARCHAR |  | The external ID for the customer service communication. |
| 55 | `SUBJECT_EAR_ID` | NUMERIC |  | If the subject of the customer service communication is a guarantor account, this column contains the Accounts Receivable (EAR) ID of that guarantor account. |
| 56 | `VALID_CRM_YN` | VARCHAR |  | Indicates whether the customer service communication is valid. 'Y' or NULL indicates the communication is valid. 'N' indicates the communication is invalid. |
| 57 | `RES_1ST_ATTEMPT_YN` | VARCHAR |  | Indicates whether the customer service communication was resolved on the first attempt. 'Y' indicates it was resolved on first attempt. 'N' indicates it was resolved after first attempt or is still unresolved. A null value indicates the customer service communication was created but never opened or required values were not entered. |
| 58 | `OWN_BUS_SEG_EAF_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 59 | `CREATION_SA_PBS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 60 | `SUB_TOPIC_C_NAME` | VARCHAR | org | The category value of the subtopic of the customer service communication record. Used in combination with TOPIC_C to further categorize the topic of the customer service communication. |
| 61 | `HAR_ID` | NUMERIC |  | If the subject of the customer service communication is a hospital account, this column contains the Hospital Account (HAR) ID. |
| 62 | `ROUT_HX_HTH_ID` | NUMERIC |  | The routing history thread for the customer service communication. |
| 63 | `SOURCE_PBA_ID` | VARCHAR |  | If the source of the customer service communication is a premium billing account, this column contains the PB Account (PBA) ID. |
| 64 | `SUBJECT_PBA_ID` | VARCHAR |  | If the subject of the customer service communication is a premium billing account, this column contains the PB Account (PBA) ID. |
| 65 | `LAB_REQ_ID` | NUMERIC |  | Laboratory requisition associated with this laboratory communication log. |
| 66 | `LAB_CASE_ID` | NUMERIC |  | The unique ID of the laboratory case associated with the laboratory communication log. |
| 67 | `BANK_RECON_ID` | NUMERIC |  | If the subject of the customer service communication is a bank reconciliation, this column contains the Cash (CSH) ID of that bank reconciliation. |
| 68 | `SOURCE_PROSPECT_ID` | NUMERIC |  | If the source of the customer service communication is a prospective patient, this column contains the Requisition Grouper (RQG) ID of that prospective patient. |
| 69 | `SUBJECT_PROSPECT_ID` | NUMERIC |  | If the subject of the customer service communication is a prospective patient, this column contains the Requisition Grouper (RQG) ID of that prospective patient. |
| 70 | `SOURCE_SUBMITTER_ID` | NUMERIC |  | If the source of the customer service communication is a submitter, this column contains the Submitter (SMT) ID of that submitter. |
| 71 | `SOURCE_SUBMITTER_ID_RECORD_NAME` | VARCHAR |  | The name of the submitter record. |
| 72 | `SUBJECT_ORDER_ID` | NUMERIC |  | If the subject of the customer service communication is an order, this column contains the Order (ORD) ID. |
| 73 | `SUBJECT_CAMPAIGN_ID` | NUMERIC |  | If the subject of the customer service communication is a campaign, this column contains the Campaign (CCT) ID of that campaign. |
| 74 | `SUBJECT_CAMPAIGN_ID_CAMPAIGN_NAME` | VARCHAR |  | The name of the campaign record. |
| 75 | `SUBJECT_DECISION_ID` | NUMERIC |  | If the subject of the customer service communication is a decision, this column contains the Financial Assistance Tracker (FNT) ID of that decision. |
| 76 | `SUBJECT_ESTIMATE_ID` | NUMERIC |  | If the subject of the customer service communication is an estimate, this column contains the Estimate (PES) ID of that estimate. |
| 77 | `ENTRY_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the customer service communication was entered, in UTC format. |
| 78 | `RESOLUTION_UTC_DTTM` | DATETIME (UTC) |  | The date and time when the customer service communication was resolved, in UTC format. |
| 79 | `SOURCE_RESP_PRTY_GUID` | VARCHAR |  | If the source of the customer service communication is a responsible party for a patient, this column contains the GUID of that responsible party. |
| 80 | `SUBJECT_RESP_PRTY_GUID` | VARCHAR |  | If the subject of the customer service communication is a responsible party for a patient, this column contains the GUID of that responsible party. |
| 81 | `SOURCE_USER_ID` | VARCHAR |  | If the source of the customer service communication is an employee, this column contains the ID of that user record. |
| 82 | `SOURCE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 83 | `VOID_USER_ID` | VARCHAR |  | The user who voided this NCS |
| 84 | `VOID_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 85 | `VOID_UTC_DTTM` | DATETIME (UTC) |  | Instant at which this NCS was voided. |
| 86 | `APPEAL_DECISION_DATE` | DATETIME |  | The date the appeal's outcome was decided. |
| 87 | `APPEAL_SENT_TO_IRE_DATE` | DATETIME |  | The date the appeal case was sent to the Independent Review Entity. |
| 88 | `SUBJECT_AUTH_REQUEST_ID` | NUMERIC |  | Auth Request (AUG) that this CRM is about. |
| 89 | `APPEAL_GRIEVANCE_NOTIF_DATE` | DATETIME |  | The date the appeal or grievance's notification was sent out. |
| 90 | `SUBJECT_CLAIM_RECON_ID` | VARCHAR |  | If the subject of the customer service communication is a rejected claim, this column contains the rejected claim (CRD) ID of that rejected claim. |
| 91 | `SUBJECT_COVERAGE_ID` | NUMERIC |  | Coverage (CVG) that this CRM is about. |
| 92 | `SUBJECT_RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 93 | `SUBJECT_USER_ID` | VARCHAR |  | Stores the subject employee for the customer service record. |
| 94 | `SUBJECT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 95 | `OVERRIDE_BUS_SEG_POS_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LOB_ID` | [CLARITY_LOB](CLARITY_LOB.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `RKP_ID` | [CLARITY_RKP](CLARITY_RKP.md) | sole_pk | high |

