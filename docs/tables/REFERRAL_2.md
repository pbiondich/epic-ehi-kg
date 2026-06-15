# REFERRAL_2

> The REFERRAL_2 table is a continuation of the REFERRAL table. These tables are the primary tables for referral information stored in the system.

**Overflow of:** [REFERRAL](REFERRAL.md)  
**Primary key:** `REFERRAL_ID`  
**Columns:** 61  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK | The referral ID for the referral record. |
| 2 | `CE_SENT_YN` | VARCHAR |  | Indicates whether this referral was sent using Care Everywhere. |
| 3 | `RFL_ATT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `RFL_CONTACT_NAME` | VARCHAR |  | Free text field that will be populated by the user who creates the referral. |
| 5 | `RPT_RECEIVED_DATE` | DATETIME |  | Indicates the date that a PCP acknowledged receipt of an internal report regarding a referral. |
| 6 | `RPT_SENT_DATE` | DATETIME |  | Indicates the date that an internal report regarding a referral is sent to the referring provider. |
| 7 | `RFL_RECEIVED_DATE` | DATETIME |  | Indicates the date in which the referred to department acknowledged receipt of the referral. |
| 8 | `AUDIT_REF_TO_NAME` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the name of the referred-to provider. |
| 9 | `AUDIT_DATE` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the referred-on date. |
| 10 | `AUDIT_RFL_TYPE` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the original text for the referral type. |
| 11 | `AUDIT_REQ_VISITS` | INTEGER |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the requested number of visits. |
| 12 | `AUDIT_AUTH_VISITS` | INTEGER |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the authorized number of visits. |
| 13 | `AUDIT_START_DATE` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the starting date for the referral in HL7 format. |
| 14 | `AUDIT_END_DATE` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the ending date for the referral in HL7 format. |
| 15 | `AUDIT_RFTO_PROVSPEC` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the original text for the referred-to provider specialty. |
| 16 | `AUDIT_RFNG_PROVSPEC` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the original text for the referring provider specialty. |
| 17 | `AUDIT_RFTO_DEPTSPEC` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the original text for the referred-to department specialty. |
| 18 | `AUDIT_RFNG_DEPTSPEC` | VARCHAR |  | This item is used to audit data from incoming Care Everywhere referrals. It stores the original text for the referring department specialty. |
| 19 | `OUTST_AMT` | NUMERIC |  | Specifies the outstanding amount. |
| 20 | `CASE_MGMT_CREATE_ID` | VARCHAR |  | Specifies the case management creation message. |
| 21 | `CASE_RATE_OVERRIDE` | INTEGER |  | Specifies the case rate override. |
| 22 | `QNR_HQA_ID` | VARCHAR |  | Questionnaire related data |
| 23 | `ALT_PYR_SVC_DT` | DATETIME |  | The service date for the alternate payor information. This date is used as the contact date to look up the alternate billing table in the plan master file. |
| 24 | `GEN_RFL_NUM_IT_1` | NUMERIC |  | This contains information from generic referral numeric item 1. |
| 25 | `GEN_RFL_NUM_IT_2` | NUMERIC |  | This contains information from generic referral numeric item 2. |
| 26 | `GEN_RFL_NUM_IT_3` | NUMERIC |  | This contains information from generic referral numeric item 3. |
| 27 | `GEN_RFL_NUM_IT_4` | NUMERIC |  | This contains information from generic referral numeric item 4. |
| 28 | `GEN_RFL_NUM_IT_5` | NUMERIC |  | This contains information from generic referral numeric item 5. |
| 29 | `GEN_RFL_NUM_IT_6` | NUMERIC |  | This contains information from generic referral numeric item 6. |
| 30 | `GEN_RFL_NUM_IT_7` | NUMERIC |  | This contains information from generic referral numeric item 7. |
| 31 | `GEN_RFL_NUM_IT_8` | NUMERIC |  | This contains information from generic referral numeric item 8. |
| 32 | `GEN_RFL_NUM_IT_9` | NUMERIC |  | This contains information from generic referral numeric item 9. |
| 33 | `GEN_RFL_NUM_IT_10` | NUMERIC |  | This contains information from generic referral numeric item 10. |
| 34 | `GEN_RFL_CAT_1_C_NAME` | VARCHAR | org | This contains information from generic referral category item 1. |
| 35 | `GEN_RFL_CAT_2_C_NAME` | VARCHAR | org | This contains information from generic referral category item 2. |
| 36 | `GEN_RFL_CAT_3_C_NAME` | VARCHAR | org | This contains information from generic referral category item 3. |
| 37 | `GEN_RFL_CAT_4_C_NAME` | VARCHAR | org | This contains information from generic referral category item 4. |
| 38 | `GEN_RFL_CAT_5_C_NAME` | VARCHAR | org | This contains information from generic referral category item 5. |
| 39 | `GEN_RFL_STR_1` | VARCHAR |  | This contains information from generic referral string item 1. |
| 40 | `GEN_RFL_STR_2` | VARCHAR |  | This contains information from generic referral string item 2. |
| 41 | `GEN_RFL_STR_3` | VARCHAR |  | This contains information from generic referral string item 3. |
| 42 | `GEN_RFL_STR_4` | VARCHAR |  | This contains information from generic referral string item 4. |
| 43 | `GEN_RFL_STR_5` | VARCHAR |  | This contains information from generic referral string item 5. |
| 44 | `GEN_RFL_DATE_1_DT` | DATETIME |  | This contains information from generic referral date item 1. |
| 45 | `GEN_RFL_DATE_2_DT` | DATETIME |  | This contains information from generic referral date item 2. |
| 46 | `GEN_RFL_DATE_3_DT` | DATETIME |  | This contains information from generic referral date item 3. |
| 47 | `GEN_RFL_DATE_4_DT` | DATETIME |  | This contains information from generic referral date item 4. |
| 48 | `GEN_RFL_DATE_5_DT` | DATETIME |  | This contains information from generic referral date item 5. |
| 49 | `TRIAGE_DECISION_C_NAME` | VARCHAR |  | The triage decision category ID for the referral. |
| 50 | `REJECT_REASON_C_NAME` | VARCHAR | org | UK referral triage information |
| 51 | `TRIAGE_APPT_CHANGE` | VARCHAR |  | The appointment change comments for the referral record. |
| 52 | `OVRRD_REF_COUNTS` | INTEGER |  | The number of visits approved for this referral, overridden by the user. |
| 53 | `CALC_SVC_LVL_CNTS` | INTEGER |  | The calculated number of service level authorizations counts, based on the service level authorizations collected. |
| 54 | `TOC_STATUS_C_NAME` | VARCHAR |  | Indicates the status of the last transfer of care transmission attempt. If the attempt was unsuccessful, the failure reason is stored. |
| 55 | `GEN_RFL_STR_6` | VARCHAR |  | This contains information from generic referral string item 6. |
| 56 | `GEN_RFL_STR_7` | VARCHAR |  | This contains information from generic referral string item 7. |
| 57 | `GEN_RFL_STR_8` | VARCHAR |  | This contains information from generic referral string item 8. |
| 58 | `GEN_RFL_STR_9` | VARCHAR |  | This contains information from generic referral string item 9. |
| 59 | `AP_CLAIM_COUNT` | NUMERIC |  | The actual AP claims count for the referral. This number is calculated from the counts table based the Counts Settings in the Referral System Definitions. |
| 60 | `RFL_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 61 | `RFL_ENC_TYPE_C_NAME` | VARCHAR | org | The expected encounter type for the referral (inpatient or outpatient). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [REFERRAL](REFERRAL.md).

