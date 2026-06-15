# AP_CLAIM_PROC_IDS

> This table stores the linkages between AP claims (CLM records) and their service lines (ETR records). A common use case for this table is to link from claim-level summary tables to service-line-level summary tables. For example, one path is to join AP_CLAIM to AP_CLAIM_PROC_IDS on CLAIM_ID and AP_CLAIM_PROC_IDS to AP_CLAIM_PROC on TX_ID.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The ID for the claim record. |
| 2 | `LINE` | INTEGER | PK | The service line number for of the claim this row corresponds to, as stored in Chronicles CLM item 18250. |
| 3 | `TX_ID` | NUMERIC | shared | The ID of the transaction (ETR) record that stores all service line information. The ETR records are commonly referred to as procedures, services, transactions, or service lines. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

