# CL_PAT_EDU_NM

> This table contains information about patient education records, including the education key.

**Primary key:** `PED_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PED_ID` | NUMERIC | PK FK→ | The Unique ID for the Patient Education Record. |
| 2 | `LINE` | INTEGER | PK | The Line Count for the items that have multiple responses but do not change over time. |
| 3 | `EDU_CSN_KEY` | VARCHAR |  | The education key with contact serial number (CSN). The education is a string of Title^Topic^Point-Patient CSN |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PED_ID` | [CL_PAT_EDU_NS](CL_PAT_EDU_NS.md) | sole_pk | high |

