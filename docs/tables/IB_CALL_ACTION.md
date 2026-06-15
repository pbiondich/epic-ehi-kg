# IB_CALL_ACTION

> The IB_CALL_ACTION table contains the actions needed to be taken to follow-up on a telephone encounter.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique ID of the In Basket Message. |
| 2 | `LINE` | INTEGER | PK | Line number to identify the call action within an In Basket Message. |
| 3 | `CALL_ACTION_C_NAME` | VARCHAR | org | The category value associated with select actions that summarize the phone call and its necessary follow-up. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

