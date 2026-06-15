# TAX_INFO

> This table contains information about the tax rate definitions applicable to the sales of goods and services within a business transaction.

**Primary key:** `TAX_ID`  
**Columns:** 3  
**Joined by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAX_ID` | NUMERIC | PK | The unique identifier for the tax definition record. |
| 2 | `TAX_ID_TAX_NAME` | VARCHAR |  | This column contains the tax definition's record name. |
| 3 | `TAX_NAME` | VARCHAR |  | This column contains the tax definition's record name. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (1)

| From | Column | Confidence |
|------|--------|------------|
| [INVOICE](INVOICE.md) | `TAX_ID` | high |

