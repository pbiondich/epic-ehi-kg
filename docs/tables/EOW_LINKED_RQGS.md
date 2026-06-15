# EOW_LINKED_RQGS

> Linked RQG requisition groupers for EHI Export.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the in basket message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RQG_GROUPER_ID` | NUMERIC | FK→ | The list of requisition groupers (RQG) that this EOW is associated with for Electronic Health Information (EHI) Export |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |
| `RQG_GROUPER_ID` | [RQG_DB_MAIN](RQG_DB_MAIN.md) | sole_pk | high |

