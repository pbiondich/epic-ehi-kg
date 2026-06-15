# DP_SVC_COORD_PLAN_AUDIT

> This table contains the audit trail data for the Services to Coordinate workflow.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `AUDIT_USER_ID` | VARCHAR |  | This column stores the user who edited the coordination plan for this audit event. |
| 7 | `AUDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `AUDIT_EVENT_UTC_DTTM` | DATETIME (UTC) |  | This column stores the UTC instant at which the audit event occurred. |
| 9 | `COORD_PLAN_AUD_ACTION_C_NAME` | VARCHAR |  | This column stores the action that was taken for this audit event. The possible actions are adding a coordination plan, modifying a coordination plan, or deleting a coordination plan. |
| 10 | `SVC_COORD_PLAN_IDENT` | VARCHAR |  | This column stores the unique identifier for the coordination plan that was affected by this change. It can be used to join audit trail events to the coordination plan data in DP_SERVICE_COORD_PLAN. |
| 11 | `AUDIT_COORD_PLAN_NAME` | VARCHAR |  | This column stores the audit history of the plan name for each audit event. |
| 12 | `AUDIT_PLAN_IS_INACTIVE_YN` | VARCHAR |  | This column stores the audit history of the whether the coordination plan was active or inactive for each event. |
| 13 | `COORD_PLAN_AUD_DEL_RSN_C_NAME` | VARCHAR | org | This column stores the reason why a coordination plan was deleted from the patient's chart. |
| 14 | `SVC_COORD_DEL_CMT` | VARCHAR |  | This column stores the comment provided by the user when deleting a coordination plan from the patient's chart. |
| 15 | `AUDIT_PLAN_IS_SENSITIVE_YN` | VARCHAR |  | This column stores the audit history of whether the coordination plan was sensitive for each audit event. |
| 16 | `AUDIT_EXPECTED_DISCH_DISP_C_NAME` | VARCHAR | org | This column stores the audit history of the expected discharge disposition associated with the coordination plan for each audit event. |
| 17 | `AUDIT_EXPECTED_DISCH_DISP_CMT` | VARCHAR |  | This contains the audit history of the user-entered comment for discharge disposition associated with this coordination plan. It may be populated when the associated discharge disposition is Other (Comment). |
| 18 | `AUDIT_ACTUAL_DISCH_DISP_C_NAME` | VARCHAR | org | This column stores the audit history of the discharge disposition associated with the coordination plan for each audit event. This is populated only when using the actual discharge disposition for planning; by default the expected discharge disposition is used and its history is stored in column AUDIT_EXPECTED_DISCH_DISP_C. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

