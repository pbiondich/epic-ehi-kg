# V_EHI_NCS_FILTER_RQG

> This view creates one column of unique requisition groupers linked to a communication record.

**Primary key:** `COMM_ID`, `GROUPER_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the customer service communication. |
| 2 | `GROUPER_ID` | NUMERIC | PK FK→ | This is the primary key for Requisition Grouper tables and refers to the ID number of the Requisition Grouper source. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GROUPER_ID` | [SCHEDULING_GROUPER_INFO](SCHEDULING_GROUPER_INFO.md) | sole_pk | high |

