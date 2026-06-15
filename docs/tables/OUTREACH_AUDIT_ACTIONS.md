# OUTREACH_AUDIT_ACTIONS

> Each row represents a line of auditing information about actions that have occurred on an outreach contact.

**Primary key:** `OUTREACH_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `APPOINTMENT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | This item tracks the changes to the CSN of an appointment linked to a task instance. |
| 5 | `VIDEO_VISIT_ID` | NUMERIC | FK→ | This item tracks the changes to the video visit record (LVV) linked to a task instance. |
| 6 | `TASK_AUDIT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The CSN of the patient's admission contact associated with the task action related audit. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `APPOINTMENT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `OUTREACH_ID` | [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | sole_pk | high |
| `TASK_AUDIT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |
| `VIDEO_VISIT_ID` | [VOIP_CALL](VOIP_CALL.md) | sole_pk | high |

