# COMM_TRACE_AGENT_ACTIONS

> Information about the actions that were attempted when chatting with AI Agent.

**Primary key:** `OUTREACH_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the outreach record record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `AGENT_ACTION_SETTING_ID` | NUMERIC |  | This item contains the list of actions that were performed by the AI Agent during a chat. |
| 5 | `AGENT_ACTION_SETTING_ID_SETTING_NAME` | VARCHAR |  | Setting record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OUTREACH_ID` | [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | sole_pk | high |

