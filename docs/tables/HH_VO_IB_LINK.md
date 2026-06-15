# HH_VO_IB_LINK

> This table contains a list of Home Health verbal orders contained in the In Basket message.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier for the task or message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HH_VERBAL_ORDER_ID` | VARCHAR |  | The unique identifier for the verbal order record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

