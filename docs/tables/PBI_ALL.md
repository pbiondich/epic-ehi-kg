# PBI_ALL

> The table contains all invoice records.

**Primary key:** `INVOICE_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INVOICE_ID` | VARCHAR | PK FK→ | The unique identifier (.1 item) for the invoice record. |
| 2 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 3 | `PB_ACCT_ID` | VARCHAR | FK→ | The account associated with the invoice |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INVOICE_ID` | [INVOICE](INVOICE.md) | name_stem | high |
| `PB_ACCT_ID` | [PB_ACCT](PB_ACCT.md) | name_stem | high |

