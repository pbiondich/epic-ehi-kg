# IB_MSG_IMG_FINDINGS

> The IB_MSG_IMG_FINDINGS table contains information about imaging finding records associated with an In Basket message.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `IMAGING_FINDING_ID` | NUMERIC |  | The imaging finding IDs associated with an In Basket message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

