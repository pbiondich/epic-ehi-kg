# PAT_ENC_MSP_EGHP3

> This table contains the Tertiary Employer Group Health Plan Info part of the Medicare Secondary Payor Information from the Patient (EPT) master file. Some questionnaires use this as the family member's EGHP info rather than the 'tertiary' EGHP info.

**Primary key:** `PAT_ENC_CSN_ID`  
**Columns:** 20  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `HAS_EGHP3_YN` | VARCHAR |  | Indicates whether the patient has a tertiary employer group health plan. Y indicates that the patient has a tertiary employer group health plan. N indicates that the patient does not have a tertiary employer group health plan. A null value indicates this item was not filled out. |
| 3 | `EGHP3_CUR_EMPL_YN` | VARCHAR |  | Indicates whether the employer group health plan is through the subscriber's current employment. Y indicates that the plan is through the subscriber's current employment. N indicates that the plan is not through the subscriber's current employment. A null value indicates this item was not filled out. |
| 4 | `EGHP3_100_EMP_YN` | VARCHAR |  | Indicates whether the employer that sponsors the group health plan has 100 or more employees. Y indicates that the employer that sponsors the group health plan has 100 or more employees. N indicates that the employer that sponsors the group health plan does not have 100 or more employees. A null value indicates this item was not filled out. |
| 5 | `EGHP3_INS_NAME` | VARCHAR |  | Name of the employer group health plan's insurance company. |
| 6 | `EGHP3_INS_ADR_1` | VARCHAR |  | First line of the employer group health plan's insurance company's address. |
| 7 | `EGHP3_INS_ADR_2` | VARCHAR |  | Second line of the employer group health plan's insurance company's address. |
| 8 | `EGHP3_INS_CITY` | VARCHAR |  | City part of the employer group health plan's insurance company's address. |
| 9 | `EGHP3_INS_ZIP` | VARCHAR |  | Postal code part of the employer group health plan's insurance company's address. |
| 10 | `EGHP3_BEN_PKG` | VARCHAR |  | The benefit package number or policy ID number for the employer group health plan. |
| 11 | `EGHP3_GROUP_NUM` | VARCHAR |  | Group number for this employer group health plan. |
| 12 | `EGHP3_MEMBER_NUM` | VARCHAR |  | Patient's membership number for this employer group health plan. |
| 13 | `EGHP3_INSURED_NAME` | VARCHAR |  | Name of the group health plan's subscriber. |
| 14 | `EGHP3_REL_PT_C_NAME` | VARCHAR | org | The group health plan's subscriber's relationship to the patient. |
| 15 | `EGHP3_EMPL_NAME` | VARCHAR |  | Name of the employer that sponsors this group health plan. |
| 16 | `EGHP3_EMPL_ADR_1` | VARCHAR |  | First line of the address of the employer that sponsors this group health plan. |
| 17 | `EGHP3_EMPL_ADR_2` | VARCHAR |  | Second line of the address of the employer that sponsors this group health plan. |
| 18 | `EGHP3_EMPL_CITY` | VARCHAR |  | City part of the address of the employer that sponsors this group health plan. |
| 19 | `EGHP3_EMPL_ZIP` | VARCHAR |  | Postal code part of the address of the employer that sponsors this group health plan. |
| 20 | `EGHP3_EMPL_PHONE` | VARCHAR |  | Phone number of the employer that sponsors this group health plan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

