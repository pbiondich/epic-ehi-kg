# AP_CLAIM_SPLIT_CLAIM

> This table summarizes data for AP Claims, with each claim that is the node of a split in an adjustment sequence given one row.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPLIT_CNT` | INTEGER |  | Contains the number of additional claims pointing to a split claim in an adjustment sequence. |
| 4 | `CLM_SPLIT_CLAIM_ID` | NUMERIC |  | Contains all of the claims that are at the node of a split in an adjustment sequence |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

