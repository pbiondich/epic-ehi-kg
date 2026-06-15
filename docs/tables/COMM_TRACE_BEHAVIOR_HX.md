# COMM_TRACE_BEHAVIOR_HX

> Notable behaviors that applied to a trace.

**Primary key:** `COMM_TRACE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_TRACE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the outreach record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `BEHAVIOR_C_NAME` | VARCHAR |  | The notable behavior being audited for this trace. |
| 5 | `ACTOR_USER_ID` | VARCHAR |  | The user who caused notable behavior for this trace. See I RCH 85920 to know what the behavior was. |
| 6 | `ACTOR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ACTOR_MYPT_ID` | VARCHAR |  | The MyChart account who caused notable behavior for this trace. See I RCH 85920 to know what the behavior was. |
| 8 | `ACTOR_PAT_ID` | VARCHAR | FK→ | The patient who caused notable behavior for this trace. See I RCH 85920 to know what the behavior was. |
| 9 | `ACTOR_ACCT_ID` | NUMERIC |  | The guarantor who caused notable behavior for this trace. See I RCH 85920 to know what the behavior was. |
| 10 | `ACTOR_PAT_RELATIONSHIP_ID` | NUMERIC |  | The patient relationship who caused notable behavior for this trace. See I RCH 85920 to know what the behavior was. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACTOR_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

