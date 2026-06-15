# DTREE_ANSWER

> This table contains information about decision tree answer records.

**Primary key:** `DTREE_ANSWER_ID`  
**Columns:** 6  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DTREE_ANSWER_ID` | VARCHAR | PK | The unique identifier (.1 item) for the answer record. |
| 2 | `ABANDONING_PROSPECT_ID` | NUMERIC |  | Stores the prospective patient record that is associated with this questionnaire answer record. |
| 3 | `ST_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 4 | `ST_INS_STEP_COMP_YN` | VARCHAR |  | This item stores whether the patient verified or updated insurance information in an insurance node in a self-triage decision tree. |
| 5 | `ST_INS_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 6 | `ST_ACCOUNT_ID` | NUMERIC |  | This item stores the guarantor (EAR) record that was created or linked to this self-triage traversal. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [DTREE_NODES_USED](DTREE_NODES_USED.md) | `DTREE_ANSWER_ID` | high |

