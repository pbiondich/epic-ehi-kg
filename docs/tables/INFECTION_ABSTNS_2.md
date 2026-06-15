# INFECTION_ABSTNS_2

> This table contains more basic information from infection abstractions.

**Overflow of:** [INFECTION_ABSTNS](INFECTION_ABSTNS.md)  
**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `DAILY_MIN_MAP_YN` | VARCHAR |  | Indicates whether the patient's daily minimum MAP value meets VAE criteria. 'Y' indicates that the patient's minimum MAP value has been documented as meeting VAE criteria. 'N' indicates that it has been documented as not meeting the criteria. NULL indicates that this information has not been documented. |
| 3 | `PEDVAE_CLIN_EVENT_C_NAME` | VARCHAR |  | Indicates whether there were clinical events associated with the pediatric VAE event. Note that the shared category list for this column is stored in ZC_DNR_HTENSION. |
| 4 | `PEDVAE_OTHER_EVENT` | VARCHAR |  | Free-text description of which "other" clinical event is associated with the pediatric VAE event. |
| 5 | `NHSN_ABX_1_DATE` | DATETIME |  | The date for the start of the first antimicrobial agent for the infection case. |
| 6 | `NHSN_ABX_2_DATE` | DATETIME |  | The date for the start of the second antimicrobial agent for the infection case. |
| 7 | `NHSN_ABX_3_DATE` | DATETIME |  | The date for the start of the third antimicrobial agent for the infection case. |
| 8 | `PATH_IDENTIFIED_YN` | VARCHAR |  | Indicates whether a pathogen was identified for the infection case. 'Y' indicates that a pathogen was identified. 'N' indicates that a pathogen was not identified. NULL indicates that this information was not documented for the infection case. |
| 9 | `BLOOD_PATHOGEN_YN` | VARCHAR |  | Indicates whether a pathogen was identified from a blood specimen for the infection case. 'Y' indicates that a blood pathogen was identified. 'N' indicates that a blood pathogen was not identified. NULL indicates that this information was not documented for the infection case. |
| 10 | `NHSN_FIRST_ADMIT_TO_FAC_DATE` | DATETIME |  | The date when the patient was first admitted to the facility where the event occurred. |
| 11 | `NHSN_LTCF_INSERT_SITE_C_NAME` | VARCHAR |  | The insertion site category ID for the abstraction. |
| 12 | `NHSN_HAS_OTHER_DEVICE_YN` | VARCHAR |  | Indicates whether another urinary device was in place besides a catheter. 'Y' indicates that another urinary device was present. 'N' indicates that another urinary device was not present. NULL indicates that this information was not documented for the infection case. |
| 13 | `NHSN_OTHER_DEVICE_TYPE_C_NAME` | VARCHAR |  | The other device type category ID for the abstraction. |
| 14 | `NHSN_LTCF_TRAN_FROM_ACUTE_YN` | VARCHAR |  | Indicates whether the resident was transferred from acute care in the 4 weeks before the event. 'Y' indicates that the patient was transferred from acute care. 'N' indicates that the patient was not transferred. NULL indicates that this information was not documented for the infection case. |
| 15 | `NHSN_LTCF_LAST_TRANSFER_DATE` | DATETIME |  | If resident was transferred from acute care before the event, the date of that transfer. |
| 16 | `NHSN_LTCF_TRAN_WITH_CATH_YN` | VARCHAR |  | Indicates whether the resident had a catheter at the time they transferred. 'Y' indicates that the patient had a catheter at the time of transfer. 'N' indicates that the patient did not have a catheter at that time. NULL indicates that this information was not documented for the infection case. |
| 17 | `NHSN_LTCF_PRIM_RES_SVC_C_NAME` | VARCHAR |  | The primary resident service type category ID for the abstraction. |
| 18 | `NHSN_LTCF_TRAN_TO_ACUTE_YN` | VARCHAR |  | Indicates whether the resident transferred to acute care in the 7 days following the event. 'Y' indicates that the patient was transferred to acute care. 'N' indicates that the patient was not transferred. NULL indicates that this information was not documented for the infection case. |
| 19 | `NHSN_FEVER_YN` | VARCHAR |  | Indicates whether the patient had a fever as supporting evidence of the event. 'Y' indicates that a fever was identified. 'N' indicates that a fever was not identified. NULL indicates that this information was not documented for the infection case. |
| 20 | `NHSN_RIGORS_YN` | VARCHAR |  | Indicates whether the patient had rigors as supporting evidence of the event. 'Y' indicates that rigors were identified. 'N' indicates that rigors were not identified. NULL indicates that this information was not documented for the infection case. |
| 21 | `NHSN_CONFUSION_YN` | VARCHAR |  | Indicates whether the patient had confusion as supporting evidence of the event. 'Y' indicates that confusion was identified. 'N' indicates that confusion was not identified. NULL indicates that this information was not documented for the infection case. |
| 22 | `NHSN_HYPOTENSION_YN` | VARCHAR |  | Indicates whether the patient had hypotension as supporting evidence of the event. 'Y' indicates that hypotension was identified. 'N' indicates that hypotension was not identified. NULL indicates that this information was not documented for the infection case. |
| 23 | `NHSN_PAIN_SWELL_TEND_YN` | VARCHAR |  | Indicates whether the patient had acute pain, swelling, or tenderness of the testes, epididymis, or prostate as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 24 | `NHSN_DYSURIA_YN` | VARCHAR |  | Indicates whether the patient had acute dysuria as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 25 | `NHSN_URGENCY_YN` | VARCHAR |  | Indicates whether the patient had urgency as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 26 | `NHSN_INCONTINENCE_YN` | VARCHAR |  | Indicates whether the patient had incontinence as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 27 | `NHSN_COSTOVERT_PAIN_YN` | VARCHAR |  | Indicates whether the patient had costovertebral angle pain or tenderness as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 28 | `NHSN_SUPRAPUBIC_TEND_YN` | VARCHAR |  | Indicates whether the patient had suprapubic tenderness as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 29 | `NHSN_HEMATURIA_YN` | VARCHAR |  | Indicates whether the patient had visible (gross) hematuria as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 30 | `NHSN_POS_URINE_CULT_YN` | VARCHAR |  | Indicates whether the patient had a positive urine culture as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 31 | `NHSN_LEUKOCYTOSIS_YN` | VARCHAR |  | Indicates whether the patient had leukocytosis as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 32 | `NHSN_BLOOD_CULT_MATCH_YN` | VARCHAR |  | Indicates whether the patient had a positive blood culture as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 33 | `NHSN_FREQUENCY_YN` | VARCHAR |  | Indicates whether the patient had frequency as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 34 | `NHSN_ABX_AT_TRANSFER_YN` | VARCHAR |  | Indicates whether the patient was on antibiotic therapy for the organism represented by the event at the time of transfer. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 35 | `NHSN_PUR_DRAINAGE_YN` | VARCHAR |  | Indicates whether the patient had purulent drainage as supporting evidence of the event. 'Y' indicates that this evidence was identified. 'N' indicates that this evidence was not identified. NULL indicates that this information was not documented for the infection case. |
| 36 | `ASSOC_RPT_HOSP_REGULATORY_ID_CMS_MU_NAME` | VARCHAR |  | The name of the CMS Meaningful Use record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

