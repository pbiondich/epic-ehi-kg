# VOIP_CALL

> This table contains information associated with Unified Communications VoIP Calls.

**Primary key:** `VIDEO_VISIT_ID`  
**Columns:** 9  
**Joined by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VIDEO_VISIT_ID` | NUMERIC | PK | The unique identifier (.1 item) for the VoIP call record. |
| 2 | `CALL_DATE` | DATETIME |  | This virtual item returns the date of the interaction. The returned date is handled differently depending on the contact type of the encounter. If there is no encounter associated with the interaction, then the interaction record creation date (I LVV 90090) is returned. If there is an encounter associated and it is not an admission, then the encounter contact date (I EPT 30) is returned. If there is an encounter associated and it is an admission, then the date of the first connect action logged in (SI LVV 100) is returned. If there is no first connect action, then the interaction record creation date is returned. |
| 3 | `END_UTC_DTTM` | DATETIME (UTC) |  | The end instant of the VoIP call in UTC. |
| 4 | `CALL_END_REASON_C_NAME` | VARCHAR |  | The end reason of the VoIP call. This is intended to capture why call workflows ended earlier, before reaching the Nebula service. |
| 5 | `END_DTTM` | DATETIME (Attached) |  | The end instant of the VoIP call in local time. |
| 6 | `START_UTC_DTTM` | DATETIME (UTC) |  | The start instant of the VoIP call in UTC. |
| 7 | `START_DTTM` | DATETIME (Attached) |  | The start instant of the VoIP call in local time. |
| 8 | `PAT_ID` | VARCHAR | FK→ | The patient associated with the VoIP call. |
| 9 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The patient encounter associated with the VoIP call. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (2)

| From | Column | Confidence |
|------|--------|------------|
| [OUTREACH_AUDIT_ACTIONS](OUTREACH_AUDIT_ACTIONS.md) | `VIDEO_VISIT_ID` | high |
| [VOIP_AUDIT_ACTIONS](VOIP_AUDIT_ACTIONS.md) | `VIDEO_VISIT_ID` | high |

