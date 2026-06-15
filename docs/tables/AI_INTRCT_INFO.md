# AI_INTRCT_INFO

> Tracks basic LLM items.

**Primary key:** `AI_INTRCT_ID`  
**Columns:** 15  
**Org-specific columns:** 1  
**Joined by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AI_INTRCT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the interaction record. |
| 2 | `USER_ID` | VARCHAR | FK→ | A pointer to the ID of the user who is interacting with the AI agents in this session |
| 3 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 4 | `AI_INTRCT_SESS_STAT_C_NAME` | VARCHAR |  | A status indicating where we are in the life cycle of this session |
| 5 | `STAT_CHNG_UTC_DTTM` | DATETIME (UTC) |  | Tracks the UTC instant when the last status change was made. |
| 6 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | Pointer to the patient encounter associated with the workflow |
| 7 | `PAT_ID` | VARCHAR | FK→ | Pointer to the patient record |
| 8 | `MSG_ID` | VARCHAR | FK→ | A pointer to the patient message associated with the session |
| 9 | `EPISODE_ID` | NUMERIC | FK→ | A pointer to the episode associated with the record. |
| 10 | `MYPT_ID` | VARCHAR | shared | A pointer to the ID of the MyChart user (I WPR .1) who is interacting with the AI agents in this session |
| 11 | `CONVERSATION_GUID` | VARCHAR |  | The GUID use to uniquely identify a conversation with a conversational AI Assistant. This should only be populated for LLM Records of type 45 - Generic Conversation. |
| 12 | `CONVERSATION_MODEL_ID` | NUMERIC |  | Stores a pointer to the Model (HDA Record) used to associate a conversation with a particular AI Assistant workflow. This should only be populated for LLM Records of type 45 - Generic Conversation. |
| 13 | `CONVERSATION_MODEL_ID_ACUITY_SYSTEM_NAME` | VARCHAR |  | The name of this HDA record. |
| 14 | `AI_CONVERSATION_TYPE_C_NAME` | NUMERIC | org | The specific type of conversation with an AI Assistant. Used to distinguish different types of conversations with the same model. This should only be populated for LLM Records of type 45 - Generic Conversation. |
| 15 | `USER_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

## Joined in — referenced by (11)

| From | Column | Confidence |
|------|--------|------------|
| [AI_INTRCT_AGENT_RESPONSES](AI_INTRCT_AGENT_RESPONSES.md) | `AI_INTRCT_ID` | high |
| [AI_INTRCT_AGENT_TASKS](AI_INTRCT_AGENT_TASKS.md) | `AI_INTRCT_ID` | high |
| [AI_INTRCT_CONTACT_INFO](AI_INTRCT_CONTACT_INFO.md) | `AI_INTRCT_ID` | high |
| [AI_INTRCT_DOCS](AI_INTRCT_DOCS.md) | `AI_INTRCT_ID` | high |
| [AI_INTRCT_OBSERVATION](AI_INTRCT_OBSERVATION.md) | `AI_INTRCT_ID` | high |
| [AI_INTRCT_REASON](AI_INTRCT_REASON.md) | `AI_INTRCT_ID` | high |
| [AI_INTRCT_SCAN_DOC](AI_INTRCT_SCAN_DOC.md) | `AI_INTRCT_ID` | high |
| [AI_SESSION_HX](AI_SESSION_HX.md) | `AI_INTRCT_ID` | high |
| [PROMPT_EXECUTION_STATE](PROMPT_EXECUTION_STATE.md) | `AI_INTRCT_ID` | high |
| [RUN_EXECUTION_SUMMARY](RUN_EXECUTION_SUMMARY.md) | `AI_INTRCT_ID` | high |
| [SMRTDTA_ELEM_AIEXTRACTED](SMRTDTA_ELEM_AIEXTRACTED.md) | `AI_INTRCT_ID` | high |

