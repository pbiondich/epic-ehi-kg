# ACTIVE_ASYNC_BPAS

> Holds the currently active asynchronous OurPractice Advisory chains.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The Line Count |
| 3 | `ACTIVE_ASYNC_ALERTS` | NUMERIC |  | This item holds the identifier of an active asynchronous advisory chain for this encounter. The values correlate to those stored in Async Chain ID (I ALT 2005). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

