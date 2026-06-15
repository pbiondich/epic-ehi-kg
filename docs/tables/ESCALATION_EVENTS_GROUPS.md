# ESCALATION_EVENTS_GROUPS

> All affected groups at that escalation level.

**Primary key:** `ESCALATION_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ESCALATION_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the subject name record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `AFFECTED_UC_GROUP_ID_RECORD_NAME` | VARCHAR |  | Record name |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ESCALATION_ID` | [ESCALATION_DYN](ESCALATION_DYN.md) | sole_pk | high |

