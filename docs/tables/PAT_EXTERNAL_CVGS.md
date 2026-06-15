# PAT_EXTERNAL_CVGS

> The PAT_EXTERNAL_CVGS table contains insurance information imported into Epic from an external system. Each row in the table corresponds to a coverage a patient had in the external system.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 28  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EXT_CVGS_SRC_SYS_C_NAME` | VARCHAR | org | The external system that the insurance information was loaded from. |
| 4 | `EXT_CVGS_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 5 | `EXT_CVGS_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |
| 6 | `EXT_CVGS_INS_NAME` | VARCHAR |  | The search string a registrar would enter in the search box when attempting to create a new coverage record. This string typically includes the payor name, plan name, or synonym used to refer to the payor or plan. |
| 7 | `EXT_CVGS_SUBSCR_NUM` | VARCHAR |  | The subscriber ID associated with the external insurance information. |
| 8 | `EXT_CVGS_SUBSCR_NAM` | VARCHAR |  | The name of the subscriber associated with the external insurance information. |
| 9 | `EXT_CVGS_SUBSCR_BIRTH_DATE` | DATETIME |  | The birth date of the subscriber associated with the external insurance information. |
| 10 | `EXT_CVGS_SUBS_SEX_C_NAME` | VARCHAR | org | The sex of the subscriber associated with the external insurance information. |
| 11 | `EXT_CVGS_MEM_REL_C_NAME` | VARCHAR | org | The relationship between the member and the subscriber associated with the external insurance information. |
| 12 | `EXT_CVGS_MEM_NUM` | VARCHAR |  | The member ID associated with the external insurance information. |
| 13 | `EXT_CVGS_MEM_NAME` | VARCHAR |  | The member name override for the patient associated with the external insurance information. This is an override for the patient name when the payor is expecting a different name. |
| 14 | `EXT_CVGS_GROUP_NUM` | VARCHAR |  | The group number associated with the external insurance information. |
| 15 | `EXT_CVGS_RESP_ID` | VARCHAR |  | The General Use Notes (HNO) ID or response text received from an eligibility query sent to verify the external coverage. |
| 16 | `EXT_CVGS_CVG_ID` | NUMERIC |  | The ID of the coverage created from the external insurance information. |
| 17 | `EXT_CVGS_ACTION_C_NAME` | VARCHAR |  | The action taken on the external insurance information. |
| 18 | `EXT_CVGS_CREAT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant when this external coverage was stored in Epic. |
| 19 | `EXT_CVGS_EFF_FRM_DATE` | DATETIME |  | The date from which the external coverage is effective. This is meant to map to what we store in Effective Date From (I CVG 400). |
| 20 | `EXT_CVGS_EFF_TO_DATE` | DATETIME |  | The date to which the external coverage is effective. This is meant to map to what we store in Effective Date To (I CVG 410) |
| 21 | `EXT_CVGS_BIN` | VARCHAR |  | The Beneficiary Identification Number (BIN) of the external coverage. |
| 22 | `EXT_CVGS_PCN` | VARCHAR |  | The processor control number (PCN) of the external coverage. |
| 23 | `EXT_CVGS_PERS_CODE` | VARCHAR |  | The person code of the external coverage. This is meant to map to what we store in Member Person Code (I CVG 316). |
| 24 | `EXT_CVGS_CSN` | NUMERIC |  | Stores the contact serial number (CSN) of the encounter that created the coverage, if it was created in an encounter. |
| 25 | `EXT_CVG_SRC_ORGANIZATION_ID` | NUMERIC |  | The Organization (DXO) that provided the information for this coverage. |
| 26 | `EXT_CVG_SRC_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 27 | `EXT_CVGS_FHIR_IDENT` | VARCHAR |  | The FHIR Id of a coverage record on an external system that was used to create this coverage. |
| 28 | `EXT_CVGS_CVG_OID` | VARCHAR |  | The OID of a coverage record on an external system that was used to create this coverage. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

