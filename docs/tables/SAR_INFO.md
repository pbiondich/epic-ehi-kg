# SAR_INFO

> The general/administrative information for a specific case of a SAR (Service Authorization Request). The diagnoses for this section of the SAR can be found in the SAR_INFO_DIAGNOSES table with the same referral and coverage ID. The associated service line adjudication information can be found in the SAR_SVC_LN_INFO table with the same referral and coverage ID.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SAR_CVG_ID` | NUMERIC |  | The coverage ID for the Service Authorization Request (SAR) adjudication information. |
| 4 | `SAR_NUM` | VARCHAR |  | The Service Authorization Request (SAR) number for the Service Authorization Request (SAR) adjudication information. |
| 5 | `CCS_CASE_NUM` | VARCHAR |  | The California Children's Services (CCS) case number for the Service Authorization Request (SAR) adjudication information. |
| 6 | `SAR_COMMENTS` | VARCHAR |  | The free text comments for the Service Authorization Request (SAR) adjudication information. |
| 7 | `CCS_COUNTY_C_NAME` | VARCHAR | org | The county for the Service Authorization Request (SAR) adjudication information. |
| 8 | `SAR_PROV_GRP_NUM` | VARCHAR |  | The provider group number for the Service Authorization Request (SAR) adjudication information. |
| 9 | `SAR_PROV_NUM` | VARCHAR |  | The provider number (NPI) for the Service Authorization Request (SAR) adjudication information. |
| 10 | `SAR_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `SAR_PROV_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 12 | `SAR_PROV_FAC_NUM` | VARCHAR |  | The facility number for the Service Authorization Request (SAR) adjudication information. |
| 13 | `SAR_REF_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

