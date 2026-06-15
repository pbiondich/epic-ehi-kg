# QUERY_INSTRUCTIONS

> The QUERY_INSTRUCTIONS table contains information about the query instructions for query records (records in the QRY master file).

**Primary key:** `QUERY_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUERY_ID` | NUMERIC | PK FK→ | The unique identifier for the query record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RESOLV_INSTRUCTIONS` | VARCHAR |  | Instructions for how to resolve the query. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QUERY_ID` | [QRY_RECORD_INFO](QRY_RECORD_INFO.md) | sole_pk | high |

