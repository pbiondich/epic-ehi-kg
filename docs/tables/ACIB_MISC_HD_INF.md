# ACIB_MISC_HD_INF

> This table stores the extra information gathered by Help Desk messages.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MISC_HELPDESK_INF` | VARCHAR |  | Stores the extra information gathered by Help Desk messages. |
| 4 | `PAT_INF_YN` | VARCHAR |  | Indicates whether help desk extra information is patient specific. |
| 5 | `HELP_DESK_INF_LABEL` | VARCHAR |  | The label for extra information stored in a help desk message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

