# REFERRAL_5

> The REFERRAL_5 table is a continuation of the REFERRAL_4 table. The REFERRAL_* tables are the primary tables for referral information stored in the system.

**Overflow of:** [REFERRAL](REFERRAL.md)  
**Primary key:** `REFERRAL_ID`  
**Columns:** 63  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK | The unique identifier for the referral record. |
| 2 | `GEN_RFL_SEC_SINCE_MIDNIGHT_7` | NUMERIC |  | This contains information from generic referral time item 7. |
| 3 | `GEN_RFL_SEC_SINCE_MIDNIGHT_8` | NUMERIC |  | This contains information from generic referral time item 8. |
| 4 | `GEN_RFL_SEC_SINCE_MIDNIGHT_9` | NUMERIC |  | This contains information from generic referral time item 9. |
| 5 | `GEN_RFL_SEC_SINCE_MIDNIGHT_10` | NUMERIC |  | This contains information from generic referral time item 10. |
| 6 | `RPT_REF_TO_CNTRCT_YN` | VARCHAR |  | Stores an override value that indicates the referred to provider/location/vendor/department should be considered contracted or not for Medicare Advantage ODAG reporting. If NULL, system defined logic will be used. If Y, a user marked the provider as contracted (CP in ODAG). If N, a user marked the provider as non-contracted (NCP in ODAG). |
| 7 | `RPT_REF_BY_CNTRCT_YN` | VARCHAR |  | Stores an override value that indicates the referred by provider/location/department should be considered contracted or not for Medicare Advantage ODAG reporting. If NULL, system defined logic will be used. If Y, a user marked the provider as contracted (CP in ODAG). If N, a user marked the provider as non-contracted (NCP in ODAG). |
| 8 | `LIVING_SITUATION_C_NAME` | VARCHAR | org | Describes who the patient or child lives with. |
| 9 | `FIRST_APPOINTMENT_BY_DATE` | DATETIME |  | The date that the first appointment for the referral should occur by. |
| 10 | `SENIORITY_DATE` | DATETIME |  | The Seniority Date for the referral which represents a 'start date' that might have been set before the referral was created. |
| 11 | `CASE_WORKER_NAME` | VARCHAR |  | The case manager of the child psychology case. |
| 12 | `CHILD_SERVICE_C_NAME` | VARCHAR | org | Indicates the child welfare service role in connection with child psychology services. |
| 13 | `PARENTAL_RESP_C_NAME` | VARCHAR | org | Indicates which entity has parental responsibility for the patient. |
| 14 | `CONSENT_TO_TREAT_STAT_C_NAME` | VARCHAR | org | Indicates the status of obtaining the patient's consent in connection with the referral's transfer of medical record information. |
| 15 | `FORWARDED_EVALUATION_DATE` | DATETIME |  | This date represents the date an external organization evaluated or triaged the referral before forwarding it to an Epic instance. This date represents the internal concept of Triage History Instant, for the forwarding decision done at the external organization. |
| 16 | `EMSG_COMM_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This item is part of a link to a communication from which the referral was created. This item contains the CSN of the contact which contains the communication. EMSG_COMM_JOB_ID (I RFL 18961) contains the communication job ID. |
| 17 | `EMSG_COMM_JOB_ID` | VARCHAR |  | Part of a link to a communication from which the referral was created. |
| 18 | `AUTHORIZED_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 19 | `INITIAL_REQUEST_TYPE_C_NAME` | VARCHAR |  | The initial request type for the referral. |
| 20 | `REF_BY_CNTRCT_AT_AUTH_YN` | VARCHAR |  | The contracted status of referred-by entities on the referral as of the last decision or the current contracted status if the referral is pending. |
| 21 | `REF_TO_CNTRCT_AT_AUTH_YN` | VARCHAR |  | The contracted status of referred-to entities on the referral as of the last decision or the current contracted status if the referral is pending. |
| 22 | `REF_BY_SER_CNTRCT_AT_AUTH_YN` | VARCHAR |  | The contracted status of referred-by provider on the referral as of the last decision or the current contracted status if the referral is pending. |
| 23 | `REF_TO_SER_CNTRCT_AT_AUTH_YN` | VARCHAR |  | The contracted status of referred-to provider on the referral as of the last decision or the current contracted status if the referral is pending. |
| 24 | `REF_BY_EAF_CNTRCT_AT_AUTH_YN` | VARCHAR |  | The contracted status of referred-by location on the referral as of the last decision or the current contracted status if the referral is pending. |
| 25 | `REF_TO_EAF_CNTRCT_AT_AUTH_YN` | VARCHAR |  | The contracted status of referred-to location on the referral as of the last decision or the current contracted status if the referral is pending. |
| 26 | `REF_TO_VEN_CNTRCT_AT_AUTH_YN` | VARCHAR |  | The contracted status of referred-to vendor on the referral as of the last decision or the current contracted status if the referral is pending. |
| 27 | `REF_BY_PROV_NET_LEVEL_C_NAME` | VARCHAR | org | The network status of the referred-by provider on the referral. |
| 28 | `REF_TO_LOCATION_NET_LEVEL_C_NAME` | VARCHAR |  | The network status of the referred-to location on the referral. |
| 29 | `REF_TO_VENDOR_NET_LEVEL_C_NAME` | VARCHAR |  | The network status of the referred-to vendor on the referral. |
| 30 | `REF_TO_PROV_NET_LEVEL_C_NAME` | VARCHAR |  | The network status of the referred-to provider on the referral. |
| 31 | `REF_BY_LOCATION_NET_LEVEL_C_NAME` | VARCHAR |  | The network status of the referred-by location on the referral. |
| 32 | `RPT_REF_BY_SER_CNTRCT_YN` | VARCHAR |  | The user override for the contracted status of the referred-by provider on the referral. |
| 33 | `RPT_REF_TO_SER_CNTRCT_YN` | VARCHAR |  | The user override for the contracted status of the referred-to provider on the referral. |
| 34 | `RPT_REF_BY_EAF_CNTRCT_YN` | VARCHAR |  | The user override for the contracted status of the referred-by location on the referral. |
| 35 | `RPT_REF_TO_EAF_CNTRCT_YN` | VARCHAR |  | The user override for the contracted status of the referred-to location on the referral. |
| 36 | `RPT_REF_TO_VEN_CNTRCT_YN` | VARCHAR |  | The user override for the contracted status of the referred-to vendor on the referral. |
| 37 | `RFL_AUTH_PROG_C_NAME` | VARCHAR | org | Authorization Prognosis code associated with a referral |
| 38 | `PRINCIPAL_DX_DATE` | DATETIME |  | Specifies the diagnois date used for Prinicpal Diagnosis |
| 39 | `ADMISSION_SOURCE_C_NAME` | VARCHAR | org | The source from which the paitent is being admitted or referred. Only available in UM referrals. |
| 40 | `DISCHRG_DISP_C_NAME` | VARCHAR | org | This disposition (location) of the patient after discharge. Only available in UM referrals. |
| 41 | `FIRST_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Ths CSN of the encounter linked to the referral or auth/cert with the earliest encounter instant. |
| 42 | `LAST_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Ths CSN of the encounter linked to the referral or auth/cert with the latest encounter instant. |
| 43 | `REF_BY_CNTRCT_AT_DEC_YN` | VARCHAR |  | The contracted status of referred-by entities on the referral as of the last decision. |
| 44 | `REF_TO_CNTRCT_AT_DEC_YN` | VARCHAR |  | The contracted status of referred-to entities on the referral as of the last decision. |
| 45 | `REF_BY_SER_CNTRCT_AT_DEC_YN` | VARCHAR |  | The contracted status of referred-by provider on the referral as of the last decision. |
| 46 | `REF_TO_SER_CNTRCT_AT_DEC_YN` | VARCHAR |  | The contracted status of referred-to provider on the referral as of the last decision. |
| 47 | `REF_BY_LOC_CNTRCT_AT_DEC_YN` | VARCHAR |  | The contracted status of referred-by location on the referral as of the last decision. |
| 48 | `REF_TO_LOC_CNTRCT_AT_DEC_YN` | VARCHAR |  | The contracted status of referred-to location on the referral as of the last decision. |
| 49 | `REF_TO_VEN_CNTRCT_AT_DEC_YN` | VARCHAR |  | The contracted status of referred-to vendor on the referral as of the last decision. |
| 50 | `REGION_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 51 | `MEDICAL_GROUP_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 52 | `PRIMARY_CONDITION_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 53 | `PRIMARY_TREATMENT_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 54 | `PRIMARY_SPECIALTY_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 55 | `PRIMARY_SUBSPEC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 56 | `CONC_UM_REV_TRANS_FROM_DELE_YN` | VARCHAR |  | Indicates if the responsiblity for concurrent review of this authorization request has been transitioned from a delegate system to this UM system. |
| 57 | `MED_ESTIMATE_CSN_ID` | NUMERIC |  | This item holds the contact serial number (CSN) of the medication estimate (LME) that was linked to the associated order when this referral was created. This item is not populated for renewals. |
| 58 | `CLM_NET_OVRIDE_STAT_C_NAME` | VARCHAR |  | The network status to override to when adjudicating the linked claim. |
| 59 | `CLM_NET_OVRIDE_LVL_C_NAME` | VARCHAR | org | The network level to override to when adjudicating the linked claim. |
| 60 | `CLM_NET_OVRIDE_RSN_C_NAME` | VARCHAR | org | The reason for override a linked claim's adjudication network. |
| 61 | `UM_AUTH_SERVICE_TYPE_C_NAME` | VARCHAR | org | Service type for Utilization Management (UM) workflows. This is set automatically for UM referrals in Referral Entry after the UM service type is ready for use. |
| 62 | `UM_AUTH_CARE_SETTING_C_NAME` | VARCHAR |  | Care setting for Utilization Management (UM) workflows. This is set automatically for UM referrals in Referral Entry after the UM service type is ready for use. |
| 63 | `RFL_REF_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EMSG_COMM_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `FIRST_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `LAST_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

## Joined in

Inbound joins are tracked on the logical base [REFERRAL](REFERRAL.md).

