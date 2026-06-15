# HEALTH_CARE_AGENT_HX

> This table records a history of HCA (Health Care Agent) status changes documented in SEC_ACP_HEALTH_CARE_AGENTS (LVN 44200). Whenever an agent is activated or deactivated, information about the agent is stored in this table.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 14  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACTIVE_STATUS_YN_NAME` | VARCHAR |  | This column displays a history of health care agent status changes. 1 indicates that the agent was activated. 0 indicates that the agent was deactivated. |
| 4 | `USER_ID` | VARCHAR | FK→ | This column displays the user ID (EMP ID) of the user who documented the change of status for the agent. |
| 5 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `UTC_INST_DTTM` | DATETIME (UTC) |  | This column displays the UTC instant that the change of status for the agent was documented. |
| 7 | `AGENT_UID` | VARCHAR |  | This column displays an ID which uniquely identifies which emergency contact stores info about the agent. |
| 8 | `AGENT_NAME` | VARCHAR |  | This column displays the name of the Health Care Agent. |
| 9 | `RELATIONSHIP_PERSONAL_C_NAME` | VARCHAR | org | This column displays the personal relationship between the Health Care Agent and the patient at the time of the status change. |
| 10 | `RELATIONSHIP_AGENT_TYP_C_NAME` | VARCHAR | org | This column displays what type of Health Care Agent relationship existed between the agent and the patient at the time of the status change. (Examples: Health Care Agent, First Alternate Health Care Agent, Second Alternate Health Care Agent.) |
| 11 | `PHONE_PRIMARY_C_NAME` | VARCHAR |  | This column displays the primary or preferred phone number on file for the agent at the time of the status change. |
| 12 | `PHONE_HOME` | VARCHAR |  | This column displays the home phone number on file for the agent at the time of the status change. |
| 13 | `PHONE_WORK` | VARCHAR |  | This column displays the work phone number on file for the agent at the time of the status change. |
| 14 | `PHONE_MOBILE` | VARCHAR |  | This column displays the mobile or cellular phone number on file for the agent at the time of the status change. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

