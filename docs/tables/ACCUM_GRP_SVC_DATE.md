# ACCUM_GRP_SVC_DATE

> This table stores the accumulated service dates for an accumulation group.

**Primary key:** `ACCUM_GRP_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCUM_GRP_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the accumulation group record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACCUMULATED_SERVICE_DATE` | DATETIME |  | The list of service dates which have been accumulated to this ACG. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCUM_GRP_ID` | [ACCUM_GRP_GENERAL](ACCUM_GRP_GENERAL.md) | sole_pk | high |

