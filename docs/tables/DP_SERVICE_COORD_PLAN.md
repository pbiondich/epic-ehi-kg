# DP_SERVICE_COORD_PLAN

> Table for CCSC services to coordinate discharge plan.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `SVC_COORD_PLAN_IDENT` | VARCHAR |  | ID of services to coordinate plan for the patient post-discharge. This column can be used to link to DP_SVC_TO_COORDINATE table, using SERVICE_COOR_PLAN_IDENT column from that table. |
| 7 | `PLAN_NAME` | VARCHAR |  | Name of a plan to coordinate for the patient's post-acute care. |
| 8 | `PLAN_IS_DISCARDED_YN` | VARCHAR |  | Indicator of whether this service coordination plan is discarded. |
| 9 | `PLAN_IS_SENSITIVE_YN` | VARCHAR |  | This column indicates whether the coordination plan should be considered sensitive for EHI export. Sensitive data is removed from the export when the sensitive filter is applied. |
| 10 | `PLAN_EXPECTED_DISCH_DISP_C_NAME` | VARCHAR | org | This column contains the expected discharge disposition associated with this coordination plan. It indicates the hospitalization outcome that the care team is planning for and coordinating services for. |
| 11 | `PLAN_EXPECTED_DISCH_DISP_CMT` | VARCHAR |  | This contains the user-entered comment for discharge disposition associated with this coordination plan. It may be populated when the associated discharge disposition is Other (Comment). |
| 12 | `PLAN_ACTUAL_DISCH_DISP_C_NAME` | VARCHAR | org | This column indicates the discharge disposition associated with this coordination plan. It indicates the hospitalization outcome that the care team is planning for and coordinating services for. This column is populated for coordination plans at sites that use the actual discharge disposition for planning. By default, coordination plans are associated with an expected discharge disposition stored in column PLAN_EXPECTED_DISCH_DISP_C. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

