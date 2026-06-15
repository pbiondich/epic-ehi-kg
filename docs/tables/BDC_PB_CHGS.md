# BDC_PB_CHGS

> This table stores PB Denial/Correspondence (BDC) denial records and the charge transactions that were denied by that denial record.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | The unique identifier for the Professional Billing denial record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_ID` | NUMERIC | shared | Professional charge this denial was posted for. For panel procedures, same denial can point to multiple charges forming a single claim line. |
| 4 | `FOL_ID` | NUMERIC | FK→ | Follow-up record this denial was posted for. For panel procedures, same denial can point to multiple follow-up records forming a single claim line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |
| `FOL_ID` | [FOL_INFO](FOL_INFO.md) | sole_pk | high |

