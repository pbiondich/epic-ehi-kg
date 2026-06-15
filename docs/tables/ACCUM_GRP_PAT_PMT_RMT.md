# ACCUM_GRP_PAT_PMT_RMT

> This table contains remittance categorization subtypes for the patient payment amount unit type for an accumulation group.

**Primary key:** `ACCUM_GRP_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUM_GRP_ID` | NUMERIC | PK FK→ | The unique identifier for the accumulation group record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAT_PMT_REMIT_CAT_C_NAME` | VARCHAR |  | The remittance categorization subtypes for the patient payment amount unit type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCUM_GRP_ID` | [ACCUM_GRP_GENERAL](ACCUM_GRP_GENERAL.md) | sole_pk | high |

