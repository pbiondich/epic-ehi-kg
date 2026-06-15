# SYN_SPECIMEN

> This table stores the specimens associated with the synoptic result record.

**Primary key:** `SYNOPTIC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SYNOPTIC_ID` | NUMERIC | PK FK→ | The unique identifier for the synoptic result record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPECIMEN_ID` | VARCHAR | shared | The unique identifier of the specimen record associated with this synoptic result. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SYNOPTIC_ID` | [SYNOPTIC_RESULT_MAIN](SYNOPTIC_RESULT_MAIN.md) | sole_pk | high |

