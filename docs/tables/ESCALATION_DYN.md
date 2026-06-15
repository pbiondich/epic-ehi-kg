# ESCALATION_DYN

> Escalation configuration options.

**Primary key:** `ESCALATION_ID`  
**Columns:** 8  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESCALATION_ID` | NUMERIC | PK | The unique identifier (.1 item) for the subject name record. |
| 2 | `CAPTION` | VARCHAR |  | Caption for the clinical attachment. |
| 3 | `ESC_DYN_STATUS_C_NAME` | VARCHAR |  | Escalation Path status. |
| 4 | `ESCALATION_LEVEL` | INTEGER |  | Level in the path the escalation is currently at. |
| 5 | `PAT_ID` | VARCHAR | FK→ | The EPT ID of the patient linked to the escalation |
| 6 | `ESC_TEMPLATE_CSN_ID` | NUMERIC |  | The ID of the Templated Escalation Execution linked to the escalation. |
| 7 | `RECORD_CREATE_INST_UTC_DTTM` | DATETIME (UTC) |  | Time when record was created. |
| 8 | `REQUEST_PNN_PRIORITY_C_NAME` | VARCHAR |  | Priority of the Request. It will be the same as whatever the DEX is attached to. For example, for a request attached to a TLK, it'll be the same as the message it's associated with. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [CHAT_MESSAGE_CONTENT](CHAT_MESSAGE_CONTENT.md) | `ESCALATION_ID` | high |
| [ESCALATION_EVENTS](ESCALATION_EVENTS.md) | `ESCALATION_ID` | high |
| [ESCALATION_EVENTS_GROUPS](ESCALATION_EVENTS_GROUPS.md) | `ESCALATION_ID` | high |
| [ESCALATION_EVENTS_USERS](ESCALATION_EVENTS_USERS.md) | `ESCALATION_ID` | high |
| [ESC_RESPONSIBLE_USERS](ESC_RESPONSIBLE_USERS.md) | `ESCALATION_ID` | high |

