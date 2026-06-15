# MC_NOTIF_INFO

> Holds non-contact based data relating to Tapestry notifications.

**Primary key:** `OUTREACH_ID`  
**Columns:** 2  
**Joined by:** 11 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OUTREACH_ID` | NUMERIC | PK | The unique identifier (.1 item) for the outreach record record. |
| 2 | `MC_PAT_ID` | VARCHAR | FK→ | Links to the EPT record associated with this communication RCH record's Tapestry member. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MC_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

## Joined in — referenced by (11)

| From | Column | Confidence |
|------|--------|------------|
| [BILLING_NOTIF_GUARANTOR](BILLING_NOTIF_GUARANTOR.md) | `OUTREACH_ID` | high |
| [COMM_TRACE_AGENT_ACTIONS](COMM_TRACE_AGENT_ACTIONS.md) | `OUTREACH_ID` | high |
| [COMM_TRACE_AUTH_DEM](COMM_TRACE_AUTH_DEM.md) | `OUTREACH_ID` | high |
| [COMM_TRACE_AUTH_FACTOR](COMM_TRACE_AUTH_FACTOR.md) | `OUTREACH_ID` | high |
| [COMM_TRACE_AUTH_SUMMARY](COMM_TRACE_AUTH_SUMMARY.md) | `OUTREACH_ID` | high |
| [COMM_TRACE_CRC_RECOM](COMM_TRACE_CRC_RECOM.md) | `OUTREACH_ID` | high |
| [COMM_TRACE_EMAIL_HX](COMM_TRACE_EMAIL_HX.md) | `OUTREACH_ID` | high |
| [COMM_TRACE_EMAIL_RECPNTS](COMM_TRACE_EMAIL_RECPNTS.md) | `OUTREACH_ID` | high |
| [MC_NOTIFICATIONS](MC_NOTIFICATIONS.md) | `OUTREACH_ID` | high |
| [OUTREACH_AUDIT_ACTIONS](OUTREACH_AUDIT_ACTIONS.md) | `OUTREACH_ID` | high |
| [OUTREACH_CONTACT_INFO](OUTREACH_CONTACT_INFO.md) | `OUTREACH_ID` | high |

