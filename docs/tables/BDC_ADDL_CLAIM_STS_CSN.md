# BDC_ADDL_CLAIM_STS_CSN

> This table contains information of contributing claim status messages for a claim status follow-up record.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the den/corr rec record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADDL_CLAIM_RECON_CSN_ID` | NUMERIC |  | This item stores contact serial numbers of claim reconciliaiton record that contribute to an existing claim status follow-up record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

