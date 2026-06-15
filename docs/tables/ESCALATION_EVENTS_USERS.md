# ESCALATION_EVENTS_USERS

> All affected users at that escalation level.

**Primary key:** `ESCALATION_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESCALATION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the subject name record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AFFECTED_USER_ID` | VARCHAR |  | EMP IDs of recipients who are affected by escalation change. |
| 5 | `AFFECTED_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ESCALATION_ID` | [ESCALATION_DYN](ESCALATION_DYN.md) | sole_pk | high |

