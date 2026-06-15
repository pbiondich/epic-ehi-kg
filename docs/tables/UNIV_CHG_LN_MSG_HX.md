# UNIV_CHG_LN_MSG_HX

> This table contains update history for the Universal Charge Line (UCL) masterfile. This table can be used to link to Universal Charge Messages (UCM) to actually find the update details.

**Primary key:** `UCL_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `UCL_ID` | VARCHAR | PK FK→ | The unique ID assigned to the UCL record (UCL .1). |
| 2 | `LINE` | INTEGER | PK | Each charge line (UCL) can have multiple messages (UCM) associated with it. The combination of UCL_ID and LINE make up a unique identifier for this message. |
| 3 | `MESSAGE_ID` | NUMERIC | FK→ | A history of Universal Charge Messages (UCM) that have updated this charge. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |
| `UCL_ID` | [CLARITY_UCL](CLARITY_UCL.md) | sole_pk | high |

