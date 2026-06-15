# AUTHORIZATIONS_2

> This table contains additional information about authorization records.

**Overflow of:** [AUTHORIZATIONS](AUTHORIZATIONS.md)  
**Primary key:** `AUTH_ID`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_ID` | NUMERIC | PK | The unique identifier (.1 item) for the authorization record. |
| 2 | `UM_WORKFLOW_STAGE_C_NAME` | VARCHAR |  | The workflow stage category ID for the authorization. |
| 3 | `DTR_DOC_NEEDED_YN` | VARCHAR |  | Whether DTR is required before submitting Authorization Request |
| 4 | `DTR_AGENCY_ID` | VARCHAR |  | The Guideline Vendor responsible for DTR Questionnaires for this request |
| 5 | `DTR_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 6 | `DTR_REQ_AUD_ID` | NUMERIC |  | The record ID of the PPR record tracking this DTR session |
| 7 | `UM_CVG_GUIDANCE_EXP_DATE` | DATETIME |  | The expiration date of the requested coverage guidance. |
| 8 | `PROV_AUTO_AUTH_YN` | VARCHAR |  | Whether authorization request will be automatically authorized. |
| 9 | `PAT_FHIR_ID` | VARCHAR |  | The FHIR Patient ID in the DTR request. |
| 10 | `SVC_REQ_FHIR_ID` | VARCHAR |  | The FHIR ServiceRequest ID in the DTR request. |
| 11 | `CVG_FHIR_ID` | VARCHAR |  | The FHIR Coverage ID in the DTR request. |
| 12 | `DTR_HISTORICAL_AUTH_ID` | NUMERIC |  | Historical coverage guidance authorization record linked to this authorization record |
| 13 | `DTR_ANSWER_ID` | VARCHAR |  | The internal guideline generated QuestionnaireResponse returned via DTR for this request |
| 14 | `APPR_PA_AMT_FREQUENCY_TYPE_C_NAME` | VARCHAR |  | Determines the approved timing of the service. This is the referral version of Tapestry frequency I AUT 2080. |
| 15 | `REQ_PA_AMT_FREQUENCY_TYPE_C_NAME` | VARCHAR |  | Determines the requested timing of the service. This is the referral version of Tapestry frequency I AUT 2083. |
| 16 | `APPEALED_ORIG_SERVICE_AUTH_ID` | NUMERIC |  | The ID of the original authorization request service that was appealed. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [AUTHORIZATIONS](AUTHORIZATIONS.md).

