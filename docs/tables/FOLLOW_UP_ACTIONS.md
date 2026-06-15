# FOLLOW_UP_ACTIONS

> This table contains information regarding follow-up actions. Each row in this table indicates a follow-up action that was taken for a particular LFT record ID.

**Primary key:** `FOLLOW_UP_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FOLLOW_UP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 4 | `FOLLOW_UP_ACT_C_NAME` | VARCHAR | org | This column displays follow-up actions such as Mail, Telephone or MyChart message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FOLLOW_UP_ID` | [FOLLOW_UP_TOPICS](FOLLOW_UP_TOPICS.md) | sole_pk | high |

