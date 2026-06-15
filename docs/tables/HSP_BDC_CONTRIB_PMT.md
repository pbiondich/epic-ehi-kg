# HSP_BDC_CONTRIB_PMT

> This table includes a list of payments that contributed to the creation of the follow-up record.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial/correspondence record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTRIB_PMT_TX_ID` | NUMERIC |  | This column stores the list of payments that contributed to the denial/correspondence record (BDC) creation. For variances this can be multiple payments in case of multiple partials forming a full payment or just the source payment. For all other BDC types, this will only be the source payment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

