# TREATMENT_TEAM

> This table stores information about patient treatment teams such as relationship, specialty, department, and start/end time. Each row represents a member of a patient's treatment team.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 19  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `TR_TEAM_BILL_PR_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 6 | `TR_TEAM_EM_CODE_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 7 | `TR_TEAM_EM_REQ_C_NAME` | VARCHAR | org | Used to determine if the evaluation and management code is required or not for use in the treatment team. |
| 8 | `TR_TEAM_SPEC_C_NAME` | VARCHAR | org | The category value corresponding to the specialty of the treatment team member to the patient. |
| 9 | `TR_TEAM_COMMENT` | VARCHAR |  | The comment for the treatment team. |
| 10 | `TR_TEAM_ISDE_YN` | VARCHAR |  | Indicates whether or not this provider was deleted. |
| 11 | `TR_TEAM_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 12 | `TR_TEAM_REL_C_NAME` | VARCHAR | org | The category value corresponding to the relationship of the treatment team member to the patient. |
| 13 | `TR_TEAM_COMM_C_NAME` | VARCHAR |  | Relates to communication being sent to the treatment team members. |
| 14 | `TR_TEAM_INFO_C_NAME` | VARCHAR | org | Additional information related to the treatment team members. |
| 15 | `TR_TEAM_BEG_DTTM` | DATETIME (Local) |  | The date and time the treatment team member started for the patient. |
| 16 | `TR_TEAM_END_DTTM` | DATETIME (Local) |  | The date and time the treatment team member ended for the patient. |
| 17 | `TR_TEAM_ED_YN` | VARCHAR |  | Indicates whether or not this provider was on the treatment team in the ED. |
| 18 | `TR_TEAM_TEAM_ADD_YN` | VARCHAR |  | Indicates whether the assignment was added by the team. |
| 19 | `TR_TEAM_SRC_CSN_ID` | NUMERIC |  | This item stores the contact serial number corresponding to the encounter responsible for assigning a specific member of the treatment team. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

