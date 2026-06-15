# OUTREACH_CONTACT_INFO

> Each row contains basic information about one outreach record contact.

**Primary key:** `OUTREACH_ID`, `CONTACT_DATE_REAL`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `TASK_INSTANCE_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The CSN of the patient's admission contact associated with the task instance state. Only available when the task instance state is set or changed because of a patient response action. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OUTREACH_ID` | [MC_NOTIF_INFO](MC_NOTIF_INFO.md) | sole_pk | high |
| `TASK_INSTANCE_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

