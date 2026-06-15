# HNO_LINKED_RQGS

> This table stores the list of requisition groupers associated with a note.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RQG_GROUPER_ID` | NUMERIC | FK→ | The unique ID of the requisition grouper associated with the note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `RQG_GROUPER_ID` | [RQG_DB_MAIN](RQG_DB_MAIN.md) | sole_pk | high |

