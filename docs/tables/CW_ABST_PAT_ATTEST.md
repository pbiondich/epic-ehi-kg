# CW_ABST_PAT_ATTEST

> Pain and clinical depression assessment information from abstractions with clinical information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `PAIN_ASSESS_TIME_PERIOD_C_NAME` | VARCHAR |  | The start and end dates of the dialysis patient's pain assessment time period. |
| 3 | `PAIN_ASSESS_DOC_STATUS_C_NAME` | VARCHAR | org | The dialysis patient's pain assessment documentation status. |
| 4 | `DEPRESS_ASSESS_TIME_PERIOD_C_NAME` | VARCHAR |  | The start and end dates of the dialysis patient's clinical depression assessment time period. |
| 5 | `DEPRESS_ASSESS_DOC_STATUS_C_NAME` | VARCHAR | org | The dialysis patient's clinical depression assessment documentation status. |
| 6 | `SDOH_ASSESS_YN` | VARCHAR |  | Indicates whether the patient was screened for Social Drivers of Health for this dialysis reporting abstraction. 'Y' indicates that the patient was screened. 'N' or NULL indicate that the patient was not screened. |
| 7 | `SDOH_ASSESS_FOOD_INSECURE_YN` | VARCHAR |  | Indicates whether the patient's screening for Food Insecurity was positive. 'Y' indicates that the screening was positive. 'N' indicates the screening was negative. NULL indicates the screening was not performed or recorded. |
| 8 | `SDOH_ASSESS_HOUSE_UNSTABLE_YN` | VARCHAR |  | Indicates whether the patient's screening for Housing Instability was positive. 'Y' indicates that the screening was positive. 'N' indicates the screening was negative. NULL indicates the screening was not performed or recorded. |
| 9 | `SDOH_ASSESS_TXPORT_NEEDS_YN` | VARCHAR |  | Indicates whether the patient's screening for Transportation Needs was positive. 'Y' indicates that the screening was positive. 'N' indicates the screening was negative. NULL indicates the screening was not performed or recorded. |
| 10 | `SDOH_ASSESS_UTILITY_DIFF_YN` | VARCHAR |  | Indicates whether the patient's screening for Utility Difficulties was positive. 'Y' indicates that the screening was positive. 'N' indicates the screening was negative. NULL indicates the screening was not performed or recorded. |
| 11 | `SDOH_ASSESS_INTERPER_SAFETY_YN` | VARCHAR |  | Indicates whether the patient's screening for Interpersonal Safety was positive. 'Y' indicates that the screening was positive. 'N' indicates the screening was negative. NULL indicates the screening was not performed or recorded. |
| 12 | `SDOH_ASSESS_NO_SCREEN_RSN_C_NAME` | VARCHAR |  | The reason why the patient was not screened for Social Drivers of Health category ID for the dialysis reporting abstraction. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

