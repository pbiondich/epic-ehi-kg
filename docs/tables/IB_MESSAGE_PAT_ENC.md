# IB_MESSAGE_PAT_ENC

> This table holds related patient contacts for the In Basket message record. This table is intended to replace IB_MESSAGES_2__EPT_CSN_ID because this table can store multiple encounters per message. Typically, this table will only have one line per message because most In Basket message records only have a singular contact associated, if any.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient encounter related to the In Basket message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

