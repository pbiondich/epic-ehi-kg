# IB_NOTES

> This table is to show In Basket notes for each message. If you want to know In Basket information, you could link this table to IB_MESSAGES.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique ID of the In Basket Message. |
| 2 | `NOTES` | VARCHAR |  | Stores the body of the message. |
| 3 | `LINE` | INTEGER | PK | The line number for message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

